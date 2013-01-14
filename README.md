# Revert Font Size package for Sublime Text 2

Helper plugin to quickly revert user's `font_size` value to a 'default'. Can be executed via keyboard shortcut `Ctrl+0` (or `Super+0` for OSX).

To start using `RevertFontSize` package, configure it by adding the following keys to your user preferences (`Preferences >> Settings - User`).

## Settings

#### `revert_font_size`

Specify your font size value to revert here. The plugin will then update Sublime Text's current font size to the value specified here on execution.

Example `Preferences.sublime-settings` file:
```json
{
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
    <td>Set Revert Font Size Value</td>
    <td>Ctrl+Shift+0</td>
    <td>Super+Shift+0</td>
    <td>Ctrl+Shift+0</td>
  </tr>
</table>
