import os
from pathlib import Path
from libqtile import bar, widget
from libqtile.config import Screen
from .colors import *

wallpaper = str(Path(__file__).resolve().parent.parent / "assets" / "anime.png")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line',
                    this_current_screen_border=cyan,
                    active=blue,
                    inactive=green,
                    font='Maple Mono NL',
                    fontsize=23,
                    disable_drag=True,
                    use_mouse_wheel=True,
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=magenta
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(
                    background=green
                ),
                widget.Clock(
                    background=yellow,
                    foreground=dark,
                    format="%Y-%m-%d %a %I:%M %p"
                ),
                widget.QuickExit(
                    background=red,
                    foreground=dark
                ),
            ],
            25,
        ),
        wallpaper=wallpaper,
        wallpaper_mode="fill",
    ),
]
