import logging

logFormat = "%(levelname)s %(asctime)s - %(message)s"

def doneBreak(res, vlFix):
    if res == True and vlFix == False:
        return "Сработала основная защита"
    elif res == False and vlFix == False:
        return "Сработала резервная защита"
    elif vlFix == True and res == False:
        return "Кз самоустроинилось"


def logFile(breaker, Dict, key, placeKz, levelKz, res, vlFix, setting, breakProt, probal, vl, fix, eventKz, iter):
    logging.basicConfig(filename = "logfile.log",
        filemode = "w",
        format = logFormat, 
        level = logging.WARNING)
    logger = logging.getLogger()
    logger.warning("Итерация")
    logger.warning(iter)
    logger.warning("Место короткого замыкания:")
    logger.warning(placeKz)
    logger.warning("Вид короткого замыкания:")
    logger.warning(eventKz)
    logger.warning(Dict[key].object_work(res, vlFix))
    logger.warning(breaker)
    logger.warning(doneBreak(res, vlFix))
    logger.warning("Уставка у рз")
    logger.warning(setting)
    logger.warning("Вероятность поломки:")
    logger.warning(breakProt)
    logger.warning("Вероятность срабатывания по ТЗ:")
    logger.warning(probal)
    if vl == True:
        logger.warning("Самоустронение кз:")
        logger.warning(fix)
    logger.warning("Уровень тока на оборудование")
    logger.warning(levelKz)
    logger.warning("Все нагрузки работают")
    logger.warning("-----------------------------------------------------------------")
