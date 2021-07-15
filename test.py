import sys

from darktheme.widget_template import DarkApplication

from PyQt5.QtWidgets import (
    QMainWindow,
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