import sublime, sublime_plugin

class SetFontSizeCommand(sublime_plugin.ApplicationCommand):
    """Plugin to set user 'font_size' value.
    http://www.sublimetext.com/forum/viewtopic.php?f=3&t=9508
    """
    def run(self, size):
        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('font_size', size)
        sublime.save_settings('Preferences.sublime-settings')
