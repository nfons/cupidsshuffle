import pygame
import random
import os

DIR = os.path.realpath('food.py')  #un-used

class Food_piece(object):
	def __init__(self,pos,color = (255,0,0)):
		self.m_x = pos[0]
		self.m_y = pos[1]
		self.x = self.m_x * 10
		self.y = self.m_y * 10
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,10,10)
		pygame.draw.rect(screen,self.color,rect)

class Food(object):
	def __init__(self):
		self.food = list()

		self.time = 30000
		self.time_tick = 30000

	def random_pos(self,snake):
		running = True 
		while running:
                        #for food, we will keep it towards the outsides...makes it somewhat harder to get
			x,y = random.randint(10,69),random.randint(10,69)
			running = False
			for t in snake.tail :
				if t.m_x == x and t.m_y == y :
					running = True
			if x == snake.x and y == snake.y :
				running = True
			for p in self.food :
				if p.m_x == x and p.m_y == y :
					running = True
		return x,y

	def restart(self):
		self.food = []
		self.time = 30000 #food has a really long time to spawn

	def spawn(self,dt,screen,snake):
		self.time += dt
		if self.time >= self.time_tick :
			self.time = 0
			x,y = self.random_pos(snake)
			f_piece = Food_piece((x,y))
			self.food.append(f_piece)

		for f_piece in self.food :
			if f_piece.m_x == snake.x and f_piece.m_y == snake.y :
				snake.decrease_length(2)
				self.food.remove(f_piece)
			f_piece.blit(screen)