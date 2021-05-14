
		
Cfinal=6083250
k1=499800 
K2=500250

class  InteresCompuesto:
	def __init__(self, cinicial, tiempo, interes):
		self.cinicial=cinicial
		self.tiempo=tiempo
		# tiempo en meses
		self.interes=interes
		# interes anual/100
		
	def Futuro(self):
		return((self.cinicial*(1+(self.interes/100))**self.tiempo))
	
	def  Evalinteres(self):
		if self.interes<0:
			print('vas a perder dinero')
		else:
			print('buen negocio')
			
	def Calcinicial(self):
		#Argumentos Calcinicial(Cfinal, tiempo, intetes)
		return((self.cinicial/(1+(self.interes/100))**self.tiempo))


Cinicial=((InteresCompuesto(Cfinal, 5, 4)).Calcinicial())

#print(Cinicial)
# itetador
if Cinicial>500000:
	
	while Cinicial>500000:
		Cinicial=((InteresCompuesto(Cfinal, 5, 4)).Calcinicial())
		Cfinal-=1
		
	else:
		print("se activo el primer bucle")
		print(Cinicial)
		print(Cfinal)	
		
if Cinicial<4980:
	
	while Cinicial<490800:
		Cfinal+=1
		
	else:
		print("se activo el segundo bucleá")
		print(Cinicial)
	


		