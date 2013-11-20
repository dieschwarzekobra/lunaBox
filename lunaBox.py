import sqlite3

# Define and initialize global variables
numEpisodesPrinted = 0
count = 0
episodeURLs = []
PASSED_URL = ''
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
    # Update the count of the number of episodes printed
    global numEpisodesPrinted
    numEpisodesPrinted += 1

    # Add URL of the current episode to the array of callable URLs / episodes
    episodeURLs.append(row[0])

    # Print the title and number of the episode
    print str(numEpisodesPrinted) + ". " + row[1]

#Wait for user input before continuing to print results or URL
def paginate():
  userInput = raw_input("Enter yes your episode number of choice to continue: ")
  if userInput == "Yes":
    printEpisodes()
  else:
    global episodeURLs
    global PASSED_URL
    PASSED_URL = episodeURLs[int(userInput)-1]
    printSelectedURL()

#Print the selected episodeURL
def printSelectedURL():
  print PASSED_URL

runProgram()