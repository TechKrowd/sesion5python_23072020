def read_int(msg):
	n = input(msg)
	if n.isdigit():
		return int(n)
	print("Debes introducir un valor numérico")
	return None