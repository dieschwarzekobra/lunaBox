import pygame, sqlite3, sys, webbrowser

#Initialize all pygame modules
pygame.init()

# Define and initialize global variables

#Program Variables
numEpisodesPrinted = 0
count = 0
episodeURLs = []
PASSED_URL = ''

#Pygame Variables
##Surfaces
DISPLAYSURF = ''

##Dimensions and Sizes
WIDTH = 1280
HEIGHT = 720
FONT_SIZE = 32
PADDING = 60

##Colors
BABYBLUE = (99, 187, 214)
WHITE = (255, 255, 255)
PINK = (252, 35, 158)

##Images and fonts
BASEFONT = pygame.font.Font('CREAMPUF.ttf', FONT_SIZE) # Downloaded as freeware under commercial use allowed license on Fontspace
WINDOW_ICON = pygame.image.load('crystal-star-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license
MENU_IMAGE = pygame.image.load('titleBanner.png') # Snagged from the Sailor Moon Wikia: http://sailormoon.wikia.com/wiki/Ami_Mizuno, retrieved using Google
SELECTOR = pygame.image.load('crisis-moon-compact-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license

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

  # Initialize all of the graphics
  initDisplay()
  pygame.display.flip()
  printEpisodes()
  drawSelector()
  drawPaginator()

  # Initialize counts
  totalNum = countRows(STATEMENT_PRINT_ALL_TITLES)  
  global numEpisodesPrinted

  # Initialize main loop
  while numEpisodesPrinted < totalNum:
    #paginate()
    keyPressed()

# Print limited number of results
def printEpisodes():
  # Set topCoord starting point for the episodes to start printing from in the display
  topCoord = PADDING
  for row in c.execute(STATEMENT_PAGINATE):
    # Update the count of the number of episodes printed
    global numEpisodesPrinted
    numEpisodesPrinted += 1

    # Add URL of the current episode to the array of callable URLs / episodes
    episodeURLs.append(row[0])

    # Print the title and number of the episode to the console
    ep = str(numEpisodesPrinted) + ". " + row[1]
    print ep

    # Print the title and number of the episode to a surface
    epSurf = BASEFONT.render(ep, True, WHITE, PINK)
    epSurfRect = epSurf.get_rect() 
    epSurfRect.top = topCoord
    epSurfRect.left = MENU_IMAGE.get_width()

    # Print episode surface onto main surface and update the display
    DISPLAYSURF.blit(epSurf, epSurfRect)
    pygame.display.flip()

    # Reset the topCoord so that the episode titles do not overlap
    topCoord += epSurfRect.height + 50

  # Reset the topCoord to PADDING for the next set of results
  topCoord = PADDING


#Wait for user input before continuing to print results or URL
def paginate():
  userInput = raw_input("Enter 'next', 'quit', or your episode number of choice to continue: ")
  if userInput == "next":
    printEpisodes()
    drawPaginator()
    drawSelector()
    pygame.display.flip()
  elif userInput == "quit":
    sys.exit("Bye bye!")
  else:
    global episodeURLs
    global PASSED_URL
    PASSED_URL = episodeURLs[int(userInput)-1]
    openSelectedURL()

#Open the selected episodeURL
def openSelectedURL():
  webbrowser.open(PASSED_URL)

#Initialize the Pygame Surface
def initDisplay():
  global DISPLAYSURF
  pygame.display.init()

  # Customize the icon that displays with the window
  pygame.display.set_icon(WINDOW_ICON)

  #Initialize the surface
  DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))

  #Fill the surface with a color.
  DISPLAYSURF.fill(BABYBLUE)

  #Draw the menu image
  MENU_IMAGE_RECT = MENU_IMAGE.get_rect()
  DISPLAYSURF.blit(MENU_IMAGE, MENU_IMAGE_RECT)


#Draw the selector
def drawSelector():
  SELECTOR_RECT = SELECTOR.get_rect()
  SELECTOR_RECT.left = WIDTH/2
  SELECTOR_RECT.top = PADDING
  DISPLAYSURF.blit(SELECTOR, SELECTOR_RECT)
  pygame.display.flip()
  

#Draw the paginator
def drawPaginator():
  PAGINATOR = BASEFONT.render("Next", True, WHITE, PINK)
  PAGINATOR_RECT = PAGINATOR.get_rect()
  PAGINATOR_RECT.left = WIDTH - PAGINATOR.get_width()
  PAGINATOR_RECT.top = HEIGHT - (PAGINATOR.get_height() + PADDING)
  DISPLAYSURF.blit(PAGINATOR, PAGINATOR_RECT)
  pygame.display.flip()

#Define Key Events
def keyPressed():
  #Listen for keydown events
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: #If the user presses a key...
      if event.key == pygame.K_LEFT:
        print "Left"
      elif event.key == pygame.K_RIGHT:
        print "Right"
      print "True"

runProgram()