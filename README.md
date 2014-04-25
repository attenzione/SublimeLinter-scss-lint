SublimeLinter-scss-lint
=========================

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to the [scss-lint](https://github.com/causes/scss-lint). It will be used with files that have the “SCSS” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `scss-lint` is installed on your system. To install `scss-lint`, do the following:

1. Install [Ruby](http://ruby-lang.org/).

2. Install `scss-lint` by typing the following in a terminal:
   ```
   gem install scss-lint
   ```

3. If you are using `rvm` or `rbenv`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.

Once scss-lint is installed, you can proceed to install the SublimeLinter-scss-lint plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `linter scss`. Among the entries you should see `SublimeLinter-scss-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `scss-lint` options in the way you would from the command line, with `.scss-lint.yml` files. If a `.scss-lint.yml` file is not found in the file hierarchy starting with the linted file, your home directory will also be searched. For more information, see the [scss-lint page](https://github.com/causes/scss-lint). Default configuration file can be found [here](https://github.com/causes/scss-lint/blob/master/config/default.yml).

In addition to the standard SublimeLinter settings, SublimeLinter-scss-lint provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings).

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|bundle-exec|runs scss-lint as "bundle exec scss-lint" instead of "scss-lint"| | |
|--include-linter|Specify which linters you specifically want to run| |&#10003;|
|--exclude-linter|Specify which linters you don't want to run| |&#10003;|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
