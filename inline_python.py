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

    def process_imports(self):
        imports = self.get_setting('imports')

        for imp in imports:
            try:
                globals()[imp] = __import__(imp)
            except:
                pass


class _InlineMixin(_Mixin):
    def run(self, edit):
        self.process_imports()

        expand_chars = self.get_setting('expand_chars')
        counters = collections.defaultdict(lambda: 0)

        class Counter:
            def __init__(self):
                self.counter = -1

            def value(self):
                self.counter += 1
                return self.counter

            def __str__(self):
                return str(self.value())

            def __repr__(self):
                return repr(self.value())

            def __call__(self, x):
                c = counters[x]
                counters[x] = c + 1
                return c

            def __add__(self, other):
                return self.value() + other

            def __sub__(self, other):
                return self.value() - other

            def __mul__(self, other):
                return self.value() * other

            def __div__(self, other):
                return self.value() / other

            def __mod__(self, other):
                return self.value() % other

        _ = Counter()

        for region in self.view.sel():
            if region.empty():
                # Expand the region until a valid selection
                self.expand_region(edit, region, expand_chars)

            # Get the selected text
            s = self.view.substr(region)

            try:
                # Build the current context
                current_locals = {}
                current_locals.update(**locals())
                current_locals.update(**temporal_locals)
                # Evaluate the selected substring
                e = eval(s, current_locals, globals())
                s = self.convert(e)
                # Replace the selection with transformed text
                self.view.replace(edit, region, s)
                msg = "InlinePython :: Replacing with `%s`" % s
                print(msg)
            except Exception as e:
                msg = "InlinePython :: Error evaluating `%s` (%s)" % (s, str(e))
                sublime.status_message(msg)
                raise e

        sublime.status_message("InlinePython :: Replacement completed.")


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


temporal_locals = {}


class InlinePythonExecuteCommand(sublime_plugin.TextCommand, _Mixin):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue

            # Get the selected text
            s = self.view.substr(region)

            try:
                # Evaluate the selected substring
                exec(s, temporal_locals)
            except Exception as e:
                msg = "InlinePython :: Error executing script (%s)" % str(e)
                sublime.status_message(msg)
                raise e

        sublime.status_message("InlinePython :: Execution completed.")


class InlinePythonRunCommand(sublime_plugin.TextCommand, _Mixin):
    def run(self, edit, function=None):
        if function is None:
            self.query_functions()
        else:
            self.evaluate_function(edit, function)

    def query_functions(self):
        functions = list(temporal_locals.keys() - ['__builtins__'])

        if not functions:
            sublime.status_message("InlinePython :: No functions available.")
            return

        def done(i):
            if i < 0:
                return

            self.view.run_command("inline_python_run", {"function": functions[i]})

        sublime.active_window().show_quick_panel(functions, done,
                                                 sublime.MONOSPACE_FONT)

    def evaluate_function(self, edit, function):
        if function not in temporal_locals:
            sublime.status_message("InlinePython :: Function `%s` "
                                   "was not found." % function)
            return

        for region in self.view.sel():
            if region.empty():
                continue

            # Get the selected text
            s = self.view.substr(region)

            try:
                # Evaluate the selected substring
                s = str(temporal_locals[function](s))
                self.view.replace(edit, region, s)
            except Exception as e:
                msg = "InlinePython :: Error executing script (%s)" % str(e)
                sublime.status_message(msg)
                raise e

        sublime.status_message("InlinePython :: Execution completed.")


class ExpandExpressionCommand(sublime_plugin.TextCommand, _Mixin):
    def run(self, edit):
        settings = sublime.load_settings(SETTINGS_FILE)
        view_settings = self.view.settings()

        expand_chars = view_settings.get('inline_python_expand_chars',
                                         settings.get('expand_chars'))

        for region in self.view.sel():
            self.expand_region(edit, region, expand_chars)
