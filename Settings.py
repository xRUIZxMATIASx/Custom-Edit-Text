class Settings:

    __colorTezt = ""
    __background = ""
    __font = ""

    def __init__(self):
        file = open("settings", "r")
        text = file.readlines()
        self.setColorText(text[0].strip("\n"))
        self.setBackground(text[1].strip("\n"))
        self.setSizeFont(text[2].strip("\n"))

    def getBackgroundColor(self):
        return self.__background

    def getColorText(self):
        return self.__colorTezt

    def getSizeFont(self):
        return self.__font

    def setColorText(self, colorText):
        self.__colorTezt = colorText
        file = open("settings", "w")
        text = self.__colorTezt + "\n" + self.__background + "\n" + self.__font
        file.write(text)

    def setBackground(self, background):
        self.__background = background
        file = open("settings", "w")
        text = self.__colorTezt + "\n" + self.__background + "\n" + self.__font
        file.write(text)

    def setSizeFont(self, size):
        self.__font = size
        file = open("settings", "w")
        text = self.__colorTezt + "\n" + self.__background + "\n" + self.__font
        file.write(text)

