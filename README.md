Sublime-InlinePython
====================

A Sublime Text 3 plugin that evaluates and replaces the selected Python code.


Usage:
------

Add the following key bindings to your preferences:

    { "keys": ["ctrl+alt+e"], "command": "inline_python" },
    { "keys": ["ctrl+shift+e"], "command": "inline_python_str" },

You can of course use a different key binding.

Next, on any open file, select a valid Python expression, and press
`ctrl+alt+e` to replace the selection for it's the Python `repr`.
Alternatively you can press `ctrl+shift+e` and it will be replaced with
the `str` representation of the expression. If the
evaluation throws any exception, you'll see it in the console, and your text
will be unchanged.


Examples:
--------

You are writing a `Markdown` document and need to add a line with
70 `=`s. Just type `'=' * 70`, select it and hit `ctrl+alt+e`.

You are writing a `JavaScript` code and need to iterate on the
set of words `['bar', 'egg', 'foo']`. Just type `'bar egg foo'.split()`
and evaluate.

You are writing a `for` loop up to some weird value like `math.floor(42 * 13)`,
which is constant. Instead of calculating it in your head, just
type it and evaluate it (BTW, it is equal to `546`).

You have to write a date that is 96 days up from now. Just type
`datetime.datetime.today() + datetime.timedelta(days=96)`, select it,
hit 'ctrl+shift+e' and it gets replaced with `2014-05-12 11:42:20.834988`
(or whatever the right day is).

In many cases you have to type in something, which you cannot easily type,
but you know how to generate it using some list comprehension or other
Python idioms. Instead of switching to the terminal, firing up IPython and
generating it, just type it and evaluate it.


License:
--------

MIT! Use at your own risk...


Forking, collaborating or whatever:
-----------------------------------

Sure, come to [Github](https://github.com/apiad/Sublime-InlinePython).
