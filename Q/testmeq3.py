# Queue Program with File Reading

from contextlib import nullcontext
import os

QueueData = ["" for _ in range(0, 20)]
StartPointer = 0
EndPointer = 0

def Enqueue(DataToAdd, QueueData, EndP):
    if EndP == 20:
        return False, EndP
    else:
        QueueData[EndP] = DataToAdd
        EndP += 1
        return True, EndP

def ReadFile(QueueData, StartP, EndP):
    FileName = input("Enter a filename: ")
    if os.path.isfile(FileName):
        with open(FileName, "r") as f:
            Flag = True
            DataToInsert = f.readline().strip()
            while Flag and DataToInsert:
                Flag, EndP = Enqueue(DataToInsert, QueueData, EndP)
                DataToInsert = f.readline().strip()
            if not Flag:
                return 1, EndP
            else:
                return 2, EndP
    else:
        print("The file does not exist.")
        return 0, EndP

def Remove(QueueData, StartP, EndP):
    if EndP - StartP < 2:
        return "No Items", StartP, EndP
    else:
        Value1 = QueueData[StartP]
        StartP += 1
        Value2 = QueueData[StartP]
        StartP += 1
        return Value1 + " " + Value2, StartP, EndP

# Main Program
ReturnValue, EndPointer = ReadFile(QueueData, StartPointer, EndPointer)
if ReturnValue == -1:
    print("The file could not be found.")
elif ReturnValue == 1:
    print("The queue was full, not all items were read.")
else:
    print("All items successfully added.")
    print("Number of elements in the queue:", EndPointer - StartPointer)
    print("Elements in the queue are:")
    for i in range(StartPointer, EndPointer):
        print(QueueData[i])

# Test Remove function
result, StartPointer, EndPointer = Remove(QueueData, StartPointer, EndPointer)
print("Removed items:", result)
