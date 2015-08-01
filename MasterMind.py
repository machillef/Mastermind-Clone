 # -*- coding: utf-8 -*-
import pygame, sys, textrect, random
import modules
import GameMenu as gm
import os
from os.path import dirname, realpath, abspath
from pygame.locals import *
from pygame import gfxdraw

pygame.init()

#constants, like screen size, and some colors
#screen
WIDTH = 800
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
#colors
BLACK = (0,0,0)
lBLACK = (51,51,51)
dWHITE = (224,224,224)
RED = (255,0,0)
#fps
clock = pygame.time.Clock()
#update global function
def update():
	pygame.display.update()
	
	
class MasterMind():
	font = pygame.font.SysFont("monospace", 36)
	gameRunning = True
	bgImage = pygame.image.load(os.path.join("Recources","woodBG.png"))
	clockBg = pygame.image.load(os.path.join("Recources","clockBlit.png"))
	
	#user event using timer
	pygame.time.set_timer(USEREVENT+1, 1000)
	
	#testing code
	peg_list = pygame.sprite.OrderedUpdates() #ordered list of sprites
	peg_list.add(modules.RedPeg(600, 70))
	peg_list.add(modules.OrangePeg(600, 140))
	peg_list.add(modules.YellowPeg(600, 210))
	peg_list.add(modules.GreenPeg(600, 280))
	peg_list.add(modules.BluePeg(600, 350))
	peg_list.add(modules.PurplePeg(600, 420))
	blackPeg = modules.BlackPeg(200, 200)
	whitePeg = modules.WhitePeg(0,0)
	#rectangle list
	rectList = []
	blackNwhiteList = []
	#stefanos defined vars
	usersAnswer = [False, False, False, False]

	tempCorrectResult = ["yellow", "red", "yellow", "yellow"]
	maura = 0
	aspra = 0
	#check button
	checkAnswerButton = modules.CheckButton("Check", 0, 0, 0, 120, 100)
	
	seconds = 0
	numberOfTries = 0
	win = False
	
	def gameMainLoop(self):
		limit = 20 #limit the user to only put pegs into the first four rects, and then move upwards.
		hourRect = pygame.Rect(WIDTH-110, 	0, 50, 20)
		display.blit(self.bgImage, display.get_rect())  
		hoursMinutesList = [0,0] 
		timePassed = 0 #the time passed in seconds
		tempImage = None
		#create the pegds, and the 2 matrices
		self.drawPegs()
		self.drawMatrix()
		self.createAnswerBoxes()
		#correctResult = self.calculateAnswer()
		correctResult = ("purple", "yellow", "blue", "orange")
		while self.gameRunning:
			clock.tick(30)
			display.blit(self.clockBg, hourRect)
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
				if ev.type == USEREVENT+1:
					self.seconds+=1
					timePassed+=1
					if timePassed == 60:
						timePassed = 0
						hoursMinutesList[1] += 1
				if ev.type == MOUSEMOTION:
					self.checkAnswerButton.hover( )
				if ev.type == MOUSEBUTTONDOWN:
				#handle
					for i in range(len(self.peg_list)):
						if self.peg_list.sprites()[i].hover():
							tempImage = self.peg_list.sprites()[i].clicked()
					if self.checkAnswerButton.clicked():
						if False not in self.usersAnswer:
							if list(correctResult) == self.usersAnswer:
								self.win = True
							self.checkAnswer(self.usersAnswer, correctResult, self.numberOfTries)
							#print(correctResult)
							#print(self.usersAnswer)
							del self.rectList[:4]
							self.usersAnswer = [False, False, False, False]
						#	print("aspra :", self.aspra)
						#	print("maura :", self.maura)
							self.aspra = 0
							self.maura = 0
							self.tempCorrectResult = correctResult
							self.numberOfTries += 1						
				if ev.type == KEYDOWN:
					pass
					#if ev.key == K_d:
					#	print(len(self.rectList))
					#if ev.key == K_q:
					#	print(correctResult)
					#if ev.key == K_b:
					#	self.numberOfTries = 8
						
					
					
				

			
			self.timePassed(hoursMinutesList[0], hoursMinutesList[1], timePassed)
			#needed else we get an error at the last try. Maybe we can fix it, by moving it at top.
			if len(self.rectList) >0:
				self.blitPegIntoRectList(tempImage)
			#TODO: HANDLE WHEN THE USER DOESNT FIND THE ANSWER IN 6 TRIES
			if self.numberOfTries == 8:
				self.defeat(correctResult)
				

		
			update()

			if self.win:
				self.winner()
			#end of testing code
			
	def timePassed(self, minutes1, minutes2, seconds):  #function to take the time passed, and blit it to the screen.
		if seconds <=9: #we need to explicitly add a "0" if seconds are lower than nine, to make a better GUI.
			counterString =  str(minutes1) + str(minutes2) + ":0" + str(seconds)
		else:
			counterString =  str(minutes1) + str(minutes2) + ":" + str(seconds)
		label = self.font.render(counterString, 1, dWHITE)
		labelRect = label.get_rect()
		labelRect.left =  WIDTH - labelRect.width
		display.blit(label, labelRect)
		
	def drawPegs(self):
		#testing code
		self.peg_list.draw(display) #built-in method to draw the sprite list in the correct order.
	
	def drawMatrix(self):
		del self.rectList[:]
		y = 520
		for i in range(8):
			x = 20
			for j in range(4):
				self.rectList.append(pygame.draw.rect(display, dWHITE, (x, y,  100, 70),1))
				x += 100
			y -= 70	


	def blitPegIntoRectList(self, tempImage):
		if tempImage != None:
			tempClicked = pygame.mouse.get_pressed()
			for i in range(4):
				if self.rectList[i].collidepoint(pygame.mouse.get_pos()):
					if tempClicked[0] == 1:
						display.blit(tempImage.image, (self.rectList[i].x + 20 , self.rectList[i].y +2 ))#20 because we can.
						self.usersAnswer[i] = tempImage.string
						
	#checks the user answer
	def checkAnswer(self, usersAnswer, correctResult, numberOfTries): #usersAnswer its a 4 element list, containing color strings, i.e "yellow", "red" etc.
		apantisi = usersAnswer
		swsto = list(correctResult)
		for i in range(len(apantisi)):
			if apantisi[i] == swsto[i]:
				apantisi[i] = "0"
				swsto[i] = "0"
				self.maura += 1
		
		for i in range(len(apantisi)):
			for j in range(len(swsto)):
				if apantisi[i] == swsto[j] and apantisi[i] != "0" and swsto[j] != "0" and i != j:
					self.aspra += 1
					apantisi[i] = "0"
					swsto[j] = "0"	
					
		top = []
		bot = []
		if self.maura <2:
			for i in range(self.maura):
				top.append(self.blackPeg.image)
			if self.aspra >= 1:
				for i in range(self.maura, 2):
					top.append(self.whitePeg.image)
			if self.aspra >=2:
				for i in range(self.aspra - len(top)):
					bot.append(self.whitePeg.image)
		
		elif self.maura == 2:
			for i in range(2):
				top.append(self.blackPeg.image)
			for i in range(self.aspra):
				bot.append(self.whitePeg.image)
				
		elif self.maura > 2:
			for i in range(2):
				top.append(self.blackPeg.image)
			for i in range(self.maura-2):
				bot.append(self.blackPeg.image)
			for i in range(self.aspra):
				bot.append(self.whitePeg.image)
		
		#print(self.aspra)
		#print(self.maura)
		offsetX = 5
		for i in range(len(top)):
			display.blit(top[i], (self.blackNwhiteList[self.numberOfTries].x + offsetX , self.blackNwhiteList[self.numberOfTries].y +2))
			offsetX += 17
		offsetX = 5
		for i in range(len(bot)):
			display.blit(bot[i], (self.blackNwhiteList[self.numberOfTries].x + offsetX , self.blackNwhiteList[self.numberOfTries].y + 17))
			offsetX += 17

	'''	offsetX = 5
		if self.maura == 1:
			self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX , self.blackNwhiteList[self.numberOfTries].y +2)
		elif self.maura == 2:
			for i in range(self.maura):	
				self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX, self.blackNwhiteList[self.numberOfTries].y +2)
				offsetX+= 17
		elif self.maura == 3:
			for i in range(2):	
				self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX, self.blackNwhiteList[self.numberOfTries].y +2)
				offsetX+= 17
			offsetX = 5	
			self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX , self.blackNwhiteList[self.numberOfTries].y + 17)
		elif self.maura == 4:
			for i in range(2):	
				self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX, self.blackNwhiteList[self.numberOfTries].y +2)
				offsetX+= 17
			offsetX = 5	
			for i in range(2):	
				self.blackPeg.draw(self.blackNwhiteList[self.numberOfTries].x + offsetX, self.blackNwhiteList[self.numberOfTries].y + 17)
				offsetX+= 17'''
	
	def createAnswerBoxes(self):
		x = self.rectList[3].right + 20
		y = self.rectList[0].y + self.rectList[0].height/4
		for i in range(8):
			self.blackNwhiteList.append(pygame.draw.rect(display, dWHITE, (x, y,  self.rectList[0].width/2, self.rectList[0].height/2),1))
			y -= self.rectList[0].height
			
	def calculateAnswer(self):
		colorList = []
		tempList = []
		for i in range(6):
			colorList.append(self.peg_list.sprites()[i].string)
		for i in range(4):
			tempList.append(colorList[random.randint(0,5)])
			
		return tuple(tempList)
	
	#TODO: ADD LAVENDER TOWN THEME.
	def defeat(self, correct):
		#defeat theme
		pygame.mixer.music.load(os.path.join("Recources","lavender.mp3"))
		pygame.mixer.music.play(-1, 0.0) #loops, starting time. If the loops is -1 then the music will repeat indefinitely.
		display.fill(BLACK) #erase everything else
		correctResult = list(correct)
		answerRect = pygame.draw.rect(display, lBLACK,  (0, HEIGHT-120,WIDTH, 120))
		#you lose msg
		stringDefeat = "You lose!"
		localFont = pygame.font.SysFont("monospace", 56)
		label = localFont.render(stringDefeat, 1, RED)
		labelRect = label.get_rect()
		displayRect = display.get_rect()
		labelRect.center = ( displayRect.centerx, displayRect.centery)
		display.blit(label, labelRect)
		#press message
		stringContinue = "Press any mouse button to exit."
		localFont = pygame.font.SysFont("monospace", 42)
		label = localFont.render(stringContinue, 1, RED)
		labelRect = label.get_rect()
		displayRect = display.get_rect()
		labelRect.center = ( displayRect.centerx, displayRect.centery + 150 )
		display.blit(label, labelRect)
		#correct answer message
		stringContinue = "The correct answer is:"
		localFont = pygame.font.SysFont("monospace", 42)
		label = localFont.render(stringContinue, 1, dWHITE)
		labelRect = label.get_rect()
		displayRect = display.get_rect()
		labelRect.center = ( displayRect.centerx, displayRect.centery + 200 )
		display.blit(label, labelRect)		
		
		x = 150
		for i in range(len(correctResult)):
			for j in range(len(self.peg_list)):
				if correctResult[i] == self.peg_list.sprites()[j].string:
					display.blit(self.peg_list.sprites()[j].image, (x, HEIGHT-70, 150, 70))
					x+=150
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					pygame.quit()
					sys.exit()
			update()
			
	#TODO: ADD POKEMON WIN THEME
	def winner(self):
		#theme
		pygame.mixer.music.load(os.path.join("Recources","victory.mp3"))
		pygame.mixer.music.play(-1, 0.0)
		pygame.mixer.music.set_volume(0.1)
		display.fill((51,153,255))
		stringDefeat = "You Won!"
		localFont = pygame.font.SysFont("monospace", 56)
		label = localFont.render(stringDefeat, 1, BLACK)
		labelRect = label.get_rect()
		displayRect = display.get_rect()
		labelRect.center = ( displayRect.centerx, displayRect.centery)
		display.blit(label, labelRect)
		stringContinue = "Press any mouse button to exit."
		localFont = pygame.font.SysFont("monospace", 42)
		label = localFont.render(stringContinue, 1, BLACK)
		labelRect = label.get_rect()
		displayRect = display.get_rect()
		labelRect.center = ( displayRect.centerx, displayRect.centery + 150 )
		display.blit(label, labelRect)
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					pygame.quit()
					sys.exit()
			update()	
			
menu = gm.GameMenu()
menu.menuLoop()		
masterMindobj = MasterMind()
masterMindobj.gameMainLoop()