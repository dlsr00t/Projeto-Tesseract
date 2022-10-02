import cliente
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Programa(App):
#	clientee = cliente.Client("0.tcp.sa.ngrok.io", 13024)
	def build(self):
		box = BoxLayout(orientation = "vertical")
		botao1 = Button(text = "Conectar-se" , on_release = self.conectar)
		#botao2 = Button(text = "Enviar foto", on_release = self.cliente.send_archive())
		box.add_widget(botao1)
		#box.add_widget(botao2)
		return box

	def conectar(self, botao1):
		cliente.Client("0.tcp.sa.ngrok.io",18976)


Programa().run()
