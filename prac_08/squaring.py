from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class SquaringApp(App):
    """Main application class for squaring numbers with Kivy."""
    result = StringProperty('')

    def build(self):
        """Load the UI and return the root widget"""
        self.title = "Squaring Numbers"
        self.root = Builder.load_file('squaring.kv')
        return self.root


