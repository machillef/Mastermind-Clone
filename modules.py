 # -*- coding: utf-8 -*	-
import pygame, sys, textrect
import os
from os.path import dirname, realpath, abspath
from pygame.locals import *
from pygame.sprite import *

pygame.init()

#constants, like screen size, and some colors
#screen
WIDTH = 800
HEIGHT = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))
#colors
BLACK = (0,0,0)
lBLACK = (51,51,51)

#update global function
def update():
	pygame.display.update()
	
#button super class.
class Button(pygame.Rect):
	font = pygame.font.SysFont("monospace", 36)
	
	def __init__(self, buttonText, heightOffset, buttonX, buttonY, buttonWidth, buttonHeight):
		#we create the rectangle, and we center it accordingly to our WIDTH, HEIGHT, and offset.
		Rect.__init__(self, buttonX, buttonY, buttonWidth, buttonHeight)
		self.center = (WIDTH/2 , HEIGHT/2-heightOffset)
		self.color = (255,255,0)
		self.text = buttonText
		
		
		
	def drawButton(self, color = (255,255,0)):
		#the label is a surface object. via get_rect() we get its rectangle, so we can center the text.
		label = self.font.render(self.text, 1, color)
		buttonRect = label.get_rect()
		#after we get the rectangle of the text, we use the coordinates of self, i.e our rect.
		buttonRect.center = (self.centerx , self.centery)
		pygame.draw.rect(display, BLACK, self )
		display.blit(label, buttonRect)
		
	def hover(self, color = (255,255,0) ):
		if self.collidepoint(pygame.mouse.get_pos()):
			self.drawButton((224,224,224))
			return True
		else:
			self.drawButton(color)
			return False
			
	def clicked(self):
		isClicked = pygame.mouse.get_pressed() #returns a tuple with the 3 elements. 
		if self.hover():
			if isClicked[0] == 1: #we check if the left mouse click was pressed
				return True
		return False
				
class StartButton(Button):

	def __init__(self, *args):
		Button.__init__(self, *args)
	
	def clicked(self):
		isClicked = pygame.mouse.get_pressed() #returns a tuple with the 3 elements. 
		if self.hover():
			if isClicked[0] == 1: #we check if the left mouse click was pressed
				return True
				
class InstructionsButton(Button):

	def __init__(self, *args):
		super().__init__(*args)
	

		
class ExitButton(Button):
	
	def __init__(self, *args):
		super().__init__(*args)
	
	def clicked(self):
		isClicked = pygame.mouse.get_pressed() #returns a tuple with the 3 elements. 
		if self.hover():
			if isClicked[0] == 1: #we check if the left mouse click was pressed
				pygame.quit()
				sys.exit()
				
class BackButton(Button):
	
	def __init__(self, *args):
		super().__init__(*args)
		self.topleft = (WIDTH-self.width, HEIGHT-self.height) #align it to the bottom corner of the screen
	
	

	def deleteButton(self):
		display.fill(lBLACK, self)
		
class AboutButton(Button):
	
	def __init__(self, *args):
		super().__init__(*args)
		self.topleft = (WIDTH-self.width, HEIGHT-self.height) #align it to the bottom corner of the screen
		
class CheckButton(Button):
	
	def __init__(self, *args):
		super().__init__(*args)
		self.topleft = (WIDTH-self.width, HEIGHT-self.height) #align it to the bottom corner of the screen
	
	def drawButton(self, color = (51,255,102)):
		#the label is a surface object. via get_rect() we get its rectangle, so we can center the text.
		label = self.font.render(self.text, 1, color)
		buttonRect = label.get_rect()
		#after we get the rectangle of the text, we use the coordinates of self, i.e our rect.
		buttonRect.center = (self.centerx , self.centery)
		pygame.draw.rect(display, BLACK, self )
		display.blit(label, buttonRect)
		
	def hover(self ):
		if self.collidepoint(pygame.mouse.get_pos()):
			self.drawButton((224,224,224))
			return True
		else:
			self.drawButton((51,255,102))
			return False
			
	def clicked(self):
		isClicked = pygame.mouse.get_pressed() #returns a tuple with the 3 elements. 
		if self.hover():
			if isClicked[0] == 1: #we check if the left mouse click was pressed
				return True
		return False

		
#Peg super class 
class Peg(Sprite):
	def __init__(self, spriteX, spriteY, width=62, height=60):
		Sprite.__init__(self)
		self.rect = pygame.Rect(spriteX, spriteY, width, height) 
		
	def hover(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return True
		return False
	
	
	def clicked(self):
		clicks = pygame.mouse.get_pressed()
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if clicks[0] == 1:
				#print("clicked")
				return self
		return None		

	def draw(self):
		pass
		
#red peg
class RedPeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","redPeg.png"))
		self.string = "red"
		

		

		
#orange peg
class OrangePeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","orangePeg.png"))
		self.string = "orange"


		
#yellow peg
class YellowPeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","yellowPeg.png"))
		self.string = "yellow"
		
#green peg
class GreenPeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","greenPeg.png"))
		self.string = "green"



#blue peg
class BluePeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","bluePeg.png"))
		self.string = "blue"



#purple peg
class PurplePeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","purplePeg.png"))
		self.string = "purple"

#black peg
class BlackPeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","blackPeg.png"))
		
	def draw(self, x, y): #draw the peg into the x,y cords
		self.rect.x = x
		self.rect.x = y
		display.blit(self.image, (x,y))
		
#white peg
class WhitePeg(Peg):
	def __init__(self, *args):
		super().__init__(*args)
		self.image = pygame.image.load(os.path.join("Recources","whitePeg.png"))

	def draw(self, x, y): #draw the peg into the x,y cords
		self.x = x
		self.y = y
		display.blit(self.image, (x,y))



	
	
		

