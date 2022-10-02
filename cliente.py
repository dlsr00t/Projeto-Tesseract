###ESSE PROGRAMA ESTA PRONTO PARA USO

import socket

class Client():
	def __init__(self, HOST, PORT):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.connection:
			self.connection.connect((HOST, PORT))
			print("Conectado ao servidor.")
		'''	with open("/home/foureyes/.programs/imagem_de_test.png", "rb") as foto:
				for data in foto.readlines():
					self.connection.send(data)

				self.enviado = "Arquivo enviado com sucesso"'''


	def send_file(self, name):
		with open("imagem_de_test.png", "rb") as foto:
			for data in foto.readlines():
				self.connection.send(data)

			self.enviado = "Arquivo enviado com sucesso"

if __name__ == "__main__":
	#SUBSTITUA OS ARGUMENTOS da instancia da classe Client(HOST, PORT):
	
	Client('127.0.0.1', 65432)


