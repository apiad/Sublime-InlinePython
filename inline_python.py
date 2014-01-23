import sublime_plugin
import sublime


SETTINGS_FILE = "InlinePython.sublime-settings"


class InlinePythonCommand(sublime_plugin.TextCommand):
    def expand_region(self, edit, region, expand_chars):
        pass

    def run(self, edit):
        settings = sublime.load_settings(SETTINGS_FILE)
        view_settings = self.view.settings()

        imports = view_settings.get('inline_python_imports', settings.get('imports'))
        expand_chars = view_settings.get('inline_python_expand_chars', settings.get('expand_chars'))

        for imp in imports:
            locals()[imp] = __import__(imp)

        for region in self.view.sel():
            if region.empty():
                # Expand the region until a valid selection
                self.expand_region(edit, region, expand_chars)

            # Get the selected text
            s = self.view.substr(region)

            try:
                # Evaluate the selected substring
                s = repr(eval(s))
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
                print("InlinePython :: Replacing with `%s`" % s)
                sublime.status_message("InlinePython :: Replacing with `%s`" % s)
            except Exception as e:
                sublime.status_message("InlinePython :: Error evaluating `%s` (%s)" % (s, str(e)))
                raise e
