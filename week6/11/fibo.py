class Fib:
    def __init__(self,n):
        self.a = 0
        self.b = 1
        self.max = n
    def __iter__(self): # robi nam obiekt iterowalny
        return self
    def __next__(self): # kazda petla w pythonie konczy sie iterowalnym wyjatkiem
        while self.a <= self.max:
            t = self.a
            self.a = self.b
            self.b +=t
            return self.a
        raise StopIteration()
   # def __enter__(self): metoda do tworzenia contestmanagra (metoda with)
#f = Fib(10)
for i in Fib(10):
    print(i)