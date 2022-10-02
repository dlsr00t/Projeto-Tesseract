###ESSE PROGRAMA ESTA PRONTO PARA USO

import socket

class Client():
	def __init__(self, HOST, PORT):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.connection:
			self.connection.connect((HOST, PORT))
			status = self.connection.recv(1024)
			if status.decode() == "":
				print("Sem conexao com o servidor")
			elif status.decode() == "CONECTADO ao servidor":
				print(status.decode())


	def send_file(self, name):
		with open(name, "rb") as foto:
			for data in foto.readlines():
				self.connection.send(data)

			self.enviado = "Arquivo enviado com sucesso"

if __name__ == "__main__":
	#SUBSTITUA OS ARGUMENTOS da instancia da classe Client(HOST, PORT):
	
	Client('127.0.0.1', 65432)


