from events.Event import Event


class ChangeWindowEvent(Event):
    def __init__(self, new_window):
        self.new_window = new_window
