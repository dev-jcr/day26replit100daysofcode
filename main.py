# os library, Audio player UI

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu: ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True #let's pause the file
      return
    else:
      continue

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 My POD Music Player🎵")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue