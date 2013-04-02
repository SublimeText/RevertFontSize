import sublime
import sublime_plugin

def is_sublime_text_3():
    """Returns True if this plugin is currently being run in Sublime Text 3."""
    try:
        return int(sublime.version()) >= 3000
    except ValueError:
        return sys.hexversion >= 0x030000F0

def plugin_loaded():
    """Called when this plugin is loaded; Sublime Text 3 API."""
    preferences = sublime.load_settings("Preferences.sublime-settings")
    if not preferences.get("revert_font_size"):
        default_font_size = preferences.get("font_size", 10)
        preferences.set("revert_font_size", default_font_size)
        sublime.save_settings("Preferences.sublime-settings")

def plugin_unloaded():
    """Called when this plugin is unloaded; Sublime Text 3 API."""
    pass

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
