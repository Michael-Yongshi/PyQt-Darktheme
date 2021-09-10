# pyqt-darktheme

## Version
### 1.2
1.2.4   changed elements for tabs, radio buttons, and checkboxes when they are disabled
1.2.3   Changed folder name to darktheme
### 1.1
1.1.1   Changed pip name to pyqt-darktheme


## Install
```
pip install pyqt-darktheme
```

## Dark Theme settings
### Import
To import the dark theme
```
from darktheme.widget_template import DarkApplication
```

### How to
```
class Application(DarkApplication):
    def __init__(self, *__args):
        super().__init__(*__args)
```

## Clickable Widgets
### Import
To import the dark themed widgets, i.e. a clickable label widget
```
from darktheme.widget_template import QClickLabel
```

### How to
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

### How to
to add a loading cursor to a called method:
```PyQt
@Decorators.loading_cursor
```

to revert back to normal cursor for some reason, usually for user input requests:
```
@Decorators.user_input_interruption
```


to use input dialogs that automatically reverts to normal arrow and back to loadingPyQt cursor after input is done:
```
result, okPressed = QInputDialogUserInterruption.getText(
    self, "User input requested", "This dialog box shows a regular cursor, letting the user know input is possible"
    )

if result and okPressed:
    print(result)
```

## License

Licensed under GPL-3.0-or-later, see LICENSE file for details.

Copyright © 2020 Michael-Yongshi.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
