import pygame
from gpiozero import Button
from time import sleep
import RPi.GPIO as g
import serial
import time 
import multiprocessing

pygame.mixer.pre_init(44100, 16, 2, 4400) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.


def process1():
    while True:
        print("1++++"+str(g.input(8)))
        print("2++++"+str(g.input(9)))
        print("3++++"+str(g.input(10)))
        print("4++++"+str(g.input(11)))
        print("5++++"+str(g.input(20)))
        print("6++++"+str(g.input(21)))
        print("hjhkjkjjhjhgghg"+str(g.input(2)))
        #print(data.decode())
        if g.input(8)==0 and f8==1:
            f8=0
        if g.input(8) and f8==0:
            
            if g.input(2):
                ch1.play(pygame.mixer.Sound(path+ac[0][1]))
            f8=1
		
		


def process2():
    # code for the second process
    while True:

    
        if g.input(9)==0 and f9==1:
            f9=0
        if g.input(9) and f9==0:
            
            if g.input(2):
                ch2.play(pygame.mixer.Sound(path+ac[1][1]))
            f9=1
            

def process3():
    # code for the first process
    while True:

    
        if g.input(10)==0 and f10==1:
            f10=0
        if g.input(10) and f10==0:
            
            if g.input(2):

                ch3.play(pygame.mixer.Sound(path+ac[2][1]))
            f10=1
            
	

def process4():
    # code for the second process
	while True:

		

			
		if g.input(11)==0 and f11==1:
			f11=0
		if g.input(11) and f11==0:
			
			if g.input(2):
		
				ch4.play(pygame.mixer.Sound(path+ac[3][1]))
			f11=1
			
def process5():
    # code for the first process
	while True:

	
		if g.input(20)==0 and f20==1:
			f20=0
		if g.input(20) and f20==0:
			
			if g.input(2):
				
				ch5.play(pygame.mixer.Sound(path+ac[4][1]))
			f20=1
		



def process6():
    # code for the second process
    while True:


        if g.input(21)==0 and f21==1:
            f21=0
        if g.input(21) and f21==0:
            
            if g.input(2):
                
                ch6.play(pygame.mixer.Sound(path+ac[5][1]))
            f21=1



if name == 'main':
    # create two process objects

	path="/home/nitheez/Downloads/New/"
	ch1=pygame.mixer.Channel(0)
	ch2=pygame.mixer.Channel(1)
	ch3=pygame.mixer.Channel(2)
	ch4=pygame.mixer.Channel(3)
	ch5=pygame.mixer.Channel(4)
	ch6=pygame.mixer.Channel(5)
	ac=[["we use 1 indexing","e1.ogg","d","em","g"],["we use 1 indexing","a1.ogg","d","em","g"],["we use 1 indexing","e2.ogg","d","em","g"],["we use 1 indexing","a2.ogg","d","em","g"],["we use 1 indexing","c3.ogg","d","em","g"],["we use 1 indexing","e3.ogg","d","em","g"]]


	g.setmode(g.BCM)
	g.setup(2,g.IN)
	g.setup(3,g.IN)
	g.setup(4,g.IN)
	g.setup(5,g.IN)

	g.setup(6,g.IN)
	g.setup(7,g.IN)

	g.setup(8,g.IN)
	g.setup(9,g.IN)
	g.setup(10,g.IN)
	g.setup(11,g.IN)
	g.setup(20,g.IN)
	g.setup(21,g.IN)



	u=g.input(6)
	d=g.input(7)

	f8=0
	f9=0
	f10=0
	f11=0
	f20=0
	f21=0
	x=0.04
	ch1.play(pygame.mixer.Sound(path+ac[0][1]))
	time.sleep(x)
	ch2.play(pygame.mixer.Sound(path+ac[1][1]))
	time.sleep(x)
	ch3.play(pygame.mixer.Sound(path+ac[2][1]))
	time.sleep(x)
	ch4.play(pygame.mixer.Sound(path+ac[3][1]))
	time.sleep(x)
	ch6.play(pygame.mixer.Sound(path+ac[5][1]))
	count=1
	p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p3 = multiprocessing.Process(target=process3)
    p4 = multiprocessing.Process(target=process4)
    p5 = multiprocessing.Process(target=process5)
    p6 = multiprocessing.Process(target=process6)
    # start both processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p2.start()

    # wait for both processes to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p2.join()
