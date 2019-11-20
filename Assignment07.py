# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: DQualley, 11/19/18 updated script to include processing functions
# Dustin Qualley, 11/18/19,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
# TODO: Add code here
    objFile = open(file_name, "ab")
    pickle.dump(list_of_data, file_name)
    objFile.close()

def read_data_from_file(file_name):
# TODO: Add code here
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# Presentation ------------------------------------ #
# get user input with structured error handling
try:
    fltNo1 = float(input("Enter your first number: "))
    fltNo2 = float(input("Enter your second number: "))
    quotient = fltNo1/fltNo2
    print("The quotient of", fltNo1, "and", fltNo2, "is", quotient)
except ZeroDivisionError as e:
    print("You cannot divide a number by 0!")
except ValueError as e:
    print("Invalid entry. Please enter a number!")
except Exception as e:
    print("There was a non-specific error!")

# Store the list object into a binary file
objFile = open("AppData.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()
# Read the data from the file into a new list object and display the contents
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print(objFileData)


