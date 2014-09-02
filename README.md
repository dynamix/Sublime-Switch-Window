*slightly modified to work with Sublime 3 and windows with project data*


SwitchWindow
============

An OSX-only Sublime Text 2 plugin for switching between open windows without having to open the Window menu.

This plugin could be a lot simpler (and faster), but I ran into lots of problems trying to get it to work correctly on OSX.
[This bug](http://www.sublimetext.com/forum/viewtopic.php?f=3&t=10691) led to a very ugly and platform-specific workaround.

### Install: ###

    # The path to Sublime Packages on OSX is usually /Users/{user}/Library/Application Support/Sublime Text 2/Packages/
    cd {SUBLIME_PACKAGES_PATH}
    git clone https://github.com/deborasetton/Sublime-Switch-Window.git SwitchWindow

### Usage: ###

The default key binding is `Command + Shift + .`.


### TODO: ###

- Bind to new window event (even though it doesn't look like it's possible);

### License ###

MIT License. Copyright 2013 Débora Setton.
