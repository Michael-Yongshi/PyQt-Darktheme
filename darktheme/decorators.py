from PyQt5.QtWidgets import (
    QApplication,
    QInputDialog,
    QMessageBox,
    )

from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class Decorators(object):

    @staticmethod
    def loading_cursor(normal_function):

        def decorated_function(*args, **kwargs):

            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

            normal_function(*args, **kwargs)

            QApplication.restoreOverrideCursor()

        return decorated_function

    @staticmethod
    def user_input_interruption(normal_function):

        def decorated_function(*args, **kwargs):

            QApplication.restoreOverrideCursor()

            result = normal_function(*args, **kwargs)

            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

            return result
            
        return decorated_function

class QInputDialogUserInterruption(QInputDialog):
    def __init__(self):
        super().__init__()

    @Decorators.user_input_interruption
    def getDouble(self, *args, **kwargs):
        result, okPressed = QInputDialog.getDouble(self, *args, **kwargs)
        return result, okPressed

    @Decorators.user_input_interruption
    def getInt(self, *args, **kwargs):
        result, okPressed = QInputDialog.getInt(self, *args, **kwargs)
        return result, okPressed

    @Decorators.user_input_interruption
    def getItem(self, *args, **kwargs):
        result, okPressed = QInputDialog.getItem(self, *args, **kwargs)
        return result, okPressed
        
    @Decorators.user_input_interruption
    def getMultiLineText(self, *args, **kwargs):
        result, okPressed = QInputDialog.getMultiLineText(self, *args, **kwargs)
        return result, okPressed

    @Decorators.user_input_interruption
    def getText(self, *args, **kwargs):
        result, okPressed = QInputDialog.getText(self, *args, **kwargs)
        return result, okPressed

class QMessageBoxUserInterruption(QMessageBox):
    def __init__(self):
        super().__init__()

    @Decorators.user_input_interruption
    def critical(self, *args, **kwargs):
        response = QMessageBox.critical(self, *args, **kwargs)
        return response
        
    @Decorators.user_input_interruption
    def information(self, *args, **kwargs):
        response = QMessageBox.information(self, *args, **kwargs)
        return response

    @Decorators.user_input_interruption
    def question(self, *args, **kwargs):
        response = QMessageBox.question(self, *args, **kwargs)
        return response

    @Decorators.user_input_interruption
    def warning(self, *args, **kwargs):
        response = QMessageBox.warning(self, *args, **kwargs)
        return response