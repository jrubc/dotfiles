# .config/qtile/modules/groups.py
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .variables import mod5

groups = [
    Group("1", label=""),
    Group("2", label=""),
    Group("3", label=""),
    Group("4", label=""),
    Group("5", label="󰝚"),
    Group("6", label=""),
    Group("7", label=""),
    Group("8", label=""),
    Group("9", label=""),
]

group_keys = []

for group in groups:
    group_keys.extend([
        Key([mod5], group.name, lazy.group[group.name].toscreen(), desc=f"Switch to group {group.name}"),
        Key([mod5, "shift"], group.name, lazy.window.togroup(group.name, switch_group=True), desc=f"Switch to & move focused window to group {group.name}"),
    ])

# If you want to add the VT switching keys, better define them somewhere else 
# where you can safely access qtile or remove the 'when' condition if not needed.

__all__ = ["groups", "group_keys"]
