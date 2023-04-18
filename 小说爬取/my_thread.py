from PyQt6.QtCore import QThread, pyqtSignal


class MyThread(QThread):
    simpleSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def connect(self, method):
        self.simpleSignal.connect(method)
        pass

    def emit(self):
        self.simpleSignal.emit()
        pass
