from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """ Load and return the Kivy interface layout defined in the 'box_layout.kv' file. """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """
        Event handler for the 'Greet' button.
        Retrieves the text from the TextInput, prints 'greet' to the console,
        and updates the Label to greet the user by name.
        """
        print('greet')
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """
        Event handler for the 'Clear' button.
        Resets both the TextInput and the output Label to be empty.
        """
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

BoxLayoutDemo().run()