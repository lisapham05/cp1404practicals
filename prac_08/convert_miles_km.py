from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM_MULTIPLIER = 1.60934

class ConvertMilesKilometers(App):
    """ Kivy BoxLayout widget for the miles to kilometres converter. """
    def build(self):
        """ Build kv app from kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

