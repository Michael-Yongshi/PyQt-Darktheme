import sys

from darktheme.widget_template import DarkApplication

import sys

from PyQt5.QtCore import (
    QSettings,
    Qt,
    )

from PyQt5.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton, 
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget, 
    )

from PyQt5.QtGui import (
    QFontDatabase,
    QIcon,
    )

def run():
    global app
    app = DarkApplication(sys.argv)
    global main
    main = QMainWindow()
    main.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()