import tkinter as tk
import os
import platform

def show_technical_information():
    def on_key_press(event):
        if event.char.lower() == 'j':
            update_ferel_message()

    def update_ferel_message():
        ferel_message = f"""
        Phantom AK Codename Jazel 
        (Build PA-1.8.1.227)
        
        This program is dedicated to Jazmin<3
        
        Written on December 21, 2023
        
        Created by Gael Meza
        
        Technical Information:
        OS: {os.name if os.name != 'posix' else 'Linux'}
        Architecture: {architecture}
        """
        info_label.config(text=ferel_message)

    info_window = tk.Tk()
    info_window.title("About Phantom AK")

    initial_message = f"""
        Phantom AK 1.8.1
        (Build PA-1.8.1.227)
        
        The PhantomAK program is distributed under the terms of
        the GNU General Public License
        
        Technical Information:
        OS: {os.name if os.name != 'posix' else 'Linux'}
        Architecture: {architecture}
    """

    info_label = tk.Label(info_window, text=initial_message)
    info_label.pack()

    info_window.bind('<KeyPress>', on_key_press)

    info_window.mainloop()

if __name__ == "__main__":
    architecture = platform.machine()
    show_technical_information()
