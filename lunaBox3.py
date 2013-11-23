import pygame, sqlite3, subprocess, sys, webbrowser

#Initialize all pygame modules
pygame.init()


#####################################################################################################

# Define and initialize global variables

#Program Variables
numEpisodesPrinted = 0
totalNumEpisodes = 0
episodes = [] #List of all of the episodes in the database
episodeURLs = [] #List of all of the episode URLs in the database
page = [] #List of episodes that go on one page
pageURLs = [] #List of episode URLs that go on one page
URL = numEpisodesPrinted #Index for the array of pageURLs
PASSED_URL = '' #URL to be passed to the video player

#####################################################################################################

#Pygame Variables
##Surfaces
DISPLAYSURF = ''

#####################################################################################################

##Dimensions and Sizes
WIDTH = 608
HEIGHT = 384
FONT_SIZE = 20
PADDING = 100

#####################################################################################################

##Colors
BABYBLUE = (99, 187, 214)
WHITE = (255, 255, 255)
PINK = (252, 35, 158)

#####################################################################################################

##Images and fonts
BASEFONT = pygame.font.Font('CREAMPUF.TTF', FONT_SIZE) # Downloaded as freeware under commercial use allowed license on Fontspace
WINDOW_ICON = pygame.image.load('crystal-star-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license
MENU_IMAGE = pygame.image.load('titleBanner.png') # Snagged from the Sailor Moon Wikia: http://sailormoon.wikia.com/wiki/Ami_Mizuno, retrieved using Google

##SELECTOR - global because position changes
SELECTOR = pygame.image.load('crisis-moon-compact-icon.png') # Image by Carla Rodriguez retrieved using google, downloaded from imagearchive.com, under free for non-commercial use license
SELECTOR_RECT = SELECTOR.get_rect()
SELECTOR_RECT.left = WIDTH/2
SELECTOR_RECT.top = PADDING

#####################################################################################################

##SQLite3 Variables
ALL_TITLES = 'SELECT * FROM sailorMoon'
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
    global totalNumEpisodes
    totalNumEpisodes += 1
  return totalNumEpisodes

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
  lastI = totalNumEpisodes - i
  page = []
  pageURLs = []

  #If going forward, grab episodes i through i+3
  if (direction == "FORWARD") and (i+3 <= totalNumEpisodes):
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
    numEpisodesPrinted = numEpisodesPrinted - (i % 3)
    for x in range((i - (3+(i % 3))),(i - (i%3))):
      page.append(episodes[x])
      pageURLs.append(episodeURLs[x])

  elif direction == "SAME":
     for x in range(i-3, i):
       page.append(episodes[x])
       pageURLs.append(episodeURLs[x])

  return page

#####################################################################################################

# Print limited number of results
def printEpisodes(direction):

  #Initialize variables
  topCoord = PADDING

  global episodes, epArray, episodeURLs
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

  global numEpisodesPrinted, URL, PASSED_URL
  
  if keyPressed == "Right":
    URL = numEpisodesPrinted
    printEpisodes("FORWARD")
    PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = PADDING
    drawPaginator()
    drawSelector()

  elif keyPressed == "Left":
    URL = numEpisodesPrinted
    printEpisodes("BACKWARD")
    if (URL - 6 >= 0) and (URL%3 != 0):
      URL = URL - (3+(URL % 3))
    elif (URL-6 >= 0):
      URL = URL - 6
    else:
      URL = 0
    PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = PADDING
    drawPaginator()
    drawSelector()

  elif keyPressed == "Return":
    openSelectedURL()

  elif keyPressed == "Quit":
    sys.exit("Bye bye!")

  elif (keyPressed == "Up") and ((URL-1) > (numEpisodesPrinted - 4)):
    URL = URL - 1
    PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = SELECTOR_RECT.top - SELECTOR.get_height()
    printEpisodes("SAME")
    drawSelector()
    drawPaginator()   

  elif keyPressed == "Down" and ((URL + 1) < numEpisodesPrinted):
    URL = URL + 1
    PASSED_URL = episodeURLs[URL]
    SELECTOR_RECT.top = SELECTOR_RECT.top + SELECTOR.get_height()
    printEpisodes("SAME")
    drawSelector()
    drawPaginator()

##################################################################################################################################

def drawBackground():
  #Fill the surface with a color.
  DISPLAYSURF.fill(BABYBLUE)

  #Draw the background
  BACKGROUND = pygame.image.load('lovehardtwihardBG.jpg') #Image by Lovehardtwihard on Deviantart, retrieved with Google
  BACKGROUND_RECT = BACKGROUND.get_rect()
  BACKGROUND_RECT.left = MENU_IMAGE.get_width()
  DISPLAYSURF.blit(BACKGROUND, BACKGROUND_RECT)

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
  DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)#,pygame.FULLSCREEN)
  drawBackground()


  #Initialize other surfaces
  printEpisodes("START")
  drawPaginator()
  drawStart()

#####################################################################################################

#Draw the selector
def drawSelector():
  global SELECTOR, SELECTOR_RECT
  DISPLAYSURF.blit(SELECTOR, SELECTOR_RECT)
  pygame.display.flip()
  

#####################################################################################################

#Draw the start screen
def drawStart():
  topCoord = PADDING
  START_TEXT = ["Press enter to select,", "an episode. Use up and", "down to navigate the list", "of episodes, and right", "and left to paginate.", "Press q to quit."]
  for text in START_TEXT:

    # Print the title and number of the episode to a surface
    epSurf = BASEFONT.render(text, True, WHITE)
    epSurfRect = epSurf.get_rect() 
    epSurfRect.top = topCoord
    epSurfRect.left = MENU_IMAGE.get_width()

    # Print episode surface onto main surface and update the display
    DISPLAYSURF.blit(epSurf, epSurfRect)
    pygame.display.flip()

    # Reset the topCoord so that the episode titles do not overlap
    topCoord += epSurfRect.height + 10

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
  global programRunning, totalNumEpisodes

  #Listen for keydown events
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: #If the user presses a key, find out which key it is
      if event.key == pygame.K_LEFT: #If the user presses the left arrow...
        if (numEpisodesPrinted - 3) > 1:
          paginate("Left")
      elif event.key == pygame.K_RIGHT: #If the user presses the right arrow...
        if (numEpisodesPrinted) < totalNumEpisodes:
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

#Open the selected episodeURL
def openSelectedURL():
  #webbrowser.open(PASSED_URL)
  epDL = 'youtube-dl --max-quality 35 -g ' + PASSED_URL
  pygame.display.quit()
  PASSED = subprocess.check_output(epDL, shell=True)
  #subprocess.call( [ "omxplayer", PASSED])
  print PASSED#_URL

###############################################################################$



runProgram()
