import ApplesoftBASIC as apple


if __name__ == '__main__':

# 1 TEXT:HOME:NORMAL:VTAB( 5): HTAB (9): PRINT "WELCOME,  FOOLISH MORTAL": VTAB (7): HTAB (14): PRINT "INTO THE WORLD": VTAB (9): HTAB (16) : INVERSE : PRINT "AKALABETH!": NORMAL
    apple.text(); apple.home()
    apple.vtab(5); apple.htab(9); apple.print("WELCOME,  FOOLISH MORTAL")
    apple.vtab(7); apple.htab(14); apple.print("INTO THE WORLD")
    apple.vtab(9); apple.htab(16); apple.inverse(); apple.print("AKALABETH!"); apple.normal()
# 2 VTAB (11): HTAB (7): PRINT "HEREIN THOU SHALT FIND GRAND" : VTAB (13): HTAB (16): INVERSE : PRINT "ADVENTURE!": NORMAL
    apple.vtab(11); apple.htab(7); apple.print("HEREIN THOU SHALT FIND GRAND")
    apple.vtab(13); apple.htab(16); apple.inverse(); apple.print("ADVENTURE!"); apple.normal()
# 3 VTAB (16): PRINT "        CREATED BY  LORD BRITISH": PRINT : PRINT "(C) 1980 BY CALIFORNIA PACIFIC COMPUTER"
    apple.vtab(16); apple.print("        CREATED BY  LORD BRITISH")
    apple.print(); apple.print("(C) 1980 BY CALIFORNIA PACIFIC COMPUTER")
# 4 VTAB (21): HTAB (10): PRINT "INSTRUCTIONS (Y/N) ?";: GET Q$: PRINT Q$: VTAB (23): HTAB (8): PRINT "(PRESS SPACE TO CONTINUE) ";: GET R$: PRINT : IF Q$ = "N" THEN 8998
    apple.vtab(21); apple.htab(10); apple.print("INSTRUCTIONS (Y/N) ?", False)
    Qs = str.upper(apple.get())
    apple.print(Qs)
    apple.vtab(23); apple.htab(8); apple.print("(PRESS SPACE TO CONTINUE) ", False)

    Rs = str.upper(apple.get()); apple.print()
    if Qs != "N":
# 5 PRINT "BLOAD AKA4"
# 6 POKE 254,32: POKE 255,32: POKE 32840,169: POKE 32841,0: CALL 32768: POKE 32840,177: POKE 32841,8
# 7 PRINT "BLOADAKA2,A$2000": POKE - 16302,0: POKE - 16297,0: POKE - 16300,0: POKE - 16304,0
# 8 PRINT "BLOADAKA5,A$4000" 9 CALL 32768
# 10 PRINT "BLOADAKA3,A$4000"
# 11 POKE 32769,39: POKE 32888,136: POKE 32890,255: CALL 3276 8: POKE 32769,0: POKE 32888, 200: POKE 32890,40
# 12 FOR O7 = 1 TO 4000 : NEXT O7
# 13 POKE 32840,169: POKE 32841,0 : CALL 32768: POKE 32840,177: POKE 32641,8
# 14 FOR O7 = 1 TO 500 : NEXT O7
# 8000 HOME : TEXT : HOME
        apple.home()
# 8010 PRINT : PRINT : PRINT "     MANY, MANY, MANY YEARS AGO THE": PRINT "DARK LORD MONDAIN, ARCHFOE OF BRITISH,": PRINT "TRAVERSED THE LANDS OF AKALABETH": PRINT "SPREADING EVIL AND DEATH AS HE PASSED."
        apple.print(); apple.print();
        apple.print("     MANY, MANY, MANY YEARS AGO THE")
        apple.print("DARK LORD MONDAIN, ARCHFOE OF BRITISH,")
        apple.print("TRAVERSED THE LANDS OF AKALABETH")
        apple.print("SPREADING EVIL AND DEATH AS HE PASSED.")
# 8020 PRINT "BY THE TIME MONDAIN WAS DRIVEN FROM THE": PRINT "LAND BY BRITISH, BEARER OF THE WHITE": PRINT "LIGHT, HE HAD DONE MUCH DAMAGE UNTO"
        apple.print("BY THE TIME MONDAIN WAS DRIVEN FROM THE")
        apple.print("LAND BY BRITISH, BEARER OF THE WHITE")
        apple.print("LIGHT, HE HAD DONE MUCH DAMAGE UNTO")
# 8030 PRINT "THE LANDS.": PRINT: PRINT "'TIS THY DUTY TO HELP RID AKALABETH OF": PRINT "THE FOUL BEASTS WHICH INFEST IT,": PRINT "WHILE TRYING TO STAY ALIVE!!!": PRINT : PRINT : PRINT "       (PRESS SPACE TO CONTINUE)";: GET Q$
        apple.print("THE LANDS.")
        apple.print(); apple.print("'TIS THY DUTY TO HELP RID AKALABETH OF")
        apple.print("THE FOUL BEASTS WHICH INFEST IT,")
        apple.print("WHILE TRYING TO STAY ALIVE!!!")
        apple.print(); apple.print(); apple.print("       (PRESS SPACE TO CONTINUE)", False)
        apple.get()

# 8100 HOME : VTAB (2): HTAB (12) : PRINT "THE PLAYER STAT'S:"
        apple.home()
        apple.vtab(2); apple.htab(12); apple.print("THE PLAYER STAT'S:")
# 8105 PRINT : PRINT : PRINT : PRINT "HIT POINTS- AMOUNT OF DAMAGE A PLAYER": HTAB (13): PRINT "CAN ABSORB BEFORE DEATH"
        apple.print(); apple.print(); apple.print()
        apple.print("HIT POINTS- AMOUNT OF DAMAGE A PLAYER")
        apple.htab(13); apple.print("CAN ABSORB BEFORE DEATH")
# 8110 PRINT : PRINT "STRENGTH--- RELATED TO DAMAGE INFLICTED ": HTAB (13): PRINT "BY PLAYER AGAINST MONSTERS."
        apple.print(); apple.print("STRENGTH--- RELATED TO DAMAGE INFLICTED ")
        apple.htab(13); apple.print("BY PLAYER AGAINST MONSTERS.")
# 8120 PRINT : PRINT "DEXTERITY-- RELATED TO THE PROBABILITY" : HTAB (13): PRINT "OF A PLAYER HITTING A MONST."
        apple.print(); apple.print("DEXTERITY-- RELATED TO THE PROBABILITY")
        apple.htab(13); apple.print("OF A PLAYER HITTING A MONST.")
# 8130 PRINT "STAMINA---- RELATED TO PLAYER DEFENSE": HTAB (1 3): PRINT "AGAINST MONSTERS"
        apple.print("STAMINA---- RELATED TO PLAYER DEFENSE")
        apple.htab(13); apple.print("AGAINST MONSTERS")
# 8140 PRINT : PRINT "WISDOM----- THIS ATTRIBUTE IS USED": HTAB(13): PRINT "IN SPECIAL (QUEST!) ROUTINES"
        apple.print(); apple.print("WISDOM----- THIS ATTRIBUTE IS USED")
        apple.htab(13); apple.print("IN SPECIAL (QUEST!) ROUTINES")
# 8150 PRINT "GOLD------- MONEY!! CASH!! ASSETS!!"
        apple.print("GOLD------- MONEY!! CASH!! ASSETS!!")
# 8160 PRINT : PRINT : HTAB (8): PRINT "(PRESS SPACE TO CONTINUE)";: GET Q$
        apple.print(); apple.print()
        apple.htab(8); apple.print("(PRESS SPACE TO CONTINUE)", False); apple.get()

# 8200 HOME : PRINT : PRINT "       THE TOWNS AND BUYING ITEMS:"
        apple.home(); apple.print()
        apple.print("       THE TOWNS AND BUYING ITEMS:")
# 8210 PRINT : PRINT : PRINT "     TO BUY ANY ITEM ONE NEED ONLY": PRINT "TYPE THE FIRST LETTER OF THE ITEM"
        apple.print(); apple.print();
        apple.print("     TO BUY ANY ITEM ONE NEED ONLY")
        apple.print("TYPE THE FIRST LETTER OF THE ITEM")
# 8220 PRINT "WANTED. THE COST OF THE RESPECTIVE": PRINT "ITEMS IS DISPLAYED WHILE IN THE TOWN."
        apple.print("WANTED. THE COST OF THE RESPECTIVE")
        apple.print("ITEMS IS DISPLAYED WHILE IN THE TOWN.")
# 8230 PRINT "THE GAME IS STARTED IN A TOWN SOMEWHERE": PRINT "ON THE 20X20 MAP."
        apple.print("THE GAME IS STARTED IN A TOWN SOMEWHERE")
        apple.print("ON THE 20X20 MAP.")
# 8240 PRINT : PRINT : HTAB (12): PRINT "FIGHTERS AND MAGI"
        apple.print(); apple.print()
        apple.htab(12); apple.print("FIGHTERS AND MAGI")
# 8250 PRINT : PRINT "     THE DISADVANTAGE OF BEING A": PRINT "FIGHTER IS THE LACK OF THE ABILITY TO": PRINT "CONTROL THE MAGIC AMULET, WHEREAS MAGI": PRINT "CAN NOT USE RAPIERS OR BOWS."
        apple.print()
        apple.print("     THE DISADVANTAGE OF BEING A")
        apple.print("FIGHTER IS THE LACK OF THE ABILITY TO")
        apple.print("CONTROL THE MAGIC AMULET, WHEREAS MAGI")
        apple.print("CAN NOT USE RAPIERS OR BOWS.")
# 8270 PRINT : PRINT : HTAB (8): PRINT "(PRESS SPACE TO CONTINUE)";: GET Q$
        apple.print(); apple.print()
        apple.htab(8); apple.print("(PRESS SPACE TO CONTINUE)", False); apple.get()

# 8300 HOME : PRINT : PRINT : HTAB (16): PRINT "MOVEMENT:"
        apple.home(); apple.print(); apple.print()
        apple.htab(16); apple.print("MOVEMENT:")
# 8310 PRINT : PRINT : PRINT "-KEY-";: HTAB (10): PRINT "OUTDOORS";: HTAB (24): PRINT "DUNGEON"
        apple.print(); apple.print(); apple.print("-KEY-", False)
        apple.htab(10); apple.print("OUTDOORS", False)
        apple.htab(24); apple.print("DUNGEON")
# 8320 PRINT : PRINT "  CR     MOVE NORTH    MOVE FORWARD": PRINT "  <=     MOVE WEST     TURN LEFT": PRINT"  =>     MOVE EAST     TURN RIGHT"
        apple.print(); apple.print("  CR     MOVE NORTH    MOVE FORWARD")
        apple.print("  <=     MOVE WEST     TURN LEFT")
        apple.print("  =>     MOVE EAST     TURN RIGHT")
# 8330 PRINT "  /      MOVE SOUTH    TURN AROUND": PRINT "  S      STATISTICS    STATISTICS": PRINT "  A      N/A           ATTACK    ": PRINT "  P      PAUSE ON/OFF  PAUSE ON/OFF"
        apple.print("  /      MOVE SOUTH    TURN AROUND")
        apple.print("  S      STATISTICS    STATISTICS")
        apple.print("  A      N/A           ATTACK    ")
        apple.print("  P      PAUSE ON/OFF  PAUSE ON/OFF")
# 8335 PRINT "  X      GO INTO TOWN  CLIMB LADDER": PRINT "  X      GO CASTLE     GO HOLE     ": PRINT "SPACE    PASS          PASS        "
        apple.print("  X      GO INTO TOWN  CLIMB LADDER")
        apple.print("  X      GO CASTLE     GO HOLE     ")
        apple.print("SPACE    PASS          PASS        ")
# 8350 PRINT : PRINT : HTAB (8): PRINT "(PRESS SPACE TO CONTINUE)";: GET Q$
        apple.print(); apple.print()
        apple.htab(8); apple.print("(PRESS SPACE TO CONTINUE)", False); apple.get()

# 8400 HOME : VTAB (5): PRINT "     THOU DOEST NOW KNOW THE BASICS OF": PRINT : PRINT "THE GAME, EXPERIMENT WITH THE COMMANDS."
        apple.home()
        apple.vtab(5); apple.print("     THOU DOEST NOW KNOW THE BASICS OF")
        apple.print(); apple.print("THE GAME, EXPERIMENT WITH THE COMMANDS.")
# 8410 PRINT : PRINT "THERE IS MUCH THAT IS LEFT UNSAID FOR": PRINT : PRINT "THEE TO DISCOVER IN THE FUTURE..."
        apple.print(); apple.print("THERE IS MUCH THAT IS LEFT UNSAID FOR")
        apple.print(); apple.print("THEE TO DISCOVER IN THE FUTURE...")
# 8420 PRINT : PRINT : PRINT "     GO NOW UNTO THE WORLD AND SEEK": PRINT : PRINT "ADVENTURE WHERE THOU MIGHT!!!"
        apple.print(); apple.print(); apple.print("     GO NOW UNTO THE WORLD AND SEEK")
        apple.print(); apple.print("ADVENTURE WHERE THOU MIGHT!!!")
# 8430 PRINT : PRINT : PRINT "P.S.-SEARCH OUT THE CASTLE OF": PRINT "LORD BRITISH, USE THE -X- KEY TO GO IN!"
        apple.print(); apple.print(); apple.print("P.S.-SEARCH OUT THE CASTLE OF")
        apple.print("LORD BRITISH, USE THE -X- KEY TO GO IN!")
# 8450 PRINT : PRINT : HTAB (8): PRINT "(PRESS SPACE TO CONTINUE)";: GET Q$
        apple.print(); apple.print()
        apple.htab(8); apple.print("(PRESS SPACE TO CONTINUE)", False); apple.get()
# 8997 PRINT
# 8998 POKE 33,1: POKE 34,23
# 8999 PRINT "RUN AKA1"
