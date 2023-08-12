"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import quotesgeneratorapi_wrapper


class TogaQuotes(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        self.qoutegen = quotesgeneratorapi_wrapper.getQuotes(category="happienes")
        content = "Here could be a qoute"
        textbox = toga.Label(text=content)
        main_box.add(textbox)
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return TogaQuotes()
