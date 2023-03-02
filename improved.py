import pygame
import RPi.GPIO as g

pygame.mixer.pre_init(44100, 16, 2, 256) #frequency, size, channels, buffersize
pygame.init()

path = "/home/nitheez/Downloads/New/"
ac = [["we use 1 indexing","e1.ogg","d","em","g"],
      ["we use 1 indexing","a1.ogg","d","em","g"],
      ["we use 1 indexing","e2.ogg","d","em","g"],
      ["we use 1 indexing","a2.ogg","d","em","g"],
      ["we use 1 indexing","c3.ogg","d","em","g"],
      ["we use 1 indexing","e3.ogg","d","em","g"]]

buttons = [    {"pin": 8, "sound": pygame.mixer.Sound(path + ac[0][1]), "channel": pygame.mixer.Channel(0)},
    {"pin": 9, "sound": pygame.mixer.Sound(path + ac[1][1]), "channel": pygame.mixer.Channel(1)},
    {"pin": 10, "sound": pygame.mixer.Sound(path + ac[2][1]), "channel": pygame.mixer.Channel(2)},
    {"pin": 11, "sound": pygame.mixer.Sound(path + ac[3][1]), "channel": pygame.mixer.Channel(3)},
    {"pin": 20, "sound": pygame.mixer.Sound(path + ac[4][1]), "channel": pygame.mixer.Channel(4)},
    {"pin": 21, "sound": pygame.mixer.Sound(path + ac[5][1]), "channel": pygame.mixer.Channel(5)}
]

g.setmode(g.BCM)

for button in buttons:
    g.setup(button["pin"], g.IN, pull_up_down=g.PUD_UP)

def button_pressed(pin):
    for button in buttons:
        if button["pin"] == pin and g.input(2):
            button["channel"].play(button["sound"])

for button in buttons:
    g.add_event_detect(button["pin"], g.FALLING, callback=lambda pin: button_pressed(pin), bouncetime=50)

while True:
    pass
