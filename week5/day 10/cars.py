
class Cars(object):
    def __init__(self, user_mark, user_model, user_colour, silnik, prod_date = 2018):
        self.mark = user_mark
        self.model = user_model
        self.colour = user_colour
        self.silnik= silnik

    def production_date(self, prod_year):
        self.prod_date = prod_year

    def turn_on(self):
        print("Włączony!")

car1 = Cars("Volvo","V60","Black metalic", "silnik")
print(car1.mark, car1.model, car1.colour)
car1.turn_on()
car1.production_date(2018)
#print('Data produkcji: ', car1.prod_date):