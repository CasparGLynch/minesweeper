from events.Event import Event


class ChangeWindowEvent(Event):
    def __init__(self, new_window: str, type_e: str):
        self.new_window = new_window
        self.type_e = type_e
