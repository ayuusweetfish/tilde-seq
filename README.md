# Tilde sequencer {'~'}

![ ](icon_large.png)

**Tilde** is a simplistic music sequencer that speaks the [Organya](https://cavestory.fandom.com/wiki/Soundtrack) format.

Tilde is entirely built in [Pixilang](http://warmplace.ru/soft/pixilang/) and runs on all platforms that Pixilang supports (Windows, Linux, macOS, iOS, Android and Windows CE), although it's primarily designed for desktop environments.

## Running

* Download Pixilang.
* Put `pixilang_config.ini` in the repository in the same folder as the Pixilang executable.
* Run the Pixilang executable, select `boot.pixi` and rock.

## Controls

### Read me first

Range actions (cut, copy, paste) and playback only involve **selected tracks** (see below). Other than that the controls should be intuitive.

### Mouse (piano roll)

* Draw/drag to create/edit notes
* **Ctrl**-drag to move around
* Scroll to move horizontally
* **Shift**-scroll to move vertically
* **Ctrl**-scroll to zoom horizontally
* **Ctrl**-**Shift**-scroll to zoom vertically
* Drag in the selection area (white bar on the top) to select

### Keyboard shortcuts

* Track tag (**1/2/3/4/5/6/7/8/Q/W/E/R/T/Y/U/I**): Select track
* **Ctrl-N**: New
* **Ctrl-O**: Open
* **Ctrl-S**: Save
* **Ctrl-Z**: Undo
* **Shift-Ctrl-Z**: Redo
* **Ctrl-X**: Cut
* **Ctrl-C**: Copy
* **Ctrl-V**: Paste
* **Space**: Play/Stop
* **Ctrl-P**: Options
* **Ctrl-,**: Config
* **Up/Down**: Transpose
* **Ctrl-Up/Down**: Transpose by octaves

### Secondary menu actions

* **Ctrl**-any track (**Ctrl-1/2/3/4/5/6/7/8/Q/W/E/R/T/Y/U/I**): Multiple track selection
* **Shift**-any track (**Shift-1/2/3/4/5/6/7/8/Q/W/E/R/T/Y/U/I**): Range track selection
* **Shift**-Save (**Shift-Ctrl-S**): Save as
* **Shift**-Cut (**Shift-Ctrl-X**): Clear selection
* **Shift**-Copy (**Shift-Ctrl-C**): Set as loop range
* **Shift**-Play (**Shift-Space**): Play all tracks

## To-do lists, known issues and notes

* Pipi support

  The main problem is to find a place in the options panel. Suggestions welcome!

* Org-2 constraint check

  To-do.

* Compiled & packaged version

  To-do.

* **(Fixed)** ~~Copying makes changes in the tracks~~

* Pressing Escape key on the file selection dialogue causes the program to freeze and/or quit

  This is an upstream issue and is present in a few recent Pixilang versions. It's because the `DECOR_FLAG_CLOSE_ON_ESCAPE` flag is (incorrectly) set at dialogue creation. See `lib_sundog/window_manager/code/wmanager.cpp`, line 4015 in Pixilang version 3.7b source code.

  The best solution so far is... to just resist the desire to press Esc to exit there. Or maybe change the above line and compile your modified Pixilang.

* **(Fixed)** ~~The timbre sounds different from other programs~~

* Occasional clipping

  Maybe include a gentle compressor?

## Licence & acknowledgements

The Organya format is created by [Studio Pixel](http://studiopixel.sakura.ne.jp/).

[fdeitylink's gist](https://gist.github.com/fdeitylink/7fc9ddcc54b33971e5f505c8da2cfd28) provides a detailed specification of the format.

[Organya 2](https://github.com/shbow/organya) is a reference implementation of many components.

[Cave Story tribute site](https://www.cavestory.org/) has provided abundant information on the game, its music and fan works.
