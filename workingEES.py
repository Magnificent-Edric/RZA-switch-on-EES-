import randomFunction
import logFile as log

def trKz(trDict, placeKz, eventKz, breakProt, protection, levelKz, iter):
    for key in trDict:
        if key == placeKz:
            breaker = trDict[key].get_break1()
            dataProt = protection[breaker]
            if dataProt['setting'] <= levelKz \
                and breakProt < dataProt['reject_probability']:
                log.logFile(breaker, trDict, key, placeKz, levelKz, True, False, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'], False, 0, eventKz, iter)
            else:
                log.logFile(breaker, trDict, key, placeKz, levelKz, False, False, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'], False, 0, eventKz,  iter)

def busKz(busDict, placeKz, eventKz, breakProt, protection, levelKz, iter):
    for key in busDict:
        if key == placeKz:
            breaker = busDict[key].get_break1()
            dataProt = protection[breaker]
            if dataProt['setting'] <= levelKz \
                and breakProt < dataProt['reject_probability']:
                log.logFile(breaker, busDict, key, placeKz, levelKz, True, False,
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        False, 0, eventKz,  iter)
            else:
                log.logFile(breaker, busDict, key, placeKz, levelKz, False, False,
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        False, 0, eventKz,  iter)

def lineKz(lineDict, placeKz, eventKz, breakProt, protection, levelKz, iter):
    for key in lineDict:
        if key == placeKz:
            breaker = lineDict[key].get_break1()
            dataProt = protection[breaker]
            if dataProt['setting'] <= levelKz \
                and breakProt < dataProt['reject_probability'] \
                    and randomFunction.FixOrNoFixKzVl() < 50:
                log.logFile(breaker, lineDict, key, placeKz, levelKz, True, False, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'], 
                        True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)
            elif dataProt['setting'] <= levelKz \
                and breakProt > dataProt['reject_probability'] \
                    and randomFunction.FixOrNoFixKzVl() > 50:
                        log.logFile(breaker, lineDict, key, placeKz, levelKz, False, True, 
                            dataProt['setting'], breakProt, dataProt['reject_probability'], 
                                True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)
            elif dataProt['setting'] <= levelKz \
                and breakProt > dataProt['reject_probability'] \
                    and 50 < randomFunction.FixOrNoFixKzVl():
                log.logFile(breaker, lineDict, key, placeKz, levelKz, False, False, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)
            elif dataProt['setting'] <= levelKz \
                and breakProt > dataProt['reject_probability'] \
                    and 50 > randomFunction.FixOrNoFixKzVl():
                log.logFile(breaker, lineDict, key, placeKz, levelKz, False, True, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)
            elif dataProt['setting'] >= levelKz \
                and breakProt < dataProt['reject_probability']\
                    and 50 > randomFunction.FixOrNoFixKzVl():
                log.logFile(breaker, lineDict, key, placeKz, levelKz, False, True, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)
            elif dataProt['setting'] >= levelKz \
                and (breakProt < dataProt['reject_probability'] or breakProt > dataProt['reject_probability'])\
                    and 50 < randomFunction.FixOrNoFixKzVl():
                log.logFile(breaker, lineDict, key, placeKz, levelKz, False, False, 
                        dataProt['setting'], breakProt, dataProt['reject_probability'],
                        True, randomFunction.FixOrNoFixKzVl(), eventKz,  iter)

def workingSystem(trDict, lineDict, busDict, protection):
    i = 0
    while i < 15:
        placeKz = randomFunction.randomPlaceKz()
        eventKz = randomFunction.randomKZ(placeKz)
        levelKz = randomFunction.levelKzCurrent(eventKz)
        breakProt = randomFunction.breakProtection()
        trKz(trDict, placeKz, eventKz, breakProt, protection, levelKz, i)
        lineKz(lineDict, placeKz, eventKz, breakProt, protection, levelKz, i)
        busKz(busDict, placeKz, eventKz, breakProt, protection, levelKz, i) 
        i += 1