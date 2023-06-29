import time
import pygame
import sys


class ApplesoftState:
    def __init__(self, displayWidth, displayHeight):
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
            self.cursorImg.set_at((i, 1), self.txtForeColour)
            self.cursorImg.set_at((i, 3), self.txtForeColour)
            self.cursorImg.set_at((i, 5), self.txtForeColour)
        self.cursorImg.set_at((2, 2), self.txtForeColour)
        self.cursorImg.set_at((4, 2), self.txtForeColour)
        self.cursorImg.set_at((2, 4), self.txtForeColour)
        self.cursorImg.set_at((4, 4), self.txtForeColour)

        self.hgrColour = "black"
        self.hgrLastPoint = (0, 0)

        self.soundBeep = pygame.mixer.Sound("Apple2Beep.wav")

        # create the display surface object of specific dimension..e(X, Y).
        sys.stdout.write("Creating window {x},{y}\n".format(x=displayWidth, y=displayHeight))
        self.appleDisplaySurface = pygame.Surface((280,192))
        self.renderDisplaySurface = pygame.display.set_mode((displayWidth, displayHeight))
        self.txtFont = pygame.font.Font('PrintChar21.ttf', 8)



def init(displayWidth = 0, displayHeight = 0):
    pygame.init()
    pygame.mixer.init()

    if displayWidth == 0 or displayHeight == 0:
        xRatio = int(pygame.display.Info().current_w / 280)
        yRatio = int((pygame.display.Info().current_h - 30) / 192)      # factor in title bar height
        if xRatio == 0 or yRatio == 0:
            displayWidth = 280
            displayHeight = 192
        else:
            displayWidth = 280 * min(xRatio, yRatio)
            displayHeight = 192 * min(xRatio, yRatio)

    global env
    env = ApplesoftState(displayWidth, displayHeight)

    global keyCodes
    keyCodes = { pygame.K_LEFT: 136,
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


def render():
    pygame.transform.scale(env.appleDisplaySurface, env.renderDisplaySurface.get_size(), env.renderDisplaySurface)
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
    env.txtX = x


def vtab(y):
    if y < 1:
        y = 1
    elif y > 40:
        y = 24
    env.txtY = y


def setTextWindowTop(y):
    global gCursor

    y = y + 1           # user specifies line before they line the want in the window (ie, default if 0)
    env.txtMinY = y
    if env.txtY < y:
        env.txtY = y


def setTextWindowBottom(y):
    global gCursor

    env.txtMaxY = y
    if env.txtY > y:
        env.txtY = y + 1     # ready to scroll


def setTextWindowRight(x):
    env.txtMaxX = x
    if env.txtX > x:
        env.txtX = 1

def text():
    env.txtMinX = 1
    env.txtMinY = 1
    env.txtMaxX = 40
    env.txtMaxY = 24


def home():
    x = (env.txtMinX - 1) * 7
    width = (env.txtMaxX - env.txtMinX + 1) * 7
    y = (env.txtMinY - 1) * 8
    height = (env.txtMaxY - env.txtMinY + 1) * 8

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(env.appleDisplaySurface, [0, 0, 0], rect)

    env.txtX = env.txtMinX
    env.txtY = env.txtMinY


def inverse():
    env.txtForeColour = "black"
    env.txtBackColour = "white"


def normal():
    env.txtForeColour = "white"
    env.txtBackColour = "black"


def hgr():
    rect = pygame.Rect(0, 0, 280, 160)
    pygame.draw.rect(env.appleDisplaySurface, [0, 0, 0], rect)
    env.txtMinY = 21; env.txtMaxY = 24


def hcolor(colour):
    colours = { 0: "black", 1: "green", 2: "violet", 3: "white", 4: "black", 5: "orange", 6: "blue", 7: "white" }
    env.hgrColour = colours[colour]


def hplot(points):
    pygame.draw.lines(env.appleDisplaySurface, env.hgrColour, False, points)
    env.hgrLastPoint = points[-1]


def hplotTo(points):
    hplot([env.hgrLastPoint] + points)


def clearLineEnd():
    x = (env.txtX - 1) * 7
    width = (env.txtMaxX - env.txtX + 1) * 7
    y = (env.txtY - 1) * 8
    height = 8
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(env.appleDisplaySurface, [0, 0, 0], rect)


def scroll():
    x = (env.txtMinX - 1) * 7
    width = (env.txtMaxX - env.txtMinX + 1) * 7
    y = (env.txtMinY - 1) * 8
    height = (env.txtMaxY - env.txtMinY + 1) * 8

    clipRect = pygame.Rect(x, y, width, height)
    env.appleDisplaySurface.set_clip(clipRect)
    env.appleDisplaySurface.scroll(0, -8)

    blankRect = pygame.Rect(x, (env.txtMaxY - 1) * 8, width, 8)
    pygame.draw.rect(env.appleDisplaySurface, [0, 0, 0], blankRect)

    env.appleDisplaySurface.set_clip(env.appleDisplaySurface.get_rect())


def drawText(x, y, text):
    image = env.txtFont.render(text, True, env.txtForeColour, env.txtBackColour)
    rect = image.get_rect()
    rect.topleft = [(x - 1) * 7, (y - 1) * 8]
    env.appleDisplaySurface.blit(image, rect)


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
        env.appleDisplaySurface.blit(img, rect)

    env.cursorFlashCount = (env.cursorFlashCount + 1) % 16      # we're using 16 as the duty cycle


def print(text = None, newLine = True):
    if not text is None:
        drawText(env.txtX, env.txtY, text)
        env.txtX = env.txtX + len(text)
        if env.txtX > env.txtMaxX:
            env.txtX = env.txtX - env.txtMaxX + env.txtMinX - 1
            env.txtY = env.txtY + 1
            if env.txtY > env.txtMaxY:
                scroll()

    if newLine:
        env.txtX = env.txtMinX
        env.txtY = env.txtY + 1
        if env.txtY > env.txtMaxY:
            scroll()

    # handle weirdness where vtab is out of current text window
    if env.txtY > env.txtMaxY:
        env.txtY = env.txtMaxY
    elif env.txtY < env.txtMinY:
        env.txtY = env.txtMinY


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

        drawText(env.txtX, env.txtY, f"{text} ")
        if not done:
            flashCursor(env.txtX + len(text), env.txtY)   # don't leave the cursor behind
        render()
        clock.tick(30)

    env.txtX = 1
    env.txtY = env.txtY + 1

    return text


def get():
    clock = pygame.time.Clock()
    done = False
    keyCode = None

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RSUPER, pygame.K_LSUPER]:
                    done = True
                    keyCode = event.unicode

        drawText(env.txtX, env.txtY, " ")
        if not done:
            flashCursor(env.txtX, env.txtY)
        render()
        clock.tick(30)
    
    return keyCode


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
                    if event.key in keyCodes:
                        return keyCodes[event.key]
                    else:
                        return event.key

        clock.tick(30)


def beep(count = 1):
    while count > 0:
        env.soundBeep.play()
        count = count - 1
        time.sleep(0.1)
