MyCats = []
class CutestCats:
    def __init__(self, Name, Description, Weight, Length, Appearance, LifeExpectancy, ImageUrl):
        self.__Name = Name
        self.__Description = Description
        self.__Weight = Weight
        self.__Length = Length
        self.__Appearance = Appearance
        self.__LifeExpectancy = LifeExpectancy
        self.__ImageUrl = ImageUrl

    def GetCatDetails(self):
        try:
            with openfile("CutestCats.txt") as f:
                for i in range(0, 101,7):
                    Name=f.readline
                    Description = f.readline()
                    Weight = f.readline()
                    Length = f.readline()
                    LifeExpectancy = f.readline()
                    ImageUrl = f.readline()
                    MyCats.append(CutestCats(Name, Description, Weight, Length, LifeExpectancy, ImageUrl))
        except FileNotFoundError:
            print("File not found.")
        return self.__Name, self.__Description, self.__Weight, self.__Length, self.__Appearance, self.__LifeExpectancy, self.__ImageUrl

    def calculateAverage(list):
        if len(list) == 1:
            return list[0]
        elif len(list) == 2:
            avg = ((list[0] + list[1])/2)
            return int(avg)

    LifeExpectancy = []

    def GetCatLife(self):
        for i in range(len(MyCats)):
            stats = Cat.GetCatLife(MyCats[i])
            print(stats)
            LifeExpectancy.append(stats)
        return self.__Name, self.__LifeExpectancy

GetCatLife()
print(LifeExpectancy)
