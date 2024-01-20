import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import platform
import random

def show_warning():
    messages = [
        "Warning: This program is in a test version, which may no longer be present or under go changes in the future."
    ]
    random_message = random.choice(messages)
    messagebox.showwarning("Warning", random_message)

def show_system_info():
    system_info = platform.uname()
    process_info = list(psutil.process_iter(['name', 'status', 'cpu_percent', 'memory_percent']))

    info_window = tk.Toplevel()
    info_window.title("Resource Manager (Beta)")

    system_label = tk.Label(info_window, text=f"System: {system_info.system} {system_info.release}")
    system_label.pack()

    phantom_label = tk.Label(info_window, text="Phantom AK 1.8.1")
    phantom_label.pack()

    processes_label = tk.Label(info_window, text="Processes Information:")
    processes_label.pack()

    # Label for total CPU percentage
    total_cpu_percent = psutil.cpu_percent()
    cpu_total_label = tk.Label(info_window, text=f"Total CPU Usage: {total_cpu_percent}% / 100%")
    cpu_total_label.pack()

    # Label for total memory percentage
    total_memory_percent = psutil.virtual_memory().percent
    memory_total_label = tk.Label(info_window, text=f"Total Memory Usage: {total_memory_percent}% / 100%")
    memory_total_label.pack()

    # Create the table
    table = ttk.Treeview(info_window, columns=('Name', 'Status', '% CPU', '% Memory'), show='headings')
    table.heading('Name', text='Name')
    table.heading('Status', text='Status')
    table.heading('% CPU', text='% CPU')
    table.heading('% Memory', text='% Memory')
    
    # Configure vertical lines to separate the columns
    table.column('Name', anchor=tk.W, width=150)
    table.column('Status', anchor=tk.CENTER, width=80)
    table.column('% CPU', anchor=tk.CENTER, width=80)
    table.column('% Memory', anchor=tk.CENTER, width=80)

    # Insert data into the table
    for i, process_info_item in enumerate(process_info[:10]):
        try:
            pid = process_info_item.info['pid']
        except KeyError:
            pid = 'N/A'
            
        table.insert('', i, values=(process_info_item.info['name'], process_info_item.info['status'],
                                    f"{process_info_item.info['cpu_percent']:.2f}", f"{process_info_item.info['memory_percent']:.2f}"))

    table.pack()

if __name__ == "__main__":
    main_window = tk.Tk()
    
    warning_button = tk.Button(main_window, text="Show Warning", command=show_warning)
    warning_button.pack()

    show_info_button = tk.Button(main_window, text="Manage Resources", command=show_system_info)
    show_info_button.pack()

    main_window.mainloop()
