import classSources.abcClass as abcClass

class Transfomator(abcClass.Object):
    def __init__(self, name, cVolt, number, breaker1):
        self._break1 = breaker1
        super().__init__(name, cVolt, number)

    def get_break1(self):
        return self._break1

    def set_break1(self, breaker):
        self._break1 = breaker

    def object_work(self, res, vlFix):
        if res == True:
            return ['Трансформатор отключен, сработала осн. защита', self._number]
        elif res == False:
            return ["Трансформатор работает, сработала резервная защита", self._number]

class LineTransport(Transfomator):
    def object_work(self, res, vlFix):
        if res == True and vlFix == False:
            return ['Линия отключена, сработала основная защита', self._number]
        elif vlFix == True and res == False:
            return ['Линия работает, кз самоусроинилось', self._number]
        elif vlFix == False and res == False:
            return ["Линия не работает, сработала резервная защита", self._number]

class Bus(Transfomator):
    def object_work(self, res, vlFix):
        if res == True:
            return ['Шина отключена, сработала основная защита', self._number]
        else:
            return ['Шина отключена, сработала резервная защита', self._number]

class Breaker(abcClass.Object):
    def object_work(self, res, vlFix):
        if res == False:
            return ['Выключатель работает', self._number]
        else:
            return ['Выключатель не работает', self._number]
