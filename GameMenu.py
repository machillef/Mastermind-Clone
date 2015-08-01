 # -*- coding: utf-8 -*-
import pygame, sys, textrect
import modules
import os
from os.path import dirname, realpath, abspath
from pygame.locals import *

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
#Background image
bgImage = pygame.image.load(os.path.join("Recources","woodBG.png"))
bgImage.convert_alpha()
#update global function
def update():
	pygame.display.update()
	
class GameMenu():
	startButton = modules.StartButton("Start Game", 150, WIDTH/2, HEIGHT/2, 300, 100) #text, offset, startingX, startingY, width, height. starting X and Y may be irrelevant, since we center them inside Button() anyway.
	instructionsButton = modules.InstructionsButton("Instructions", 0, WIDTH/2, HEIGHT/2, 300, 100)
	exitButton = modules.ExitButton("Exit Game", -150, WIDTH/2, HEIGHT/2, 300, 100)
	backButton = modules.BackButton("Back", 0, 0, HEIGHT-60, 100, 60)
	aboutButton = modules.AboutButton("About us", 0, 0, HEIGHT-60, 200, 60)
	
	
	
	display.blit(bgImage, display.get_rect())
	
	def menuLoop(self):
		display.blit(bgImage, display.get_rect())
		self.gameName()
		self.aboutButton.drawButton()
		gameMenu = True
		while gameMenu:
			#handle all the various events
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEMOTION:
					self.startButton.hover()
					self.instructionsButton.hover()
					self.exitButton.hover()
					self.aboutButton.hover()
				if event.type == MOUSEBUTTONDOWN:
					if self.startButton.clicked():
						gameMenu = False
						break
					elif self.instructionsButton.clicked():
						self.instructions()
					elif self.aboutButton.clicked():
						self.aboutUs()
					self.exitButton.clicked()
					

			
			update()
		
	def instructions(self):
		
		display.blit(bgImage, display.get_rect()) #first we delete everything
		#the instructions String. Its a long one.
		instructionsString = 'Το Mastermind είναι παιχνίδι σπάσιμου κώδικα. Ο υπολογιστής θέτει τον κώδικα, ο οποίος αποτελείται από 4 "πούλια". Κάθε πούλι χαρακτηρίζεται από το χρώμα του και τη θέση του.  Ένα πούλι μπορεί να έχει 1 από 6 χρώματα, και σε κάθε κλειδί δύο ή περισσότερα πούλια μπορούν να έχουν το ίδιο χρώμα. Σκοπός του παιχνιδιού είναι ο παίχτης να μαντέψει το κλειδί που έχει θέσει ο υπολογιστής σε 8 ή λιγότερες προσπάθειες.'
		instructionsString+=	' Ο παίχτης αρχικά μαντέυει ένα κλειδί, τοποθετώντας στην πρώτη σειρά (ξεκινώντας από κάτω) του πίνακα τυχαία έναν συνδυασμό. Όταν ο συνδυασμός είναι έτοιμος, πατώντας το κουμπί  "Έλεγχος", ο παίχτης μπορεί να τσεκάρει πόσες σωστές επιλογές χρώματος και πόσες σωστές επιλογές χρώματος και σειράς έχει κάνει. Εάν ένας παίχτης έχει βρει το σωστό χρώμα και τη σωστή σειρά από ένα οποιοδήποτε πούλι, επιστρέφεται ένας μαύρος πόντος. Εάν ένας παίχτης έχει βάλει στην υπόθεσή του ένα πούλι, το χρώμα του οποίου υπάρχει μέσα στο κλείδι, αλλά το πούλι αυτό δεν βρίσκεται στην ίδια θέση με αυτή του κλειδιού, επιστρέφεται ένας άσπρος πόντος. Το παιχνίδι τελειώνει επιτυχώς, όταν επιστραφούν 4 μαύροι πόντοι, όποτε όλα τα πούλια βρίσκονται στην ίδια θέση και έχουν το ίδιο χρώμα με αυτό του κλειδιού.\n ΠΡΟΣΟΧΗ: Οι άσπροι ή μαύροι πόντοι συμβολίζουν μόνο πόσες και όχι ποιες είναι οι σωστές υποθέσεις.'
		instructionsString+=	' Σε περίπτωση που μία υπόθεση είναι λάθος, μετά το πάτημα του "Έλεγχος", δίνεται μία νέα ευκαιρία στον παίχτη να βρει το σωστό κλειδί. Ο παίχτης πρέπει κάθε φορά να συγκρίνει κάθε υπόθεσή του με τις προηγούμενες και, μελετώντας τους άσπρους και μαύρους πόντους  που του επιστράφηκαν την εκάστοτε φορά, να καταλήξει στο σωστό αποτέλεσμα.'
	
		localFont = pygame.font.SysFont("monospace", 18) #we render a new local font so we can fit the whole instructions String.
		rectToPlaceText = pygame.Rect(0, 0, WIDTH, HEIGHT) #we create a rectangle to place our string. In this case it's the whole screen.
		rendered_text = textrect.render_textrect(instructionsString, localFont, rectToPlaceText, dWHITE, bgImage) #the result of the render_textrect method, i.e the instructions ready to be transferred in the screen (blit). 
		display.blit(bgImage, display.get_rect())
		if rendered_text: #we check if there is an actual text
				display.blit(rendered_text, (rectToPlaceText.left, rectToPlaceText.top))
		instructionsLoop = True
		self.backButton.drawButton()
		
		while instructionsLoop:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
				if ev.type == MOUSEMOTION:
					self.backButton.hover()
				if ev.type == MOUSEBUTTONDOWN:
					if self.backButton.clicked(): #if we press the back button, we first delete it, and then we redraw the other three before we exit.
						display.blit(bgImage, display.get_rect())
						instructionsLoop = False
						self.backButton.deleteButton() #not needed any more. still it's nice to have a delete function
						self.startButton.drawButton()
						self.instructionsButton.drawButton()
						self.exitButton.drawButton()
						self.gameName()
						self.aboutButton.drawButton()
			update()
		
		
	def gameName(self):
		localFont =  pygame.font.SysFont("monospace", 66)
		label = localFont.render("MasterMind Clone", 1, (255,255,0))
		labelRect = label.get_rect()
		labelRect.centerx = WIDTH/2
		display.blit(label, labelRect)
		
	def aboutUs(self):
		aboutUsString = 'Η εφαρμογή αυτή υλοποιήθηκε στα πλαίσια του 3ου Σχολείου Κώδικα της Μονάδας Αριστείας ΕΛ/ΛΑΚ του Αριστοτελείου Πανεπιστημίου Θεσσαλονίκης. Συντελεστές του είναι οι:\nΑχιλλέας Μόσχος\nΣτέφανος Δραγούτσης\nΑλέξανδρος - Γεώργιος Μουντογιαννάκης\nΥπεύθυνοι του εγχειρήματος ήταν οι κ. Ιωάννης Σταμέλος και κ. Σταύρος Δημητριάδης, τους οποίους και ευχαριστούμε.'
		localFont = pygame.font.SysFont("monospace", 24)
		rectToPlaceText = pygame.Rect(0, 0, WIDTH, HEIGHT)
		rendered_text = textrect.render_textrect(aboutUsString, localFont, rectToPlaceText, dWHITE, bgImage)

		if rendered_text: 
			display.blit(rendered_text, (rectToPlaceText.left, rectToPlaceText.top))
		aboutLoop = True
		self.backButton.drawButton()
		while aboutLoop:
			for ev in pygame.event.get():
				if ev.type == QUIT:
					pygame.quit()
					sys.exit()
				if ev.type == MOUSEMOTION:
					self.backButton.hover()
				if ev.type == MOUSEBUTTONDOWN:
					if self.backButton.clicked(): #if we press the back button, we first delete it, and then we redraw the other three before we exit.
						display.blit(bgImage, display.get_rect())
						aboutLoop = False
						self.backButton.deleteButton() #not needed any more. still it's nice to have a delete function
						self.startButton.drawButton()
						self.instructionsButton.drawButton()
						self.exitButton.drawButton()
						self.gameName()
						self.aboutButton.drawButton()
						
			update()

	
		
#menu = GameMenu()
#menu.menuLoop()
