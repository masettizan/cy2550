import argparse
import random
# Defining a class with constructor and a method

def readFile():
        file = open("words.txt", "r")
        data = file.read()
  
        # replacing end splitting the text 
        # when newline ('\n') is seen.
        data_into_list = data.split("\n")
        file.close()

        return data_into_list

def generatePassword(data, words, caps, numbers, symbols):
        password = list()
        indexToCaps = wordsToCaps(words, caps)

        i = 0
        while i < words:
            word = random.choice(data)
            if (i in indexToCaps):
                word = word[:1].upper() + word[1:]

            password.append(word)
            #data.remove(word)
            i += 1
        
        password = addNumbers(password, numbers)
        password = addSymbols(password, symbols)
        return "".join(str(x) for x in password)
    
def wordsToCaps(words,caps):
        indexes = list()
    
        while len(indexes) < caps:
            index = random.randrange(0, words)
            if (index not in indexes):
                indexes.append(index)
        
        return indexes
    
def addNumbers(password, numbers):
        i = 0
        while i < numbers:
            index = random.randint(0, len(password))
            password.insert(index, random.randrange(0,10))
            i += 1
      
        return password
    
def addSymbols(password, symbols):
        sym = "`~!@#$%^&*()-_+=[]\;',./{}|:\"<>?"
        i = 0
        while i < symbols:
            index = random.randint(0, len(password))
            password.insert(index, random.choice(sym))
            i += 1
        
        return password

wordArg = 4
capArg = 0
numArg = 0
symArg = 0

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--words", type = int, help = "include WORDS words in the password (default=4)")
parser.add_argument("-c","--caps", type = int, help = "capitalize the first letter of CAPS random words (default=0)");
parser.add_argument("-n","--numbers", type = int, help = "insert NUMBERS random numbers in the password (default=0)");
parser.add_argument("-s","--symbols", type = int, help = "insert SYMBOLS random symbols in the password (default=0)");

args = parser.parse_args()

if args.words: 
    wordArg = args.words
if args.caps:
    capArg = args.caps
if args.numbers:
    numArg = args.numbers
if args.symbols:
    symArg = args.symbols

data = readFile()
print(generatePassword(data,wordArg,capArg,numArg,symArg)) 



