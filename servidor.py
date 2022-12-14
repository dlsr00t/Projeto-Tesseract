import socket

class Server:
	HOST = '127.0.0.1'
	PORT = 65432
	def __init__(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
			connection.bind((self.HOST, self.PORT))
			while True:
				connection.listen()
				print("Esperando por conexoes...")
				self.connected, self.addr = connection.accept()
				print(f'O seguinte ip foi conectado: {self.addr}')
			#	with self.connected as con:	
				self.receptor()

	def receptor(self, nome="foto.png"):
		self.clean_file(nome = nome)
		with self.connected as con:
			con.send(b'CONECTADO ao servidor')
			with open(nome, "wb") as foto:
				while True:
					data = con.recv(1024)
					cont = 0
					while cont <= 0:
						cont +=1
						if not data:
							print("Nenhum dado foi recebido")
							print(f"O seguinte ip foi desconectado: {self.addr}")
							print(data.decode())
					
					if cont == 1:
						break
					
					cont += 1
					
					if not data:
						print('O aquivo foi recebido!')
						print(f'O seguinte ip foi desconetado: {self.addr}')
						break

					foto.write(data)

	def clean_file(self, nome):
		with open(nome, "wb") as foto:
			foto.write(b'')


if __name__ == "__main__":
	Server().receptor()

