
class WorldMusic:
    def __init__(self,Fullname):
        self.Fullname = Fullname
    def show(self):
        print(self.Fullname+"is a Music Artist")
class DancehallMusic(WorldMusic):
    pass
class ReggeaMusic(WorldMusic):
    pass
RM = ReggeaMusic("Chronixx")
RM.show()