import sys
import pyxdf
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
import pyqtgraph as pg


class EEGViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EEG viewer with PyQt5 and pyqtgraph")
        self.setGeometry(100, 100, 800, 600)

        # Creating a PyQtGraph widget to display EEG signals
        self.graphics_layout = pg.GraphicsLayoutWidget(parent=self)
        self.graphics_layout.ci.layout.setContentsMargins(0, 0, 0, 0)
        self.graphics_layout.ci.layout.setSpacing(0)

        self.plot_widget = self.graphics_layout.addPlot()

        # Create a button to load the XDF file
        self.load_button = QPushButton("Load XDF file")
        self.load_button.clicked.connect(self.load_xdf_file)

        # Configure the layout of the main window
        layout = QVBoxLayout()
        layout.addWidget(self.graphics_layout)
        layout.addWidget(self.load_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.data = None

    def load_xdf_file(self):
        # Display the dialog for loading the XDF file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Load XDF file", "", "XDF Files (*.xdf);;All Files (*)",
                                                   options=options)
        if file_name:
            # Load XDF file
            data, header = pyxdf.load_xdf(file_name)

            # Clear the chart before displaying new data
            self.plot_widget.clear()

            for stream in data:
                y = stream['time_series']

                if isinstance(y, list):
                    # list of strings, draw one vertical line for each marker
                    for timestamp, marker in zip(stream['time_stamps'], y):
                        self.plot_widget.addLine(x=timestamp, pen=pg.mkPen('k'))
                        print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
                elif isinstance(y, np.ndarray):
                    # numeric data, transpose and draw as lines
                    y = y.T
                    num_channels, num_samples = y.shape
                    time_points = np.arange(num_samples)  # PTime points as 0, 1, 2, ...
                    for channel_index in range(num_channels):
                        channel_data = y[channel_index]
                        self.plot_widget.plot(time_points, channel_data, pen=pg.mkPen(width=1, color=channel_index))
                else:
                    raise RuntimeError('Unknown stream format')


def start_experiment():
    app = QApplication(sys.argv)
    window = EEGViewerWindow()
    window.show()
    sys.exit(app.exec_())
