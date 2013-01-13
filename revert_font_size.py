import sublime
import sublime_plugin

class RevertFontSizeCommand(sublime_plugin.ApplicationCommand):
    """Plugin to revert user 'font_size' value.

    Based on code by bizoo
    http://www.sublimetext.com/forum/viewtopic.php?f=3&t=9508
    """
    def run(self):
        user_settings = sublime.load_settings('RevertFontSize.sublime-settings')
        default_font_size = user_settings.get('default_font_size')

        pref_settings = sublime.load_settings('Preferences.sublime-settings')
        pref_settings.set('font_size', default_font_size)
        sublime.save_settings('Preferences.sublime-settings')
