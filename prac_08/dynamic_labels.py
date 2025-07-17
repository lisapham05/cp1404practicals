from kivy.app import App
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        """ Kivy for the Dynamic Labels App. """
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

