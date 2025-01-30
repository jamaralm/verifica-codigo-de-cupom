import json

filePath = "./codes.json"

def transformToTuple(code, discount):
    codeTransformed = (code, discount)
    return codeTransformed

def readJsonFile(file):
    try: 
        with open(file, 'r') as f:
            return json.load(f)
            print("File read successfully")
    except FileExistsError:
        print('File does not exist')
    except FileNotFoundError:
        print('File not found')
    except json.JSONDecodeError:
        print('Invalid JSON format')

def verifyIfCodeExists(codeInput):
    data = readJsonFile(filePath)
    for i in data:
        codeData = transformToTuple(i['code'], i['discount'])
        code, discount = codeData
        
        try:
            if codeInput == code:
                print("Code Found!")
                return True
            
            print("Code Not Found!")
            return False
        except ValueError:
            print('TYPE A VALID CODE!')

def askForCode():
    while True:
        codeInput = input("Enter the code: ").strip()  # Get user input and remove extra spaces
        if verifyIfCodeExists(codeInput):
            break  # Exit the loop if the code is found
        else:
            print("Please try again.\n")