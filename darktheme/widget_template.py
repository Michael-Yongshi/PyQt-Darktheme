
from PyQt5.QtCore import (
    Qt,
    pyqtSignal,
    )

from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QWidget, 
    )

from PyQt5.QtGui import (
    QColor,
    QPalette,
    )


class DarkPalette(QPalette):
    """A Dark palette meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        self.setColor(QPalette.Window, QColor(53, 53, 53))          #dark grey (normal background widgets and main)
        self.setColor(QPalette.WindowText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.Base, QColor(25, 25, 25))            #darker grey (selected text in pop up)
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))   #dark grey (not used far as i can see)
        self.setColor(QPalette.ToolTipBase, QColor(100, 100, 100))  #medium grey (tooltip background)
        self.setColor(QPalette.ToolTipText, QColor(255, 255, 255))  #white (tooltip text)
        self.setColor(QPalette.Text, QColor(255, 255, 255))         #white
        self.setColor(QPalette.Button, QColor(53, 53, 53))          #dark grey (drop down arrow colour and tabs)
        self.setColor(QPalette.ButtonText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.BrightText, QColor(255, 0, 0))       #red
        self.setColor(QPalette.Link, QColor(42, 130, 218))          #blue
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))     #blue
        self.setColor(QPalette.HighlightedText, QColor(0, 0, 0))    #black

        # If item is disabled, use alternative colours
        # self.setColor(QPalette.Disabled, QPalette.Light, QColor(100, 100, 100))
        # self.setColor(QPalette.Disabled, QPalette.Shadow, QColor(255, 255, 255))
        self.setColor(QPalette.Disabled, QPalette.Button, QColor(53, 53, 53))       #dark grey
        self.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(25, 25, 25))   #darker grey
        self.setColor(QPalette.Disabled, QPalette.Base, QColor(53, 53, 53))          #dark grey
        self.setColor(QPalette.Disabled, QPalette.Text, QColor(100, 100, 100))  #medium grey
        self.setColor(QPalette.Disabled, QPalette.Window, QColor(53, 53, 53))          #dark grey
        self.setColor(QPalette.Disabled, QPalette.WindowText, QColor(100, 100, 100))  #medium grey

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
