class Room:
	def __init__(self, n, nSeats):
		self.__n = n
		self.__film = ''
		self.__seats = [True]*nSeats

	@property
	def n(self):
		return self.__n

	@property
	def film(self):
		return self.__film

	@film.setter
	def film(self, film):
		self.__film = film

	@property
	def seats(self):
		return self.__seats

	def __str__(self):
		return "Sala: {} Película: {} Butacas: {}".format(self.__n, '-' if self.__film=='' else self.__film, len(self.__seats))
	
	def reset(self):
		self.__seats = [True]*len(self.__seats)

	def new_film (self, film):
		self.__film = film
		self.reset()

	def show_all(self):
		for i in range(len(self.__seats)):
			print("{} - {}".format(i+1,'Libre' if self.__seats[i] else 'Ocupada'))

	def show_free(self):
		for i in range(len(self.__seats)):
			if self.__seats[i]:
				print("{} - Libre".format(i+1))

	def select_seat(self, n):
		if n>0 and n<=len(self.__seats):
			if self.__seats[n-1]:
				self.__seats[n-1] = False
				return True
		return False