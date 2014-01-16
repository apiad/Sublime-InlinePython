import sublime_plugin
import math


class PythonEvalInPlaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Transform it via rot13
                s = repr(eval(s))
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
