import sublime_plugin
import sublime


SETTINGS_FILE = "InlinePython.sublime-settings"


class InlinePythonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings(SETTINGS_FILE)
        view_settings = self.view.settings()

        imports = view_settings.get('inline_python_imports', settings.get('imports'))

        for imp in imports:
            locals()[imp] = __import__(imp)

        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Evaluate the selected substring
                s = repr(eval(s))
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
