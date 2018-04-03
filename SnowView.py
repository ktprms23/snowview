##############################
#
# The Snow and SnowMan, and Tree
# Author: David Wu, CQTC
# Version: 201412120942 v1.0
#############################
import random
import os
import threading


class Snowthread(threading.Thread):

    # constructor with one parameter
    def __init__(self, event):
        threading.Thread.__init__(self)
        # set the stopped event
        self.stopped = event
        # the max X and Y for View
        self.maxX = 25
        self.maxY = 30

        # generate a array and set the value ' '
        # array [][]outerList = new array[maxX][maxY]
        self.outerList = [[' ' for m in range(self.maxY)] for n in range(self.maxX)]
        self.outerList[1][1] = '*'
        self.outerList[3][1] = '*'
        self.outerList[5][6] = '*'
        self.outerList[7][2] = '*'
        self.outerList[4][5] = '*'
        
        self.createSnowMan()
        self.createTree()
        os.system('cls')
        self.printView()


    def createTree(self):
        self.viewReplaceSnowChecking(self.maxX - 1, self.maxY - 9, '|')
        self.viewReplaceSnowChecking(self.maxX - 1, self.maxY - 8, '_')
        self.viewReplaceSnowChecking(self.maxX - 1, self.maxY - 7, '_')
        self.viewReplaceSnowChecking(self.maxX - 1, self.maxY - 6, '_')
        self.viewReplaceSnowChecking(self.maxX - 1, self.maxY - 5, '|')
        self.viewReplaceSnowChecking(self.maxX - 2, self.maxY - 9, '|')
        self.viewReplaceSnowChecking(self.maxX - 2, self.maxY - 5, '|')
        self.viewReplaceSnowChecking(self.maxX - 3, self.maxY - 9, '|')
        self.viewReplaceSnowChecking(self.maxX - 3, self.maxY - 5, '|')
        self.viewReplaceSnowChecking(self.maxX - 4, self.maxY - 9, '|')
        self.viewReplaceSnowChecking(self.maxX - 4, self.maxY - 5, '|')
        self.viewReplaceSnowChecking(self.maxX - 5, self.maxY - 9, '|')
        self.viewReplaceSnowChecking(self.maxX - 5, self.maxY - 5, '|')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 13, '/')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 5, '\\')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 12, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 11, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 10, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 4, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 3, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 2, '_')
        self.viewReplaceSnowChecking(self.maxX - 6, self.maxY - 1, '\\')
        self.viewReplaceSnowChecking(self.maxX - 7, self.maxY - 12, '/')
        self.viewReplaceSnowChecking(self.maxX - 7, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 7, self.maxY - 5, '\\')
        self.viewReplaceSnowChecking(self.maxX - 7, self.maxY - 2, '\\')
        self.viewReplaceSnowChecking(self.maxX - 8, self.maxY - 11, '/')
        self.viewReplaceSnowChecking(self.maxX - 8, self.maxY - 7, '\\')
        self.viewReplaceSnowChecking(self.maxX - 8, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 8, self.maxY - 3, '\\')
        self.viewReplaceSnowChecking(self.maxX - 9, self.maxY - 10, '/')
        self.viewReplaceSnowChecking(self.maxX - 9, self.maxY - 8, '\\')
        self.viewReplaceSnowChecking(self.maxX - 9, self.maxY - 7, '\\')
        self.viewReplaceSnowChecking(self.maxX - 9, self.maxY - 4, '\\')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 14, '/')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 8, '/')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 7, '/')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 13, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 12, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 11, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 4, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 3, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 2, '_')
        self.viewReplaceSnowChecking(self.maxX - 10, self.maxY - 1, '\\')
        self.viewReplaceSnowChecking(self.maxX - 11, self.maxY - 13, '/')
        self.viewReplaceSnowChecking(self.maxX - 11, self.maxY - 8, '/')
        self.viewReplaceSnowChecking(self.maxX - 11, self.maxY - 7, '/')
        self.viewReplaceSnowChecking(self.maxX - 11, self.maxY - 2, '\\')
        self.viewReplaceSnowChecking(self.maxX - 12, self.maxY - 12, '/')
        self.viewReplaceSnowChecking(self.maxX - 12, self.maxY - 7, '/')
        self.viewReplaceSnowChecking(self.maxX - 12, self.maxY - 6, '/')
        self.viewReplaceSnowChecking(self.maxX - 12, self.maxY - 3, '\\')
        self.viewReplaceSnowChecking(self.maxX - 13, self.maxY - 11, '/')
        self.viewReplaceSnowChecking(self.maxX - 13, self.maxY - 6, '/')
        self.viewReplaceSnowChecking(self.maxX - 13, self.maxY - 5, '/')
        self.viewReplaceSnowChecking(self.maxX - 13, self.maxY - 4, '\\')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 13, '/')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 5, '\\')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 12, '_')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 11, '_')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 4, '_')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 3, '_')
        self.viewReplaceSnowChecking(self.maxX - 14, self.maxY - 2, '\\')
        self.viewReplaceSnowChecking(self.maxX - 15, self.maxY - 12, '/')
        self.viewReplaceSnowChecking(self.maxX - 15, self.maxY - 7, '\\')
        self.viewReplaceSnowChecking(self.maxX - 15, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 15, self.maxY - 3, '\\')
        self.viewReplaceSnowChecking(self.maxX - 16, self.maxY - 11, '/')
        self.viewReplaceSnowChecking(self.maxX - 16, self.maxY - 8, '\\')
        self.viewReplaceSnowChecking(self.maxX - 16, self.maxY - 7, '\\')
        self.viewReplaceSnowChecking(self.maxX - 16, self.maxY - 4, '\\')
        self.viewReplaceSnowChecking(self.maxX - 17, self.maxY - 10, '/')
        self.viewReplaceSnowChecking(self.maxX - 17, self.maxY - 9, '\\')
        self.viewReplaceSnowChecking(self.maxX - 17, self.maxY - 8, '\\')
        self.viewReplaceSnowChecking(self.maxX - 17, self.maxY - 5, '\\')
        self.viewReplaceSnowChecking(self.maxX - 18, self.maxY - 9, '/')
        self.viewReplaceSnowChecking(self.maxX - 18, self.maxY - 6, '\\')
        self.viewReplaceSnowChecking(self.maxX - 18, self.maxY - 7, '|')
        self.viewReplaceSnowChecking(self.maxX - 18, self.maxY - 8, '|')
        self.viewReplaceSnowChecking(self.maxX - 19, self.maxY - 7, '|')
        self.viewReplaceSnowChecking(self.maxX - 19, self.maxY - 8, '|')

    def createSnowMan(self):
        self.viewReplaceSnowChecking(self.maxX - 17, 3, '#')
        self.viewReplaceSnowChecking(self.maxX - 17, 4, '#')
        self.viewReplaceSnowChecking(self.maxX - 17, 5, '#')
        self.viewReplaceSnowChecking(self.maxX - 16, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 16, 6, '#')
        self.viewReplaceSnowChecking(self.maxX - 15, 1, '#')
        self.viewReplaceSnowChecking(self.maxX - 15, 7, '#')
        self.viewReplaceSnowChecking(self.maxX - 14, 1, '#')
        self.viewReplaceSnowChecking(self.maxX - 14, 7, '#')
        self.viewReplaceSnowChecking(self.maxX - 13, 1, '#')
        self.viewReplaceSnowChecking(self.maxX - 13, 7, '#')
        self.viewReplaceSnowChecking(self.maxX - 12, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 12, 6, '#')
        self.viewReplaceSnowChecking(self.maxX - 11, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 11, 3, '#')
        self.viewReplaceSnowChecking(self.maxX - 11, 4, '#')
        self.viewReplaceSnowChecking(self.maxX - 11, 5, '#')
        self.viewReplaceSnowChecking(self.maxX - 11, 6, '#')
        self.viewReplaceSnowChecking(self.maxX - 10, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 10, 3, '#')
        self.viewReplaceSnowChecking(self.maxX - 10, 4, '#')
        self.viewReplaceSnowChecking(self.maxX - 10, 5, '#')
        self.viewReplaceSnowChecking(self.maxX - 10, 6, '#')
        self.viewReplaceSnowChecking(self.maxX - 9, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 9, 6, '#')
        self.viewReplaceSnowChecking(self.maxX - 8, 1, '#')
        self.viewReplaceSnowChecking(self.maxX - 8, 7, '#')
        self.viewReplaceSnowChecking(self.maxX - 7, 0, '#')
        self.viewReplaceSnowChecking(self.maxX - 7, 8, '#')
        self.viewReplaceSnowChecking(self.maxX - 6, 0, '#')
        self.viewReplaceSnowChecking(self.maxX - 6, 8, '#')
        self.viewReplaceSnowChecking(self.maxX - 5, 0, '#')
        self.viewReplaceSnowChecking(self.maxX - 5, 8, '#')
        self.viewReplaceSnowChecking(self.maxX - 4, 0, '#')
        self.viewReplaceSnowChecking(self.maxX - 4, 8, '#')
        self.viewReplaceSnowChecking(self.maxX - 3, 0, '#')
        self.viewReplaceSnowChecking(self.maxX - 3, 8, '#')
        self.viewReplaceSnowChecking(self.maxX - 2, 1, '#')
        self.viewReplaceSnowChecking(self.maxX - 2, 7, '#')
        self.viewReplaceSnowChecking(self.maxX - 1, 2, '#')
        self.viewReplaceSnowChecking(self.maxX - 1, 3, '#')
        self.viewReplaceSnowChecking(self.maxX - 1, 4, '#')
        self.viewReplaceSnowChecking(self.maxX - 1, 5, '#')
        self.viewReplaceSnowChecking(self.maxX - 1, 6, '#')

        self.viewReplaceSnowChecking(self.maxX - 14, 3, '@')
        self.viewReplaceSnowChecking(self.maxX - 14, 5, '@')

        self.viewReplaceSnowChecking(self.maxX - 8, 8, '/')
        self.viewReplaceSnowChecking(self.maxX - 8, 9, '/')
        self.viewReplaceSnowChecking(self.maxX - 9, 9, '/')
        self.viewReplaceSnowChecking(self.maxX - 9, 10, '/')
        self.viewReplaceSnowChecking(self.maxX - 10, 10, '/')
        self.viewReplaceSnowChecking(self.maxX - 10, 11, '/')
        self.viewReplaceSnowChecking(self.maxX - 11, 10, '\\')
#        self.outerList[self.maxX - 11][12] = '_'
        self.viewReplaceSnowChecking(self.maxX - 11, 12, '/')
        self.viewReplaceSnowChecking(self.maxX - 12, 10, '/')
        self.viewReplaceSnowChecking(self.maxX - 12, 12, '\\')
        self.viewReplaceSnowChecking(self.maxX - 13, 11, '_')
#        self.outerList[self.maxX - 13][12] = '_'

    def viewReplaceSnowChecking(self, x, y, r):
        # snow will cover the view, and after that the view must recover again
        if self.outerList[x][y] == ' ':
            self.outerList[x][y] = r

    # generate snow from the top
    def generateSnow(self):
        # range(0, x) -> [0, 1, ..., x-1]
        for outIndex in range(0, self.maxY):
            # randint(0, 5) -> generate random integer from [0, 1, 2, 3, 4, 5]
            r = random.randint(0, 5)
            if r == 0:
                self.outerList[0][outIndex] = '*'

    # decide the direction of snow down
    def snowDown(self):
        # range( x, y, z ) -> [ x, x + z, x + z + z, ...., y - z ]
        for outIndex in range(self.maxX - 1, -1, -1):
            for inIndex in range(self.maxY - 1, -1, -1):
                # check the index has snow and not at bottom
                if self.outerList[outIndex][inIndex] == '*' and outIndex != (self.maxX - 1):
                    r = random.randint(0, 4)
                    if r == 0 or r == 3 or r == 4:
                        #if self.outerList[outIndex + 1][inIndex] == ' ':
                        self.outerList[outIndex + 1][inIndex] = '*'
                        self.outerList[outIndex][inIndex] = ' '
                        #else:
                        #    self.outerList[outIndex][inIndex] = ' '
                    # down right
                    elif r == 1:
                        #if inIndex != (self.maxY - 1) and self.outerList[outIndex + 1][inIndex + 1] == ' ':
                        if inIndex != (self.maxY - 1):
                            self.outerList[outIndex + 1][inIndex + 1] = '*'
                            self.outerList[outIndex][inIndex] = ' '
                        #else:
                         #   self.outerList[outIndex][inIndex] = ' '
                    # down left
                    elif r == 2:
                        #if inIndex != 0 and self.outerList[outIndex + 1][inIndex - 1] == ' ':
                        if inIndex != 0:
                            self.outerList[outIndex + 1][inIndex - 1] = '*'
                            self.outerList[outIndex][inIndex] = ' '
                        #else:
                         #   self.outerList[outIndex][inIndex] = ' '
    def run(self):
        #repeatC = 0
        while not self.stopped.wait(1):

            # snow down
            self.snowDown()
                    
            # generate snow
            self.generateSnow()

            # regenerate snowman and tree
            self.createSnowMan()
            self.createTree()

            # clean the screen
            os.system('cls')
            self.printView()
            #repeatC = repeatC + 1


    def printView(self):
        for outIndex in range(self.maxX):
            for inIndex in range(self.maxY):
                print self.outerList[outIndex][inIndex],
            print
        print
            

# ------------------------------------
# --------- main ---------------------

# create a event flag for thread stopped
stopFlag = threading.Event()
# create a thread with one parameter
thread = Snowthread(stopFlag)
thread.start()
# wait for user to click enter -> scanf in C
raw_input()
# set the stop event to stop the thread
stopFlag.set()
# wait for user to click enter -> scanf in C
raw_input()
