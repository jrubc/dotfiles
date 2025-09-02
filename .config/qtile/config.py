# Variables imported to be used by Qtile

from modules.variables import mod
from modules.groups import groups
from modules.keys import keys
from modules.layouts import layouts
from modules.screens import screens
from modules.widgets import widget_defaults, extension_defaults
from modules.floating import floating_layout
from modules.settings import *
from libqtile import hook
import subprocess

# Assign to _ to avoid unused import warnings
_ = mod
_ = groups
_ = keys
_ = layouts
_ = screens
_ = widget_defaults
_ = extension_defaults
_ = floating_layout

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(['setxkbmap', 'latam'])
    subprocess.Popen(['nm-applet'])
    subprocess.Popen(['volumeicon'])
