from cinema import Cinema
import utils



#1
def new_room(cinema):
	n = utils.read_int("Introduce el número de butacas: ")
	if n is not None:
		if n > 0:
			cinema.new_room(n)
			print("La sala ha sido dada de alta correctamente.")
		else:
			print("La sala debe tener al menos una butaca.")

#2
def new_film(cinema):
	cinema.show_rooms()
	n = utils.read_int("Introduce el número de sala: ")
	if n is not None:
		film = input("Introduce el título de la película: ")
		if cinema.new_film(n, film):
			print ("La película ha sido dada de alta satisfactoriamente.")
		else:
			print("Las sala indicada no existe")


#3
def sell_ticket(cinema):
	cinema.show_rooms()
	n = utils.read_int("Introduce el número de sala: ")
	if n is not None:
		room = cinema.get_room(n)
		if room is not None:
			room.show_free()
			seat = utils.read_int("Introduce el número de butaca: ")
			if seat is not None:
				if room.select_seat(seat):
					print("Se ha reservado la butaca")
					#room.show_all()
				else:
					print("La butaca es incorrecta")
		else:
			print("El número de sala es incorrecto")


#4
def reset_room(cinema):
	cinema.show_rooms()
	n = utils.read_int("Introduce el número de sala: ")
	if n is not None:
		if cinema.reset_room(n):
			print("Sala libre")
		else:
			print("El número de sala es incorrecto")

#5
def show_room(cinema):
	cinema.show_rooms()
	n = utils.read_int("Introduce el número de sala: ")
	if n is not None:
		room = cinema.get_room(n)
		if room is not None:
			print(room)
			room.show_all()

def menu():
	print("1. Alta sala")
	print("2. Alta película")
	print("3. Venta entrada")
	print("4. Liberar sala")
	print("5. Consultar sala")
	print("0. Salir")

def main():
	options = [new_room,new_film,sell_ticket,reset_room, show_room]
	cinema = Cinema()
	while True:
		print("************")
		menu()
		n = utils.read_int("Selecciona una opción: ")
		if n is not None:
			if n == 0:
				break
			elif n>0 and n<6:
				options[n-1](cinema)
			else:
				print ("Opción incorrecta")

	print("Hasta pronto!")

main()