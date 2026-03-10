from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import subprocess

class SherlockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Введите никнейм для поиска:")
        self.layout.add_widget(self.label)
        
        self.input = TextInput(multiline=False)
        self.layout.add_widget(self.input)
        
        self.btn = Button(text="Начать поиск", background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.run_sherlock)
        self.layout.add_widget(self.btn)
        
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def run_sherlock(self, instance):
        username = self.input.text
        if username:
            self.result_label.text = f"Ищу {username}..."
            # Здесь будет логика вызова Sherlock
        else:
            self.result_label.text = "Ошибка: введите ник!"

if __name__ == '__main__':
    SherlockApp().run() 
    
  
