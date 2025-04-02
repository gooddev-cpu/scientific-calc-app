from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class SciCalcApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', '^']
        self.last_was_operator = False
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
            ['sin', 'cos', 'tan', 'sqrt'],
            ['log', 'exp', 'atan', '^'],
            ['(', ')', 'DEL', '=']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        return layout
    
    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text
        
        if button_text == "C":
            self.result.text = ""
        elif button_text == "DEL":
            self.result.text = current_text[:-1]
        elif button_text == "=":
            try:
                expression = current_text.replace('^', '**')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('atan', 'math.atan')
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('exp', 'math.exp')
                self.result.text = str(eval(expression))
            except Exception:
                self.result.text = "Error"
        else:
            self.result.text += button_text

if __name__ == "__main__":
    SciCalcApp().run()
