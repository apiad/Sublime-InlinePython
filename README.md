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
---------

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
hit `ctrl+shift+e` and it gets replaced with `2014-05-12 11:42:20.834988`
(or whatever the right day is).

In many cases you have to type in something, which you cannot easily type,
but you know how to generate it using some list comprehension or other
Python idioms. Instead of switching to the terminal, firing up IPython and
generating it, just type it and evaluate it.


Imported context:
-----------------

By default all of `math`, `collections`, `datetime`, `os`, `sys`, `itertools`
all imported into the local context where your code will evaluate.
That means that `math.sin(123.45)` works, as well as `os.listdir()`.

If you have a `helpers.py` module in your `Packages` folder, it will
be included as well. You can modify the default settings file to add
other imports you want.


Automatic counter:
------------------

The local context also contains a handy automatic counter variable,
under the name of `_`. For instance, suppose you have the following
text, somewhere in your files:

    item -> blah blah blah
    item -> bleh bleh bleh
    item -> bluh bluh bluh

Very easily with ST3 you can select all `item`, append and `_` at the
end, select the three `_`s:

    item_ -> blah blah blah
    item_ -> bleh bleh bleh
    item_ -> bluh bluh bluh

Hit `ctrl+shift+e` and it will transforms to:

    item0 -> blah blah blah
    item1 -> bleh bleh bleh
    item2 -> bluh bluh bluh

In fact, `_` is actually a bit more complicated than that. You
can call it like a function with a parameter and it will increase
a different counter for each different parameter.
For instance:

    item_(0) -> blah blah blah
    item_(0) -> bleh bleh bleh
    item_(1) -> bluh bluh bluh
    item_(1) -> bloh bloh bloh

Transforms into:

    item0 -> blah blah blah
    item1 -> bleh bleh bleh
    item0 -> bluh bluh bluh
    item1 -> bloh bloh bloh

You can use any Python type, like `int` or `str` for the argument
of `_`.


License:
--------

The MIT License (MIT)

Copyright (c) 2014 Alejandro Piad

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Summing up: MIT! Use at your own risk...


Forking, collaborating or whatever:
-----------------------------------

Sure, come to [Github](https://github.com/apiad/Sublime-InlinePython).
