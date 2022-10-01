import socket

class Server():
	HOST = '127.0.0.1'
	PORT = 65432
	def __init__(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
			connection.bind((self.HOST, self.PORT))
			while True:
				connection.listen()
				print("Esperando por conexoes")
				self.connected, self.addr = connection.accept()
				print(f'O seguinte ip foi conectado: {self.addr}')
				self.arquivo()

	def arquivo(self):
		with self.connected as con:
			with open("foto.png", "wb") as foto:
				while True:
					data = con.recv(1024)
					if not data:
						print('O aquivo foi recebido!')
						print(f'O seguinte ip foi desconetado: {self.addr}')
						break

					foto.write(data)

if __name__ == "__main__":
	Server()

