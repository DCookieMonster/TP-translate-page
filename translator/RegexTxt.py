__author__ = 'dor'
import os, sys, re

ReList=[('<br>','\n')]


def RepleceTxt(txt):
    newTxt=txt
    for law in ReList:
        newTxt=newTxt.replace(law[0],law[1])
    return newTxt
