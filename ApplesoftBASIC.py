import time
import pygame


class ApplesoftState:
    def __init__(self):
        self.txtX = 1
        self.txtY = 1
        self.txtMinX = 1
        self.txtMinY = 1
        self.txtMaxX = 40
        self.txtMaxY = 24
        self.txtForeColour = "white"
        self.txtBackColour = "black"

        self.cursorFlashCount = 0
        self.cursorImg = pygame.Surface((7,8))
        pygame.draw.rect(self.cursorImg, [0, 0, 0], [0, 0, 7, 8])
        for i in range(1, 6, 2):
            pygame.draw.line(self.cursorImg, self.txtForeColour, (i, 1), (i, 1))
            pygame.draw.line(self.cursorImg, self.txtForeColour, (i, 3), (i, 3))
            pygame.draw.line(self.cursorImg, self.txtForeColour, (i, 5), (i, 5))
        pygame.draw.line(self.cursorImg, self.txtForeColour, (2, 2), (2, 2))
        pygame.draw.line(self.cursorImg, self.txtForeColour, (4, 2), (4, 2))
        pygame.draw.line(self.cursorImg, self.txtForeColour, (2, 4), (2, 4))
        pygame.draw.line(self.cursorImg, self.txtForeColour, (4, 4), (4, 4))

        self.hgrColour = "black"
        self.hgrLastPoint = (0, 0)

        self.beepSound = pygame.mixer.Sound("Apple2Beep.wav")


def render():
    pygame.transform.scale(gAppleDisplaySurface, gMainDisplaySize, gMainDisplaySurface)
    pygame.display.update()
  

def sgn(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0


def htab(x):
    if x < 1:
        x = 1
    elif x > 40:
        x = 40
    env.x = x


def vtab(y):
    if y < 1:
        y = 1
    elif y > 40:
        y = 24
    env.y = y


def setTextWindowTop(y):
    global gCursor

    y = y + 1           # user specifies line before they line the want in the window (ie, default if 0)
    env.minY = y
    if env.y < y:
        env.y = y


def setTextWindowBottom(y):
    global gCursor

    env.maxY = y
    if env.y > y:
        env.y = y + 1     # ready to scroll


def setTextWindowRight(x):
    env.maxX = x
    if env.x > x:
        env.x = 1

def text():
    env.minX = 1
    env.minY = 1
    env.maxX = 40
    env.maxY = 24


def home():
    x = (env.minX - 1) * 7
    width = (env.maxX - env.minX + 1) * 7
    y = (env.minY - 1) * 8
    height = (env.maxY - env.minY + 1) * 8

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(gAppleDisplaySurface, [0, 0, 0], rect)

    env.x = env.minX
    env.y = env.minY


def inverse():
    env.txtForeColour = "black"
    env.txtBackColour = "white"


def normal():
    env.txtForeColour = "white"
    env.txtBackColour = "black"


def hgr():
    rect = pygame.Rect(0, 0, 280, 160)
    pygame.draw.rect(gAppleDisplaySurface, [0, 0, 0], rect)
    env.minY = 21; env.maxY = 24


def hcolor(colour):
    colours = { 0: "black", 1: "green", 2: "violet", 3: "white", 4: "black", 5: "orange", 6: "blue", 7: "white" }
    env.hgrColour = colours[colour]


def hplot(points):
    pygame.draw.lines(gAppleDisplaySurface, env.hgrColour, False, points)
    env.hgrLastPoint = points[-1]


def hplotTo(points):
    hplot([env.hgrLastPoint] + points)


def clearLineEnd():
    x = (env.x - 1) * 7
    width = (env.maxX - env.x + 1) * 7
    y = (env.y - 1) * 8
    height = 8
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(gAppleDisplaySurface, [0, 0, 0], rect)


def scroll():
    x = (env.minX - 1) * 7
    width = (env.maxX - env.minX + 1) * 7
    y = (env.minY - 1) * 8
    height = (env.maxY - env.minY + 1) * 8

    clipRect = pygame.Rect(x, y, width, height)
    gAppleDisplaySurface.set_clip(clipRect)
    gAppleDisplaySurface.scroll(0, -8)

    blankRect = pygame.Rect(x, (env.maxY - 1) * 8, width, 8)
    pygame.draw.rect(gAppleDisplaySurface, [0, 0, 0], blankRect)

    gAppleDisplaySurface.set_clip(gAppleDisplaySurface.get_rect())


def drawText(x, y, text):
    image = gMainFont.render(text, True, env.txtForeColour, env.txtBackColour)
    rect = image.get_rect()
    rect.topleft = [(x - 1) * 7, (y - 1) * 8]
    gAppleDisplaySurface.blit(image, rect)


def flashCursor(x, y):
    # According to https://retrocomputing.stackexchange.com/questions/13960/how-is-the-apple-ii-text-flash-mode-timed
    #  cursor cycle is based on a NE555 time and is roughly is 2.1 seconds. Based on 30fps that's 63 frames. Let's call it 64 frames.
    # After staring at the MicroM8 emulator cursor, it's on for ~9 frames and off for ~7, which is a total of 16 frames.
    cursorOn = False
    if env.cursorFlashCount < 9:        # on for 9 frames, off for 6
        cursorOn = True

    # Only draw the cursor if it's on. Don't draw it off (blank) so that the underlying text will show
    if cursorOn:
        img = env.cursorImg
        rect = img.get_rect().move((x - 1) * 7, (y - 1) * 8)
        gAppleDisplaySurface.blit(img, rect)

    env.cursorFlashCount = (env.cursorFlashCount + 1) % 16      # we're using 16 as the duty cycle


def print(text = None, newLine = True):
    if not text is None:
        drawText(env.x, env.y, text)

    if newLine:
        env.x = env.minX
        env.y = env.y + 1
        if env.y > env.maxY:
            scroll()
    elif not text is None:
        env.x = env.x + len(text)

    # handle weirdness where vtab is out of current text window
    if env.y > env.maxY:
        env.y = env.maxY
    elif env.y < env.minY:
        env.y = env.minY


def input(promptText):
    text = ""
    clock = pygame.time.Clock()
    done = False

    print(promptText, False)
    clearLineEnd()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        drawText(env.x, env.y, f"{text} ")
        flashCursor(env.x + len(text), env.y)
        render()
        clock.tick(30)

    env.x = 1
    env.y = env.y + 1

    return text


def get():
    clock = pygame.time.Clock()

    render()        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RSUPER, pygame.K_LSUPER]:
                    return event.unicode

        clock.tick(30)


def getKeypress():
    clock = pygame.time.Clock()

    render()        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RSUPER, pygame.K_LSUPER]:
                    if event.key in gKeyCodes:
                        return gKeyCodes[event.key]
                    else:
                        return event.key

        clock.tick(30)


def beep(count = 1):
    while count > 0:
        env.beepSound.play()
        count = count - 1
        time.sleep(0.1)





pygame.init()
pygame.mixer.init()

env = ApplesoftState()
gMainDisplaySize = (560, 384)
gKeyCodes = { pygame.K_LEFT: 136,
              pygame.K_RETURN: 141,
              pygame.K_RIGHT: 149,
              pygame.K_ESCAPE: 155,
              pygame.K_SPACE: 160,
              pygame.K_SLASH: 175,
              pygame.K_a: 193,
              pygame.K_p: 208,
              pygame.K_s: 211,
              pygame.K_x: 216,
            }
  
# create the display surface object of specific dimension..e(X, Y).
gAppleDisplaySurface = pygame.Surface((280,192))
gMainDisplaySurface = pygame.display.set_mode(gMainDisplaySize)
gMainFont = pygame.font.Font('PrintChar21.ttf', 8)

