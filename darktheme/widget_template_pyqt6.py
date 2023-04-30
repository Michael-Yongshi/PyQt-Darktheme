
from PyQt6.QtCore import (
    Qt,
    pyqtSignal,
    )

from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QWidget, 
    )

from PyQt6.QtGui import (
    QColor,
    QPalette,
    )


class DarkPalette(QPalette):
    """A Dark palette meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        self.setColor(QPalette.ColorRole.Window, QColor(50, 50, 50))          #dark grey (normal background widgets and main)
        self.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))            #darker grey (selected text in pop up)
        self.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))   #dark grey (not used far as i can see)
        self.setColor(QPalette.ColorRole.ToolTipBase, QColor(100, 100, 100))  #medium grey (tooltip background)
        self.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))  #white (tooltip text)
        self.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))         #white
        self.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))          #dark grey (drop down arrow colour and tabs)
        self.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))       #red
        self.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))          #blue
        self.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))     #blue
        self.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))    #black

        # If item is disabled, use alternative colours
        # self.setColor(QPalette.Disabled, QPalette.Light, QColor(100, 100, 100))
        # self.setColor(QPalette.Disabled, QPalette.Shadow, QColor(255, 255, 255))
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, QColor(50, 50, 50))       #dark grey
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(25, 25, 25))   #darker grey
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, QColor(50, 50, 50))          #dark grey
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(100, 100, 100))  #medium grey
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, QColor(50, 50, 50))          #dark grey
        self.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(100, 100, 100))  #medium grey

class DarkApplication(QApplication):
    """A Dark styled application."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        # self.setStyle("Fusion")
        self.setPalette(DarkPalette())

class QClickWidget (QWidget):
    """A widget which is clickable"""
    def __init__(self, *args):
        super().__init__(*args)
    
    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if QApplication.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()

class QBorderedWidget(QClickWidget):
    """A widget which is the default, but with some different stylesheet details (borders)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setStyleSheet("border: 1px solid rgb(100, 100, 100)")

class QUnBorderedWidget(QClickWidget):
    """A widget which is the default, but with some different stylesheet details (borders)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setStyleSheet("border: 0px")

class QClickFrame (QFrame):
    """A frame which is clickable"""
    def __init__(self, *args):
        super().__init__(*args)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if QApplication.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()

class QFlatFrame (QClickFrame):
    """A visible frame to hold a layout of widgets."""
    def __init__(self, *args):
        super().__init__(*args)

        self.setFrameStyle(QFrame.Box)

class QBorderlessFrame (QClickFrame):
    """An invisible frame to hold a layout of widgets."""
    def __init__(self, *args):
        super().__init__(*args)

        self.setFrameStyle(QFrame.NoFrame)

class QRaisedFrame (QClickFrame):
    """A raised frame to hold a layout of widgets."""
    def __init__(self, *args):
        super().__init__(*args)

        self.setFrameStyle(QFrame.Panel | QFrame.Raised)

class QClickLabel (QLabel):
    """A label which is clickable"""
    def __init__(self, *args):
        super().__init__(*args)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if QApplication.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()
