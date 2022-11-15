class WorldMusic:
    def __init__(self, FullName):
        self.FullName = FullName
    def show(self):
        print(self.FullName , "is a Music Artist")
class DacehallMusic(WorldMusic):
    pass
class ReggeaMusic (WorldMusic):
    pass
DM = DacehallMusic("Buju Banton")
DM.show()
RM = ReggeaMusic("Chris Martins")
RM.show()