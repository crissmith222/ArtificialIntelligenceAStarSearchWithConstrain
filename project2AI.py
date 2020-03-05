#Cristian Cedeno
#N01369950

import pygame
from shapely.geometry import Polygon, LineString
from queue import PriorityQueue
import math

pygame.init()

white = (255,255,255)
black = (0,0,0,)

red = (255,0,0)
green=(0,255,0)
blue=(0,0,255)


gameDisplay = pygame.display.set_mode((1000,500))
gameDisplay.fill(white)



class Vertex:

	    def __init__(self, x, y):
	        self.childs = []
	        self.x = x
	        self.y = y


	    def cord(self):
	    	return str(self.x) + "," + str(self.y)

	    def printVertex(self):
	    	print(str(self.x) + "," + str(self.y))

	    def addChild(self, c):
	    	self.childs.append(c)

	    def getchilds(self):
	    	return self.childs

	    def setgn(self, g):
	    	self.gn = g
	    
	    def getgn(self):
	    	return self.gn

	    def setfn(self, f):
	    	self.fn = f

	    def getfn(self):
	    	return self.fn

def enviroment(vertexList, pList, start, goal):


	class Graph:
		
		matrixTable = []
		def __init__(self, nodes, matSize):
			self.nodes = nodes
			self.matSize = matSize

			for x in range(matSize):
				self.matrixTable.append([])
				for y in range(matSize):
					self.matrixTable[x].append(0)

		def printMatrixTable(self):

			for m in self.matrixTable:
				print(m)

		def addEdge(self, s, e):
			self.matrixTable[s][e] = 1
			self.matrixTable[e][s] = 1


	def findHN(v):
		hn = math.sqrt((v.x - goal.x)**2 + (v.y - goal.y)**2)
		return hn

	def findGN(v1, v2):
		gn = math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)
		return gn

	def findFN(v1, v2):
		fn = findGN(v1, v2) + findHN(v2)
		return fn




	graph = Graph(vertexList, (len(vertexList ) ))


	'''
	for x in range(len(vertexList) ):
		for y in range(len(vertexList) ):
			if(x == y):
				continue

			line = LineString([(vertexList[x].x, vertexList[x].y), (vertexList[y].x, vertexList[y].y)])

			change = False
			for p in pList:


				if line.intersects(p) == False and line.touches(p) == True:

					change = True


				elif line.intersects(p) == True and line.touches(p) == True:
					print("TSSSSSSSSSSSST")
					change = True
				elif line.intersects(p) == True and line.touches(p) == False: 
					change = False 
					break
			if change:
				vertexList[x].addChild(vertexList[y])
				graph.addEdge(x, y)'''



	def actions(x,vertexObject):
		for y in range(len(vertexList) ):
			if(x == y):
				continue

			line = LineString([(vertexObject.x, vertexObject.y), (vertexList[y].x, vertexList[y].y)])
		
			change = False
			for p in pList:


				if line.intersects(p) == False and line.touches(p) == True:
					change = True
				elif line.intersects(p) == True and line.touches(p) == True:
					change = True
				elif line.intersects(p) == True and line.touches(p) == False: 
					change = False 
					break
			if change:
				vertexObject.addChild(vertexList[y])
				graph.addEdge(x, y)
				
		return vertexObject.childs

	for x in range(len(vertexList) ):
		actions(x,vertexList[x])

	amount = 0
	noSolution = False
	flag = True

	op = []
	cl = []

	transfer = vertexList[0]

	cl.append(transfer)

	graph.printMatrixTable()



	numt = 0
	while(flag):
		print("-------------")
		transfer.printVertex()
		print("--------------")

		#sets GN and FX for each child of the current node
		for x in transfer.getchilds():
			x.setgn(findGN(transfer, x))
			x.setfn(findFN(transfer, x))

			x.printVertex()
			print("FN:"+ str(x.getfn()))
			print("GN:"+ str(x.getgn()))

		for x in transfer.getchilds():
			#print(str(len(op)))
			visited = 0 

			for v in cl:
				if(x==v):
					visited = 1


			if(amount ==  0 and x.getgn() < cost):
				op.append(x)
				print
				amount +=1
				continue


			if(visited != 1 and x.getgn() < cost):
				if(len(op) == 0):
					op.append(x)
				elif(x.getfn() <= op[len(op)-1].getfn()):
					op.append(x)
					
				else:
					op.insert(0, x)
					
			amount +=1	
		
		if(len(op) == 0):
			noSolution = True
			break

		numt += 1
		
		

		transfer = op.pop()
		#amount -= 1
		cl.append(transfer)
		
		'''
		if(numt == 10):
			break
		'''

		#print(transfer.printVertex())
		if(transfer == goal):
			flag = False
		print(op)
		op.clear()







	start.setfn(findFN(start, goal))
	thefn = start.getfn()
	print(thefn)



	poly = Polygon([(300, 300), (400, 300), (350, 100)])

	print(str(goal.x))


	'''
	print("number: " + str(len(vertexList)))


	#path = LineString([(300, 300), (400, 300)])
	col = path.intersects(poly)

	#coli = lTest.within(sOne)

	colided = sOne.collidepoint(120, 130)
	print(str(col))




	graph.printMatrixTable();
	'''
	
	pygame.display.update()
	for p in range(len(cl)-1):
		pygame.time.wait(500)
		pygame.draw.line(gameDisplay, green, (cl[p].x, cl[p].y), (cl[p+1].x, cl[p+1].y), 4)
		pygame.display.update()
	if(noSolution == True):
		print("---THERE IS NO SOLUTION!!!---")


def enviroment1():
	
	pList = []

	pList.append(Polygon([(200, 350),(200, 450), (450,450),(450, 350)]))
	pList.append(Polygon([(120, 130), (150, 245), (275, 275),(300, 120),(200, 5)]))
	pList.append(Polygon([(300, 300), (400, 300), (350, 100)]))
	pList.append(Polygon([(425, 30), (400, 175), (575, 100), (550, 25)]))
	pList.append(Polygon([(545, 260), (520, 400), (625, 375)]))
	pList.append(Polygon([(600, 40),(600, 290), (750, 290), (750, 40)]))
	pList.append(Polygon([(640, 375), (640, 440), (700, 475), (755,440), (755,375), (700,320)]))
	pList.append(Polygon([(775, 75),(810, 350), (885, 75), (830,20)]))


	vertexList1 = []


	


	start1 = Vertex(75, 400)
	vertexList1.append(start1)

	vertexList1.append(Vertex(200, 350))
	vertexList1.append(Vertex(200,450))
	vertexList1.append(Vertex(450,450))
	vertexList1.append(Vertex(450,350))


	vertexList1.append(Vertex(120, 130))
	vertexList1.append(Vertex(150, 245))
	vertexList1.append(Vertex(275, 275))
	vertexList1.append(Vertex(300, 120))
	vertexList1.append(Vertex(200, 5))


	vertexList1.append(Vertex(300, 300))
	vertexList1.append(Vertex(400, 300))
	vertexList1.append(Vertex(350, 100))

	vertexList1.append(Vertex(425, 30))
	vertexList1.append(Vertex(400, 175))
	vertexList1.append(Vertex(575, 100))
	vertexList1.append(Vertex(550, 25))

	vertexList1.append(Vertex(545, 260))
	vertexList1.append(Vertex(520, 400))
	vertexList1.append(Vertex(625, 375))


	vertexList1.append(Vertex(600, 40))
	vertexList1.append(Vertex(600, 290))
	vertexList1.append(Vertex(750, 290))
	vertexList1.append(Vertex(750,40))


	vertexList1.append(Vertex(640, 375))
	vertexList1.append(Vertex(640, 440))
	vertexList1.append(Vertex(700, 475))
	vertexList1.append(Vertex(755, 440))
	vertexList1.append(Vertex(755, 375))
	vertexList1.append(Vertex(700, 320))


	vertexList1.append(Vertex(775, 75))
	vertexList1.append(Vertex(810, 350))
	vertexList1.append(Vertex(885, 75))
	vertexList1.append(Vertex(830,20))

	goal1 = Vertex(925, 75)
	vertexList1.append(goal1)




	dot = pygame.PixelArray(gameDisplay)

	pygame.draw.circle(gameDisplay, green, (75, 400), 10)

	sOne = pygame.draw.polygon(gameDisplay, blue, ((200, 350),(200, 450), (450,450),(450, 350)), 3)
	sTwo = pygame.draw.polygon(gameDisplay, blue, ((120, 130), (150, 245), (275, 275),(300, 120),(200, 5)), 3)
	sThree = pygame.draw.polygon(gameDisplay, blue, ((300, 300), (400, 300), (350, 100)), 3)
	sFour = pygame.draw.polygon(gameDisplay, blue, ((425, 30), (400, 175), (575, 100), (550, 25)), 3)
	sFive = pygame.draw.polygon(gameDisplay, blue, ((545, 260), (520, 400), (625, 375)), 3)
	sSix = pygame.draw.polygon(gameDisplay, blue, ((600, 40),(600, 290), (750, 290), (750, 40)), 3)
	sSeven = pygame.draw.polygon(gameDisplay, blue, ((640, 375), (640, 440), (700, 475), (755,440), (755,375), (700,320)), 3)
	sEight = pygame.draw.polygon(gameDisplay, blue, ((775, 75),(810, 350), (885, 75), (830,20)), 3)

	pygame.draw.circle(gameDisplay, red, (925, 75), 10)

	enviroment(vertexList1,pList, start1, goal1);


def enviroment2():
	
	pList2 = []

	pList2.append(Polygon([(120, 100),(120, 250), (250, 250),(250, 100)]))
	pList2.append(Polygon([(350, 200), (200, 320), (170, 400),(300, 350)]))
	pList2.append(Polygon([(470, 50), (400, 150), (400, 270),(530,270),(530,150)]))
	pList2.append(Polygon([(350, 300), (430, 430), (500, 300)]))
	pList2.append(Polygon([(570, 230), (570, 350), (770, 350),(770,230)]))
	pList2.append(Polygon([(580, 360),(530, 400), (580, 450), (640, 400)]))
	pList2.append(Polygon([(750, 50), (560, 100), (600, 200)]))
	pList2.append(Polygon([(730, 100),(730, 215), (850, 215), (850, 100)]))


	vertexList2 = []




	start2 = Vertex(90, 330)
	vertexList2.append(start2)

	vertexList2.append(Vertex(120, 100))
	vertexList2.append(Vertex(120, 250))
	vertexList2.append(Vertex(250, 250))
	vertexList2.append(Vertex(250, 100))


	vertexList2.append(Vertex(350, 200))
	vertexList2.append(Vertex(200, 320))
	vertexList2.append(Vertex(170, 400))
	vertexList2.append(Vertex(300, 350))
	

	vertexList2.append(Vertex(470, 20))
	vertexList2.append(Vertex(400, 100))
	vertexList2.append(Vertex(400, 200))
	vertexList2.append(Vertex(530, 200))
	vertexList2.append(Vertex(530, 100))

	vertexList2.append(Vertex(350, 300))
	vertexList2.append(Vertex(430, 430))
	vertexList2.append(Vertex(500, 300))

	vertexList2.append(Vertex(570, 230))
	vertexList2.append(Vertex(570, 350))
	vertexList2.append(Vertex(770, 350))
	vertexList2.append(Vertex(770, 230))

	vertexList2.append(Vertex(580, 360))
	vertexList2.append(Vertex(530, 400))
	vertexList2.append(Vertex(580, 450))
	vertexList2.append(Vertex(640, 400))

	vertexList2.append(Vertex(750, 50))
	vertexList2.append(Vertex(560, 100))
	vertexList2.append(Vertex(600, 200))

	vertexList2.append(Vertex(730, 100))
	vertexList2.append(Vertex(730, 215))
	vertexList2.append(Vertex(850, 215))
	vertexList2.append(Vertex(850, 100))



	goal2 = Vertex(800, 260)
	vertexList2.append(goal2)




	dot = pygame.PixelArray(gameDisplay)

	pygame.draw.circle(gameDisplay, green, (90, 330), 10)

	sOne = pygame.draw.polygon(gameDisplay, blue, ((120, 100),(120, 250), (250,250),(250, 100)), 3)
	sTwo = pygame.draw.polygon(gameDisplay, blue, ((350, 200), (200, 320), (170, 400),(300, 350)), 3)
	sThree = pygame.draw.polygon(gameDisplay, blue, ((470, 20), (400, 100), (400, 200),(530,200),(530,100)), 3)
	sFour = pygame.draw.polygon(gameDisplay, blue, ((350, 300), (430, 430), (500, 300)), 3)
	sFive = pygame.draw.polygon(gameDisplay, blue, ((570, 230), (570, 350), (770, 350),(770,230)), 3)
	sSix = pygame.draw.polygon(gameDisplay, blue, ((580, 360),(530, 400), (580, 450), (640, 400)), 3)
	sSeven = pygame.draw.polygon(gameDisplay, blue, ((750, 50), (560, 100), (600, 200)), 3)
	sEight = pygame.draw.polygon(gameDisplay, blue, ((730, 100),(730, 215), (850, 215), (850, 100)), 3)

	pygame.draw.circle(gameDisplay, red, (800, 260), 10)

	enviroment(vertexList2, pList2, start2, goal2);





def switch_env(argument):
	switcher = {
		1: enviroment1,
		2: enviroment2
	}
	runEnviroment = switcher.get(argument)
	runEnviroment()

quit = False

#while(not quit):
	

while True:
	gameDisplay.fill(white)
	inEnviroment = input("Enter 1 for enviroment 1. Enter 2 for enviroment 2. For quiting enter eny other key: ")
	#print(inEnviroment)
	if (inEnviroment != "1" and inEnviroment != "2"):
		break
	inEnviroment = int(inEnviroment)
	

	#print("Enter Cost: ")
	cost = input("Enter C Cost: ")
	cost = int(cost)
	#pygame.display.update()

	if(inEnviroment == 1 or inEnviroment == 2):
		switch_env(inEnviroment)
		
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			pygame.quit()
			quit()
	
	pygame.display.update()












