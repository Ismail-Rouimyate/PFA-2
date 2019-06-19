import os
import numpy as np
import cv2
import pyarabic
from openpyxl import load_workbook

class DataProvider():
    "this class creates machine-written text for a word list. TODO: change getNext() to return your samples."
    
            



    

    def __init__(self, wordList, imageList):
        
        self.wordList = wordList
        self.idx = 0
        self.imageList = imageList

    def hasNext(self):
        return self.idx < len(self.wordList)

    def getNext(self):
        
        img = cv2.imread(self.imageList[self.idx],0)    
        word = self.wordList[self.idx]
        self.idx += 1
        return (word, img)


def createIAMCompatibleDataset(dataProvider):
    "this function converts the passed dataset to an IAM compatible dataset"

    # create files and directories
    f = open('words.txt', 'w+')
    if not os.path.exists('sub'):
        os.makedirs('sub')
    if not os.path.exists('sub/sub-sub'):
        os.makedirs('sub/sub-sub')

    # go through data and convert it to IAM format
    ctr = 0
    while dataProvider.hasNext():
        sample = dataProvider.getNext()

        # write img
        cv2.imwrite('sub/sub-sub-%d.png'%ctr, sample[1])

        # write filename, dummy-values and text
        line = 'sub-sub-%d'%ctr + ' X X X X X X X ' + sample[0] + '\n'
        f.write(line)

        ctr += 1


if __name__ == '__main__':
    words = []
    filename = "separated-test.txt"
    file = open(filename,"r")
    content = file.readlines()
    for i in content :
        words.append(i[24:])
    file.close()
    images = []
    filename = "separated-test.txt"
    file = open(filename,"r")
    content = file.readlines()
    for i in content :
        images.append(i[0:22])
    file.close()
    dataProvider = DataProvider(words,images)
    createIAMCompatibleDataset(dataProvider)