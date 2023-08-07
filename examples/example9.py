import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QObject, pyqtSignal


# We create a class that will handle the events
class HandlerEvents(QObject):
    # We define a customized signal to be emitted when the event occurs
    my_event = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        # We connect the signal to our custom driver
        self.my_event.connect(self.my_manager)

    def my_manager(self, data):
        print(f"Customized handler executed with the following data: {data}")


def start_handler():
    app = QApplication(sys.argv)

    # We create an instance of the handler
    handler = HandlerEvents()

    # We create a button to emit the event
    button = QPushButton("Click here")

    def broadcast_event():
        # We broadcast the personalized signal with some data
        handler.my_event.emit({"message": "Hello from the customized event!"})

    button.clicked.connect(broadcast_event)

    button.show()
    sys.exit(app.exec_())
