from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class ConvertMilesKilometers(App):
    """ Kivy BoxLayout widget for the miles to kilometres converter. """
    def build(self):
        """ Build kv app from kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculate(self):
        """ Handle calculation for label widgets """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        Handle up/down button press, update the text input with new value, call calculation function
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

ConvertMilesKilometers().run()