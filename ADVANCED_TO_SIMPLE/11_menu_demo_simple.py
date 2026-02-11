"""
Simplified version of 11_menu_demo.py

ORIGINAL: Separate handler function for every single menu action,
repetitive add_command calls.
SIMPLIFIED: Uses a dict-driven menu builder and a single generic handler.
"""

from tkinter import *
from tkinter import ttk
import sys


class MenuDemo:
    def __init__(self):
        root = Tk()
        root.title("HelloWin")
        root.option_add("*tearOff", False)

        menu_bar = Menu(root)
        root.configure(menu=menu_bar)

        # Define menu structure as data
        menus = {
            "File": ["New", "Open", "---", "Save", "SaveAs", "---", "Exit"],
            "Edit": ["Cut", "Copy", "Paste", "---",
                      {"Actions": ["Undo", "Redo"]}],
        }

        for menu_name, items in menus.items():
            menu = Menu(menu_bar)
            menu_bar.add_cascade(menu=menu, label=menu_name)
            self._build_menu(menu, menu_name, items)

        root.mainloop()

    def _build_menu(self, parent_menu, path, items):
        for item in items:
            if item == "---":
                parent_menu.add_separator()
            elif isinstance(item, dict):
                for sub_name, sub_items in item.items():
                    sub_menu = Menu(parent_menu)
                    parent_menu.add_cascade(menu=sub_menu, label=sub_name)
                    self._build_menu(sub_menu, f"{path}->{sub_name}", sub_items)
            else:
                full_path = f"Menubar->{path}->{item}"
                if item == "Exit":
                    parent_menu.add_command(label=item, command=lambda: sys.exit(0))
                else:
                    parent_menu.add_command(
                        label=item,
                        command=lambda p=full_path: print(p),
                    )


if __name__ == "__main__":
    MenuDemo()
