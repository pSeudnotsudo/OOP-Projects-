class HiddenBox:
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation):
        self.__BoxName = NewBoxName
        self.__Creator = NewCreator
        self.__DateHidden = NewDateHidden
        self.__GameLocation = NewLocation
        self.__LastFinds = [["" for j in range(0, 2)] for i in range(0, 10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetLocation(self):
        return self.__GameLocation

class PuzzleBox(HiddenBox):
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution):
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution

    def ShowHide(self):
        if self.__Active == True:
            print("This is a puzzle box. Please enter the correct solution to reveal\n", "the contents:\n", self.__PuzzleText)
        else:
            print("Sorry, this is not a puzzle box.")

TheBoxes = [HiddenBox("", "", "", "") for i in range(0, 10000)]
def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Enter the name of the box")
    Creator = input("Enter the creator’s name")
    DateHidden = input("Enter the date the box was hidden")
    GameLocation = input("Enter the location of the box")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return NumBoxes + 1

NewBox(TheBoxes, 0)
print(TheBoxes[5].GetBoxName())
