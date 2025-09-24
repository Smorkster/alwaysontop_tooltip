"""
A demo script demonstrating AlwaysOnTopToolTip

Author: Smorkster
GitHub: https://github.com/Smorkster/splashscreen
License: MIT
Version: 1.2
Created: 2025-08-11
"""

import tkinter as tk
from tkinter.ttk import Button
from alwaysontop_tooltip import AlwaysOnTopToolTip

def main():
    def config_tt():
        tt.config( new_text = 'ToolTip have a new text', new_font = ( 'Arial', 12, 'italic' ) )

    root = tk.Tk()
    root.title( 'AlwaysOnTopToolTip Demo' )
    root.geometry( '300x200' )

    label = tk.Label( root, text = 'Hover over me', font = ( "Arial", 14 ) )
    label.grid( row = 0 )

    tt = AlwaysOnTopToolTip(
        label,
        msg = "This is an always-on-top tooltip, with blinking effect, that appears when you hover over Tkinter widgets.",
        delay = 500,
        bg = "#f0f0f0",
        font = ( "Verdana", 10 ),
        wraplength = 350,
        borderstyle = 'solid',
        borderwidth = 2,
        stationary = True,
        #blink = {
        #        "enabled": True,
        #        "interval": 200,
        #        "mode": "opacity",
        #        "min_alpha": -2.3,
        #        "max_alpha": 1.0,
        #        "step": 0.9,
        #        "duration": 3000  # Stops after 3 seconds
        #    }
        )

    btn = Button( root, text = 'Click me', command = config_tt )
    btn.grid( row = 1 )

    root.grid_rowconfigure( index = 0 , weight = 0 )
    root.grid_rowconfigure( index = 1 , weight = 0 )
    root.mainloop()

if __name__ == "__main__":
    main()
