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

    def calculate_square(self):
        """Calculate the square of the user's input and update the result property."""
        try:
            number = float(self.root.ids.input_number.text)
            self.result = str(number ** 2)
        except ValueError:
            self.result = 'Invalid input'

    def clear_fields(self):
        """Clear the input and result fields."""
        self.root.ids.input_number.text = ''
        self.result = ''

SquaringApp().run()