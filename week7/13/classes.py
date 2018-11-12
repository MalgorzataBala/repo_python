# Metody pseud-prywatne

class F(object):
    privv = 123
    def __priv(self):
        print("Priv")
    def jawny(self):
        self.__priv() #wywoluje metode specjalna

f=F() #tworze instancje

f.jawny()
print(f.__dict__)


print(dir(f)) #listuje wszystkie atrybuty i metody, ktore przechowuje nasza klas


class Person(object):
    def __init__(self, fn, ln):
        self.__fn = fn
        self.__ln = ln

    @property
    def fn(self):
            return self.__fn


    @property
    def ln(self):
            return self.__ln

    @property
    def full_name(self):
        return f"{self.__fn} {self.__ln}"


p = Person("Jan", "Kowalski")
print(p.full_name)