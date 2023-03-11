import time
from mingus.core import notes,chords
from mingus.containers import *
from mingus.midi import fluidsynth

from gpiozero import Button
import RPi.GPIO as g
import serial

def setting():
	uart_channel = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=2)
	data1=""
	data2=""
	while(1):
		data2=uart_channel.read(100)
		print(data2)
		data2=str(data2.decode())
		data1+=data2
		if(data2!=""):
			break
		
		uart_channel.flush()
		data1=""
		data2=""
	chords= data2.split()
	print(chords)
	for i in range(len(chords)):

		if chords[i]=="A..":
			active_chords[i]=A
		elif chords[i]=="B..":
			active_chords[i]=B
		elif chords[i]=="C..":
			active_chords[i]=C
		elif chords[i]=="D..":
			active_chords[i]=D
		elif chords[i]=="E..":
			active_chords[i]=E
		elif chords[i]=="F..":
			active_chords[i]=F
		elif chords[i]=="G..":
			active_chords[i]=G

		elif chords[i]=="Am.":
			active_chords[i]=Am
		elif chords[i]=="Bm.":
			active_chords[i]=Bm
		elif chords[i]=="Cm.":
			active_chords[i]=Cm
		elif chords[i]=="Dm.":
			active_chords[i]=Dm
		elif chords[i]=="Em.":
			active_chords[i]=Em
		elif chords[i]=="Fm.":
			active_chords[i]=Fm
		elif chords[i]=="Gm.":
			active_chords[i]=Gm

		elif chords[i]=="A#m":
			active_chords[i]=Asm
		elif chords[i]=="C#m":
			active_chords[i]=Csm
		elif chords[i]=="D#m":
			active_chords[i]=Dsm
		elif chords[i]=="F#m":
			active_chords[i]=Fsm
		elif chords[i]=="G#m":
			active_chords[i]=Gsm

		elif chords[i]=="A7.":
			active_chords[i]=A7
		elif chords[i]=="B7.":
			active_chords[i]=B7
		elif chords[i]=="C7.":
			active_chords[i]=C7
		elif chords[i]=="D7.":
			active_chords[i]=D7
		elif chords[i]=="E7.":
			active_chords[i]=E7
		elif chords[i]=="F7.":
			active_chords[i]=F7
		elif chords[i]=="G7.":
			active_chords[i]=G7

		elif chords[i]=="A#7":
			active_chords[i]=As7
		elif chords[i]=="C#7":
			active_chords[i]=Cs7
		elif chords[i]=="D#7":
			active_chords[i]=Ds7
		elif chords[i]=="F#7":
			active_chords[i]=Fs7
		elif chords[i]=="G#7":
			active_chords[i]=Gs7

		elif chords[i]=="A#.":
			active_chords[i]=As
		elif chords[i]=="C#.":
			active_chords[i]=Cs
		elif chords[i]=="D#.":
			active_chords[i]=Ds
		elif chords[i]=="F#.":
			active_chords[i]=Fs
		elif chords[i]=="G#.":
			active_chords[i]=Gs
		else:
			active_chords[i]=StdTun
	print(active_chords)
	return
	


uart_channel = serial.Serial("/dev/ttyAMA0",baudrate=9600,timeout=2)
data1=""
data2=""
while(1):
	data2=uart_channel.read(1)
	data2=str(data2.decode())
	data1+=data2
	if(data2!=""):
		break
	
	uart_channel.flush()
	data1=""
	data2=""


SFFILES=["1.SF2","2.sf2","3.sf2","4.sf2","5.sf3","6.sf2"]	
sf=SFFILES[int(data2)-1]
fluidsynth.init(sf,"alsa")
# fluidsynth.set_instrument(1,25)
fluidsynth.main_volume(1,1000)
A = NoteContainer(["E-2","A-2","E-3","A-3","C#-3","E-4"])
Am = NoteContainer(["E-2","A-2","E-3","A-3","C-3","E-4"])
A7 = NoteContainer(["E-2", "A-2", "E-3", "G-3", "C#-4", "E-4"])

As = NoteContainer(["F-2","A#-2","F-3","A#-3","D-4","F-4"])
Asm = NoteContainer(["F-2", "A#-2", "F-3", "A#-3", "C#-4", "F-4"])
As7 = NoteContainer(["F-2", "A#-2", "F-3", "G#-3", "D-4", "F-4"])

B = NoteContainer(["F#-2","B-2","F#-3","B-3","D#-4","F#-4"])
Bm = NoteContainer(["G-2","C-3","G-3","C-4","D#-4","G-4"])
B7 = NoteContainer(["B-2", "F#-3", "A-3", "D#-4", "F#-4", "B-4"])

C = NoteContainer(["E-2","C-3","E-3","G-3","C-4","E-4"])
Cm = NoteContainer(["C-1","G-1","C-2","D#-2","G-2","C-3"])
C7 = NoteContainer(["E-2", "C-3", "G-3", "A#-3", "E-4", "G-4"])

Cs = NoteContainer(["F-2", "C#-3", "F-3", "G#-3", "C#-4", "F-4"])
Csm = NoteContainer(["G#-2","C#-3","G#-3","C#-4","E-4","G#-4"])
Cs7 = NoteContainer(["G#-2","C#-3","G#-3","B-3","F-4","G#-4"])

D = NoteContainer(["A-2","D-3","A-3","D-4","F#-4","A-4"])
Dm = NoteContainer(["A-2","D-3","A-3","D-4","F-4","A-4"])
D7 = NoteContainer(["A-2", "D-3", "A-3", "C-4", "F#-4","A-4"])

Ds = NoteContainer(["A#-2", "D#-3", "A#-3", "D#-4", "G-4", "A#-4"])
Dsm = NoteContainer(["A#-2","D#-3","A#-3","D#-4","F#-4","A#-4"])
Ds7 = NoteContainer(["A#-2","D#-3","A#-3","C#-4","G-4","A#-4"])

E = NoteContainer(["E-2","B-2","E-3","G#-3","B-3","E-4"])
Em = NoteContainer(["E-2","B-2","E-3","G-3","B-3","E-4"])
E7 = NoteContainer(["E-2", "B-2", "D-3", "G#-3", "D-4","E-4"])

F = NoteContainer(["F-2","C-3","F-3","A-3","C-4","F-4"])
Fm = NoteContainer(["F-2","C-3","F-3","G#-3","C-4","F-4"])
F7 = NoteContainer(["F-2", "C-3", "D#-3", "A-3", "C-4","F-4"])

Fs = NoteContainer(["F#-2", "C#-3", "F#-3", "A#-3", "C#-4", "F#-4"])
Fsm = NoteContainer(["F#-2","C#-2","F#-3","A-3","C#-4","F#-4"])
Fs7 = NoteContainer(["F#-2","C#-3","E-3","A#-3","E-4","F#-4"])

G = NoteContainer(["G-2","B-2","D-3","G-3","B-3","G-4"])
Gs = NoteContainer(["C-2", "G#-2", "C-3", "D#-3", "G#-3", "C-4"])
G7 = NoteContainer(["G-2", "B-2", "D-3", "G-3", "B-3","F-4"])

Gm = NoteContainer(["G-2","D-3","G-3","A#-3","D-4","G-4"])
Gsm = NoteContainer(["G#-2","D#-3","G#-3","B-3","D#-4","G#-4"])
Gs7 = NoteContainer(["G#-2","D#-3","F#-3","C-4","F#-4","G#-4"])

StdTun = NoteContainer(["E-2","A-2","D-3","G-3","B-3","E-4"])

active_chords=[StdTun,StdTun,StdTun,StdTun,StdTun,StdTun,StdTun,StdTun]



g.setmode(g.BCM)
g.setup(2,g.IN)
g.setup(3,g.IN)
g.setup(4,g.IN)
g.setup(5,g.IN)
g.setup(6,g.IN)
g.setup(7,g.IN)
g.setup(16,g.IN)
g.setup(17,g.IN)

g.setup(8,g.IN)
g.setup(9,g.IN)
g.setup(10,g.IN)
g.setup(11,g.IN)
g.setup(20,g.IN)
g.setup(21,g.IN)

g.setup(26,g.IN)

u=g.input(6)
d=g.input(7)

f8=0
f9=0
f10=0
f11=0
f20=0
f21=0
x=0.04

while True:

	"""print("Chord 1 = ",g.input(2))
	print("Chord 2 = ",g.input(3))
	print("Chord 3 = ",g.input(4))
	print("Chord 4 = ",g.input(5))
	print("Chord 5 = ",g.input(6))
	print("Chord 6 = ",g.input(7))
	print("Chord 7 = ",g.input(16))
	print("Chord 8 =",g.input(17))"""
	if g.input(8)==0 and f8==1:
		f8=0
	if g.input(8) and f8==0:
		print("iuykjgtf")
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][0].name,active_chords[0][0].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][0].name,active_chords[1][0].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][0].name,active_chords[2][0].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][0].name,active_chords[3][0].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][0].name,active_chords[4][0].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][0].name,active_chords[5][0].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][0].name,active_chords[6][0].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][0].name,active_chords[7][0].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[0].name,StdTun[0].octave),1,127)

		f8=1
	
	
	if g.input(9)==0 and f9==1:
		f9=0
	if g.input(9) and f9==0:
		
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][1].name,active_chords[0][1].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][1].name,active_chords[1][1].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][1].name,active_chords[2][1].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][1].name,active_chords[3][1].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][1].name,active_chords[4][1].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][1].name,active_chords[5][1].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][1].name,active_chords[6][1].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][1].name,active_chords[7][1].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[1].name,StdTun[1].octave),1,127)
		f9=1
		
	if g.input(10)==0 and f10==1:
		f10=0
	if g.input(10) and f10==0:
		
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][2].name,active_chords[0][2].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][2].name,active_chords[1][2].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][2].name,active_chords[2][2].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][2].name,active_chords[3][2].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][2].name,active_chords[4][2].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][2].name,active_chords[5][2].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][2].name,active_chords[6][2].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][2].name,active_chords[7][2].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[2].name,StdTun[2].octave),1,127)
		f10=1
		
		
	if g.input(11)==0 and f11==1:
		f11=0
	if g.input(11) and f11==0:
		
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][3].name,active_chords[0][3].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][3].name,active_chords[1][3].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][3].name,active_chords[2][3].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][3].name,active_chords[3][3].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][3].name,active_chords[4][3].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][3].name,active_chords[5][3].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][3].name,active_chords[6][3].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][3].name,active_chords[7][3].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[3].name,StdTun[3].octave),1,127)
		f11=1
		
	if g.input(20)==0 and f20==1:
		f20=0
	if g.input(20) and f20==0:
		
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][4].name,active_chords[0][4].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][4].name,active_chords[1][4].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][4].name,active_chords[2][4].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][4].name,active_chords[3][4].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][4].name,active_chords[4][4].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][4].name,active_chords[5][4].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][4].name,active_chords[6][4].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][4].name,active_chords[7][4].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[4].name,StdTun[4].octave),1,127)
		f20=1
	
	if g.input(21)==0 and f21==1:
		f21=0
	if g.input(21) and f21==0:
		
		if g.input(2):
			fluidsynth.play_Note(Note(active_chords[0][5].name,active_chords[0][5].octave),1,127)
		elif g.input(3):
			fluidsynth.play_Note(Note(active_chords[1][5].name,active_chords[1][5].octave),1,127)
		elif g.input(4):
			fluidsynth.play_Note(Note(active_chords[2][5].name,active_chords[2][5].octave),1,127)
		elif g.input(5):
			fluidsynth.play_Note(Note(active_chords[3][5].name,active_chords[3][5].octave),1,127)
		elif g.input(6):
			fluidsynth.play_Note(Note(active_chords[4][5].name,active_chords[4][5].octave),1,127)
		elif g.input(7):
			fluidsynth.play_Note(Note(active_chords[5][5].name,active_chords[5][5].octave),1,127)
		elif g.input(16):
			fluidsynth.play_Note(Note(active_chords[6][5].name,active_chords[6][5].octave),1,127)
		elif g.input(17):
			fluidsynth.play_Note(Note(active_chords[7][5].name,active_chords[7][5].octave),1,127)
		else:
			fluidsynth.play_Note(Note(StdTun[5].name,StdTun[5].octave),1,127)
		f21=1
		
	if g.input(26):
		setting()
		
	time.sleep(0.0005)
	
	
