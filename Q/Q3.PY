#Q3(a) program that declears the queue data
from contextlib import nullcontext
import os


QueueData = ["" for I in range(0, 20)]
StartPointer = 0
EndPointer = 0
#Q3(b)function should take an item to be added to the queue as a parameter:
def Enqueue(DataToAdd, QueueData, EndP):
    if(EndP == 20):
     return False, EndP
    else:
       QueueData[EndP] = DataToAdd
       EndP = EndP + 1
       return True, EndP
#Q3(c) program code for a function, ReadFile, which: 
    #• asks the user to input a filename • reads the data from the text file into QueueData
def ReadFile(QueueData, StartP, EndP):
  FileName = input("Enter a filename")
  if(os.path.isfile(FileName)):
    f = open(FileName, "r")
    Flag = True
    DataToInsert = (f.readline()).strip()
    while(Flag == True and DataToInsert != nullcontext):
      Flag, EndP = Enqueue(QueueData, EndP)
      DataToInsert = (f.readline()).strip()
      if(Flag == False):
        f.close()
        return 1, EndP
      else:
        f.close()
        return 2, EndP
    else:
      return -1, EndP
    #else:
      print("The file does not exist.")
      return 0, EndP  
  else:
    return 0, EndP
#Q3(d)(i)The main program calls ReadFile. ReadFile outputs an appropriate message to identify if:
 #the text file could not be found • the queue was full • all items were added to the queue.
ReturnValue, EndPointer = ReadFile(QueueData, StartPointer, EndPointer)
if(ReturnValue == -1):
 print("The file could not be found.")
elif(ReturnValue == 1):
 print("The queue was full, not all items were read.")
else:
 print("All items successfully added.")
 print("Number of elements in the queue: ", EndPointer-StartPointer)
print("Elements in the queue are: ")
for i in range(StartPointer, EndPointer):
  print(QueueData[i])

#Q(e) function, Remove: to removes the first two elements from the queue
def Remove(QueueData, StartP, EndP):
  if(EndP - StartP < 2):
    return "No Items", StartP, EndP
  else:
    Value1 = QueueData[StartP]
    StartP = StartP + 1
    Value2 = QueueData[StartP]
    StartP = StartP + 1
    return(Value1 + " " + Value2), StartP, EndP
