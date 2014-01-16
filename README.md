Sublime-InlinePython
====================

A Sublime Text 3 plugin that evaluates and replaces the selected Python code.

Usage:
------

Add the following key bindings to your preferences:

    { "keys": ["ctrl+alt+e"], "command": "inline_python" },

You can of course use a different key binding.

Next, on any open file, select a valid Python expression, and press
`ctrl+alt+e` to replace the selection for it's the Python `repr`. If the
evaluation throws any exception, you'll see it in the console, and your text
will be unchanged.


License:
--------

MIT! Use at your own risk...


Forking, collaborating or whatever:
-----------------------------------

Sure, come to [Github](https://github.com/apiad/Sublime-InlinePython).
