class Restore:

    __saved = False

    def push(self, text):
        if not self.__saved:
            open("temp", "w").write(text)

    def saved(self):
        self.__saved = True
        open("temp", "w").write("")

    def delete(self):
        open("temp", "w").write("")

