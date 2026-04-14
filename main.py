"""
#######[Made By Deadcode]#######
"""
from random import choice
import pyttsx3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time

def speak(text):
    # Reinitialize engine each time to avoid "first time only" bug
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

class RPSGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=20, **kwargs)

        self.lbl_pc = Label(text="Computer chose: ?", font_size=22, color=(0, 0, 0, 1))
        self.lbl_result = Label(text="Result will appear here", font_size=28, bold=True, color=(0.2, 0.4, 0.8, 1))

        self.add_widget(self.lbl_pc)
        self.add_widget(self.lbl_result)

        btn_layout = BoxLayout(size_hint=(1, 0.3), spacing=15)

        btn_layout.add_widget(Button(
            text="✂ Scissor", background_color=(1, 0.6, 0.6, 1),
            font_size=20, on_press=lambda x: self.play(1)
        ))
        btn_layout.add_widget(Button(
            text="🪨 Rock", background_color=(0.6, 0.8, 1, 1),
            font_size=20, on_press=lambda x: self.play(2)
        ))
        btn_layout.add_widget(Button(
            text="📄 Paper", background_color=(0.6, 1, 0.6, 1),
            font_size=20, on_press=lambda x: self.play(3)
        ))

        self.add_widget(btn_layout)

    def play(self, choice_num):
        pc_choice = choice(['Rock', 'Paper', 'Scissor'])
        user_choice = {1: 'Scissor', 2: 'Rock', 3: 'Paper'}[choice_num]

        # Decide outcome
        if user_choice == 'Scissor':
            if pc_choice == 'Paper':
                result = "You Won!"
            elif pc_choice == 'Rock':
                result = "I Won!"
            else:
                result = "Tie!"
        elif user_choice == 'Rock':
            if pc_choice == 'Paper':
                result = "I Won!"
            elif pc_choice == 'Rock':
                result = "Tie!"
            else:
                result = "You Won!"
        elif user_choice == 'Paper':
            if pc_choice == 'Paper':
                result = "Tie!"
            elif pc_choice == 'Rock':
                result = "You Won!"
            else:
                result = "I Won!"

        # Update UI
        self.lbl_pc.text = f"Computer chose: {pc_choice}"
        self.lbl_result.text = result

        # Speak result
        speak(f"Computer chose {pc_choice}. {result}")

class RPSApp(App):
    def build(self):
        return RPSGame()

if __name__ == "__main__":
    RPSApp().run()
