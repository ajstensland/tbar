# tbar
An ultra-configurable terminal status bar for tmux users.

I recently made the switch to i3wm, but noticed that I didn't really enjoy the i3-bar. I didn't really want an extra GUI element taking up screen real estate, and I wanted everything to be consolidated into one place. One day, I noticed that a status bar could easily fit inside of a shrunken tmux pane, and thus tbar was born!

## Features
### Widgets
1. Time
1. Battery Percentage

    ...and more to come! (See *Planned Features* below)

### Customization
tbar is customizable in gratuitously many ways. If you want, the options are out there to:
  * Change the foreground and background colors of each individual piece of your tbar (e.g. widget labels, non-widget labels, widget contents, special widget contents, etc.)
  * Change the time widget format (e.g. 24-hour, include AM/PM, put a gap between the time and AM/PM, etc.)
  * Change the percent at which your battery widget will change color to signify low power
  * Change the layout of your tbar with intuitive markup (e.g. spread it over multiple lines, add decorations and extra text, etc.)

## Install
#### *CURRENTLY, TBAR IS ONLY WRITTEN FOR LINUX SYSTEMS.*

#### Directions
1. Make sure you have Python 3.x and tmux installed
1. Clone this repo to a directory of your choice

## Usage
#### To run tbar:
1. Start tmux in your terminal
1. Split the window horizontally (i.e. two terminals on top of one another)
1. Shrink the upper terminal as small as you please
1. Run `python tbar.py` in it

#### To configure tbar:
1. Open up the included `tbar.conf` in your text editor of choice
1. Read the included comments on every line to configure tbar to your heart's desire!

    **Note:** `tbar.conf` is in `.ini` format

## Planned Features
### Widgets
1. Battery Estimated Time (with all of the formatting options of the time widget)
1. Power Status (e.g. using battery, charging)
1. Date (with many different date formats)

### Other Features
1. Add support for bars at the bottom of the terminal
1. Configuration file validation
1. More time format configurations (e.g. "Nine twenty, P.M.", HH:MM:SS)
1. Windows/MacOS support

### Fixes
1. Change `line1` in config to `format` or something, since it determines all lines
1. Simplify time formatting logic
1. Disable newline printing
