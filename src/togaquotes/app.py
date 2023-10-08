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
        main_box.style.direction = "column"
        try:
            self.qoutegen = quotesgeneratorapi_wrapper.getQuotes(
                category="happiness", api_key="As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk"
            )
            content = self.qoutegen
            content, quoteauthor = content.split(sep="\n\n")
        except:
            content = "Check your Connection"
            author = ""
        self.quote = toga.MultilineTextInput()
        self.quoteauthor = toga.Label(text=quoteauthor, style=Pack(padding=5))
        refreshbtn = toga.Button(
            text="Refresh", on_press=self.get, style=Pack(padding=5)
        )
        main_box.add(self.quote)
        main_box.add(self.quoteauthor)
        main_box.add(refreshbtn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get(self, widget):
        self.quote.clear()
        try:
            self.qoutegen = quotesgeneratorapi_wrapper.getQuotes(
                category="happiness", api_key="As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk"
            )
            content = self.qoutegen
            content, quoteauthor = content.split(sep="\n\n")
        except:
            content = "Check your Connection"
            author = ""
        self.quote.text = content
        self.quoteauthor.text


def main():
    return TogaQuotes()
