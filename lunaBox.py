import pygame, sqlite3, sys, webbrowser

# Define and initialize global variables

#Program Variables
numEpisodesPrinted = 0
count = 0
episodeURLs = []
PASSED_URL = ''

#Pygame Variables
DISPLAYSURF = ''
WIDTH = 800
HEIGHT = 600
BABYBLUE = (99, 187, 214)
WINDOW_ICON = pygame.image.load('crystal-star-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license

#SQLite3 Variables
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
  initDisplay()
  pygame.display.flip()
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
  userInput = raw_input("Enter 'next', 'quit', or your episode number of choice to continue: ")
  if userInput == "next":
    printEpisodes()
    pygame.display.flip()
  elif userInput == "quit":
    sys.exit("Bye bye!")
  else:
    global episodeURLs
    global PASSED_URL
    PASSED_URL = episodeURLs[int(userInput)-1]
    openSelectedURL()

#Print the selected episodeURL
def openSelectedURL():
  webbrowser.open(PASSED_URL)

#Initialize the Pygame Surface
def initDisplay():
  global DISPLAYSURF, WIDTH, HEIGHT, WINDOW_ICON, BABYBLUE
  pygame.display.init()

  # Customize the icon that displays with the window
  pygame.display.set_icon(WINDOW_ICON)

  #Initialize the surface
  DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)

  #Fill the surface with a color.
  DISPLAYSURF.fill(BABYBLUE)

runProgram()