import sqlite3

# Define and initialize global variables
numEpisodesPrinted = 0
count = 0
STATEMENT_PRINT_ALL_TITLES = 'SELECT * FROM sailorMoon'
STATEMENT_PAGINATE = 'SELECT * FROM sailorMoon WHERE episode > ' + str(numEpisodesPrinted) + ' ORDER BY episode LIMIT 3'

# Connect to the database
conn = sqlite3.connect('sailorMoon.sqlite')
c = conn.cursor()

# Count all of the rows in the database
def countRows(statement):
  for row in c.execute(statement):
    global count
    count += 1
  global count
  return count

# Main Loop for the program
def runProgram():
  totalNum = countRows(STATEMENT_PRINT_ALL_TITLES)  
  global numEpisodesPrinted
  printEpisodes()
  while numEpisodesPrinted < totalNum:
    paginate()

# Print limited number of results
def printEpisodes():
  for row in c.execute(STATEMENT_PAGINATE):
    global numEpisodesPrinted
    numEpisodesPrinted += 1
    print row[1] + ". Num Printed: " + str(numEpisodesPrinted)

#Wait for user input before continuing to print results
def paginate():
  userInput = raw_input("Continue?: ")
  if userInput == "Yes":
    printEpisodes()



runProgram()