from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class ConvertMilesKilometers(App):
    """ Kivy BoxLayout widget for the miles to kilometres converter. """
    def build(self):
        """ Build kv app from kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
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
