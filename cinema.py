from room import Room

class Cinema:

	def __init__(self):
		self.__rooms = list()

	@property
	def rooms(self):
		return self.__rooms
	
	def new_room(self, n):
		room = Room(len(self.__rooms)+1,n)
		self.__rooms.append(room)

	def show_rooms(self):
		for room in self.__rooms:
			print(room)

	def new_film(self, n, film):
		if n > 0 and n<=len(self.__rooms):
			#self.__rooms[n-1].film = film
			#self.__rooms[n-1].reset()
			self.__rooms[n-1].new_film(film)
			return True
		return False

	def get_room(self, n):
		if n > 0 and n<=len(self.__rooms):
			return self.__rooms[n-1]
		return None

	def reset_room(self,n):
		room = self.get_room(n)
		if room is not None:
			room.reset()
			return True
		return False