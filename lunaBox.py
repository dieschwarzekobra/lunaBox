import pygame, sqlite3, sys, webbrowser

#Initialize all pygame modules
pygame.init()


#####################################################################################################

# Define and initialize global variables

#Program Variables
numEpisodesPrinted = 0
count = 0
episodes = []
episodeURLs = []
#PASSED_URL = ''
#printed = numEpisodesPrinted
greatestEpisode = 0
begOfCurrentGroup = 0
episodeList = []
endOfPreviousGroup = ''
counter = 0
page = []
pageURLs = []
#####################################################################################################


#Pygame Variables
##Surfaces
DISPLAYSURF = ''
URL = numEpisodesPrinted

#####################################################################################################

##Dimensions and Sizes
WIDTH = 1280
HEIGHT = 720
FONT_SIZE = 32
PADDING = 60

#####################################################################################################

##Colors
BABYBLUE = (99, 187, 214)
WHITE = (255, 255, 255)
PINK = (252, 35, 158)

#####################################################################################################

##Images and fonts
BASEFONT = pygame.font.Font('CREAMPUF.ttf', FONT_SIZE) # Downloaded as freeware under commercial use allowed license on Fontspace
WINDOW_ICON = pygame.image.load('crystal-star-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license
MENU_IMAGE = pygame.image.load('titleBanner.png') # Snagged from the Sailor Moon Wikia: http://sailormoon.wikia.com/wiki/Ami_Mizuno, retrieved using Google
SELECTOR = pygame.image.load('crisis-moon-compact-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license
SELECTOR_RECT = SELECTOR.get_rect()
SELECTOR_RECT.left = WIDTH/2
SELECTOR_RECT.top = PADDING

#####################################################################################################

##SQLite3 Variables
ALL_TITLES = 'SELECT * FROM sailorMoon'
PAGINATE = ''
FORWARD = str(numEpisodesPrinted)
BACKWARD = str(numEpisodesPrinted - 6)
LIMIT = 3

#####################################################################################################

##Main Loop variables
programRunning = True

#####################################################################################################

# Connect to the database
conn = sqlite3.connect('sailorMoon.sqlite')
c = conn.cursor()

#####################################################################################################

# Count all of the rows in the database
def countRows(statement):
  for row in c.execute(statement):
    global count
    count += 1
  return count

#####################################################################################################

# Main Loop for the program
def runProgram():

  #Initialize all of the graphics
  initDisplay()
  readEpisodes()

  #Initialize variables
  global programRunning

  #Initialize main loop
  while programRunning:
    keyDownEvents()

#####################################################################################################


def readEpisodes():
  global episodes, episodeURLs

  for row in c.execute(ALL_TITLES):
    episodes.append(str(row[3]) + ". " + row[1])
    episodeURLs.append(row[0])


#####################################################################################################

def grabEpisodes(direction):
  global numEpisodesPrinted, page, pageURLs

  i = numEpisodesPrinted
  lastI = count - i
  page = []
  pageURLs = []

  #If going forward, grab episodes i through i+3
  if (direction == "FORWARD") and (i+3 <= count):
    for x in range(i, i+3):
      page.append(episodes[x])
      pageURLs.append(episodeURLs[x])
    numEpisodesPrinted += 3
  elif (direction == "FORWARD"):
    for x in range(i, i+lastI):
      page.append(episodes[x])
      pageURLs.append(episodeURLs[x])
    numEpisodesPrinted = i + lastI


  #If going backward, grab episodes i-6 through i-3
  elif (direction == "BACKWARD") and (numEpisodesPrinted % 3 == 0):
    for x in range(i-6, i-3):
      page.append(episodes[x])
      pageURLs.append(episodeURLs[x])
    numEpisodesPrinted = numEpisodesPrinted - 3
  elif direction == "BACKWARD":
    for x in range((i - (3+(i % 3))),(i - (i%3))):
      page.append(episodes[x])
      pageURLs.append(episodeURLs[x])
    numEpisodesPrinted = numEpisodesPrinted - (i % 3)
    print numEpisodesPrinted

  return page
#####################################################################################################

# Print limited number of results
def printEpisodes(direction):


  #Initialize variables
  topCoord = PADDING

  global episodes, epArray, episodeURLs, begOfCurrentGroup
  epArray = grabEpisodes(direction)

  drawBackground()

  for i in range(len(epArray)):


    # Print the title and number of the episode to the console
    ep = epArray[i]

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
  epArray = []

#####################################################################################################

#Wait for user input before continuing to print results or URL
def paginate(keyPressed):

  global numEpisodesPrinted, URL,  greatestEpisode
  URL = numEpisodesPrinted
  
  if keyPressed == "Right":
    printEpisodes("FORWARD")
    #URL = URL
    #print str(URL) + " FORWARD"
    #print len(episodeURLs)
    #PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = PADDING
    drawPaginator()
    drawSelector()

  elif keyPressed == "Left":
    printEpisodes("BACKWARD")
    if URL - 6 >= 0:
      URL = URL - 6
    else:
      URL = 0
    #print str(URL) + " BACKWARD"
    #print len(episodeURLs)
    #PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = PADDING
    drawPaginator()
    drawSelector()

  elif keyPressed == "Return":
    openSelectedURL()

  elif keyPressed == "Quit":
    sys.exit("Bye bye!")

  elif (keyPressed == "Up") and ((URL-1) >= (numEpisodesPrinted - 4)):
    URL = URL - 1
    print str(URL) + " URL"
    ##PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = SELECTOR_RECT.top - SELECTOR.get_height()
    printEpisodes("SAME")
    drawSelector()
    drawPaginator()   

  elif keyPressed == "Down" and ((URL + 2) < numEpisodesPrinted):
    URL = URL + 1
    print str(URL) + " URL"
    #PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = SELECTOR_RECT.top + SELECTOR.get_height()
    printEpisodes("SAME")
    drawSelector()
    drawPaginator()

#####################################################################################################

#Open the selected episodeURL
def openSelectedURL():
#  webbrowser.open(#PASSED_URL)
  
  print #PASSED_URL

#####################################################################################################

def drawBackground():
  #Fill the surface with a color.
  DISPLAYSURF.fill(BABYBLUE)

  #Draw the menu image
  MENU_IMAGE_RECT = MENU_IMAGE.get_rect()
  DISPLAYSURF.blit(MENU_IMAGE, MENU_IMAGE_RECT)

#####################################################################################################

#Initialize the Pygame Surface
def initDisplay():
  global DISPLAYSURF, URL,  episodeURLs
  pygame.display.init()
  countRows(ALL_TITLES)

  # Customize the icon that displays with the window
  pygame.display.set_icon(WINDOW_ICON)

  #Initialize the surface
  DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
  drawBackground()


  #Initialize other surfaces
  printEpisodes("START")
  drawSelector()
  #URL = 1
  #PASSED_URL = episodeURLs[URL]
  drawPaginator()

#####################################################################################################

#Draw the selector
def drawSelector():
  global SELECTOR, SELECTOR_RECT
  DISPLAYSURF.blit(SELECTOR, SELECTOR_RECT)
  pygame.display.flip()
  

#####################################################################################################

#Draw the paginator
def drawPaginator():
  PAGINATOR = BASEFONT.render("Next", True, WHITE, PINK)
  PAGINATOR_RECT = PAGINATOR.get_rect()
  PAGINATOR_RECT.left = WIDTH - PAGINATOR.get_width()
  PAGINATOR_RECT.top = HEIGHT - (PAGINATOR.get_height() + PADDING)
  DISPLAYSURF.blit(PAGINATOR, PAGINATOR_RECT)
  pygame.display.flip()

#####################################################################################################

#Define Key Events
def keyDownEvents():

  #Initialize variables
  global programRunning, count

  #Listen for keydown events
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: #If the user presses a key, find out which key it is
      if event.key == pygame.K_LEFT: #If the user presses the left arrow...
        if (numEpisodesPrinted - 3) > 1:
          paginate("Left")
      elif event.key == pygame.K_RIGHT: #If the user presses the right arrow...
        if (numEpisodesPrinted) <= count:
          paginate("Right")
      elif event.key == pygame.K_q: #If the user presses q, quit the program.
        paginate("Quit")
        programRunning = False
      elif event.key == pygame.K_RETURN:
        paginate("Return")
      elif event.key == pygame.K_UP:
        paginate("Up")
      elif event.key == pygame.K_DOWN:
        paginate("Down")

#####################################################################################################

runProgram()