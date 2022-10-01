from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tarefas(BoxLayout):
	def __init__(self, tarefas, **kwargs):
		super().__init__(**kwargs)
		#box = BoxLayout(orientation = "vertical")
		self.orientation = "vertical"
		self.size_hint_y = None
		self.height = self.minimum_height
		for item in tarefas:
			self.add_widget(Label(text = item, font_size = 30, size_hint_y = None, height = 100))

class Programa(App):
	def build(self):
#		box = BoxLayout(orientation = "vertical")
#		label1 = Label(text = "Texto 1")
#		box.add_widget(label1)
#		return box

		return Tarefas(['comer', 'programar', 'dormir'])


Programa().run()
