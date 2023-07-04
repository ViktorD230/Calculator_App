from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('design.kv')


class Box(Widget):

    def show(self, num):
        display = self.ids.display_result

        if display.text == "0":
            display.text = ""
        display.text += num

    def clear(self):
        display = self.ids.display_result
        display.text = "0"

    def CE(self):
        display = self.ids.display_result
        l = len(display.text)
        digit = display.text[:-1]
        display.text = digit

    def equal(self):
        display = self.ids.display_result
        try:
            result = eval(display.text)
            display.text = str(result)
        except ZeroDivisionError:
            display.text = "Error"

        if display.text == "69":
            display.text += "OMG!"


class MyApp(App):
    def build(self):
        return Box()


MyApp().run()
