import sublime_plugin
import sublime
import collections


SETTINGS_FILE = "InlinePython.sublime-settings"


class _Mixin:
    def char_at(self, region, index):
        s = self.view.substr(region)
        if index >= 0:
            return s[index] if s and len(s) > index else None

    def expand_region(self, edit, region, expand_chars):
        pass

    def get_setting(self, setting, default=None):
        settings = sublime.load_settings(SETTINGS_FILE)
        view_settings = self.view.settings()

        global_value = settings.get(setting, default)
        local_value = view_settings.get(setting, global_value)

        return local_value


class _InlineMixin(_Mixin):
    def run(self, edit):
        imports = self.get_setting('imports')
        expand_chars = self.get_setting('expand_chars')

        for imp in imports:
            try:
                locals()[imp] = __import__(imp)
            except:
                pass

        counters = collections.defaultdict(lambda: 0)

        class Counter:
            def __init__(self):
                self.counter = -1

            def __str__(self):
                self.counter += 1
                return str(self.counter)

            def __repr__(self):
                self.counter += 1
                return repr(self.counter)

            def __call__(self, x):
                c = counters[x]
                counters[x] = c + 1
                return c

        _ = Counter()

        for region in self.view.sel():
            if region.empty():
                # Expand the region until a valid selection
                self.expand_region(edit, region, expand_chars)

            # Get the selected text
            s = self.view.substr(region)

            try:
                # Evaluate the selected substring
                e = eval(s)
                s = self.convert(e)
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
                msg = "InlinePython :: Replacing with `%s`" % s
                print(msg)
                sublime.status_message(msg)
            except Exception as e:
                msg = "InlinePython :: Error evaluating `%s` (%s)" % (s, str(e))
                sublime.status_message(msg)
                raise e


class InlinePythonCommand(sublime_plugin.TextCommand, _InlineMixin):
    def convert(self, e):
        return repr(e)

    def run(self, edit):
        _InlineMixin.run(self, edit)


class InlinePythonStrCommand(sublime_plugin.TextCommand, _InlineMixin):
    def convert(self, e):
        return str(e)

    def run(self, edit):
        _InlineMixin.run(self, edit)


class ExpandExpressionCommand(sublime_plugin.TextCommand, _Mixin):
    def run(self, edit):
        settings = sublime.load_settings(SETTINGS_FILE)
        view_settings = self.view.settings()

        expand_chars = view_settings.get('inline_python_expand_chars',
                                         settings.get('expand_chars'))

        for region in self.view.sel():
            self.expand_region(edit, region, expand_chars)
