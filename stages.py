from emotions import *
from newperson import *

def firstStage(michelle, interlocutor):
    a = (digitize(michelle.employment)/digitize(interlocutor.employment)+digitize(michelle.hobby)/digitize(interlocutor.hobby))/2
    while a > 1:
        a-=1
    incorporation = a * 5
    rejection = a * 6
    patronage = a * 70
    destruction = a * 10
    reproduction = a * 100
    reintegration = a * 190
    orientation = a * 20
    exploration = a * 110
    return {incorporation: 'Incorporation()', rejection: 'Rejection()', patronage: 'Patronage()', destruction: 'Destruction()', reproduction: 'Reproduction()', reintegration: 'Reintegration()', orientation: 'Orientation()', exploration: 'Exploration()'}

def secondStage(michelle, interlocutor, emo1stage):
    a = (digitize(michelle.employment)/digitize(interlocutor.employment)+digitize(michelle.hobby)/digitize(interlocutor.hobby))/2
    while a > 1:
        a-=1
    # level1 = a * 20
    # level2 = a * 10
    level3 = a * 16
    if emo1stage == 'Incorporation()':
        return Delight()
    if emo1stage == 'Rejection()':
        return Disgust()
    if emo1stage == 'Patronage()':
        return Horror()
    if emo1stage == 'Destruction()':
        return Anger()
    if emo1stage == 'Reproduction()':
        return Amazement()
    if emo1stage == 'Reintegration()':
        return Grief()
    if emo1stage == 'Orientation()':
        return Alertness()
    if emo1stage == 'Exploration()':
        return Admiration()
    return

def digitize(str):          #Преобразование кортежа в число
    a = 0
    for y in range(len(str)):
        l=list(str[y])
        for x in l: a+=ord(x)
    return a
