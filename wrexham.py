players = []

class Wrexham:
    def __init__(self, PlayerNumber, Forename, Surname, Position):
        self.__PlayerNumber = PlayerNumber
        self.__Forename = Forename
        self.__Surname = Surname
        self.__Position = Position
        self.__CommunityInvolvement = 0
        self.__Injured = False

    def GetPlayerInfo(self):
        return self.__Forename, self.__Surname, self.__Position

    def ChangeCommunityInvolvement(self, Change):
        self.__CommunityInvolvement = self.__CommunityInvolvement + change

    def ChangeInjured(self):
        if self.__Injured == True:
            self.__Injured == False
        elif self.__Injured == False:
            self.__Injured == True

try:
    with open("wrexham.txt") as f:
        for i in range(0, 112, 4):
            PlayerNumber = f.readline().strip()
            Forename = f.readline().strip()
            Surname = f.readline().strip()
            Position = f.readline().strip()
            players.append(Wrexham(PlayerNumber, Forename, Surname, Position))
except FileNotFoundError:
    print("File not found.")

print(Wrexham.GetPlayerInfo(players[2]))

for i in range(len(players)):
    print(Wrexham.GetPlayerInfo(players[i]))
