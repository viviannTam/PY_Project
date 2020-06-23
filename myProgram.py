print('Hello World')

class Computer:
    def __init__(self, type_of_computer, computer_manufacturer, windows_edition, memory_space):
        self.type_of_computer = type_of_computer
        self.computer_manufacturer = computer_manufacturer
        self.windows_edition = windows_edition
        self.memory_space = memory_space

    def playGame(self, game):
        print("The name of the game is ", game)

laptop = Computer('laptop', 'Acer', 5, '8GB')
print(laptop.type_of_computer)
print(laptop.computer_manufacturer)
print(laptop.windows_edition)
print(laptop.memory_space)
laptop.playGame("Line Play")

class Computer2(Computer):
    def __init__(self, computer_manufacturer, windows_edition, memory_space):
        Computer.__init__(self, 'desktop', computer_manufacturer, windows_edition, memory_space)

desktop = Computer2('Acer', 5, '8GB')
print(desktop.computer_manufacturer)
print(desktop.windows_edition)
print(desktop.memory_space)
desktop.playGame("Mobile Legend")