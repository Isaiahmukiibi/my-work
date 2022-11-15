class WorldMusic:
    def __init__(self, FullName):
        self.FullName = FullName
    def show(self):
        print(self.FullName,"is a Music Artist")
class DancehallMusic:
    def Credit (self):
        print( self.FullName ,"is multi-talented !!!!")
class ReggeaMusic(WorldMusic, DancehallMusic):
    pass
RM = ReggeaMusic("Tarrus Rilley")
RM.show()
RM.Credit()

