import sublime
import sublime_plugin

class RevertFontSizeCommand(sublime_plugin.ApplicationCommand):
    """Plugin to revert user 'font_size' to a 'default' value.

    Based on code by bizoo
    http://www.sublimetext.com/forum/viewtopic.php?f=3&t=9508
    """
    def run(self):
        preferences = sublime.load_settings("Preferences.sublime-settings")
        revert_font_size = preferences.get("revert_font_size", 10)    # value 10 is the fallback, just in case
        preferences.set("font_size", revert_font_size)
        sublime.save_settings("Preferences.sublime-settings")

class SetRevertFontSizeValueCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        preferences = sublime.load_settings("Preferences.sublime-settings")
        font_size = preferences.get("font_size")
        preferences.set("revert_font_size", font_size)
        sublime.save_settings("Preferences.sublime-settings")
        sublime.status_message("revert_font_size value is set to " + str(font_size))
