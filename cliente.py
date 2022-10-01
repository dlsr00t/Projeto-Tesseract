import socket

class Client():
	def __init__(self, HOST, PORT):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.connection:
			self.connection.connect((HOST, PORT))
			with open("/home/foureyes/.programs/imagem_de_test.png", "rb") as foto:
				for data in foto.readlines():
					self.connection.send(data)

				self.enviado = "Arquivo enviado com sucesso"


	'''def send_archive(self):
		with open("imagem_de_test.png", "rb") as foto:
			for data in foto.readlines():
				self.connection.send(data)

			self.enviado = "Arquivo enviado com sucesso"
'''
if __name__ == "__main__":
	Client("0.tcp.sa.ngrok.io", 13024)
