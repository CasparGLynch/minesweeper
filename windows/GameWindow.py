from windows.Window import Window


class GameWindow(Window):

    def __init__(self, width, height):
        super().__init__(width, height)

    def handle_event(self, event):
        pass

    def update(self, mouse_pos):
        pass

    def display(self):
        return []
