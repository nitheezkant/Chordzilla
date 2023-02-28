import pygame
from gpiozero import Button
from time import sleep
import RPi.GPIO as g
pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load("/home/nitheez/Downloads/c-d.mp3")
#M=[["a"],["a"],["/home/nitheez/Downloads/c-u.mp3"],"d","e","f",g 
path="/home/nitheez/Downloads/"

ac=["we use 1 indexing","c","d","em","g"]

g.setmode(g.BCM)
g.setup(2,g.IN)
g.setup(3,g.IN)
g.setup(4,g.IN)
g.setup(5,g.IN)

g.setup(6,g.IN)
g.setup(7,g.IN)

c1=g.setup(2,g.IN)
c2=g.setup(3,g.IN)
c3=g.setup(4,g.IN)
c4=g.setup(5,g.IN)


u=g.input(6)
d=g.input(7)

fu=0
fd=0
while True:
	if u==0 and fu==1:
		fu=0
	if u and fu==0:
		pygame.mixer.music.stop()
		if c1:
			pygame.mixer.music.load(path+ac[1]+"-u.mp3")
		elif c2:
			pygame.mixer.music.load(path+ac[2]+"-u.mp3")
		elif c3:
			pygame.mixer.music.load(path+ac[3]+"-u.mp3")
		elif c4:
			pygame.mixer.music.load(path+ac[4]+"-u.mp3")
		pygame.mixer.music.play()
		fu=1
	if d==0 and fd==1:
		fd=0
	if d and fd==0:
		pygame.mixer.music.stop()
		if c1:
			pygame.mixer.music.load(path+ac[1]+"-d.mp3")
		elif c2:
			pygame.mixer.music.load(path+ac[2]+"-d.mp3")
		elif c3:
			pygame.mixer.music.load(path+ac[3]+"-d.mp3")
		elif c4:
			pygame.mixer.music.load(path+ac[4]+"-d.mp3")
		pygame.mixer.music.play()
		fd=1
