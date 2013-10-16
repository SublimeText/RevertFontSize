# Revert Font Size package for Sublime Text [![Build Status](https://travis-ci.org/SublimeText/RevertFontSize.png?branch=master)](https://travis-ci.org/SublimeText/RevertFontSize)

Helper plugin to quickly revert user's font size value. Can be executed via keyboard shortcut `Ctrl+0` (or `Super+0` for OS X).

**Notes:**

- Sublime Text 2
  - To start using this package, configure it by adding the `revert_font_size` key to your user preferences (`Preferences >> Settings - User`) or by invoking the `Set the Value for Revert Font Size` command.

- Sublime Text 3
  - No additional work needed, the `revert_font_size` setting will be created automatically on initial load.

## Settings

- `"revert_font_size": {font size}`

Example `../User/Preferences.sublime-settings` file:
```json
{
    "font_face": "Source Code Pro",
    "font_size": 14.0,
    "revert_font_size": 12.0
}
```

## Keyboard Shortcuts

<table>
  <tr>
    <th>Command</th>
    <th>Windows</th>
    <th>OS X</th>
    <th>Linux</th>
  </tr>
  <tr>
    <td>Revert Font Size</td>
    <td>Ctrl+0</td>
    <td>Super+0</td>
    <td>Ctrl+0</td>
  </tr>
  <tr>
    <td>Set the Value for Revert Font Size</td>
    <td>Ctrl+Shift+0</td>
    <td>Super+Shift+0</td>
    <td>Ctrl+Shift+0</td>
  </tr>
</table>
