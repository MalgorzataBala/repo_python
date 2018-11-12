class Person(object):
    def __init__(self, fn, ln):
        self._fn = fn
        self.__ln = ln

    @property #to jest getter
    def fn(self):
        return self._fn

    @fn.setter
    def fn(self, val): #nie bedzie nadpisane mimo, ze nazywaja sie tak samo
        print("Ktos probuje zaktualizowac wartosc!")
        self._fn = val  #setter przyjmuje jeden argument - wartosc która nadajemy i mozemy zaktualizowac prywatny atrybut
    @fn.deleter
    def fn(self):
        print('deleter')
        self._fn = None

    """" @property
 def ln(self):
     return self.__ln   """

    @property
    def ln(self):
        return f"{self._fn} {self.__ln}"

    @ln.setter
    def ln(self, new_name):
        print('zmiana imienia')
        self.__ln= new_name

    @ln.deleter
    def ln(self):
        self.__ln = ""



p = Person("Jan", "Kowalski")
print(p.fn)
del p.fn
print(p.fn) # nie daje nam errora jak usuwamy atrybut
print("*******bawie sie full_name**********")
print(p.ln)
p.ln = "xx"
print(p.ln)
del p.ln
print(p.ln)