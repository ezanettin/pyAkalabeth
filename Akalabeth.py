import time
import random
import math
import ApplesoftBASIC as apple


def drawMap(surface):
    global TX
    global TY

#  100  HGR : FOR Y =  - 1 TO 1: FOR X =  - 1 TO 1
    apple.hgr()

    for Y in range(-1, 2):
        for X in range(-1, 2):
#  105  HPLOT 138,75 TO 142,75: HPLOT 140,73 TO 140,77
            apple.hplot([(138, 75), (142, 75)])
            apple.hplot([(140, 73), (140, 77)])
#  110 ZZ = TER%(TX + X,TY + Y):X1 = 65 + (X + 1) * 50:Y1 = (Y + 1) * 50
            ZZ = TE[TX + X][TY + Y]; X1 = 65 + (X + 1) * 50; Y1 = (Y + 1) * 50

#  120  IF ZZ = 2 THEN  HPLOT X1 + 20,Y1 + 20 TO X1 + 30,Y1 + 20 TO X1 + 30,Y1 + 30 TO X1 + 20,Y1 + 30 TO X1 + 20,Y1 + 20
            if ZZ == 2:
                apple.hplot([(X1 + 20,Y1 + 20), (X1 + 30,Y1 + 20), (X1 + 30,Y1 + 30), (X1 + 20,Y1 + 30), (X1 + 20,Y1 + 20)])
#  130  IF ZZ = 3 THEN  HPLOT X1 + 10,Y1 + 10 TO X1 + 20,Y1 + 10 TO X1 + 20,Y1 + 40 TO X1 + 10,Y1 + 40 TO X1 + 10,Y1 + 30 TO X1 + 40,Y1 + 30 TO X1 + 40,Y1 + 40 TO X1 + 30,Y1 + 40 TO X1 + 30,Y1 + 10 TO X1 + 40,Y1 + 10 TO X1 + 40,Y1 + 20 TO X1 + 10,Y1 + 20 TO X1 + 10,Y1 + 10
            elif ZZ == 3:
                apple.hplot([ [X1 + 10,Y1 + 10], [X1 + 20,Y1 + 10], [X1 + 20,Y1 + 40], [X1 + 10,Y1 + 40], [X1 + 10,Y1 + 30], [X1 + 40,Y1 + 30], [X1 + 40,Y1 + 40], [X1 + 30,Y1 + 40], [X1 + 30,Y1 + 10], [X1 + 40,Y1 + 10], [X1 + 40,Y1 + 20], [X1 + 10,Y1 + 20], [X1 + 10,Y1 + 10] ])
#  140  IF ZZ = 4 THEN  HPLOT X1 + 20,Y1 + 20 TO X1 + 30,Y1 + 30: HPLOT X1 + 20,Y1 + 30 TO X1 + 30,Y1 + 20
            elif ZZ == 4:
                apple.hplot([(X1 + 20,Y1 + 20), (X1 + 30,Y1 + 30)])
                apple.hplot([(X1 + 20,Y1 + 30), (X1 + 30,Y1 + 20)])
#  150  IF ZZ = 5 THEN  HPLOT X1,Y1 TO X1 + 50,Y1 TO X1 + 50,Y1 + 50 TO X1,Y1 + 50 TO X1,Y1: HPLOT X1 + 10,Y1 + 10 TO X1 + 10,Y1 + 40 TO X1 + 40,Y1 + 40 TO X1 + 40,Y1 + 10 TO X1 + 10,Y1 + 10 TO X1 + 40,Y1 + 40: HPLOT X1 + 10,Y1 + 40 TO X1 + 40,Y1 + 10
            elif ZZ == 5:
                apple.hplot([(X1,Y1), (X1 + 50,Y1), (X1 + 50,Y1 + 50), (X1,Y1 + 50), (X1,Y1) ])
                apple.hplot([ [X1 + 10,Y1 + 10], [X1 + 10,Y1 + 40], [X1 + 40,Y1 + 40], [X1 + 40,Y1 + 10], [X1 + 10,Y1 + 10], [X1 + 40,Y1 + 40] ])
                apple.hplot([(X1 + 10,Y1 + 40), (X1 + 40,Y1 + 10)])
#  160  IF ZZ = 1 THEN  HPLOT X1 + 10,Y1 + 50 TO X1 + 10,Y1 + 40 TO X1 + 20,Y1 + 30 TO X1 + 40,Y1 + 30 TO X1 + 40,Y1 + 50: HPLOT X1,Y1 + 10 TO X1 + 10,Y1 + 10: HPLOT X1 + 50,Y1 + 10 TO X1 + 40,Y1 + 10: HPLOT X1,Y1 + 40 TO X1 + 10,Y1 + 40: HPLOT X1 + 40,Y1 + 40 TO X1 + 50,Y1 + 40
#  170  IF ZZ = 1 THEN  HPLOT X1 + 10,Y1 TO X1 + 10,Y1 + 20 TO X1 + 20,Y1 + 20 TO X1 + 20,Y1 + 30 TO X1 + 30,Y1 + 30 TO X1 + 30,Y1 + 10 TO X1 + 40,Y1 + 10 TO X1 + 40,Y1
            elif ZZ == 1:
                apple.hplot([ [X1 + 10,Y1 + 50], [X1 + 10,Y1 + 40], [X1 + 20,Y1 + 30], [X1 + 40,Y1 + 30], [X1 + 40,Y1 + 50] ])
                apple.hplot([(X1,Y1 + 10), (X1 + 10,Y1 + 10)])
                apple.hplot([(X1 + 50,Y1 + 10), (X1 + 40,Y1 + 10)])
                apple.hplot([(X1,Y1 + 40), (X1 + 10,Y1 + 40)])
                apple.hplot([(X1 + 40,Y1 + 40), (X1 + 50,Y1 + 40)])
                apple.hplot([ [X1 + 10,Y1], [X1 + 10,Y1 + 20], [X1 + 20,Y1 + 20], [X1 + 20,Y1 + 30], [X1 + 30,Y1 + 30], [X1 + 30,Y1 + 10], [X1 + 40,Y1 + 10], [X1 + 40,Y1] ])
#  190  NEXT : NEXT : RETURN 


def drawDungeon(surface):
#  200  HGR :DIS = 0: HCOLOR= 3
    apple.hgr(); apple.hcolor(3)
    DIS = 0
    EN = 0      # only used here, always set to 0 on exit, so just keep it local and initialised to 0

    while True:
#  202 CENT = DNG%(PX + DX * DIS,PY + DY * DIS):LEFT = DNG%(PX + DX * DIS + DY,PY + DY * DIS - DX):RIGH = DNG%(PX + DX * DIS - DY,PY + DY * DIS + DX)
        CENT = DNG[PX + DX * DIS][PY + DY * DIS]
        LEFT = DNG[PX + DX * DIS + DY][PY + DY * DIS - DX]
        RIGHT = DNG[PX + DX * DIS - DY][PY + DY * DIS + DX]

#  204 L1 = PER%(DIS,0):R1 = PER%(DIS,1):T1 = PER%(DIS,2):B1 = PER%(DIS,3):L2 = PER%(DIS + 1,0):R2 = PER%(DIS + 1,1):T2 = PER%(DIS + 1,2):B2 = PER%(DIS + 1,3)
        L1 = PER[DIS][0]; R1 = PER[DIS][1]; T1 = PER[DIS][2]; B1 = PER[DIS][3]
        L2 = PER[DIS + 1][0]; R2 = PER[DIS + 1][1]; T2 = PER[DIS + 1][2]; B2 = PER[DIS + 1][3]

#  205 CENT =  INT (CENT):LEFT =  INT (LEFT):RIGHT =  INT (RIGHT)
        CENT = int(CENT); LEFT = int(LEFT); RIGHT = int(RIGHT)

#  206 MC =  INT (CENT / 10):CENT = CENT - MC * 10:LEFT =  INT ((LEFT / 10 -  INT (LEF / 10)) * 10 + .1):RIGH =  INT ((RIGH / 10 -  INT (RIG / 10)) * 10 + .1)
        MC = int(CENT / 10); CENT = CENT - MC * 10
        LEFT = int((LEFT / 10 - int(LEFT / 10)) * 10 + 0.1)
        RIGHT = int((RIGHT / 10 - int(RIGHT / 10)) * 10 + 0.1)

#  208  IF DIS = 0 THEN 216
#  210  IF CENT = 1 OR CENT = 3 OR CENT = 4 THEN  HPLOT L1,T1 TO R1,T1 TO R1,B1 TO L1,B1 TO L1,T1
#  212  IF CENT = 1 OR CENT = 3 THEN EN = 1: GOTO 260
#  214  IF CENT = 4 THEN  HPLOT CD%(DIS,0),CD%(DIS,3) TO CD%(DIS,0),CD%(DIS,2) TO CD%(DIS,1),CD%(DIS,2) TO CD%(DIS,1),CD%(DIS,3):EN = 1: GOTO 260
        skipTo260 = False
        if DIS != 0:
            if CENT == 1 or CENT == 3 or CENT == 4:
                apple.hplot([(L1,T1), (R1,T1), (R1,B1), (L1,B1), (L1,T1)])
                EN = 1
                skipTo260 = True
                if CENT == 4:
                    apple.hplot([(CD[DIS][0],CD[DIS][3]), (CD[DIS][0],CD[DIS][2]), (CD[DIS][1],CD[DIS][2]), (CD[DIS][1],CD[DIS][3])])

        if not skipTo260:
#  216  IF LEFT = 1 OR LEFT = 3 OR LEFT = 4 THEN  HPLOT L1,T1 TO L2,T2: HPLOT L1,B1 TO L2,B2
            if LEFT == 1 or LEFT == 3 or LEFT == 4:
                apple.hplot([(L1,T1), (L2,T2)])
                apple.hplot([(L1,B1), (L2,B2)])
#  218  IF RIGH = 1 OR RIGH = 3 OR RIGH = 4 THEN  HPLOT R1,T1 TO R2,T2: HPLOT R1,B1 TO R2,B2
            if RIGHT == 1 or RIGHT == 3 or RIGHT == 4:
                apple.hplot([(R1,T1), (R2,T2)])
                apple.hplot([(R1,B1), (R2,B2)])
#  220  IF LEFT = 4 AND DIS > 0 THEN  HPLOT LD%(DIS,0),LD%(DIS,4) TO LD%(DIS,0),LD%(DIS,2) TO LD%(DIS,1),LD%(DIS,3) TO LD%(DIS,1),LD%(DIS,5)
            if LEFT == 4 and DIS > 0:
                apple.hplot([(LD[DIS][0],LD[DIS][4]), (LD[DIS][0],LD[DIS][2]), (LD[DIS][1],LD[DIS][3]), (LD[DIS][1],LD[DIS][5])])
#  222  IF LEFT = 4 AND DIS = 0 THEN  HPLOT 0,LD%(DIS,2) - 3 TO LD%(DIS,1),LD%(DIS,3) TO LD%(DIS,1),LD%(DIS,5)
            if LEFT == 4 and DIS == 0:
                apple.hplot([(0,LD[DIS][2] - 3), (LD[DIS][1],LD[DIS][3]), (LD[DIS][1],LD[DIS][5])])
#  224  IF RIGH = 4 AND DIS > 0 THEN  HPLOT 279 - LD%(DIS,0),LD%(DIS,4) TO 279 - LD%(DIS,0),LD%(DIS,2) TO 279 - LD%(DIS,1),LD%(DIS,3) TO 279 - LD%(DIS,1),LD%(DIS,5)
            if RIGHT == 4 and DIS > 0:
                apple.hplot([(279 - LD[DIS][0],LD[DIS][4]), (279 - LD[DIS][0],LD[DIS][2]), (279 - LD[DIS][1],LD[DIS][3]), (279 - LD[DIS][1],LD[DIS][5])])
#  226  IF RIGH = 4 AND DIS = 0 THEN  HPLOT 279,LD%(DIS,2) - 3 TO 279 - LD%(DIS,1),LD%(DIS,3) TO 279 - LD%(DIS,1),LD%(DIS,5)
            if RIGHT == 4 and DIS == 0:
                apple.hplot([(279,LD[DIS][2] - 3), (279 - LD[DIS][1],LD[DIS][3]), (279 - LD[DIS][1],LD[DIS][5])])
#  228  IF LEFT = 3 OR LEFT = 1 OR LEFT = 4 THEN 234
#  230  IF DIS <  > 0 THEN  HPLOT L1,T1 TO L1,B1
#  232  HPLOT L1,T2 TO L2,T2 TO L2,B2 TO L1,B2
            if not (LEFT == 3 or LEFT == 1 or LEFT == 4):
                if DIS != 0:
                    apple.hplot([(L1,T1), (L1,B1)])
                apple.hplot([(L1,T2), (L2,T2), (L2,B2), (L1,B2)])
#  234  IF RIGH = 3 OR RIGH = 1 OR RIGH = 4 THEN 240
#  236  IF DIS <  > 0 THEN  HPLOT R1,T1 TO R1,B1
#  238  HPLOT R1,T2 TO R2,T2 TO R2,B2 TO R1,B2
            if not (RIGHT == 3 or RIGHT == 1 or RIGHT == 4):
                if DIS != 0:
                    apple.hplot([(R1,T1), (R1,B1)])
                apple.hplot([(R1,T2), (R2,T2), (R2,B2), (R1,B2)])
#  240  IF CENT = 7 OR CENT = 9 THEN  HPLOT FT%(DIS,0),FT%(DIS,4) TO FT%(DIS,2),FT%(DIS,5) TO FT%(DIS,3),FT%(DIS,5) TO FT%(DIS,1),FT%(DIS,4) TO FT%(DIS,0),FT%(DIS,4)
            if CENT == 7 or CENT == 9:
                apple.hplot([(FT[DIS][0],FT[DIS][4]), (FT[DIS][2],FT[DIS][5]), (FT[DIS][3],FT[DIS][5]), (FT[DIS][1],FT[DIS][4]), (FT[DIS][0],FT[DIS][4])])
#  242  IF CENT = 8 THEN  HPLOT FT%(DIS,0),158 - FT%(DIS,4) TO FT%(DIS,2),158 - FT%(DIS,5) TO FT%(DIS,3),158 - FT%(DIS,5) TO FT%(DIS,1),158 - FT%(DIS,4) TO FT%(DIS,0),158 - FT%(DIS,4)
            if CENT == 8:
                apple.hplot([(FT[DIS][0],158 - FT[DIS][4]), (FT[DIS][2],158 - FT[DIS][5]), (FT[DIS][3],158 - FT[DIS][5]), (FT[DIS][1],158 - FT[DIS][4]), (FT[DIS][0],158 - FT[DIS][4])])
#  244  IF CENT = 7 OR CENT = 8 THEN BASE = LAD%(DIS,3):TP = LAD%(DIS,2):LX = LAD%(DIS,0):RX = LAD%(DIS,1): HPLOT LX,BA TO LX,TP: HPLOT RX,TP TO RX,BA
#  246  IF CENT = 7 OR CENT = 8 THEN Y1 = (BA * 4 + TP) / 5:Y2 = (BA * 3 + TP * 2) / 5:Y3 = (BA * 2 + TP * 3) / 5:Y4 = (BA + TP * 4) / 5: HPLOT LX,Y1 TO RX,Y1: HPLOT LX,Y2 TO RX,Y2: HPLOT LX,Y3 TO RX,Y3: HPLOT LX,Y4 TO RX,Y4
            if CENT == 7 or CENT == 8:
                BASE = LAD[DIS][3]; TP = LAD[DIS][2]
                LX = LAD[DIS][0]; RX = LAD[DIS][1]
                apple.hplot([(LX,BASE), (LX,TP)])
                apple.hplot([(RX,TP), (RX,BASE)])
                Y1 = (BASE * 4 + TP) / 5; Y2 = (BASE * 3 + TP * 2) / 5; Y3 = (BASE * 2 + TP * 3) / 5; Y4 = (BASE + TP * 4) / 5
                apple.hplot([(LX,Y1), (RX,Y1)])
                apple.hplot([(LX,Y2), (RX,Y2)])
                apple.hplot([(LX,Y3), (RX,Y3)])
                apple.hplot([(LX,Y4), (RX,Y4)])
#  248  IF DIS > 0 AND CENT = 5 THEN  HPLOT 139 - 10 / DIS,PER%(DIS,3) TO 139 - 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 10 / DIS,PER%(DIS,3) TO 139 - 10 / DIS,PER%(DIS,3)
#  249  IF CENT = 5 AND DIS > 0 THEN  INVERSE : PRINT "CHEST!": NORMAL 
#  250  IF DIS > 0 AND CENT = 5 THEN  HPLOT 139 - 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 - 5 / DIS,PER%(DIS,3) - 15 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 15 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 5 / DIS TO 139 + 10 / DIS,PER%(DIS,3)
#  252  IF DIS > 0 AND CENT = 5 THEN  HPLOT 139 + 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 15 / DIS
            if DIS > 0 and CENT == 5:
                apple.hplot([ [139 - 10 / DIS,PER[DIS][3]], [139 - 10 / DIS,PER[DIS][3] - 10 / DIS], [139 + 10 / DIS,PER[DIS][3] - 10 / DIS], [139 + 10 / DIS,PER[DIS][3]], [139 - 10 / DIS,PER[DIS][3]] ])
                apple.inverse(); apple.print("CHEST!"); apple.normal()
                apple.hplot([ [139 - 10 / DIS,PER[DIS][3] - 10 / DIS], [139 - 5 / DIS,PER[DIS][3] - 15 / DIS], [139 + 15 / DIS,PER[DIS][3] - 15 / DIS], [139 + 15 / DIS,PER[DIS][3] - 5 / DIS], [139 + 10 / DIS,PER[DIS][3]] ])
                apple.hplot([(139 + 10 / DIS,PER[DIS][3] - 10 / DIS), (139 + 15 / DIS,PER[DIS][3] - 15 / DIS)])

#  260  IF MC < 1 THEN 490
# 490  IF EN = 1 THEN EN = 0: RETURN 
# 491 DIS = DIS + 1: GOTO 202
        if MC < 1:
            if EN == 1:
                break
            DIS = DIS + 1
            continue

#  265 B = 79 + YY%(DIS):C = 139
        B = 79 + YY[DIS]; C = 139
#  266  INVERSE : IF MC = 8 THEN  PRINT "CHEST!";: CALL  - 868: PRINT : NORMAL : GOTO 269
#  267  PRINT M$(MC);: CALL  - 868: PRINT : NORMAL 
        apple.inverse()
        if MC == 8:
            apple.print("CHEST!", False)
        else:
            apple.print(f"{Ms[MC]}", False)
        apple.clearLineEnd()
        apple.print()
        apple.normal()

#  269  IF DIS = 0 THEN 490
# 490  IF EN = 1 THEN EN = 0: RETURN 
# 491 DIS = DIS + 1: GOTO 202
        if DIS == 0:
            if EN == 1:
                break
            DIS = DIS + 1
            continue

#  270  ON MC GOTO 300,310,320,330,340,350,360,370,380,390
        if MC == 1:
            drawSkeleton(C, B, DIS)
        elif MC == 2:
            drawThief(C, B, DIS)
        elif MC == 3:
            drawGiantRat(C, B, DIS)
        elif MC == 4:
            drawOrc(C, B, DIS)
        elif MC == 5:
            drawViper(C, B, DIS)
        elif MC == 6:
            drawCarrionCrawler(C, B, DIS)
        elif MC == 7:
            drawGremlin(C, B, DIS)
        elif MC == 8:
            drawMimic(C, B, DIS)
        elif MC == 9:
            drawDaemon(C, B, DIS)
        elif MC == 10:
            drawBalrog(C, B, DIS)

#  280  GOTO 490
# 490  IF EN = 1 THEN EN = 0: RETURN 
# 491 DIS = DIS + 1: GOTO 202
        if EN == 1:
            break
        DIS = DIS + 1


def drawSkeleton(C, B, DI):
#  300  HPLOT C - 23 / DIS,B TO C - 15 / DIS,B TO C - 15 / DI,B - 15 / DI TO C - 8 / DI,B - 30 / DI TO C + 8 / DI,B - 30 / DI TO C + 15 / DI,B - 15 / DI TO C + 15 / DI,B TO C + 23 / DI,B
    apple.hplot([ [C - 23 / DI,B], [C - 15 / DI,B], [C - 15 / DI,B - 15 / DI], [C - 8 / DI,B - 30 / DI], [C + 8 / DI,B - 30 / DI], [C + 15 / DI,B - 15 / DI], [C + 15 / DI,B], [C + 23 / DI,B] ])
#  301  HPLOT C,B - 26 / DI TO C,B - 65 / DI: HPLOT C - 2 / DI + .5,B - 38 / DI TO C + 2 / DI + .5,B - 38 / DI: HPLOT C - 3 / DI + .5,B - 45 / DI TO C + 3 / DI + .5,B - 45 / DI: HPLOT C - 5 / DI + .5,B - 53 / DI TO C + 5 / DI + .5,B - 53 / DI
    apple.hplot([(C,B - 26 / DI), (C,B - 65 / DI)])
    apple.hplot([(C - 2 / DI + .5,B - 38 / DI), (C + 2 / DI + .5,B - 38 / DI)])
    apple.hplot([(C - 3 / DI + .5,B - 45 / DI), (C + 3 / DI + .5,B - 45 / DI)])
    apple.hplot([(C - 5 / DI + .5,B - 53 / DI), (C + 5 / DI + .5,B - 53 / DI)])
#  302  HPLOT C - 23 / DI,B - 56 / DI TO C - 30 / DI,B - 53 / DI TO C - 23 / DI,B - 45 / DI TO C - 23 / DI,B - 53 / DI TO C - 8 / DI,B - 38 / DI
    apple.hplot([ [C - 23 / DI,B - 56 / DI], [C - 30 / DI,B - 53 / DI], [C - 23 / DI,B - 45 / DI], [C - 23 / DI,B - 53 / DI], [C - 8 / DI,B - 38 / DI] ])
#  303  HPLOT C - 15 / DI,B - 45 / DI TO C - 8 / DI,B - 60 / DI TO C + 8 / DI,B - 60 / DI TO C + 15 / DI,B - 45 / DI: HPLOT C + 15 / DI,B - 42 / DI TO C + 15 / DI,B - 57 / DI: HPLOT C + 12 / DI,B - 45 / DI TO C + 20 / DI,B - 45 / DI
    apple.hplot([ [C - 15 / DI,B - 45 / DI], [C - 8 / DI,B - 60 / DI], [C + 8 / DI,B - 60 / DI], [C + 15 / DI,B - 45 / DI] ])
    apple.hplot([(C + 15 / DI,B - 42 / DI), (C + 15 / DI,B - 57 / DI)])
    apple.hplot([(C + 12 / DI,B - 45 / DI), (C + 20 / DI,B - 45 / DI)])
#  304  HPLOT C,B - 75 / DI TO C - 5 / DI + .5,B - 80 / DI TO C - 8 / DI,B - 75 / DI TO C - 5 / DI + .5,B - 65 / DI TO C + 5 / DI + .5,B - 65 / DI TO C + 5 / DI + .5,B - 68 / DI TO C - 5 / DI + .5,B - 68 / DI TO C - 5 / DI + .5,B - 65 / DI
#  305  HPLOT  TO C + 5 / DI + .5,B - 65 / DI TO C + 8 / DI,B - 75 / DI TO C + 5 / DI + .5,B - 80 / DI TO C - 5 / DI + .5,B - 80 / DI: HPLOT C - 5 / DI + .5,B - 72 / DI: HPLOT C + 5 / DI + .5,B - 72 / DI
    apple.hplot([ [C,B - 75 / DI], [C - 5 / DI + .5,B - 80 / DI], [C - 8 / DI,B - 75 / DI], [C - 5 / DI + .5,B - 65 / DI], [C + 5 / DI + .5,B - 65 / DI], [C + 5 / DI + .5,B - 68 / DI], [C - 5 / DI + .5,B - 68 / DI], [C - 5 / DI + .5,B - 65 / DI] ])
    apple.hplotTo([ [C + 5 / DI + .5,B - 65 / DI], [C + 8 / DI,B - 75 / DI], [C + 5 / DI + .5,B - 80 / DI], [C - 5 / DI + .5,B - 80 / DI] ])
    apple.hplot([(C - 5 / DI + .5,B - 72 / DI), (C - 5 / DI + .5,B - 72 / DI)])
    apple.hplot([(C + 5 / DI + .5,B - 72 / DI), (C + 5 / DI + .5,B - 72 / DI)])
#  309  GOTO 490


def drawThief(C, B, DI):
#  310  HPLOT C,B - 56 / DI TO C,B - 8 / DI TO C + 10 / DI,B TO C + 30 / DI,B TO C + 30 / DI,B - 45 / DI TO C + 10 / DI,B - 64 / DI TO C,B - 56 / DI
#  311  HPLOT  TO C - 10 / DI,B - 64 / DI TO C - 30 / DI,B - 45 / DI TO C - 30 / DI,B TO C - 10 / DI,B TO C,B - 8 / DI
    apple.hplot([ [C,B - 56 / DI], [C,B - 8 / DI], [C + 10 / DI,B], [C + 30 / DI,B], [C + 30 / DI,B - 45 / DI], [C + 10 / DI,B - 64 / DI], [C,B - 56 / DI] ])
    apple.hplotTo([ [C - 10 / DI,B - 64 / DI], [C - 30 / DI,B - 45 / DI], [C - 30 / DI,B], [C - 10 / DI,B], [C,B - 8 / DI] ])
#  312  HPLOT C - 10 / DI,B - 64 / DI TO C - 10 / DI,B - 75 / DI TO C,B - 83 / DI TO C + 10 / DI,B - 75 / DI TO C,B - 79 / DI TO C - 10 / DI,B - 75 / DI TO C,B - 60 / DI TO C + 10 / DI,B - 75 / DI TO C + 10 / DI,B - 64 / DI
    apple.hplot([ [C - 10 / DI,B - 64 / DI], [C - 10 / DI,B - 75 / DI], [C,B - 83 / DI], [C + 10 / DI,B - 75 / DI], [C,B - 79 / DI], [C - 10 / DI,B - 75 / DI], [C,B - 60 / DI], [C + 10 / DI,B - 75 / DI], [C + 10 / DI,B - 64 / DI] ])
#  319  GOTO 490


def drawGiantRat(C, B, DI):
#  320  HPLOT C + 5 / DI,B - 30 / DI TO C,B - 25 / DI TO C - 5 / DI,B - 30 / DI TO C - 15 / DI,B - 5 / DI TO C - 10 / DI,B TO C + 10 / DI,B TO C + 15 / DI,B - 5 / DI
#  321  HPLOT  TO C + 20 / DI,B - 5 / DI TO C + 10 / DI,B TO C + 15 / DI,B - 5 / DI TO C + 5 / DI,B - 30 / DI TO C + 10 / DI,B - 40 / DI TO C + 3 / DI + .5,B - 35 / DI TO C - 3 / DI + .5,B - 35 / DI TO C - 10 / DI,B - 40 / DI TO C - 5 / DI,B - 30 / DI
    apple.hplot([ [C + 5 / DI,B - 30 / DI], [C,B - 25 / DI], [C - 5 / DI,B - 30 / DI], [C - 15 / DI,B - 5 / DI], [C - 10 / DI,B], [C + 10 / DI,B], [C + 15 / DI,B - 5 / DI] ])
    apple.hplotTo([ [C + 20 / DI,B - 5 / DI], [C + 10 / DI,B], [C + 15 / DI,B - 5 / DI], [C + 5 / DI,B - 30 / DI], [C + 10 / DI,B - 40 / DI], [C + 3 / DI + .5,B - 35 / DI], [C - 3 / DI + .5,B - 35 / DI], [C - 10 / DI,B - 40 / DI], [C - 5 / DI,B - 30 / DI] ])
#  322  HPLOT C - 5 / DI,B - 33 / DI TO C - 3 / DI + .5,B - 30 / DI: HPLOT C + 5 / DI,B - 33 / DI TO C + 3 / DI + .5,B - 30 / DI: HPLOT C - 5 / DI,B - 20 / DI TO C - 5 / DI,B - 15 / DI
    apple.hplot([(C - 5 / DI,B - 33 / DI), (C - 3 / DI + .5,B - 30 / DI)])
    apple.hplot([(C + 5 / DI,B - 33 / DI), (C + 3 / DI + .5,B - 30 / DI)])
    apple.hplot([(C - 5 / DI,B - 20 / DI), (C - 5 / DI,B - 15 / DI)])
#  323  HPLOT C + 5 / DI,B - 20 / DI TO C + 5 / DI,B - 15 / DI: HPLOT C - 7 / DI,B - 20 / DI TO C - 7 / DI,B - 15 / DI: HPLOT C + 7 / DI,B - 20 / DI TO C + 7 / DI,B - 15 / DI
    apple.hplot([(C + 5 / DI,B - 20 / DI), (C + 5 / DI,B - 15 / DI)])
    apple.hplot([(C - 7 / DI,B - 20 / DI), (C - 7 / DI,B - 15 / DI)])
    apple.hplot([(C + 7 / DI,B - 20 / DI), (C + 7 / DI,B - 15 / DI)])
# 329  GOTO 490


def drawOrc(C, B, DI):
#  330  HPLOT C,B TO C - 15 / DI,B TO C - 8 / DI,B - 8 / DI TO C - 8 / DI,B - 15 / DI TO C - 15 / DI,B - 23 / DI TO C - 15 / DI,B - 15 / DI TO C - 23 / DI,B - 23 / DI
#  331  HPLOT  TO C - 23 / DI,B - 45 / DI TO C - 15 / DI,B - 53 / DI TO C - 8 / DI,B - 53 / DI TO C - 15 / DI,B - 68 / DI TO C - 8 / DI,B - 75 / DI TO C,B - 75 / DI
    apple.hplot([ [C,B], [C - 15 / DI,B], [C - 8 / DI,B - 8 / DI], [C - 8 / DI,B - 15 / DI], [C - 15 / DI,B - 23 / DI], [C - 15 / DI,B - 15 / DI], [C - 23 / DI,B - 23 / DI] ])
    apple.hplotTo([ [C - 23 / DI,B - 45 / DI], [C - 15 / DI,B - 53 / DI], [C - 8 / DI,B - 53 / DI], [C - 15 / DI,B - 68 / DI], [C - 8 / DI,B - 75 / DI], [C,B - 75 / DI] ])
#  332  HPLOT C,B TO C + 15 / DI,B TO C + 8 / DI,B - 8 / DI TO C + 8 / DI,B - 15 / DI TO C + 15 / DI,B - 23 / DI TO C + 15 / DI,B - 15 / DI TO C + 23 / DI,B - 23 / DI
#  333  HPLOT  TO C + 23 / DI,B - 45 / DI TO C + 15 / DI,B - 53 / DI TO C + 8 / DI,B - 53 / DI TO C + 15 / DI,B - 68 / DI TO C + 8 / DI,B - 75 / DI TO C,B - 75 / DI
    apple.hplot([ [C,B], [C + 15 / DI,B], [C + 8 / DI,B - 8 / DI], [C + 8 / DI,B - 15 / DI], [C + 15 / DI,B - 23 / DI], [C + 15 / DI,B - 15 / DI], [C + 23 / DI,B - 23 / DI] ])
    apple.hplotTo([ [C + 23 / DI,B - 45 / DI], [C + 15 / DI,B - 53 / DI], [C + 8 / DI,B - 53 / DI], [C + 15 / DI,B - 68 / DI], [C + 8 / DI,B - 75 / DI], [C,B - 75 / DI] ])
#  334  HPLOT C - 15 / DI,B - 68 / DI TO C + 15 / DI,B - 68 / DI: HPLOT C - 8 / DI,B - 53 / DI TO C + 8 / DI,B - 53 / DI: HPLOT C - 23 / DI,B - 15 / DI TO C + 8 / DI,B - 45 / DI
    apple.hplot([(C - 15 / DI,B - 68 / DI), (C + 15 / DI,B - 68 / DI)])
    apple.hplot([(C - 8 / DI,B - 53 / DI), (C + 8 / DI,B - 53 / DI)])
    apple.hplot([(C - 23 / DI,B - 15 / DI), (C + 8 / DI,B - 45 / DI)])
#  335  HPLOT C - 8 / DI,B - 68 / DI TO C,B - 60 / DI TO C + 8 / DI,B - 68 / DI TO C + 8 / DI,B - 60 / DI TO C - 8 / DI,B - 60 / DI TO C - 8 / DI,B - 68 / DI
    apple.hplot([ [C - 8 / DI,B - 68 / DI], [C,B - 60 / DI], [C + 8 / DI,B - 68 / DI], [C + 8 / DI,B - 60 / DI], [C - 8 / DI,B - 60 / DI], [C - 8 / DI,B - 68 / DI] ])
#  336  HPLOT C,B - 38 / DI TO C - 8 / DI,B - 38 / DI TO C + 8 / DI,B - 53 / DI TO C + 8 / DI,B - 45 / DI TO C + 15 / DI,B - 45 / DI TO C,B - 30 / DI TO C,B - 38 / DI
    apple.hplot([ [C,B - 38 / DI], [C - 8 / DI,B - 38 / DI], [C + 8 / DI,B - 53 / DI], [C + 8 / DI,B - 45 / DI], [C + 15 / DI,B - 45 / DI], [C,B - 30 / DI], [C,B - 38 / DI] ])
#  339  GOTO 490


def drawViper(C, B, DI):
#  340  HPLOT C - 10 / DI,B - 15 / DI TO C - 10 / DI,B - 30 / DI TO C - 15 / DI,B - 20 / DI TO C - 15 / DI,B - 15 / DI TO C - 15 / DI,B TO C + 15 / DI,B TO C + 15 / DI,B - 15 / DI TO C - 15 / DI,B - 15 / DI
    apple.hplot([ [C - 10 / DI,B - 15 / DI], [C - 10 / DI,B - 30 / DI], [C - 15 / DI,B - 20 / DI], [C - 15 / DI,B - 15 / DI], [C - 15 / DI,B], [C + 15 / DI,B], [C + 15 / DI,B - 15 / DI], [C - 15 / DI,B - 15 / DI] ])
#  341  HPLOT C - 15 / DI,B - 10 / DI TO C + 15 / DI,B - 10 / DI: HPLOT C - 15 / DI,B - 5 / DI TO C + 15 / DI,B - 5 / DI
    apple.hplot([(C - 15 / DI,B - 10 / DI), (C + 15 / DI,B - 10 / DI)])
    apple.hplot([(C - 15 / DI,B - 5 / DI), (C + 15 / DI,B - 5 / DI)])
#  342  HPLOT C,B - 15 / DI TO C - 5 / DI,B - 20 / DI TO C - 5 / DI,B - 35 / DI TO C + 5 / DI,B - 35 / DI TO C + 5 / DI,B - 20 / DI TO C + 10 / DI,B - 15 / DI
    apple.hplot([ [C,B - 15 / DI], [C - 5 / DI,B - 20 / DI], [C - 5 / DI,B - 35 / DI], [C + 5 / DI,B - 35 / DI], [C + 5 / DI,B - 20 / DI], [C + 10 / DI,B - 15 / DI] ])
#  343  HPLOT C - 5 / DI,B - 20 / DI TO C + 5 / DI,B - 20 / DI: HPLOT C - 5 / DI,B - 25 / DI TO C + 5 / DI,B - 25 / DI: HPLOT C - 5 / DI,B - 30 / DI TO C + 5 / DI,B - 30 / DI
    apple.hplot([(C - 5 / DI,B - 20 / DI), (C + 5 / DI,B - 20 / DI)])
    apple.hplot([(C - 5 / DI,B - 25 / DI), (C + 5 / DI,B - 25 / DI)])
    apple.hplot([(C - 5 / DI,B - 30 / DI), (C + 5 / DI,B - 30 / DI)])
#  344  HPLOT C - 10 / DI,B - 35 / DI TO C - 10 / DI,B - 40 / DI TO C - 5 / DI,B - 45 / DI TO C + 5 / DI,B - 45 / DI TO C + 10 / DI,B - 40 / DI TO C + 10 / DI,B - 35 / DI
    apple.hplot([ [C - 10 / DI,B - 35 / DI], [C - 10 / DI,B - 40 / DI], [C - 5 / DI,B - 45 / DI], [C + 5 / DI,B - 45 / DI], [C + 10 / DI,B - 40 / DI], [C + 10 / DI,B - 35 / DI] ])
#  345  HPLOT C - 10 / DI,B - 40 / DI TO C,B - 45 / DI TO C + 10 / DI,B - 40 / DI
    apple.hplot([ [C - 10 / DI,B - 40 / DI], [C,B - 45 / DI], [C + 10 / DI,B - 40 / DI] ])
#  346  HPLOT C - 5 / DI,B - 40 / DI TO C + 5 / DI,B - 40 / DI TO C + 15 / DI,B - 30 / DI TO C,B - 40 / DI TO C - 15 / DI,B - 30 / DI TO C - 5 / DI + .5,B - 40 / DI
    apple.hplot([ [C - 5 / DI,B - 40 / DI], [C + 5 / DI,B - 40 / DI], [C + 15 / DI,B - 30 / DI], [C,B - 40 / DI], [C - 15 / DI,B - 30 / DI], [C - 5 / DI + .5,B - 40 / DI] ])
#  349  GOTO 490


def drawCarrionCrawler(C, B, DI):
    global YY
#  350  HPLOT C - 20 / DI,79 - YY%(DIS) TO C - 20 / DI,B - 88 / DI TO C - 10 / DI,B - 83 / DI TO C + 10 / DI,B - 83 / DI TO C + 20 / DI,B - 88 / DI TO C + 20 / DI,79 - YY%(DIS) TO C - 20 / DI,79 - YY%(DI)
    apple.hplot([ [C - 20 / DI,79 - YY[DI]], [C - 20 / DI,B - 88 / DI], [C - 10 / DI,B - 83 / DI], [C + 10 / DI,B - 83 / DI], [C + 20 / DI,B - 88 / DI], [C + 20 / DI,79 - YY[DI]], [C - 20 / DI,79 - YY[DI]] ])
#  351  HPLOT C - 20 / DI,B - 88 / DI TO C - 30 / DI,B - 83 / DI TO C - 30 / DI,B - 78 / DI: HPLOT C + 20 / DI,B - 88 / DI TO C + 30 / DI,B - 83 / DI TO C + 40 / DI,B - 83 / DI
    apple.hplot([ [C - 20 / DI,B - 88 / DI], [C - 30 / DI,B - 83 / DI], [C - 30 / DI,B - 78 / DI] ])
    apple.hplot([ [C + 20 / DI,B - 88 / DI], [C + 30 / DI,B - 83 / DI], [C + 40 / DI,B - 83 / DI] ])
#  352  HPLOT C - 15 / DI,B - 86 / DI TO C - 20 / DI,B - 83 / DI TO C - 20 / DI,B - 78 / DI TO C - 30 / DI,B - 73 / DI TO C - 30 / DI,B - 68 / DI TO C - 20 / DI,B - 63 / DI
    apple.hplot([ [C - 15 / DI,B - 86 / DI], [C - 20 / DI,B - 83 / DI], [C - 20 / DI,B - 78 / DI], [C - 30 / DI,B - 73 / DI], [C - 30 / DI,B - 68 / DI], [C - 20 / DI,B - 63 / DI] ])
#  353  HPLOT C - 10 / DI,B - 83 / DI TO C - 10 / DI,B - 58 / DI TO C,B - 50 / DI: HPLOT C + 10 / DI,B - 83 / DI TO C + 10 / DI,B - 78 / DI TO C + 20 / DI,B - 73 / DI TO C + 20 / DI,B - 40 / DI
    apple.hplot([ [C - 10 / DI,B - 83 / DI], [C - 10 / DI,B - 58 / DI], [C,B - 50 / DI] ])
    apple.hplot([ [C + 10 / DI,B - 83 / DI], [C + 10 / DI,B - 78 / DI], [C + 20 / DI,B - 73 / DI], [C + 20 / DI,B - 40 / DI] ])
#  354  HPLOT C + 15 / DI,B - 85 / DI TO C + 20 / DI,B - 78 / DI TO C + 30 / DI,B - 76 / DI TO C + 30 / DI,B - 60 / DI
    apple.hplot([ [C + 15 / DI,B - 85 / DI], [C + 20 / DI,B - 78 / DI], [C + 30 / DI,B - 76 / DI], [C + 30 / DI,B - 60 / DI] ])
#  355  HPLOT C,B - 83 / DI TO C,B - 73 / DI TO C + 10 / DI,B - 68 / DI TO C + 10 / DI,B - 63 / DI TO C,B - 58 / DI
    apple.hplot([ [C,B - 83 / DI], [C,B - 73 / DI], [C + 10 / DI,B - 68 / DI], [C + 10 / DI,B - 63 / DI], [C,B - 58 / DI] ])
#  359  GOTO 490


def drawGremlin(C, B, DI):
#  360  HPLOT C + 5 / DI + .5,B - 10 / DI TO C - 5 / DI + .5,B - 10 / DI TO C,B - 15 / DI TO C + 10 / DI,B - 20 / DI TO C + 5 / DI + .5,B - 15 / DI TO C + 5 / DI + .5,B - 10 / DI
#  361  HPLOT  TO C + 7 / DI + .5,B - 6 / DI TO C + 5 / DI + .5,B - 3 / DI TO C - 5 / DI + .5,B - 3 / DI TO C - 7 / DI + .5,B - 6 / DI TO C - 5 / DI + .5,B - 10 / DI
    apple.hplot([ [C + 5 / DI + .5,B - 10 / DI ], [ C - 5 / DI + .5,B - 10 / DI ], [ C,B - 15 / DI ], [ C + 10 / DI,B - 20 / DI ], [ C + 5 / DI + .5,B - 15 / DI ], [ C + 5 / DI + .5,B - 10 / DI] ])
    apple.hplotTo([ [C + 7 / DI + .5,B - 6 / DI ], [ C + 5 / DI + .5,B - 3 / DI ], [ C - 5 / DI + .5,B - 3 / DI ], [ C - 7 / DI + .5,B - 6 / DI ], [ C - 5 / DI + .5,B - 10 / DI] ])
#  362  HPLOT C + 2 / DI + .5,B - 3 / DI TO C + 5 / DI + .5,B TO C + 8 / DI,B: HPLOT C - 2 / DI + .5,B - 3 / DI TO C - 5 / DI + .5,B TO C - 8 / DI,B: HPLOT C + 3 / DI + .5,B - 8 / DI: HPLOT C - 3 / DI + .5,B - 8 / DI: HPLOT C + 3 / DI + .5,B - 5 / DI TO C - 3 / DI + .5,B - 5 / DI
    apple.hplot([ [C + 2 / DI + .5,B - 3 / DI ], [ C + 5 / DI + .5,B ], [ C + 8 / DI,B] ])
    apple.hplot([ [C - 2 / DI + .5,B - 3 / DI ], [ C - 5 / DI + .5,B ], [ C - 8 / DI,B] ])
    apple.hplot([(C + 3 / DI + .5,B - 8 / DI), (C + 3 / DI + .5,B - 8 / DI)])
    apple.hplot([(C - 3 / DI + .5,B - 8 / DI), (C - 3 / DI + .5,B - 8 / DI)])
    apple.hplot([(C + 3 / DI + .5,B - 5 / DI), (C - 3 / DI + .5,B - 5 / DI)])
#  363  GOTO 490


def drawMimic(C, B, DI):
    global PER
#  370  HPLOT 139 - 10 / DIS,PER%(DIS,3) TO 139 - 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 10 / DIS,PER%(DIS,3) TO 139 - 10 / DIS,PER%(DIS,3)
    apple.hplot([ [139 - 10 / DI, PER[DI][3]], [139 - 10 / DI, PER[DI][3] - 10 / DI], [139 + 10 / DI, PER[DI][3] - 10 / DI], [139 + 10 / DI, PER[DI][3]], [139 - 10 / DI, PER[DI][3]] ])
#  371  HPLOT 139 - 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 - 5 / DIS,PER%(DIS,3) - 15 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 15 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 5 / DIS TO 139 + 10 / DIS,PER%(DIS,3)
    apple.hplot([ [139 - 10 / DI, PER[DI][3] - 10 / DI], [139 - 5 / DI, PER[DI][3] - 15 / DI], [139 + 15 / DI, PER[DI][3] - 15 / DI], [139 + 15 / DI, PER[DI][3] - 5 / DI], [139 + 10 / DI, PER[DI][3]] ])
#  372  HPLOT 139 + 10 / DIS,PER%(DIS,3) - 10 / DIS TO 139 + 15 / DIS,PER%(DIS,3) - 15 / DIS
    apple.hplot([(139 + 10 / DI, PER[DI][3] - 10 / DI), (139 + 15 / DI, PER[DI][3] - 15 / DI)])
#  373  GOTO 490


def drawDaemon(C, B, DI):
#  380  HPLOT C - 14 / DI,B - 46 / DI TO C - 12 / DI,B - 37 / DI TO C - 20 / DI,B - 32 / DI TO C - 30 / DI,B - 32 / DI TO C - 22 / DI,B - 24 / DI TO C - 40 / DI,B - 17 / DI TO C - 40 / DI,B - 7 / DI TO C - 38 / DI,B - 5 / DI TO C - 40 / DI,B - 3 / DI TO C - 40 / DI,B
#  381  HPLOT  TO C - 36 / DI,B TO C - 34 / DI,B - 2 / DI TO C - 32 / DI,B TO C - 28 / DI,B TO C - 28 / DI,B - 3 / DI TO C - 30 / DI,B - 5 / DI TO C - 28 / DI,B - 7 / DI TO C - 28 / DI,B - 15 / DI TO C,B - 27 / DI
    apple.hplot([ [C - 14 / DI,B - 46 / DI], [C - 12 / DI,B - 37 / DI], [C - 20 / DI,B - 32 / DI], [C - 30 / DI,B - 32 / DI], [C - 22 / DI,B - 24 / DI], [C - 40 / DI,B - 17 / DI], [C - 40 / DI,B - 7 / DI], [C - 38 / DI,B - 5 / DI], [C - 40 / DI,B - 3 / DI], [C - 40 / DI,B] ])
    apple.hplotTo([ [C - 36 / DI,B], [C - 34 / DI,B - 2 / DI], [C - 32 / DI,B], [C - 28 / DI,B], [C - 28 / DI,B - 3 / DI], [C - 30 / DI,B - 5 / DI], [C - 28 / DI,B - 7 / DI], [C - 28 / DI,B - 15 / DI], [C,B - 27 / DI] ])
#  382  HPLOT C + 14 / DI,B - 46 / DI TO C + 12 / DI,B - 37 / DI TO C + 20 / DI,B - 32 / DI TO C + 30 / DI,B - 32 / DI TO C + 22 / DI,B - 24 / DI TO C + 40 / DI,B - 17 / DI TO C + 40 / DI,B - 7 / DI TO C + 38 / DI,B - 5 / DI TO C + 40 / DI,B - 3 / DI TO C + 40 / DI,B
#  383  HPLOT  TO C + 36 / DI,B TO C + 34 / DI,B - 2 / DI TO C + 32 / DI,B TO C + 28 / DI,B TO C + 28 / DI,B - 3 / DI TO C + 30 / DI,B - 5 / DI TO C + 28 / DI,B - 7 / DI TO C + 28 / DI,B - 15 / DI TO C,B - 27 / DI
    apple.hplot([ [C + 14 / DI,B - 46 / DI], [C + 12 / DI,B - 37 / DI], [C + 20 / DI,B - 32 / DI], [C + 30 / DI,B - 32 / DI], [C + 22 / DI,B - 24 / DI], [C + 40 / DI,B - 17 / DI], [C + 40 / DI,B - 7 / DI], [C + 38 / DI,B - 5 / DI], [C + 40 / DI,B - 3 / DI], [C + 40 / DI,B] ])
    apple.hplotTo([ [C + 36 / DI,B], [C + 34 / DI,B - 2 / DI], [C + 32 / DI,B], [C + 28 / DI,B], [C + 28 / DI,B - 3 / DI], [C + 30 / DI,B - 5 / DI], [C + 28 / DI,B - 7 / DI], [C + 28 / DI,B - 15 / DI], [C,B - 27 / DI] ])
#  384  HPLOT C + 6 / DI,B - 48 / DI TO C + 38 / DI,B - 41 / DI TO C + 40 / DI,B - 42 / DI TO C + 18 / DI,B - 56 / DI TO C + 12 / DI,B - 56 / DI TO C + 10 / DI,B - 57 / DI TO C + 8 / DI,B - 56 / DI TO C - 8 / DI,B - 56 / DI TO C - 10 / DI,B - 58 / DI TO C + 14 / DI,B - 58 / DI TO C + 16 / DI,B - 59 / DI
#  385  HPLOT  TO C + 8 / DI,B - 63 / DI TO C + 6 / DI,B - 63 / DI TO C + 2 / DI + .5,B - 70 / DI TO C + 2 / DI + .5,B - 63 / DI TO C - 2 / DI + .5,B - 63 / DI TO C - 2 / DI + .5,B - 70 / DI TO C - 6 / DI,B - 63 / DI TO C - 8 / DI,B - 63 / DI TO C - 16 / DI,B - 59 / DI TO C - 14 / DI,B - 58 / DI
#  386  HPLOT  TO C - 10 / DI,B - 57 / DI TO C - 12 / DI,B - 56 / DI TO C - 18 / DI,B - 56 / DI TO C - 36 / DI,B - 47 / DI TO C - 36 / DI,B - 39 / DI TO C - 28 / DI,B - 41 / DI TO C - 28 / DI,B - 46 / DI TO C - 20 / DI,B - 50 / DI TO C - 18 / DI,B - 50 / DI TO C - 14 / DI,B - 46 / DI
    apple.hplot([ [C + 6 / DI,B - 48 / DI], [C + 38 / DI,B - 41 / DI], [C + 40 / DI,B - 42 / DI], [C + 18 / DI,B - 56 / DI], [C + 12 / DI,B - 56 / DI], [C + 10 / DI,B - 57 / DI], [C + 8 / DI,B - 56 / DI], [C - 8 / DI,B - 56 / DI], [C - 10 / DI,B - 58 / DI], [C + 14 / DI,B - 58 / DI], [C + 16 / DI,B - 59 / DI] ])
    apple.hplotTo([ [C + 8 / DI,B - 63 / DI], [C + 6 / DI,B - 63 / DI], [C + 2 / DI + .5,B - 70 / DI], [C + 2 / DI + .5,B - 63 / DI], [C - 2 / DI + .5,B - 63 / DI], [C - 2 / DI + .5,B - 70 / DI], [C - 6 / DI,B - 63 / DI], [C - 8 / DI,B - 63 / DI], [C - 16 / DI,B - 59 / DI], [C - 14 / DI,B - 58 / DI] ])
    apple.hplotTo([ [C - 10 / DI,B - 57 / DI], [C - 12 / DI,B - 56 / DI], [C - 18 / DI,B - 56 / DI], [C - 36 / DI,B - 47 / DI], [C - 36 / DI,B - 39 / DI], [C - 28 / DI,B - 41 / DI], [C - 28 / DI,B - 46 / DI], [C - 20 / DI,B - 50 / DI], [C - 18 / DI,B - 50 / DI], [C - 14 / DI,B - 46 / DI] ])
#  387  GOTO 3087
#  3087  HPLOT C - 28 / DI,B - 41 / DI TO C + 30 / DI,B - 55 / DI: HPLOT C + 28 / DI,B - 58 / DI TO C + 22 / DI,B - 56 / DI TO C + 22 / DI,B - 53 / DI TO C + 28 / DI,B - 52 / DI TO C + 34 / DI,B - 54 / DI: HPLOT C + 20 / DI,B - 50 / DI TO C + 26 / DI,B - 47 / DI
    apple.hplot([(C - 28 / DI,B - 41 / DI), (C + 30 / DI,B - 55 / DI)])
    apple.hplot([ [C + 28 / DI,B - 58 / DI], [C + 22 / DI,B - 56 / DI], [C + 22 / DI,B - 53 / DI], [C + 28 / DI,B - 52 / DI], [C + 34 / DI,B - 54 / DI] ])
    apple.hplot([(C + 20 / DI,B - 50 / DI), (C + 26 / DI,B - 47 / DI)])
#  3088  HPLOT C + 10 / DI,B - 58 / DI TO C + 10 / DI,B - 61 / DI TO C + 4 / DI,B - 58 / DI: HPLOT C - 10 / DI,B - 58 / DI TO C - 10 / DI,B - 61 / DI TO C - 4 / DI,B - 58 / DI: HPLOT C + 40 / DI,B - 9 / DI TO C + 50 / DI,B - 12 / DI TO C + 40 / DI,B - 7 / DI
    apple.hplot([ [C + 10 / DI,B - 58 / DI], [C + 10 / DI,B - 61 / DI], [C + 4 / DI,B - 58 / DI] ])
    apple.hplot([ [C - 10 / DI,B - 58 / DI], [C - 10 / DI,B - 61 / DI], [C - 4 / DI,B - 58 / DI] ])
    apple.hplot([ [C + 40 / DI,B - 9 / DI], [C + 50 / DI,B - 12 / DI], [C + 40 / DI,B - 7 / DI] ])
#  3089  HPLOT C - 8 / DI,B - 25 / DI TO C + 6 / DI,B - 7 / DI TO C + 28 / DI,B - 7 / DI TO C + 28 / DI,B - 9 / DI TO C + 20 / DI,B - 9 / DI TO C + 6 / DI,B - 25 / DI: GOTO 490
    apple.hplot([ [C - 8 / DI,B - 25 / DI], [C + 6 / DI,B - 7 / DI], [C + 28 / DI,B - 7 / DI], [C + 28 / DI,B - 9 / DI], [C + 20 / DI,B - 9 / DI], [C + 6 / DI,B - 25 / DI] ])


def drawBalrog(C, B, DI):
#  390  HPLOT C + 6 / DI,B - 60 / DI TO C + 30 / DI,B - 90 / DI TO C + 60 / DI,B - 30 / DI TO C + 60 / DI,B - 10 / DI TO C + 30 / DI,B - 40 / DI TO C + 15 / DI,B - 40 / DI
    apple.hplot([ [C + 6 / DI,B - 60 / DI], [C + 30 / DI,B - 90 / DI], [C + 60 / DI,B - 30 / DI], [C + 60 / DI,B - 10 / DI], [C + 30 / DI,B - 40 / DI], [C + 15 / DI,B - 40 / DI] ])
#  391  HPLOT C - 6 / DI,B - 60 / DI TO C - 30 / DI,B - 90 / DI TO C - 60 / DI,B - 30 / DI TO C - 60 / DI,B - 10 / DI TO C - 30 / DI,B - 40 / DI TO C - 15 / DI,B - 40 / DI
    apple.hplot([ [C - 6 / DI,B - 60 / DI], [C - 30 / DI,B - 90 / DI], [C - 60 / DI,B - 30 / DI], [C - 60 / DI,B - 10 / DI], [C - 30 / DI,B - 40 / DI], [C - 15 / DI,B - 40 / DI] ])
#  392  HPLOT C,B - 25 / DI TO C + 6 / DI,B - 25 / DI TO C + 10 / DI,B - 20 / DI TO C + 12 / DI,B - 10 / DI TO C + 10 / DI,B - 6 / DI TO C + 10 / DI,B TO C + 14 / DI,B TO C + 15 / DI,B - 5 / DI TO C + 16 / DI,B TO C + 20 / DI,B
#  393  HPLOT  TO C + 20 / DI,B - 6 / DI TO C + 18 / DI,B - 10 / DI TO C + 18 / DI,B - 20 / DI TO C + 15 / DI,B - 30 / DI TO C + 15 / DI,B - 45 / DI TO C + 40 / DI,B - 60 / DI TO C + 40 / DI,B - 70 / DI
#  394  HPLOT  TO C + 10 / DI,B - 55 / DI TO C + 6 / DI,B - 60 / DI TO C + 10 / DI,B - 74 / DI TO C + 6 / DI,B - 80 / DI TO C + 4 / DI + .5,B - 80 / DI TO C + 3 / DI + .5,B - 82 / DI TO C + 2 / DI + .5,B - 80 / DI TO C,B - 80 / DI
    apple.hplot([ (C,B - 25 / DI), (C + 6 / DI,B - 25 / DI), (C + 10 / DI,B - 20 / DI), (C + 12 / DI,B - 10 / DI), (C + 10 / DI,B - 6 / DI), (C + 10 / DI,B), (C + 14 / DI,B), (C + 15 / DI,B - 5 / DI), (C + 16 / DI,B), (C + 20 / DI,B) ])
    apple.hplotTo([ (C + 20 / DI,B - 6 / DI), (C + 18 / DI,B - 10 / DI), (C + 18 / DI,B - 20 / DI), (C + 15 / DI,B - 30 / DI), (C + 15 / DI,B - 45 / DI), (C + 40 / DI,B - 60 / DI), (C + 40 / DI,B - 70 / DI) ])
    apple.hplot([ [C + 10 / DI,B - 55 / DI], [C + 6 / DI,B - 60 / DI], [C + 10 / DI,B - 74 / DI], [C + 6 / DI,B - 80 / DI], [C + 4 / DI + .5,B - 80 / DI], [C + 3 / DI + .5,B - 82 / DI], [C + 2 / DI + .5,B - 80 / DI], [C,B - 80 / DI] ])
#  395  HPLOT C,B - 25 / DI TO C - 6 / DI,B - 25 / DI TO C - 10 / DI,B - 20 / DI TO C - 12 / DI,B - 10 / DI TO C - 10 / DI,B - 6 / DI TO C - 10 / DI,B TO C - 14 / DI,B TO C - 15 / DI,B - 5 / DI TO C - 16 / DI,B TO C - 20 / DI,B
#  396  HPLOT  TO C - 20 / DI,B - 6 / DI TO C - 18 / DI,B - 10 / DI TO C - 18 / DI,B - 20 / DI TO C - 15 / DI,B - 30 / DI TO C - 15 / DI,B - 45 / DI TO C - 40 / DI,B - 60 / DI TO C - 40 / DI,B - 70 / DI
#  397  HPLOT  TO C - 10 / DI,B - 55 / DI TO C - 6 / DI,B - 60 / DI TO C - 10 / DI,B - 74 / DI TO C - 6 / DI,B - 80 / DI TO C - 4 / DI + .5,B - 80 / DI TO C - 3 / DI + .5,B - 82 / DI TO C - 2 / DI + .5,B - 80 / DI TO C,B - 80 / DI
    apple.hplot([ (C,B - 25 / DI), (C - 6 / DI,B - 25 / DI), (C - 10 / DI,B - 20 / DI), (C - 12 / DI,B - 10 / DI), (C - 10 / DI,B - 6 / DI), (C - 10 / DI,B), (C - 14 / DI,B), (C - 15 / DI,B - 5 / DI), (C - 16 / DI,B), (C - 20 / DI,B) ])
    apple.hplotTo([ [C - 20 / DI,B - 6 / DI], [C - 18 / DI,B - 10 / DI], [C - 18 / DI,B - 20 / DI], [C - 15 / DI,B - 30 / DI], [C - 15 / DI,B - 45 / DI], [C - 40 / DI,B - 60 / DI], [C - 40 / DI,B - 70 / DI] ])
    apple.hplotTo([ [C - 10 / DI,B - 55 / DI], [C - 6 / DI,B - 60 / DI], [C - 10 / DI,B - 74 / DI], [C - 6 / DI,B - 80 / DI], [C - 4 / DI + .5,B - 80 / DI], [C - 3 / DI + .5,B - 82 / DI], [C - 2 / DI + .5,B - 80 / DI], [C,B - 80 / DI] ])
#  398  HPLOT C - 6 / DI,B - 25 / DI TO C,B - 6 / DI TO C + 10 / DI,B TO C + 4 / DI + .5,B - 8 / DI TO C + 6 / DI,B - 25 / DI: HPLOT C - 40 / DI,B - 64 / DI TO C - 40 / DI,B - 90 / DI TO C - 52 / DI,B - 80 / DI TO C - 52 / DI,B - 40 / DI
    apple.hplot([ [C - 6 / DI,B - 25 / DI], [C,B - 6 / DI], [C + 10 / DI,B], [C + 4 / DI + .5,B - 8 / DI], [C + 6 / DI,B - 25 / DI] ])
    apple.hplot([ [C - 40 / DI,B - 64 / DI], [C - 40 / DI,B - 90 / DI], [C - 52 / DI,B - 80 / DI], [C - 52 / DI,B - 40 / DI] ])
#  399  HPLOT C + 40 / DI,B - 86 / DI TO C + 38 / DI,B - 92 / DI TO C + 42 / DI,B - 92 / DI TO C + 40 / DI,B - 86 / DI TO C + 40 / DI,B - 50 / DI
    apple.hplot([ [C + 40 / DI,B - 86 / DI], [C + 38 / DI,B - 92 / DI], [C + 42 / DI,B - 92 / DI], [C + 40 / DI,B - 86 / DI], [C + 40 / DI,B - 50 / DI] ])
#  400  HPLOT C + 4 / DI + .5,B - 70 / DI TO C + 6 / DI,B - 74 / DI: HPLOT C - 4 / DI + .5,B - 70 / DI TO C - 6 / DI,B - 74 / DI: HPLOT C,B - 64 / DI TO C,B - 60 / DI: GOTO 490
    apple.hplot([(C + 4 / DI + .5,B - 70 / DI), (C + 6 / DI,B - 74 / DI)])
    apple.hplot([(C - 4 / DI + .5,B - 70 / DI), (C - 6 / DI,B - 74 / DI)])
    apple.hplot([(C,B - 64 / DI), (C,B - 60 / DI)])

#  490  IF EN = 1 THEN EN = 0: RETURN 
#  491 DIS = DIS + 1: GOTO 202
# covered elsewhere

def generateDungeon():
    global LN
    global TX; global TY
    global INOUT

#  500 ZZ =  RND ( -  ABS (LN) - TX * 10 - TY * 1000 + INOUT * 31.4)
    ZZ = random.seed(abs(LN) - TX * 10 - TY * 1000 + INOUT * 31.4)

#  501  FOR X = 1 TO 9: FOR Y = 1 TO 9:DNG%(X,Y) = 0: NEXT : NEXT 
    for X in range(1, 10):
        for Y in range(1, 10):
            DNG[X][Y] = 0
#  510  FOR X = 0 TO 10:DNG%(X,0) = 1:DNG%(X,10) = 1:DNG%(0,X) = 1:DNG%(10,X) = 1: NEXT 
    for X in range(0, 11):
        DNG[X][0] = 1
        DNG[X][10] = 1
        DNG[0][X] = 1
        DNG[10][X] = 1
#  520  FOR X = 2 TO 8 STEP 2: FOR Y = 1 TO 9:DNG%(X,Y) = 1:DNG(Y,X) = 1: NEXT : NEXT 
    for X in range(2, 9, 2):
        for Y in range(1, 10):
            DNG[X][Y] = 1
            DNG[Y][X] = 1
#  530  FOR X = 2 TO 8 STEP 2: FOR Y = 1 TO 9 STEP 2
    for X in range(2, 9, 2):
        for Y in range(1, 10, 2):
#  540  IF  RND (1) > .95 THEN DNG%(X,Y) = 2
            if random.random() > 0.95:
                DNG[X][Y] = 2
#  541  IF  RND (1) > .95 THEN DNG%(Y,X) = 2
            if random.random() > 0.95:
                DNG[Y][X] = 2
#  542  IF  RND (1) > .6 THEN DNG%(Y,X) = 3
            if random.random() > 0.6:
                DNG[Y][X] = 3
#  543  IF  RND (1) > .6 THEN DNG%(X,Y) = 3
            if random.random() > 0.6:
                DNG[X][Y] = 3
#  544  IF  RND (1) > .6 THEN DNG%(X,Y) = 4
            if random.random() > 0.6:
                DNG[X][Y] = 4
#  545  IF  RND (1) > .6 THEN DNG%(Y,X) = 4
            if random.random() > 0.6:
                DNG[Y][X] = 4
#  546  IF  RND (1) > .97 THEN DNG%(Y,X) = 9
            if random.random() > 0.97:
                DNG[Y][X] = 9
#  547  IF  RND (1) > .97 THEN DNG%(X,Y) = 9
            if random.random() > 0.97:
                DNG[X][Y] = 9
#  548  IF  RND (1) > .94 THEN DNG%(X,Y) = 5
            if random.random() > 0.94:
                DNG[X][Y] = 5
#  549  IF  RND (1) > .94 THEN DNG%(Y,X) = 5
            if random.random() > 0.94:
                DNG[Y][X] = 5
#  568  NEXT : NEXT 
#  569 DNG%(2,1) = 0: IF INOUT / 2 =  INT (INOUT / 2) THEN DNG%(7,3) = 7:DNG%(3,7) = 8
    DNG[2][1] = 0
    if INOUT / 2 == int(INOUT / 2):
        DNG[7][3] = 7
        DNG[3][7] = 8
#  570  IF INOUT / 2 <  >  INT (INOUT / 2) THEN DNG%(7,3) = 8:DNG%(3,7) = 7
    else:
        DNG[7][3] = 8
        DNG[3][7] = 7
#  580  IF INOUT = 1 THEN DNG%(1,1) = 8:DNG%(7,3) = 0
    if INOUT == 1:
        DNG[1][1] = 8
        DNG[7][3] = 0
#  585  GOSUB 2000

    monsterSetup()
#  590  RETURN 


def mainLoop(surface):
    global INOUT
    global TX; global TY
    global DX; global DY
    global PX; global PY
    global LK
    global PA

    while True:
#  1000 VTAB (24): PRINT "COMMAND? ";: CALL  - 868
        apple.vtab(24); apple.print("COMMAND? ", False); apple.clearLineEnd()
#  1001 X =  PEEK ( - 16384): IF X < 128 THEN 1001
#  1002 Q =  FRE (0)
#  1010  POKE  - 16368,0
        X = apple.getKeypress()
#  1030  IF X = 141 THEN  ON  SGN (INOUT) + 1 GOTO 1100,1150
#  1100  PRINT "NORTH": IF TER%(TX,TY - 1) = 1 THEN  PRINT "YOU CAN'T PASS THE MOUNTAINS": GOTO 1090
#  1110 TY = TY - 1: GOTO 1090
#  1150  IF DNG%(PX + DX,PY + DY) <  > 1 AND DNG%(PX + DX,PY + DY) < 10 THEN PX = PX + DX:PY = PY + DY
#  1155  PRINT "FORWARD"
#  1160  IF DNG%(PX,PY) = 2 THEN  PRINT "AAARRRGGGHHH!!! A TRAP!":C(0)= C(0) -  INT ( RND (1) * INOUT + 3):MR = 1:INOUT = INOUT + 1: PRINT "FALLING TO LEVEL ";IN: GOSUB 500: GOTO 1090
#  1165 Z = 0
#  1170  IF DNG%(PX,PY) = 5 THEN DNG%(PX,PY) = 0: PRINT "GOLD!!!!!":Z =  INT ( RND (1) * 5 * INOUT + INOUT): PRINT Z;"-PIECES OF EIGHT":C(5) = C(5) + Z
#  1175  IF Z > 0 THEN Z =  INT ( RND (1) * 6): PRINT "AND A ";W$(Z):PW(Z) = PW(Z) + 1: GOTO 1090
#  1190  GOTO 1090
        sgnInout = apple.sgn(INOUT) + 1
        if X == 141:
            if sgnInout == 1:
                apple.print("NORTH")
                if TE[TX][TY - 1] == 1:
                    apple.print("YOU CAN'T PASS THE MOUNTAINS")
                else:
                    TY = TY - 1
            elif sgnInout == 2:
                if DNG[PX + DX][PY + DY] != 1 and DNG[PX + DX][PY + DY] < 10:
                    PX = PX + DX; PY = PY + DY
                apple.print("FORWARD")
                if DNG[PX][PY] == 2:
                    apple.print("AAARRRGGGHHH!!! A TRAP!")
                    C[0] = C[0] - int(random.random() * INOUT + 3)
                    MR = 1
                    INOUT = INOUT + 1
                    apple.print(f"FALLING TO LEVEL {INOUT}")
                    generateDungeon()
                else:
                    Z = 0
                    if DNG[PX][PY] == 5:
                        DNG[PX][PY] = 0
                        apple.print("GOLD!!!!!")
                        Z =  int(random.random() * 5 * INOUT + INOUT)
                        apple.print(f"{Z}-PIECES OF EIGHT")
                        C[5] = C[5] + Z
                        Z = int(random.random() * 6)
                        apple.print(f"AND A {Ws[Z]}")
                        PW[Z] = PW[Z] + 1
# 1040  IF X = 149 THEN  ON  SGN (INOUT) + 1 GOTO 1200,1250
#  1200  PRINT "EAST": IF TER%(TX + 1,TY) = 1 THEN  PRINT "YOU CAN'T PASS THE MOUNTAINS": GOTO 1090
#  1210 TX = TX + 1: GOTO 1090
#  1250  PRINT "TURN RIGHT"
#  1255  IF DX <  > 0 THEN DY = DX:DX = 0: GOTO 1090
#  1260 DX =  - DY:DY = 0: GOTO 1090
        elif X == 149:
            if sgnInout == 1:
                apple.print("EAST")
                if TE[TX + 1][TY] == 1:
                    apple.print("YOU CAN'T PASS THE MOUNTAINS")
                else:                
                    TX = TX + 1
            elif sgnInout == 2:
                apple.print("TURN RIGHT")
                if DX != 0:
                    DY = DX; DX = 0
                else:
                    DX = -DY; DY = 0
#  1050  IF X = 136 THEN  ON  SGN (INOUT) + 1 GOTO 1300,1350
#  1300  PRINT "WEST": IF TER%(TX - 1,TY) = 1 THEN  PRINT "YOU CAN'T PASS THE MOUNTAINS": GOTO 1090
#  1310 TX = TX - 1: GOTO 1090
#  1350  PRINT "TURN LEFT"
#  1355  IF DX <  > 0 THEN DY =  - DX:DX = 0: GOTO 1090
#  1360 DX = DY:DY = 0: GOTO 1090
        elif X == 136:
            if sgnInout == 1:
                apple.print("WEST")
                if TE[TX - 1][TY] == 1:
                    apple.print("YOU CAN'T PASS THE MOUNTAINS")
                else:
                    TX = TX - 1
            elif sgnInout == 2:
                apple.print("TURN LEFT")
                if DX != 0:
                    DY = -DX; DX = 0
                else:
                    DX = DY; DY = 0
#  1060  IF X = 175 THEN  ON  SGN (INOUT) + 1 GOTO 1400,1450
#  1400  PRINT "SOUTH": IF TER%(TX,TY + 1) = 1 THEN  PRINT "YOU CAN'T PASS THE MOUNTAINS": GOTO 1090
#  1410 TY = TY + 1: GOTO 1090
#  1450  PRINT "TURN AROUND":DX =  - DX:DY =  - DY: GOTO 1090
        elif X == 175:
            if sgnInout == 1:
                apple.print("SOUTH")
                if TE[TX][TY + 1] == 1:
                    apple.print("YOU CAN'T PASS THE MOUNTAINS")
                else:
                    TY = TY + 1
            elif sgnInout == 2:
                apple.print("TURN AROUND")
                DX = -DX; DY = -DY
#  1070  IF X = 216 THEN  ON  SGN (INOUT) + 1 GOTO 1500,1550
#  1500  IF TE%(TX,TY) = 3 THEN  GOSUB 60080: GOSUB 60200: GOTO 1090
#  1510  IF TE%(TX,TY) = 4 AND INOUT = 0 THEN  PRINT "GO DUNGEON": PRINT "PLEASE WAIT ":INOUT = 1: GOSUB 500:DX = 1:DY = 0:PX = 1:PY = 1: GOTO 1090
#  1515  IF TE%(TX,TY) = 5 THEN 7000
#  1520  PRINT "HUH?": GOTO 1000
#  1550  IF DNG%(PX,PY) <  > 7 AND DNG%(PX,PY) <  > 9 THEN 1580
#  1555  PRINT "GO DOWN TO LEVEL ";INOUT + 1
#  1560 INOUT = INOUT + 1: GOSUB 500:MR = 1: GOTO 1090
#  1580  IF DNG%(PX,PY) <  > 8 THEN  PRINT "HUH?": GOTO 1090
#  1581  IF IN = 1 THEN  PRINT "LEAVE DUNGEON":IN = 0: GOTO 1586
#  1584  PRINT "GO UP TO LEVEL ";INOUT - 1
#  1585 INOUT = INOUT - 1: GOSUB 500:MR = 1
#  1586  IF IN = 0 THEN  PRINT "THOU HAST GAINED": PRINT LK;" HIT POINTS":C(0) = C(0) + LK:LK = 0
#  1587  GOTO 1090
        elif X == 216:
            if sgnInout == 1:
                if TE[TX][TY] == 3:
                    stats()
                    town()
                elif TE[TX][TY] == 4 and INOUT == 0:
                    apple.print("GO DUNGEON")
                    apple.print("PLEASE WAIT ")
                    INOUT = 1
                    generateDungeon()
                    DX = 1; DY = 0; PX = 1; PY = 1
                elif TE[TX][TY] == 5:
                    castle(surface)
                else:
                    apple.print("HUH?")
                    continue
            elif sgnInout == 2:
                if not (DNG[PX][PY] != 7 and DNG[PX][PY] != 9):
                    apple.print(f"GO DOWN TO LEVEL {INOUT + 1}")
                    INOUT = INOUT + 1
                    generateDungeon()
                    MR = 1
                else:
                    if DNG[PX][PY] != 8:
                        apple.print("HUH?")
                    else:
                        if INOUT == 1:
                            apple.print("LEAVE DUNGEON")
                            INOUT = 0
                        else:
                            apple.print(f"GO UP TO LEVEL {INOUT - 1}")
                            INOUT = INOUT - 1
                            generateDungeon()
                            MR = 1
                        if INOUT == 0:
                            apple.print("THOU HAST GAINED")
                            apple.print(f"{LK} HIT POINTS")
                            C[0] = C[0] + LK
                            LK = 0
#  1080  IF X = 193 OR X = 155 THEN  ON  SGN (INOUT) + 1 GOTO 1600,1650
#  1600  GOTO 1090
        elif X == 193 or X == 155:
            if sgnInout == 2:
                playerAttack(surface)
#  1081  IF X = 160 THEN  PRINT "PASS": GOTO 1090
        elif X == 160:
            apple.print("PASS")
#  1085  IF X = 211 THEN 1700
#  1700  GOSUB 60080: HOME : PRINT "PRESS -CR- TO CONTINUE";: INPUT Q$: TEXT : HOME : GOTO 1090
        elif X == 211:
            stats()
            apple.home()
            apple.input("PRESS -CR- TO CONTINUE")
            apple.text(); apple.home()
#  1086  IF X = 208 THEN  IF PA = 1 THEN PA = 0: PRINT "PAUSE OFF": GOTO 1000
#  1087  IF X = 208 THEN  IF PA = 0 THEN PA = 1: PRINT "PAUSE ON": GOTO 1000
        elif X == 208:
            if PA == 1:
                PA = 0
                apple.print("PAUSE OFF")
            elif PA == 0:
                PA = 1
                apple.print("PAUSE ON")
            continue
#  1089  PRINT "HUH?": GOTO 1000
        else:
            apple.print("HUH?")
            continue
    
#  1090 PW(0) = PW(0) - 1 +  SGN (INOUT) * .9: IF PW(0) < 0 THEN C(0) = 0: PRINT : PRINT "YOU HAVE STARVED!!!!!": GOTO 1093
# 1091  POKE 33,40: VTAB (22): HTAB (30): PRINT "FOOD=";PW(0);: CALL  - 868: VTAB (23): HTAB (30): PRINT "H.P.=";C(0);: CALL  - 868: VTAB (24): HTAB (30): PRINT "GOLD=";C(5);: CALL  - 868: POKE 33,29: HTAB (1)
# 1092 PW(0) =  INT (PW(0) * 10) / 10
        PW[0] = PW[0] - 1 + apple.sgn(INOUT) * 0.9
        if PW[0] < 0:
            C[0] = 0
            apple.print(); apple.print("YOU HAVE STARVED!!!!!")
        else:
            apple.setTextWindowRight(40)
            apple.vtab(22); apple.htab(30); apple.print(f"FOOD={PW[0]}", False); apple.clearLineEnd()
            apple.vtab(23); apple.htab(30); apple.print(f"H.P.={C[0]}", False); apple.clearLineEnd()
            apple.vtab(24); apple.htab(30); apple.print(f"GOLD={C[5]}", False); apple.clearLineEnd()
            apple.setTextWindowRight(29)
            PW[0] = int(PW[0] * 10) / 10
# 1093  IF C(0) <  = 0 THEN 6000
#  1095  IF IN > 0 THEN  GOSUB 4000: IF C(0) <  = 0 THEN 1093
        if INOUT > 0 and C[0] > 0:
            monsters(surface)
        if C[0] <= 0:
            youHaveDied(surface)
            restartGame()
#  1096  POKE 33,40: VTAB (22): HTAB (30): PRINT "FOOD=";PW(0);: CALL  - 868: VTAB (23): HTAB (30): PRINT "H.P.=";C(0);: CALL  - 868: VTAB (24): HTAB (30): PRINT "GOLD=";C(5);: CALL  - 868: POKE 33,29: HTAB (1)
        apple.setTextWindowRight(40)
        apple.vtab(22); apple.htab(30); apple.print(f"FOOD={PW[0]}", False); apple.clearLineEnd()
        apple.vtab(23); apple.htab(30); apple.print(f"H.P.={C[0]}", False); apple.clearLineEnd()
        apple.vtab(24); apple.htab(30); apple.print(f"GOLD={C[5]}", False); apple.clearLineEnd()
        apple.setTextWindowRight(29)
#  1097  IF INOUT = 0 THEN  GOSUB 100: GOTO 1000
        if INOUT == 0:
            drawMap(surface)
#  1098  IF INOUT > 0 THEN  GOSUB 200: GOTO 1000
        elif INOUT > 0:
            drawDungeon(surface)
#  1600  GOTO 1090


def playerAttack(surface):
    global LK
    global PW
    global PTs
    global C
    global INOUT
    global DNG; global MZ; global ML

    shoot = False
    while True:
#  1650 MN = 0:DAM = 0: PRINT "ATTACK": PRINT "WHICH WEAPON ";: GET Q$
        MN = 0; DAM = 0
        apple.print("ATTACK")
        apple.print("WHICH WEAPON ", False)
        Qs = str.upper(apple.get())
#  1651  IF Q$ = "R" THEN DAM = 10: PRINT "RAPIER": IF PW(1) < 1 THEN  PRINT "NOT OWNED": GOTO 1650
        if Qs == "R":
            DAM = 10
            apple.print("RAPIER")
            if PW[1] < 1:
                apple.print("NOT OWNED")
                continue
#  1652  IF Q$ = "A" THEN DAM = 5: PRINT "AXE": IF PW(2) < 1 THEN  PRINT "NOT OWNED": GOTO 1650
        elif Qs == "A":
            DAM = 5
            apple.print("AXE")
            if PW[2] < 1:
                apple.print("NOT OWNED")
                continue
#  1653  IF Q$ = "S" THEN DAM = 1: PRINT "SHIELD": IF PW(3) < 1 THEN  PRINT "NOT OWNED": GOTO 1650
        elif Qs == "S":
            DAM = 1
            apple.print("SHIELD")
            if PW[3] < 1:
                apple.print("NOT OWNED")
                continue
#  1654  IF Q$ = "B" THEN DAM = 4: PRINT "BOW": IF PW(4) < 1 THEN  PRINT "NOT OWNED": GOTO 1650
        elif Qs == "B":
            DAM = 4
            apple.print("BOW")
            if PW[4] < 1:
                apple.print("NOT OWNED")
                continue
#  1655  IF Q$ = "M" THEN  PRINT "MAGIC AMULET": GOTO 1680
#  1680  IF PW(5) < 1 THEN  PRINT "NONE OWNED": GOTO 1650
#  1681  IF PT$ = "F" THEN Q =  INT ( RND (1) * 4 + 1): GOTO 1685
#  1682  PRINT "1-LADDER-UP","2-LADDER-DN": PRINT "3-KILL","4-BAD??": PRINT "CHOICE ";: GET Q$:Q =  VAL (Q$): PRINT Q: IF Q < 1 OR Q > 4 THEN 1682
#  1683  IF  RND (1) > .75 THEN  PRINT "LAST CHARGE ON THIS AMULET!":PW(5) = PW(5) - 1
#  1685  ON Q GOTO 1686,1690,1691,1692
#  1686  PRINT "LADDER UP":DNG%(PX,PY) = 8: GOTO 1090
#  1690  PRINT "LADDER DOWN":DNG%(PX,PY) = 7: GOTO 1090
#  1691  PRINT "MAGIC ATTACK":DAM = 10 + INOUT: GOTO 1672
#  1692  ON  INT ( RND (1) * 3 + 1) GOTO 1693,1695,1697
#  1693  PRINT "YOU HAVE BEEN TURNED": PRINT "INTO A TOAD!"
#  1694  FOR Z2 = 1 TO 4:C(Z2) = 3: NEXT Z2: GOTO 1090
#  1695  PRINT "YOU HAVE BEEN TURNED": PRINT "INTO A LIZARD MAN": FOR Y = 0 TO 4:C(Y) =  INT (C(Y) * 2.5): NEXT : GOTO 1090
#  1697  PRINT "BACKFIRE":C(0) = C(0) / 2: GOTO 1090
        elif Qs == "M":
            apple.print("MAGIC AMULET")
            if PW[5] < 1:
                apple.print("NONE OWNED")
                continue
            if PTs == "F":
                Q = int(random.random() * 4 + 1)
            else:
                Q = 0
                while Q >= 1 and Q <= 4:
                    apple.print("1-LADDER-UP    2-LADDER-DN")
                    apple.print("3-KILL         4-BAD??")
                    apple.print("CHOICE ", False)
                    Q = int(apple.get())
                    apple.print(f"{Q}")
                if random.random() > 0.75:
                    apple.print("LAST CHARGE ON THIS AMULET!")
                    PW[5] = PW[5] - 1
            if Q == 1:
                apple.print("LADDER UP")
                DNG[PX][PY] = 8
                return
            elif Q == 2:
                apple.print("LADDER DOWN")
                DNG[PX][PY] = 7
                return
            elif Q == 3:
                apple.print("MAGIC ATTACK")
                DAM = 10 + INOUT
                shoot = True
                break
            elif Q == 4:
                badChance = int(random.random() * 3 + 1)
                if badChance == 1:
                    apple.print("YOU HAVE BEEN TURNED")
                    apple.print("INTO A TOAD!")
                    for Z2 in range(1, 5):
                        C[Z2] = 3
                elif badChance == 2:
                    apple.print("YOU HAVE BEEN TURNED")
                    apple.print("INTO A LIZARD MAN")
                    for Y in range(0, 5):
                        C[Y] = int(C[Y] * 2.5)
                elif badChance == 3:
                    apple.print("BACKFIRE")
                    C[0] = C[0] / 2

                return

#  1656  IF Q$ = "B" AND PT$ = "M" THEN  PRINT "MAGES CAN'T USE BOWS!": GOTO 1650
        if Qs == "B" and PTs == "M":
            apple.print("MAGES CAN'T USE BOWS!")
            continue
#  1657  IF Q$ = "R" AND PT$ = "M" THEN  PRINT "MAGES CAN'T USE RAPIERS!": GOTO 1650
        if Qs == "R" and PTs == "M":
            apple.print("MAGES CAN'T USE RAPIERS!")
            continue
#  1659  IF DAM = 0 THEN  PRINT "HANDS"
        if DAM == 0:
            apple.print("HANDS")

        break
#  1660  IF DAM = 5 OR DAM = 4 THEN 1670
#  1670  IF DAM = 5 THEN  PRINT "TO THROW OR SWING:";: GET Q$: IF Q$ <  > "T" THEN  PRINT "SWING": GOTO 1661
#  1671  IF DAM = 5 THEN  PRINT "THROW":PW(2) = PW(2) - 1
#  1672  FOR Y = 1 TO 5: IF PX + DX * Y < 1 OR PX + DX * Y > 9 OR PY + DY * Y > 9 OR PY + DY * Y < 0 THEN 1662
#  1673 MN = DNG%(PX + DX * Y,PY + DY * Y):MN =  INT (MN / 10): IF MN > 0 THEN 1662
#  1674  NEXT : GOTO 1662
    if DAM == 5 or DAM == 4:
        shoot = True
        if DAM == 5:
            apple.print("TO THROW OR SWING:", False)
            Qs = str.upper(apple.get())
            if Qs != "T":
                apple.print("SWING")
                shoot = False
            else:
                apple.print("THROW")
                PW[2] = PW[2] - 1
    if shoot:
        for Y in range(1, 6):
            if PX + DX * Y < 1 or PX + DX * Y > 9 or PY + DY * Y > 9 or PY + DY * Y < 0:
                break
            MN = DNG[PX + DX * Y][PY + DY * Y]
            MN = int(MN / 10)
            if MN > 0:
                break
#  1661 MN = DN%(PX + DX,PY + DY) / 10:MN =  INT (MN)
    else:
        MN = DNG[PX + DX][PY + DY] / 10; MN =  int(MN)
#  1662  IF MN < 1 OR C(2) -  RND (1) * 25 < MN + INOUT THEN  PRINT "YOU MISSED": GOTO 1668
    if MN < 1 or C[2] - random.random() * 25 < MN + INOUT:
        apple.print("YOU MISSED")
    else:
#  1663  PRINT "HIT!!! ":DAM  ( RND (1) * DAM + C(1) / 5):MZ%(MN,1) = MZ%(MN,1) - DAM
        apple.print("HIT!!!")
        DAM = (random.random() * DAM + C[1] / 5)
        MZ[MN][1] = int(MZ[MN][1] - DAM)
# 1664  PRINT M$(MN);"'S HIT POINTS=";MZ%(MN,1)
        apple.print(f"{Ms[MN]}'S HIT POINTS={MZ[MN][1]}")
#  1665  IF MZ%(MN,1) < 1 THEN  PRINT "THOU HAST KILLED A ";M$(MN): PRINT "THOU SHALT RECEIVE":DA =  INT (MN + IN): PRINT DA;" PIECES OF EIGHT"
        if MZ[MN][1] < 1:
            apple.print(f"THOU HAST KILLED A {Ms[MN]}")
            apple.print("THOU SHALT RECEIVE")
            DA =  int(MN + INOUT)
            apple.print(f"{DA} PIECES OF EIGHT")
#  1666  IF MZ%(MN,1) < 1 THEN C(5) =  INT (C(5) + DA):DNG%(ML%(MN,0),ML%(MN,1)) = DNG%(ML%(MN,0),ML%(MN,1)) - 10 * MN:MZ%(MN,0) = 0
            C[5] = int(C[5] + DA)
            DNG[ML[MN][0]][ML[MN][1]] = DNG[ML[MN][0]][ML[MN][1]] - 10 * MN
            MZ[MN][0] = 0
#  1667 LK = LK +  INT (MN * IN / 2): IF MN = TASK THEN TASK =  - TASK
        LK = LK + int(MN * INOUT / 2)
        if MN == TASK:
            TASK == -TASK

#  1668  IF PA = 1 THEN  PRINT "-CR- TO CONT. ";: INPUT Q$
    if PA == 1:
        apple.input("-CR- TO CONT. ")
#  1669  GOTO 1090


def monsterSetup():
    global PX; global PY
    global MZ; global ML
    global INOUT
    global DNG
    global LP

#  2000 NM = 0: FOR X = 1 TO 10
    NM = 0
    for X in range(1, 11):
#  2005 MZ%(X,0) = 0:MZ%(X,1) = X + 3 + INOUT
        MZ[X][0] = 0; MZ[X][1] = X + 3 + INOUT

#  2010  IF X - 2 > INO OR  RND (1) > .4 THEN 2090
        if X - 2 > INOUT or random.random() > 0.4:
            continue

#  2020 ML%(X,0) =  INT ( RND (1) * 9 + 1):ML%(X,1) =  INT ( RND (1) * 9 + 1)
#  2030  IF DNG%(ML%(X,0),ML%(X,1)) <  > 0 THEN 2020
#  2040  IF ML%(X,0) = PX AND ML%(X,1) = PY THEN 2020
        while True:
            ML[X][0] = int(random.random() * 9 + 1); ML[X][1] = int(random.random() * 9 + 1)
            if not (DNG[ML[X][0]][ML[X][1]] != 0) or not (ML[X][0] == PX and ML[X][1] == PY):
                break

#  2050 DNG%(ML%(X,0),ML%(X,1)) = X * 10
        DNG[ML[X][0]][ML[X][1]] = X * 10
#  2051 MZ%(X,0) = 1
        MZ[X][0] = 1
#  2052 NM = NM + 1
        NM = NM + 1
#  2055 MZ%(X,1) = X * 2 + IN * 2 * LP
        MZ[X][1] = X * 2 + INOUT * 2 * LP
#  2090  NEXT : RETURN 


def monsterAttack(surface, MM):
#  4500  IF MM = 2 OR MM = 7 THEN 4600
#  4509  PRINT "YOU ARE BEING ATTACKED": PRINT "BY A ";M$(MM)
#  4510  IF  RND (1) * 20 -  SGN (PW(3)) - C(3) + MM + IN < 0 THEN  PRINT "MISSED": GOTO 4525
#  4520  PRINT "HIT":C(0) = C(0) -  INT ( RND (1) * MM + IN)
#  4525  IF PA = 1 THEN  PRINT "-CR- TO CONT. ";: INPUT Q$
#  4530  GOTO 4999
#  4600  IF  RND (1) < .5 THEN 4509
#  4610  IF MM = 7 THEN PW(0) =  INT (PW(0) / 2): PRINT "A GREMLIN STOLE SOME FOOD": GOTO 4525
#  4620 ZZ =  INT ( RND (1) * 6): IF PW(ZZ) < 1 THEN 4620
#  4630  PRINT "A THIEF STOLE A ";W$(ZZ):PW(ZZ) = PW(ZZ) - 1: GOTO 4525
    if (MM == 2 or MM == 7) and random.random() >= 0.5:
        if MM == 7:
            PW[0] = int(PW[0] / 2)
            apple.print("A GREMLIN STOLE SOME FOOD")
        else:
            while True:
                ZZ = int(random.random() * 6)
                if not (PW[ZZ] < 1):
                    break
            apple.print(f"A THIEF STOLE A {Ws[ZZ]}")
            PW[ZZ] = PW[ZZ] - 1
    else:
        apple.print("YOU ARE BEING ATTACKED")
        apple.print(f"BY A {Ms[MM]}")
        if random.random() * 20 - apple.sgn(PW[3]) - C[3] + MM + INOUT < 0:
            apple.print("MISSED")
        else:
            apple.print("HIT")
            C[0] = C[0] -  int(random.random() * MM + INOUT)

    if PA == 1:
        apple.input("-CR- TO CONT. ")


def monsters(surface):
    global MZ; global ML
    global PX; global PY
    global DNG
    global INOUT
    global LP

#  4000  FOR MM = 1 TO 10: IF MZ%(MM,0) = 0 THEN 4999
    for MM in range(1, 11):
        if MZ[MM][0] == 0:
            continue
#  4010 RA =  SQR ((PX - ML%(MM,0)) ^ 2 + (PY - ML%(MM,1)) ^ 2)
        RA =  math.sqrt((PX - ML[MM][0]) ** 2 + (PY - ML[MM][1]) ** 2)
#  4011  IF MZ%(MM,1) < IN * LP THEN 4030
#  4020  IF RA < 1.3 THEN 4500
#  4025  IF MM = 8 AND RA < 3 THEN 4999
        if MZ[MM][1] >= INOUT * LP:
            if RA < 1.3:
                monsterAttack(surface, MM)
                continue
            if MM == 8 and RA < 3:
                continue
#  4030 X1 =  SGN (PX - ML%(MM,0)):Y1 =  SGN (PY - ML%(MM,1))
        X1 = apple.sgn(PX - ML[MM][0]); Y1 = apple.sgn(PY - ML[MM][1])
#  4031  IF MZ%(MM,1) < IN * LP THEN X1 =  - X1:Y1 =  - Y1
        if MZ[MM][1] < INOUT * LP:
            X1 = -X1; Y1 = -Y1
#  4035  IF Y1 = 0 THEN 4045
#  4040 D = DNG%(ML%(MM,0),(ML%(MM,1) + Y1 + .5)): IF D = 1 OR D > 9 OR D = 2 THEN 4045
#  4042 X1 = 0: GOTO 4050
#  4045 Y1 = 0: IF X1 = 0 THEN 4050
#  4046 D = DN%((ML%(MM,0) + X1 + .5),ML%(MM,1)): IF D = 1 OR D > 9 OR D = 2 THEN X1 = 0: GOTO 4081
        skipNext = False
        if Y1 != 0:
            D = DNG[ML[MM][0]][int(ML[MM][1] + Y1 + 0.5)]
            if D == 1 or D > 9 or D == 2:
                Y1 = 0
            else:
                X1 = 0
        if X1 != 0:
            D = DNG[int(ML[MM][0] + X1 + 0.5)][ML[MM][1]]
            if (D == 1 or D > 9 or D == 2):
                X1 = 0
                skipNext = True

        if not skipNext:
#  4050 DNG%(ML%(MM,0),ML%(MM,1)) = DNG%(ML%(MM,0),ML%(MM,1)) - 10 * MM
#  4055  IF ML%(MM,0) + X1 = PX AND ML%(MM,1) + Y1 = PY THEN 4999
#  4060 ML%(MM,0) = ML%(MM,0) + X1:ML%(MM,1) = ML%(MM,1) + Y1
#  4080 DNG%(ML%(MM,0),ML%(MM,1)) = (DNG%(ML%(MM,0),ML%(MM,1)) + 10 * MM + .5)
            DNG[ML[MM][0]][ML[MM][1]] = DNG[ML[MM][0]][ML[MM][1]] - 10 * MM
            if ML[MM][0] + X1 == PX and ML[MM][1] + Y1 == PY:
                continue
            ML[MM][0] = ML[MM][0] + X1
            ML[MM][1] = ML[MM][1] + Y1
            DNG[ML[MM][0]][ML[MM][1]] = (DNG[ML[MM][0]][ML[MM][1]] + 10 * MM + .5)
#  4081  IF X1 <  > 0 OR Y1 <  > 0 THEN 4999
        if X1 != 0 or Y1 != 0:
            continue
#  4082  IF MZ%(MM,1) < IN * LP AND RA < 1.3 THEN 4500
        if MZ[MM][1] < INOUT * LP and RA < 1.3:
            monsterAttack(surface, MM)
#  4083  IF MZ%(MM,1) < IN * LP THEN MZ%(MM,1) = MZ%(MM,1) + MM + IN
        if MZ[MM][1] < INOUT * LP:
            MZ[MM][1] = MZ[MM][1] + MM + INOUT
#  4499  GOTO 4999
#  4999  NEXT : RETURN 

def youHaveDied(surface):
    global PNs

    scrollInfo = { "firstLine" : 21, "lastLine": 24, "currentLine": 24 }
#  6000  POKE 33,40: PRINT : PRINT : PRINT "        WE MOURN THE PASSING OF"
    apple.setTextWindowRight(40)
    apple.print(); apple.print(); apple.print("        WE MOURN THE PASSING OF")
#  6005  IF  LEN (PN$) > 22 THEN PN$ = ""
    if len(PNs) > 22:
        PNs = ""
#  6010  IF PN$ = "" THEN PN$ = "THE PEASANT"
    if PNs == "":
        PNs = "THE PEASANT"
#  6020 PN$ = PN$ + " AND HIS COMPUTER"
    PNs = PNs + " AND HIS COMPUTER"
#  6030  HTAB (20 -  INT ( LEN (PN$) / 2)): PRINT PN$
    apple.htab(20 - int(len(PNs) / 2)); apple.print(PNs)
#  6035  PRINT "  TO INVOKE A MIRACLE OF RESSURECTION"
#  6040  PRINT "             <HIT ESC KEY>";
    apple.print("  TO INVOKE A MIRACLE OF RESSURECTION")
    apple.print("             <HIT ESC KEY>", False)
#  6050  IF  PEEK ( - 16384) = 155 THEN 1
    while apple.getKeypress() != 155:
        time.sleep(1)
#  6060  GOTO 6050


def goQuest(surface, y):
    #  7060  PRINT : PRINT "     GO NOW UPON THIS QUEST, AND MAY": PRINT "LADY LUCK BE FAIR UNTO YOU.....": PRINT ".....ALSO I, BRITISH, HAVE INCREASED": PRINT "EACH OF THY ATTRIBUTES BY ONE!"
    apple.print("     GO NOW UPON THIS QUEST, AND MAY")
    apple.print("LADY LUCK BE FAIR UNTO YOU.....")
    apple.print(".....ALSO I, BRITISH, HAVE INCREASED")
    apple.print("EACH OF THY ATTRIBUTES BY ONE!")

#  7070  PRINT : PRINT "         PRESS -SPACE- TO CONT.";: GET Q$: FOR X = 0 TO 5:C(X) = C(X) + 1: NEXT : HOME : GOTO 1090
    apple.print(); apple.print("         PRESS -SPACE- TO CONT.", False)
    apple.get()
    for X in range(0, 6):
        C[X] += 1
    apple.home()
    return


def castle(surface):
    global PNs
    global TASK
    global LP

#  7000  HOME : TEXT : HOME 
#  7001  CALL 62450
    apple.text(); apple.home()
    # CALL 62450

#  7010  IF PN$ <  > "" THEN 7500
    if PNs == "":
#  7020  PRINT : PRINT : PRINT "     WELCOME PEASANT INTO THE HALLS OF": PRINT "THE MIGHTY LORD BRITISH. HEREIN THOU MAYCHOOSE TO DARE BATTLE WITH THE EVIL": PRINT "CREATURES OF THE DEPTHS, FOR GREAT": PRINT "REWARD!"
        apple.print("     WELCOME PEASANT INTO THE HALLS OF")
        apple.print("THE MIGHTY LORD BRITISH. HEREIN THOU MAY")
        apple.print("CHOOSE TO DARE BATTLE WITH THE EVIL")
        apple.print("CREATURES OF THE DEPTHS, FOR GREAT")
        apple.print("REWARD!")

#  7030  PRINT : PRINT "WHAT IS THY NAME PEASANT ";: INPUT PN$
        PNs = apple.input("WHAT IS THY NAME PEASANT ")
#  7040  PRINT "DOEST THOU WISH FOR GRAND ADVENTURE ? ";: GET Q$: IF Q$ <  > "Y" THEN  PRINT : PRINT "THEN LEAVE AND BEGONE!":PN$ = "": PRINT : PRINT "         PRESS -SPACE- TO CONT.";: GET Q$: GOTO 1090
        apple.print("DOEST THOU WISH FOR GRAND ADVENTURE ? ")
        Qs = str.upper(apple.get())
        if Qs != "Y":
            apple.print("THEN LEAVE AND BEGONE!")
            PNs = ""
            apple.print("         PRESS -SPACE- TO CONT.", False)
            apple.get()
            return

#  7045  PRINT 
#  7050  PRINT : PRINT "GOOD! THOU SHALT TRY TO BECOME A ": PRINT "KNIGHT!!!": PRINT : PRINT "THY FIRST TASK IS TO GO INTO THE": PRINT "DUNGEONS AND TO RETURN ONLY AFTER": PRINT "KILLING A(N) ";:TASK =  INT (C(4) / 3): PRINT M$(TASK)
        apple.print("GOOD! THOU SHALT TRY TO BECOME A ")
        apple.print("KNIGHT!!!")
        apple.print("THY FIRST TASK IS TO GO INTO THE")
        apple.print("DUNGEONS AND TO RETURN ONLY AFTER")
        apple.print("KILLING A(N) ", False)
        TASK = int(C[4] / 3)
        apple.print(f"{Ms[TASK]}")

#  7060  PRINT : PRINT "     GO NOW UPON THIS QUEST, AND MAY": PRINT "LADY LUCK BE FAIR UNTO YOU.....": PRINT ".....ALSO I, BRITISH, HAVE INCREASED": PRINT "EACH OF THY ATTRIBUTES BY ONE!"
#  7070  PRINT : PRINT "         PRESS -SPACE- TO CONT.";: GET Q$: FOR X = 0 TO 5:C(X) = C(X) + 1: NEXT : HOME : GOTO 1090
        goQuest(surface, 19)
        return

#  7500  IF TASK > 0 THEN  PRINT : PRINT : PRINT PN$;" WHY HAST THOU RETURNED?": PRINT "THOU MUST KILL A(N) ";M$(TASK): PRINT "GO NOW AND COMPLETE THY QUEST!": PRINT : PRINT "         PRESS -SPACE- TO CONT.";: GET Q$: HOME : GOTO 1090
    if TASK > 0:
        apple.print(f"{PNs} WHY HAST THOU RETURNED?")
        apple.print(f"THOU MUST KILL A(N) {Ms[TASK]}")
        apple.print("GO NOW AND COMPLETE THY QUEST!")
        apple.print("         PRESS -SPACE- TO CONT.", False)
        apple.get()
        apple.home()
        return

#  7510  PRINT : PRINT : PRINT : PRINT "AAHH!!.....";PN$: PRINT : PRINT "THOU HAST ACOMPLISHED THY QUEST!": IF  ABS (TASK) = 10 THEN 7900
    apple.print(f"AAHH!!.....{PNs}")
    apple.print("THOU HAST ACOMPLISHED THY QUEST!")
    if (abs(TASK) != 10):

#  7520  PRINT "UNFORTUNATELY, THIS IS NOT ENOUGH TO": PRINT "BECOME A KNIGHT.":TASK =  ABS (TASK) + 1: PRINT : PRINT "NOW THOU MUST KILL A(N) ";M$(TASK)
        apple.print("UNFORTUNATELY, THIS IS NOT ENOUGH TO")
        apple.print("BECOME A KNIGHT.")
        TASK = abs(TASK) + 1
        apple.print(f"NOW THOU MUST KILL A(N) {Ms[TASK]}")

#  7530  GOTO 7060
        goQuest(surface, 11)

#  7900  TEXT : HOME : PRINT : PRINT : PRINT :PN$ = "LORD " + PN$: PRINT "     ";PN$;","
    else:
        apple.home()
        PNs = "LORD " + PNs
        apple.print(f"     {PNs},")

#  7910  PRINT "       THOU HAST PROVED THYSELF WORTHY": PRINT "OF KNIGHTHOOD, CONTINUE PLAY IF THOU": PRINT "DOTH WISH, BUT THOU HAST ACOMPLISHED": PRINT "THE MAIN OBJECTIVE OF THIS GAME..."
        apple.print("       THOU HAST PROVED THYSELF WORTHY")
        apple.print("OF KNIGHTHOOD, CONTINUE PLAY IF THOU")
        apple.print("DOTH WISH, BUT THOU HAST ACOMPLISHED")
        apple.print("THE MAIN OBJECTIVE OF THIS GAME...")

#  7920  IF LP = 10 THEN 7950
        if LP != 10:

#  7930  PRINT : PRINT "   NOW MAYBE THOU ART FOOLHEARTY": PRINT "ENOUGH TO TRY DIFFICULTY LEVEL ";LP + 1
            apple.print("   NOW MAYBE THOU ART FOOLHEARTY")
            apple.print(f"ENOUGH TO TRY DIFFICULTY LEVEL {LP + 1}")
#  7940  GOTO 7070
        else:

#  7950  PRINT : PRINT "...CALL CALIFORNIA PACIFIC COMPUTER": PRINT "AT (415)-569-9126 TO REPORT THIS": PRINT "AMAZING FEAT!"
            apple.print("...CALL CALIFORNIA PACIFIC COMPUTER")
            apple.print("AT (415)-569-9126 TO REPORT THIS")
            apple.print("AMAZING FEAT!")

#  7990  GOTO 7070
            apple.print("         PRESS -SPACE- TO CONT.")
            apple.get()
            for X in range(0, 6):
                C[X] += 1
            apple.home()
            return


def init():
    global LN
    global LP

# 60000  TEXT : HOME : VTAB (5): INPUT "TYPE THY LUCKY NUMBER.....";Q$:LN =  VAL (Q$)
    apple.text(); apple.home()
    apple.vtab(5); Qs = apple.input("TYPE THY LUCKY NUMBER.....")
    try:
        LN = int(Qs)
    except ValueError:
        LN = 0

# 60005  VTAB (7): INPUT "LEVEL OF PLAY (1-10)......";Q$:LP =  INT ( VAL (Q$))
# 60006  IF LP < 1 OR LP > 10 THEN 60005
    LP = 0
    while LP < 1 or LP > 10:
        apple.vtab(7); Qs = apple.input("LEVEL OF PLAY (1-10)......")
        try:
            LP = int(Qs)
        except ValueError:
            LP = 0

# 60010 ZZ =  RND ( -  ABS (LN))
    ZZ = random.seed(abs(LN))
# 60020  DATA   "HIT POINTS.....","STRENGTH.......","DEXTERITY......","STAMINA........","WISDOM.........","GOLD..........."
# 60025  DIM PW(5)
# 60030  DIM C$(5): FOR X = 0 TO 5: READ C$(X): NEXT 
    global PW
    PW = [ 0.0, 0, 0, 0, 0, 0 ]
    global Cs
    Cs = [ "HIT POINTS.....", "STRENGTH.......", "DEXTERITY......", "STAMINA........", "WISDOM.........", "GOLD..........." ]

# 60040  DIM C(5)
# 60041  DIM M$(10),ML%(10,1),MZ%(10,1)
# 60042  DATA       "SKELETON","THIEF","GIANT RAT","ORC","VIPER","CARRION CRAWLER","GREMLIN","MIMIC","DAEMON","BALROG"
# 60043  FOR X = 1 TO 10: READ M$(X): NEXT 
    global Ms
    Ms = [ "", "SKELETON", "THIEF", "GIANT RAT", "ORC", "VIPER", "CARRION CRAWLER", "GREMLIN", "MIMIC", "DAEMON", "BALROG" ]
    global ML
    ML = [[0] * 2 for i in range(0, 11)]
    global MZ
    MZ = [[0] * 2 for i in range(0, 11)]

# 60050  FOR X = 0 TO 5:C(X) =  INT ( SQR ( RND (1)) * 21 + 4): NEXT X
# 60060  HOME : VTAB (8): FOR X = 0 TO 5: PRINT C$(X),C(X): NEXT : PRINT : PRINT "SHALT THOU PLAY WITH THESE QUALITIES?": HTAB (20): GET Q$: IF Q$ <  > "Y" THEN 60050
    global C
    C = [ 0, 0, 0, 0, 0, 0 ]

    while True:
        apple.home()
        for X in range(0, 6):
            C[X] = int(math.sqrt(random.random()) * 21 + 4)
        apple.vtab(8)
        for X in range(0, 6):
            apple.print(f"{Cs[X]}{C[X]} ")
        apple.print()
        apple.print("SHALT THOU PLAY WITH THESE QUALITIES?")
        Qs = str.upper(apple.get())
        if Qs == "Y":
            break

# 60061  VTAB (15): PRINT : PRINT "AND SHALT THOU BE A FIGHTER OR A MAGE?": HTAB (20): GET PT$
# 60062  IF PT$ = "M" OR PT$ = "F" THEN 60070
# 60063  GOTO 60061
    global PTs
    while True:
        apple.vtab(15); apple.print(); apple.print("AND SHALT THOU BE A FIGHTER OR A MAGE?")
        PTs = str.upper(apple.get())
        if PTs == "M" or PTs == "F":
            break

# 60070  DIM W$(5): DATA    "FOOD","RAPIER","AXE","SHIELD","BOW AND ARROWS","MAGIC AMULET": FOR X = 0 TO 5: READ W$(X): NEXT 
    global Ws
    Ws = [ "FOOD","RAPIER","AXE","SHIELD","BOW AND ARROWS","MAGIC AMULET" ]

# 60075  GOSUB 60080: GOSUB 60200: RETURN 
    stats()
    town()


def stats():
#60080  TEXT : HOME : PRINT : PRINT : PRINT "     STAT'S              WEAPONS": PRINT : FOR X = 0 TO 5: PRINT C$(X);C(X); TAB( 24);"0-";W$(X): NEXT : POKE 34,12: HOME : POKE 35,15
    apple.text(); apple.home()
    apple.print(); apple.print(); apple.print("     STAT'S              WEAPONS"); apple.print()
    for X in range(0, 6):
        apple.print(f"{Cs[X]}{C[X]}", False)
        apple.htab(24); apple.print(f"0-{Ws[X]}")
    apple.setTextWindowTop(12); apple.setTextWindowBottom(15)

#60081  VTAB (11): HTAB (18): PRINT "Q-QUIT"
    apple.vtab(11); apple.htab(18); apple.print("Q-QUIT")

#60082  IF PW(0) > 0 THEN  CALL 62450

#60085  FOR Z = 0 TO 5: VTAB (5 + Z): HTAB (25 -  LEN ( STR$ (PW(Z)))): PRINT PW(Z);: NEXT 
    for Z in range(0, 6):
        apple.vtab(5 + Z)
        apple.htab(25 - len(str(PW[Z])))
        apple.print(f"{PW[Z]}", False)

#60090  VTAB (17): HTAB (5): PRINT "PRICE";: HTAB (15): PRINT "DAMAGE";: HTAB (25): PRINT "ITEM"
    apple.vtab(17); apple.htab(5); apple.print("PRICE", False)
    apple.vtab(17); apple.htab(15); apple.print("DAMAGE", False)
    apple.vtab(17); apple.htab(25); apple.print("ITEM")

#60100  FOR X = 0 TO 5: VTAB (19 + X): HTAB (25): PRINT W$(X): NEXT 
    for X in range(0, 6):
        apple.vtab(19 + X)
        apple.htab(25); apple.print(f"{Ws[X]}", False)

#60110  VTAB (19): HTAB (5): PRINT "1 FOR 10": HTAB (15): PRINT "N/A": VTAB (20): HTAB (5): PRINT "8": HTAB (15): PRINT "1-10": VTAB (21): HTAB (5): PRINT "5": HTAB (15): PRINT "1-5"
    apple.vtab(19); apple.htab(5); apple.print("1 FOR 10")
    apple.vtab(19); apple.htab(15); apple.print("N/A")
    apple.vtab(20); apple.htab(5); apple.print("8")
    apple.vtab(20); apple.htab(15); apple.print("1-10")
    apple.vtab(21); apple.htab(5); apple.print("5")
    apple.vtab(21); apple.htab(15); apple.print("1-5")
#60120  VTAB (22): HTAB (5): PRINT "6": HTAB (15): PRINT "1": VTAB (23): HTAB (5): PRINT "3": HTAB (15): PRINT "1-4": VTAB (24): HTAB (5): PRINT "15": HTAB (15): PRINT "?????": HOME 
    apple.vtab(22); apple.htab(5); apple.print("6")
    apple.vtab(22); apple.htab(15); apple.print("1")
    apple.vtab(23); apple.htab(5); apple.print("3")
    apple.vtab(23); apple.htab(15); apple.print("1-4")
    apple.vtab(24); apple.htab(5); apple.print("15")
    apple.vtab(24); apple.htab(15); apple.print("?????")
#60130  RETURN 


def town():
    # this routine is called with poke 34,12 : poke 35,15 which bounds the scrolling to those lines
    apple.setTextWindowTop(12); apple.setTextWindowBottom(15)

# 60200  HOME : PRINT "WELCOME TO THE ADVENTURE SHOP"
    apple.home()
    apple.print("WELCOME TO THE ADVENTURE SHOP")

    while True:
# 60210  PRINT "WHICH ITEM SHALT THOU BUY ";: GET Q$: IF Q$ = "Q" THEN  PRINT : PRINT "BYE": FOR Z = 1 TO 1000: NEXT : TEXT : HOME : RETURN 
        apple.print("WHICH ITEM SHALT THOU BUY ", False)
        Qs = str.upper(apple.get())
        if Qs == "Q":
            apple.print(); apple.print("BYE")
            apple.render()
            time.sleep(1)
            apple.text(); apple.home()
            break

# 60215 Z =  - 1
        Z = -1
# 60220  IF Q$ = "F" THEN  PRINT "FOOD":Z = 0:P = 1
# 60221  IF Q$ = "R" THEN  PRINT "RAPIER":Z = 1:P = 8
# 60222  IF Q$ = "A" THEN  PRINT "AXE":Z = 2:P = 5
# 60223  IF Q$ = "S" THEN  PRINT "SHIELD":Z = 3:P = 6
# 60224  IF Q$ = "B" THEN  PRINT "BOW":Z = 4:P = 3
# 60225  IF Q$ = "M" THEN  PRINT "AMULET":Z = 5:P = 15
# 60226  IF Z =  - 1 THEN  PRINT Q$: PRINT "I'M SORRY WE DON'T HAVE THAT.": GOTO 60210
        if Qs == "F":
            apple.print("FOOD")
            Z = 0; P = 1
        elif Qs == "R":
            apple.print("RAPIER")
            Z = 1; P = 8
        elif Qs == "A":
            apple.print("AXE")
            Z = 2; P = 5
        elif Qs == "S":
            apple.print("SHIELD")
            Z = 3; P = 6
        elif Qs == "B":
            apple.print("BOW")
            Z = 4; P = 3
        elif Qs == "M":
            apple.print("AMULET")
            Z = 5; P = 15
        else:
            apple.print(Qs)
            apple.print("I'M SORRY WE DON'T HAVE THAT.        ")
            continue

# 60227  IF Q$ = "R" AND PT$ = "M" THEN  PRINT "I'M SORRY MAGES": PRINT "CAN'T USE THAT!": GOTO 60210
# 60228  IF Q$ = "B" AND PT$ = "M" THEN  PRINT "I'M SORRY MAGES": PRINT "CAN'T USE THAT!": GOTO 60210
        if (Qs== "R" and PTs == "M") or (Qs == "B" and PTs == "M"):
            apple.print("I'M SORRY MAGES")
            apple.print("CAN'T USE THAT!")
            continue
# 60230  IF C(5) - P < 0 THEN  PRINT "M'LORD THOU CAN NOT AFFORD THAT ITEM.": GOTO 60210
        if C[5] - P < 0:
            apple.print("M'LORD THOU CAN NOT AFFORD THAT ITEM.")
            continue

# 60235  IF Z = 0 THEN PW(Z) = PW(Z) + 9
        if Z == 0:
            PW[Z] = PW[Z] + 9
# 60236 PW(Z) = PW(Z) + 1:C(5) = C(5) - P
        PW[Z] = PW[Z] + 1
        C[5] = C[5] - P
# 60237  VTAB (10): HTAB (16): PRINT C(5);"  "
        apple.drawText(16, 10, f"{C[5]}  ")
# 60240  VTAB (5 + Z): HTAB (25 -  LEN ( STR$ (PW(Z)))): PRINT PW(Z);: HTAB (1): VTAB (14): PRINT 
        apple.vtab(5 + Z); apple.htab(25 - len(str(PW[Z]))); apple.print(f"{PW[Z]}", False)
        apple.htab(1); apple.vtab(14); apple.print()

    apple.setTextWindowTop(0); apple.setTextWindowBottom(24)
# 60250  GOTO 60210


if __name__ == '__main__':

    # All variables in Apple BASIC begin at 0
    INOUT = 0
    PNs = ""
    PA = 0
    PX = 0; PY = 0
    LK = 0
    TASK = 0


    #  0  ONERR  GOTO 4
    #  1  REM 
    #  4  PR# 0: IN# 0
    #  5  HIMEM: 49151
    #  7  CLEAR : GOSUB 60000    
    init()

    #  8 ZZ =  RND ( -  ABS (LN))
    #  9 LEVEL = 0
    ZZ = random.seed(abs(LN))
    LEVEL = 0

    #  10  TEXT : HOME : NORMAL : VTAB (12): PRINT " WELCOME TO AKALABETH, WORLD OF DOOM!"
    apple.text() ; apple.home(); apple.vtab(12); apple.print(" WELCOME TO AKALABETH, WORLD OF DOOM!")

    #  20  DIM DN%(10,10),TE%(20,20),XX%(10),YY%(10),PER%(10,3),LD%(10,5),CD%(10,3),FT%(10,5),LAD%(10,3)
    DNG = [[0] * 11 for i in range(0, 11)]
    TE = [[0] * 21 for i in range(0, 21)]
    XX = [ 0 ] * 11; YY = [ 0 ] * 11
    PER = [[0] * 4 for i in range(0, 11)]
    LD = [[0] * 6 for i in range(0, 11)]
    CD = [[0] * 4 for i in range(0, 11)]
    FT = [[0] * 6 for i in range(0, 11)]
    LAD = [[0] * 4 for i in range(0, 11)]

    #  30  FOR X = 0 TO 20:TE%(X,0) = 1:TE%(0,X) = 1:TE%(X,20) = 1:TE%(20,X) = 1: NEXT 
    for X in range(0, 21):
        TE[X][0] = 1; TE[0][X] = 1; TE[X][20] = 1; TE[20][X] = 1

    #  35 : VTAB (23): PRINT "  (PLEASE WAIT)";
    apple.vtab(23); apple.print("  (PLEASE WAIT)", False)
    apple.render()

    #  40  FOR X = 1 TO 19: FOR Y = 1 TO 19:TE%(X,Y) =  INT ( RND (1) ^ 5 * 4.5)
    #  41  IF TE%(X,Y) = 3 AND  RND (1) > .5 THEN TE%(X,Y) = 0
    #  42  NEXT : PRINT ".";: NEXT 
    for X in range(1, 20):
        for Y in range(1, 20):
            TE[X][Y] = int(random.random() ** 5 * 4.5)
            if TE[X][Y] == 3 and random.random() > 0.5:
                TE[X][Y] = 0

        apple.print(".", False)
    apple.render()
    time.sleep(1)

    #  50 TE%( INT ( RND (1) * 19 + 1), INT ( RND (1) * 19 + 1)) = 5:TX =  INT ( RND (1) * 19 + 1):TY =  INT ( RND (1) * 19 + 1):TE%(TX,TY) = 3
    TE[int(random.random() * 19 + 1)][int(random.random() * 19 + 1)] = 5
    TX = int(random.random() * 19 + 1)
    TY = int(random.random() * 19 + 1)
    TE[TX][TY] = 3

    #  51 XX%(0) = 139:YY%(0) = 79
    XX[0] = 139; YY[0] = 79

    #  52  FOR X = 2 TO 20 STEP 2:XX%(X / 2) =  INT ( ATN (1 / X) /  ATN (1) * 140 + .5):YY%(X / 2) =  INT (XX%(X / 2) * 4 / 7)
    #  53 PER%(X / 2,0) = 139 - XX%(X / 2):PER%(X / 2,1) = 139 + XX%(X / 2):PER%(X / 2,2) = 79 - YY%(X / 2):PER%(X / 2,3) = 79 + YY%(X / 2): NEXT 
    for X in range(2, 21, 2):
        XX[int(X/2)] = int(math.atan(1 / X) / math.atan(1) * 140 + 0.5)
        YY[int(X/2)] = int(XX[int(X/2)] * 4 / 7)
        PER[int(X / 2)][0] = 139 - XX[int(X / 2)]
        PER[int(X / 2)][1] = 139 + XX[int(X / 2)]
        PER[int(X / 2)][2] = 79 - YY[int(X / 2)]
        PER[int(X / 2)][3] = 79 + YY[int(X / 2)]

    #  54 PER%(0,0) = 0:PER%(0,1) = 279:PER%(0,2) = 0:PE%(0,3) = 159
    PER[0][0] = 0; PER[0][1] = 279; PER[0][2] = 0; PER[0][3] = 159

    #  55  FOR X = 1 TO 10:CD%(X,0) = 139 - XX%(X) / 3:CD%(X,1) = 139 + XX%(X) / 3:CD%(X,2) = 79 - YY%(X) * .7:CD%(X,3) = 79 + YY%(X): NEXT : PRINT ".";
    for X in range(1, 11):
        CD[X][0] = 139 - XX[X] / 3
        CD[X][1] = 139 + XX[X] / 3
        CD[X][2] = 79 - YY[X] * 0.7
        CD[X][3] = 79 + YY[X]
    apple.print(".", False)

    #  56  FOR X = 0 TO 9:LD%(X,0) = (PER%(X,0) * 2 + PER%(X + 1,0)) / 3:LD%(X,1) = (PER%(X,0) + 2 * PER%(X + 1,0)) / 3:W = LD%(X,0) - PE%(X,0)
    #  57 LD%(X,2) = PE%(X,2) + W * 4 / 7:LD%(X,3) = PER%(X,2) + 2 * W * 4 / 7:LD%(X,4) = (PE%(X,3) * 2 + PE%(X + 1,3)) / 3:LD%(X,5) = (PE%(X,3) + 2 * PE%(X + 1,3)) / 3
    #  58 LD%(X,2) = LD%(X,4) - (LD%(X,4) - LD%(X,2)) * .8:LD%(X,3) = LD%(X,5) - (LD%(X,5) - LD%(X,3)) * .8: IF LD%(X,3) = LD%(X,4) THEN LD%(X,3) = LD%(X,3) - 1
    #  59  NEXT 
    for X in range (0, 10):
        LD[X][0] = (PER[X][0] * 2 + PER[X + 1][0]) / 3
        LD[X][1] = (PER[X][0] + 2 * PER[X + 1][0]) / 3
        W = LD[X][0] - PER[X][0]
        LD[X][2] = PER[X][2] + W * 4 / 7
        LD[X][3] = PER[X][2] + 2 * W * 4 / 7
        LD[X][4] = (PER[X][3] * 2 + PER[X + 1][3]) / 3
        LD[X][5] = (PER[X][3] + 2 * PER[X + 1][3]) / 3
        LD[X][2] = LD[X][4] - (LD[X][4] - LD[X][2]) * 0.8
        LD[X][3] = LD[X][5] - (LD[X][5] - LD[X][3]) * 0.8
        if LD[X][3] == LD[X][4]:
            LD[X][3] = LD[X][3] - 1

    #  60  FOR X = 0 TO 9:FT%(X,0) = 139 - XX%(X) / 3:FT%(X,1) = 139 + XX%(X) / 3:FT%(X,2) = 139 - XX%(X + 1) / 3:FT%(X,3) = 139 + XX%(X + 1) / 3
    #  61 FT%(X,4) = 79 + (YY%(X) * 2 + YY%(X + 1)) / 3:FT%(X,5) = 79 + (YY%(X) + 2 * YY%(X + 1)) / 3: NEXT 
    for X in range(0, 10):
        FT[X][0] = 139 - XX[X] / 3
        FT[X][1] = 139 + XX[X] / 3
        FT[X][2] = 139 - XX[X + 1] / 3
        FT[X][3] = 139 + XX[X + 1] / 3
        FT[X][4] = 79 + (YY[X] * 2 + YY[X + 1]) / 3
        FT[X][5] = 79 + (YY[X] + 2 * YY[X + 1]) / 3

    #  62  FOR X = 0 TO 9:LAD%(X,0) = (FT%(X,0) * 2 + FT%(X,1)) / 3:LAD%(X,1) = (FT%(X,0) + 2 * FT%(X,1)) / 3:LAD%(X,3) = FT%(X,4):LAD%(X,2) = 159 - LAD%(X,3): NEXT 
    for X in range(0, 10):
        LAD[X][0] = (FT[X][0] * 2 + FT[X][1]) / 3
        LAD[X][1] = (FT[X][0] + 2 * FT[X][1]) / 3
        LAD[X][3] = FT[X][4]
        LAD[X][2] = 159 - LAD[X][3]

    apple.render()
    time.sleep(1)
    #  68  HOME : HCOLOR= 3
    apple.home(); apple.hcolor(3)
    #  69  POKE 34,20: POKE 33,29: HOME 
    apple.setTextWindowTop(20); apple.setTextWindowRight(29)

    #  70  GOSUB 100: GOTO 1000
    drawMap(apple.gAppleDisplaySurface)
    mainLoop(apple.gAppleDisplaySurface)

    #  90  FOR X = 0 TO 9: FOR Y = 0 TO 5: PRINT LD%(X,Y);" ";: NEXT : PRINT : NEXT : GET Q$
    # This looks like dead code
    for X in range(0, 10):
        for Y in range(0, 6):
            apple.print(f"{LD[X][Y]} ")
            xPos = xPos + 1
            if (xPos > 40):
                xPos = 1
                yPos = yPos + 1
    apple.get()
