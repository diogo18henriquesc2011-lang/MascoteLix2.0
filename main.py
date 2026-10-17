import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class AxoloteApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Procura as imagens enviadas no repositório
        self.images = [f for f in os.listdir('.') if f.endswith('.png')]
        self.images.sort()
        self.current_idx = 0
        
        # Exibe a primeira imagem (se existir)
        initial_image = self.images[0] if self.images else ''
        self.img_display = Image(source=initial_image)
        self.root.add_widget(self.img_display)
        
        # Botão para mudar de expressão
        self.btn = Button(text='Mudar Expressão', size_hint=(1, 0.2))
        self.btn.bind(on_press=self.change_expression)
        self.root.add_widget(self.btn)
        
        return self.root

    def change_expression(self, instance):
        if self.images:
            self.current_idx = (self.current_idx + 1) % len(self.images)
            self.img_display.source = self.images[self.current_idx]
            self.img_display.reload()

if __name__ == '__main__':
    AxoloteApp().run()
      
