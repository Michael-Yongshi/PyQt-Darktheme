import sys

from darktheme.widget_template_pyqt6 import DarkPalette

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QStyleFactory,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    )

from PyQt6.QtGui import (
    QAction,
    QPalette,
    )


class TestApplication(QApplication):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.dark = False

        self.styles = ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
        self.style = 0

class TestMainWindow(QMainWindow):
    def __init__(self, *__args):
        super().__init__(*__args)

        # set menu bar
        bar = self.menuBar()

        file_menu = bar.addMenu('File')
        open_action = QAction('Open', self)
        close_action = QAction('Close', self)
        file_menu.addAction(open_action)
        file_menu.addAction(close_action)

        edit_menu = bar.addMenu('Edit')
        undo_action = QAction('Undo', self)
        redo_action = QAction('Redo', self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # central widget
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

class CentralWidget(QWidget):
    def __init__(self, *__args):
        super().__init__(*__args)

        # vertical main layout
        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        # middle grid
        self.middle_grid = QWidget()
        self.grid_layout = QGridLayout()
        self.middle_grid.setLayout(self.grid_layout)

        # add diverse set of elements in middle grid
        self.tabs = QTabWidget()
        self.tab = QWidget()
        self.tabdis = QWidget()
        self.tabs.addTab(self.tab, 'Normal tab')
        self.tabs.addTab(self.tabdis, 'Disabled tab')
        self.tabs.setTabEnabled(1, False)

        self.label_box = QLabel('label with tooltip', self)
        self.label_box.setToolTip('This is how a tooltip will look like')

        self.text_box = QTextEdit(self)

        self.radiowidget = QWidget()
        self.radiolayout = QHBoxLayout()
        self.radiowidget.setLayout(self.radiolayout)
        clickedradiobutton = QRadioButton("Clicked radio button")
        clickedradiobutton.setChecked(True)
        uncheckedradiobutton = QRadioButton("Not clicked radio button")
        disabledradiobutton = QRadioButton("disabled radio button")
        disabledradiobutton.setDisabled(True)
        self.radiolayout.addWidget(clickedradiobutton)
        self.radiolayout.addWidget(uncheckedradiobutton)
        self.radiolayout.addWidget(disabledradiobutton)

        self.checkwidget = QWidget()
        self.checklayout = QHBoxLayout()
        self.checkwidget.setLayout(self.checklayout)
        self.check = QCheckBox('unclicked checkbox')
        self.checkclicked = QCheckBox('clicked checkbox')
        self.checkclicked.setChecked(True)
        self.checkdis = QCheckBox('disabled checkbox')
        self.checkdis.setDisabled(True)
        self.checklayout.addWidget(self.check)
        self.checklayout.addWidget(self.checkclicked)
        self.checklayout.addWidget(self.checkdis)

        self.progress = QProgressBar()
        self.progress.setValue(50)

        # (fromRow, fromColumn, rowSpan=1, columnSpan=1)
        self.grid_layout.addWidget(self.tabs, 0, 0)
        self.grid_layout.addWidget(self.label_box, 1, 0)
        self.grid_layout.addWidget(self.text_box, 2, 0)
        self.grid_layout.addWidget(self.radiowidget, 1, 1)
        self.grid_layout.addWidget(self.checkwidget, 2, 1)
        self.grid_layout.addWidget(self.progress, 3, 0, 1, 2)

        # set main layout
        self.theme_button = QPushButton('Switch Theme', self)
        self.theme_button.setToolTip('This switches from light to dark theme')
        self.theme_button.clicked.connect(self.on_click_change_theme)
        self.style_button = QPushButton('Switch Style')
        self.style_button.setToolTip(f'This switches the default OS styles\nStyles are: {QStyleFactory.keys()}')
        self.style_button.clicked.connect(self.on_click_change_style)
        self.vertical_layout.addWidget(self.middle_grid)
        self.vertical_layout.addWidget(self.theme_button)
        self.vertical_layout.addWidget(self.style_button)


    def on_click_change_theme(self):
        if app.dark == False:
            app.setPalette(DarkPalette())
            app.dark = True
        else:
            app.setPalette(QPalette())
            app.dark = False

    def on_click_change_style(self):

        try:
            app.setStyle(QStyleFactory.keys()[app.style])
        except:
            app.style = 0
            app.setStyle(QStyleFactory.keys()[app.style])
        app.style += 1


def run():
    global app
    app = TestApplication(sys.argv)
    global main
    main = TestMainWindow()
    main.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()