import time
import pygame


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
    gCursor["x"] = x


def vtab(y):
    if y < 1:
        y = 1
    elif y > 40:
        y = 24
    gCursor["y"] = y


def setTextWindowTop(y):
    gCursor["minY"] = y
    if gCursor["y"] < y:
        gCursor["y"] = y


def setTextWindowBottom(y):
    gCursor["maxY"] = y
    if gCursor["y"] > y:
        gCursor["y"] = y + 1     # ready to scroll


def home():
    x = (gCursor["minX"] - 1) * 7
    width = (gCursor["maxX"] - gCursor["minX"] + 1) * 7
    y = (gCursor["minY"] - 1) * 8
    height = (gCursor["maxY"] - gCursor["minY"] + 1) * 8

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(gDisplaySurface, [0, 0, 0], rect)

    gCursor["x"] = gCursor["minX"]
    gCursor["y"] = gCursor["minY"]


def hgr():
    rect = pygame.Rect(0, 0, 280, 160)
    pygame.draw.rect(gDisplaySurface, [0, 0, 0], rect)


def clearLineEnd():
    x = (gCursor["x"] - 1) * 7
    width = (gCursor["maxX"] - gCursor["x"] + 1) * 7
    y = (gCursor["y"] - 1) * 8
    height = 8
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(gDisplaySurface, [0, 0, 0], rect)


def scroll():
    x = (gCursor["minX"] - 1) * 7
    width = (gCursor["maxX"] - gCursor["minX"] + 1) * 7
    y = (gCursor["minY"] - 1) * 8
    height = (gCursor["maxY"] - gCursor["minY"] + 1) * 8

    clipRect = pygame.Rect(x, y, width, height)
    gDisplaySurface.set_clip(clipRect)
    gDisplaySurface.scroll(0, -8)

    blankRect = pygame.Rect(x, (gCursor["maxY"] - 1) * 8, width, 8)
    pygame.draw.rect(gDisplaySurface, [0, 0, 0], blankRect)

    gDisplaySurface.set_clip(gDisplaySurface.get_rect())


def drawText(x, y, text):
    image = gMainFont.render(text, True, [255, 255, 255], [0, 0, 0])
    rect = image.get_rect()
    rect.topleft = [(x - 1) * 7, (y - 1) * 8]
    gDisplaySurface.blit(image, rect)


def print(text, newLine = True):
    if gCursor["y"] > gCursor["maxY"]:
        scroll()
        gCursor["y"] = gCursor["maxY"]

    x = gCursor["x"]
    y = gCursor["y"]
    drawText(x, y, text)

    if newLine:
        gCursor["x"] = gCursor["minX"]
        gCursor["y"] = y + 1
    else:
        gCursor["x"] = x + len(text)


def input(promptText):
    text = ""
    clock = pygame.time.Clock()
    dt = 0
    done = False

    print(promptText, False)
    clearLineEnd()
    x = gCursor["x"]; y = gCursor["y"]

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

        drawText(x, y, f"{text} ")
        pygame.display.update()
        dt = clock.tick(30) / 1000

    gCursor["x"] = 1
    gCursor["y"] = gCursor["y"] + 1

    return text


def get():
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.update()        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RSUPER, pygame.K_LSUPER]:
                    return event.unicode

        dt = clock.tick(30) / 1000


def getKeypress():
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.update()        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key not in [pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT, pygame.K_RSUPER, pygame.K_LSUPER]:
                    return event.key

        dt = clock.tick(30) / 1000



 
gCursor = { "x": 1, "y": 1, "minX": 1, "minY": 1, "maxX": 40, "maxY": 24 }
  
# create the display surface object of specific dimension..e(X, Y).
pygame.init()
gDisplaySurface = pygame.display.set_mode((280, 192))
gMainFont = pygame.font.Font('PrintChar21.ttf', 8)
