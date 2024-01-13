import tkinter as tk
import os
import pygame
import random

# Initialize pygame
pygame.init()

# Create the main window
window = tk.Tk()
window.title("Music Player")

# Music folder
script_directory = os.path.dirname(os.path.abspath(__file__))
music_folder = os.path.join(os.path.expanduser("~/Documents/Phantom-AK-1.8"), "Music")


print(f"Music Folder: {music_folder}")
songs = [file for file in os.listdir(music_folder) if file.endswith(".mp3")]

# Function to play a song
def play_song():
    selection = song_list.curselection()
    if selection:
        song = songs[selection[0]]
        pygame.mixer.music.load(os.path.join(music_folder, song))
        pygame.mixer.music.play()

# Function to stop playback
def stop_playback():
    pygame.mixer.music.stop()

# Function to play the next song
def next_song():
    selection = song_list.curselection()
    if selection:
        index = selection[0] + 1
        if index < len(songs):
            song = songs[index]
            pygame.mixer.music.load(os.path.join(music_folder, song))
            pygame.mixer.music.play()

# Function to play the previous song
def previous_song():
    selection = song_list.curselection()
    if selection:
        index = selection[0] - 1
        if index >= 0:
            song = songs[index]
            pygame.mixer.music.load(os.path.join(music_folder, song))
            pygame.mixer.music.play()

# Function to play a random song
def play_random_song():
    random_song = random.choice(songs)
    pygame.mixer.music.load(os.path.join(music_folder, random_song))
    pygame.mixer.music.play()

# Song list
song_list = tk.Listbox(window)
song_list.config(height=20, width=50)  # Increase width to 80 characters
for song in songs:
    song_list.insert(tk.END, song)
song_list.pack()

# Buttons
play_button = tk.Button(window, text="Play", command=play_song)
play_button.pack(side=tk.LEFT)

stop_button = tk.Button(window, text="Stop", command=stop_playback)
stop_button.pack(side=tk.LEFT)

next_button = tk.Button(window, text="Next", command=next_song)
next_button.pack(side=tk.LEFT)

previous_button = tk.Button(window, text="Previous", command=previous_song)
previous_button.pack(side=tk.LEFT)

shuffle_button = tk.Button(window, text="Shuffle", command=play_random_song)
shuffle_button.pack(side=tk.LEFT)

# Run the window
window.mainloop()
