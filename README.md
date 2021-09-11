# pyqt-darktheme
A dark themed QPalette class for use in GUI's implemented using PyQt5, some many-used widgets that are by default clickable and decorators to change the mouse to an hourglass and back in certain circumstances.

## Test and examples
Run the 'test_gui.py' file to see how it compares to the normal light theme and to test the library on your device.

## Version
### 1.2
1.2.5   Added a test_gui to showcase the themes and for testing
1.2.4   changed elements for tabs, radio buttons, and checkboxes when they are disabled
1.2.3   Changed folder name to darktheme
### 1.1
1.1.1   Changed pip name to pyqt-darktheme

## Install
```
pip install pyqt-darktheme
```

## How to use the dark theme
### Import
To import the dark theme as a class based on QPalette
```
from darktheme.widget_template import DarkPalette
```

### Configure
Create a QApplication object and set the DarkPalette like below
```
app = QApplication()
app.setPalette(DarkPalette())
```

See the 'test_gui.py' file for an example how to make it configurable

## How to use the Clickable Widgets
### Import
To import the clickable widgets, i.e. a clickable label widget
```
from darktheme.widget_template import QClickLabel
```

### Configure
```
label = QClickLabel()
label.setText('This label is clickable')
label.clicked.connect(clicklabel)

def clicklabel:
    print("This label is clicked")
```

## Decorators
### Import
To import the decorators
```
from darktheme.decorators import (
    Decorators,
    QInputDialogUserInterruption,
    QMessageBoxUserInterruption,
)
```

### How to use normal decorators
to add a loading cursor to a called method:
```
@Decorators.loading_cursor
```

to revert back to normal cursor manually for some reason, i.e. to ask user for input:
```
@Decorators.user_input_interruption
```

### How to use the decorated dialogs
Two dialogs are given that have the decorator 'user_input_interruption' built-in:
- QInputDialogUserInterruption
- QMessageBoxUserInterruption

to use these dialogs:
```
@Decorators.loading_cursor
def program():

    print(doing stuff and showing loading cursor)

    result, okPressed = QInputDialogUserInterruption.getText(
        self, "User input requested", "This dialog box shows a regular cursor, letting the user know input is requested")
    if result and okPressed:
        print(result)
    
    print(continue doing stuff and showing loading cursor)
```

## License

Licensed under GPL-3.0-or-later, see LICENSE file for details.

Copyright © 2020 Michael-Yongshi.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
