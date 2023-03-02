import time
from mingus.core import notes,chords
from mingus.containers import *
from mingus.midi import fluidsynth
sf="Final_Guitar1.SF2"
fluidsynth.init(sf,"alsa")
# fluidsynth.set_instrument(1,25)
note_container=NoteContainer(["E-1","B-1","E-2","G-2","B-2","E-3"])
# g=Guitar()
i =0
x=0.01
while 1:
    fluidsynth.play_Note(Note(note_container[i].name),1,100)
    time.sleep(x)
    fluidsynth.play_Note(Note(note_container[i+1].name),1,100)
    time.sleep(x)
    fluidsynth.play_Note(Note(note_container[i+2].name),1,100)
    time.sleep(x)
    fluidsynth.play_Note(Note(note_container[i+3].name),1,100)
    time.sleep(x)
    fluidsynth.play_Note(Note(note_container[i+4].name),1,100)
    time.sleep(x)
    fluidsynth.play_Note(Note(note_container[i+5].name),1,100)
    # time.sleep(0.03)
    time.sleep(1)
    # fluidsynth.stop_Note(Note(note_container[i].name),1)
    # time.sleep(0.02)
    # fluidsynth.stop_Note(Note(note_container[i+1].name),1)
    # time.sleep(0.02)
    # fluidsynth.stop_Note(Note(note_container[i+2].name),1)
    # time.sleep(0.04)
    # fluidsynth.stop_Note(Note(note_container[i+3].name),1)
    # time.sleep(0.04)
    # fluidsynth.stop_Note(Note(note_container[i+4].name),1)
    # time.sleep(0.04)
    # fluidsynth.stop_Note(Note(note_container[i+5].name),1)
    # time.sleep(0.15)
    # time.sleep(0.2)
#  while 1:
#     n1=Note("E-3")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
#     n1=Note("B-3")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
#     n1=Note("E-4")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
#     n1=Note("G-4")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
#     n1=Note("B-4")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
#     n1=Note("E-5")
#     n1.channel=5
#     n1.velocity=100
#     print(fluidsynth.play_Note(n1))
#     time.sleep(0.5)
    # print(fluidsynth.stop_Note(n1,1))
