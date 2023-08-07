import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QWidget, QCheckBox, QRadioButton, QComboBox


class GreetingController:
    def __init__(self):
        self.message = None

    def show(self, name, options, radio_text, combo_text):
        text_options = ", ".join(options)
        self.message = f"Welcome, {name}!\n"
        self.message += f"Selected options: {text_options}\n"
        self.message += f"Radio selected: {radio_text}\n"
        self.message += f"Combo selected: {combo_text}"
        return self.message


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets PyQt5")
        self.setGeometry(100, 100, 400, 300)

        # Create widgets and layouts
        self.label = QLabel("Name:")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Enter Message")
        self.result_label = QLabel()

        self.checkbox1 = QCheckBox("Option 1")
        self.checkbox2 = QCheckBox("Option 2")
        self.radio_button1 = QRadioButton("Radio 1")
        self.radio_button2 = QRadioButton("Radio 2")
        self.combo_box = QComboBox()
        self.combo_box.addItem("Option 1")
        self.combo_box.addItem("Option 2")
        self.combo_box.addItem("Option 3")

        # Create layouts
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        checkbox_layout = QVBoxLayout()
        radio_layout = QVBoxLayout()

        # Add widgets to the form
        form_layout.addWidget(self.label)
        form_layout.addWidget(self.line_edit)

        # Adding checkboxes and radio buttons to their respective layouts
        checkbox_layout.addWidget(self.checkbox1)
        checkbox_layout.addWidget(self.checkbox2)
        radio_layout.addWidget(self.radio_button1)
        radio_layout.addWidget(self.radio_button2)

        # Adding checkbox and radio button layouts to the main layout
        form_layout.addLayout(checkbox_layout)
        form_layout.addLayout(radio_layout)

        # Add form layout and button to main layout
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.combo_box)

        # Create central widget for the window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Configuring the central widget for the main window
        self.setCentralWidget(central_widget)

        # Connecting the button to the greeting function
        self.button.clicked.connect(self.show_result)

        # Create an instance of the controller
        self.greeting_controller = GreetingController()

    def show_result(self):
        name = self.line_edit.text()
        options = []
        if self.checkbox1.isChecked():
            options.append("Option 1")
        if self.checkbox2.isChecked():
            options.append("Option 2")
        radio_text = ""
        if self.radio_button1.isChecked():
            radio_text = "Radio 1"
        elif self.radio_button2.isChecked():
            radio_text = "Radio 2"
        combo_text = self.combo_box.currentText()

        # Instantiate the driver to get the message
        message = self.greeting_controller.show(name, options, radio_text, combo_text)

        self.result_label.setText(message)


def start_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
