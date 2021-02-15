"""
DEPEND TELNET TCPIP NETCARD
DEPEND TCPIP NETCARD
DEPEND NETCARD TCPIP
TCPIP depends on NETCARD, ignoring command
DEPEND DNS TCPIP NETCARD
DEPEND BROWSER TCPIP HTML
INSTALL NETCARD
Installing NETCARD
INSTALL TELNET
Installing TCPIP
Installing TELNET
INSTALL foo
Installing foo
REMOVE NETCARD
NETCARD is still needed
INSTALL BROWSER
Installing HTML
Installing BROWSER
INSTALL DNS
Installing DNS
LIST
NETCARD
TCPIP
TELNET
foo
HTML
BROWSER
DNS
REMOVE TELNET
Removing TELNET
REMOVE NETCARD
NETCARD is still needed
REMOVE DNS
Removing DNS
REMOVE NETCARD
NETCARD is still needed
INSTALL NETCARD
NETCARD is already installed
REMOVE TCPIP
TCPIP is still needed
REMOVE BROWSER
Removing BROWSER
Removing TCPIP
Removing HTML
REMOVE TCPIP
TCPIP is not installed
LIST
NETCARD
foo
END
"""

from collections import namedtuple

COMMANDS = namedtuple('COMMANDS', 'DEPEND,INSTALL,REMOVE,LIST,END')


class SI(object):

    def __init__(self):
        self.ALLOWED_COMMANDS = COMMANDS('DEPEND', 'INSTALL', 'REMOVE', 'LIST', 'END')
        self.items = dict()

    def validate_commands(self, command_list):
        print(' '.join(command_list))
        if command_list[0] == self.ALLOWED_COMMANDS.DEPEND:
            self.add_dependency(command_list[1:])
        elif command_list[0] == self.ALLOWED_COMMANDS.INSTALL:
            self.install_item(command_list[1])
        elif command_list[0] == self.ALLOWED_COMMANDS.REMOVE:
            self.remove_item(command_list[1])
        elif command_list[0] == self.ALLOWED_COMMANDS.LIST:
            self.list_items()

    def add_dependency(self, dependency_list, index=0, dependent_by=None):
        name = dependency_list[index]
        item = SI.Item(name) if name not in self.items else self.items.get(name)
        if index < len(dependency_list) - 1:
            on_item = dependency_list[index + 1]
            if name in self.items and name in self.items[on_item].dependent_on:
                print(on_item, 'depends on ', name, ',ignoring command')
                return
            self.add_dependency(dependency_list, index + 1, name)
            item.dependent_on.add(on_item)
        if dependent_by is not None:
            item.dependent_by.add(dependent_by)
        self.items[name] = item

    def install_item(self, item_name):
        if item_name not in self.items:
            print(" DEPENDENCY GRAPH NOT KNOWN")
            return
        item: SI.Item = self.items.get(item_name)
        if not item.is_installed:
            for on_item in item.dependent_on:
                if on_item in self.items and not self.items[on_item].is_installed:
                    self.install_item(on_item)
            print('Installing ', item_name)
            item.is_installed = True
        elif item.is_installed:
            print(item_name, ' is already installed')

    def remove_item(self, item_name, remove_chain_item=None):
        item: SI.Item = self.items.get(item_name)
        if item is None:
            return
        # check if there are any dependent by items
        if remove_chain_item is None:
            if len(item.dependent_by) > 0:
                print(item_name, ' is still needed')
                return
            elif len(item.dependent_on) > 0:
                for on_item in item.dependent_on:
                    self.remove_item(on_item, item_name)
            print("Removing ", item_name)
            self.items.pop(item_name)
        else:
            if len(item.dependent_by) == 1 and remove_chain_item in item.dependent_by:
                if len(item.dependent_on) > 0:
                    for on_item in item.dependent_on:
                        self.remove_item(on_item, item_name)
                print("Removing ", item_name)
                self.items.pop(item_name)
            else:
                item.dependent_by.remove(remove_chain_item)

    def list_items(self):
        for item_name in self.items:
            if self.items[item_name].is_installed:
                print(item_name)

    class Item(object):
        def __init__(self, name):
            self.name = name
            self._dependent_on = set()
            self._dependent_by = set()
            self._is_installed = False

        @property
        def dependent_on(self):
            return self._dependent_on

        @property
        def dependent_by(self):
            return self._dependent_by

        @dependent_on.setter
        def dependent_on(self, item):
            self._dependent_on.add(item)

        @dependent_by.setter
        def dependent_by(self, item):
            self._dependent_by.add(item)

        @property
        def is_installed(self):
            return self._is_installed

        @is_installed.setter
        def is_installed(self, is_installed):
            self._is_installed = is_installed


if __name__ == "__main__":
    number_of_commands = 0
    cmd_list = []
    systemInstaller = SI()
    while True:
        cmd = input()
        """ condition to check number of commands has been entered"""
        if number_of_commands > 0:
            cmd_list = cmd.split()
            command_name = cmd_list[0]
            if command_name not in systemInstaller.ALLOWED_COMMANDS:
                print("Unrecognized command")
            else:
                systemInstaller.validate_commands(cmd_list)
        else:
            try:
                number_of_commands = int(cmd)
            except ValueError:
                print(" As first command enter the number of Test cases ")
        if len(cmd_list) > 0 and cmd_list[0] == "END":
            print("END")
            break
