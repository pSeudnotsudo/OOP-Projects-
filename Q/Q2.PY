 #Question 2(a) Constructor declaration taking four parameters
class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String
#Q2(b)
     def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation):
         self.__BoxName = NewBoxName
         self.__Creator = NewCreator
         self.__DateHidden = NewDateHidden
         self.__GameLocation = NewLocation
         self.__LastFinds = [["" for j in range(0, 2)] for I in range(0, 10)]
         self.__Active = False
#2(c)
     def GetBoxName():
            return Self.__BoxName
            def GetLocation():
                 return self.__GameLocation
#2(d)(i)
TheBoxes = [HiddenBox("","","","") for I in range(0, 10000)]  
#Q2(d)(ii)
def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Enter the name of the box")
    Creator = input("Enter the creator’s name")
    DateHidden = input("Enter the date the box was hidden")
    GameLocation = input("Enter the location of the box")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return(NumBoxes + 1)
NewBox(TheBoxes, 0)
print(TheBoxes[5].GetBoxName())
#Q2(e)
class PuzzleBox(HiddenBox):
  # __PuzzleText String
  # __Solution String
     def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText,
                  NewSolution):
          super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
          self.__PuzzleText = NewPuzzleText
          self.__Solution = NewSolution
          def ShowHide(Self):
               if (Self.__Active == True):
                   print("This is a puzzle box. Please enter the correct solution to reveal\n",
                         "the contents:\n", Self.__PuzzleText)
               else:
                   print("Sorry, this is not a puzzle box.")
          
