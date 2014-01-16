import sublime_plugin


class InlinePythonCommand(sublime_plugin.TextCommand):
    import math
    import time
    import datetime

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Evaluate the selected substring
                s = repr(eval(s))
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
