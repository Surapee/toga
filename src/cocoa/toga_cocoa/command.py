# from toga.interface.command import Group, Command as BaseCommand

from toga.widgets.icon import Icon


class Command:
    def __init__(self, interface):
        self.interface = interface
        self.icon = None

        if self.interface.icon_id:
            self.icon = Icon.load(self.interface.icon_id)
