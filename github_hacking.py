#!/usr/bin/python
# -----------------------------------------------------------------------------
#                       Ethical Hacking just for fun
#
#                                                           by 0x21@0x21.fr
# -----------------------------------------------------------------------------
import datetime
import os

# The matrix
DATA = ["#     #    #     #####  #    # ### #     #  #####   ", "#     #   # #   #     # #   #   #  ##    # #     #  ","#     #  #   #  #       #  #    #  # #   # #        ","####### #     # #       ###     #  #  #  # #  ####  ","#     # ####### #       #  #    #  #   # # #     #  ","#     # #     # #     # #   #   #  #    ## #     #  ","#     # #     #  #####  #    # ### #     #  #####   "]


DATE_Start = datetime.datetime(2018, 11, 25)
DATE_Now   = datetime.datetime.now()
DELTA = (DATE_Now - DATE_Start).days

# position in the DATA matrix
Y = (DATE_Now.weekday() + 1)%7
X = (DELTA / 7)%52

# Just to modify one file 
F = open("date.txt","w")
F.write(str(DATE_Now))
F.close()

# github commit & push, if the matrix say ok !
if DATA[Y][X] == "#" :

    os.system('/usr/bin/git commit -am "'+ str(DATE_Now) +'"')
    os.system('/usr/bin/git push')


exit(0)
# -----------------------------------------------------------------------------
