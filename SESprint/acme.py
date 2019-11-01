"""This class describe the products"""
from random import randint


class Product:
    # name,price(int),weight(int), and flammability(float))
    def __init__(self, name, price=10.00, weight=20, flammability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        # calculate price / weight
        test = self.price / self.weight
        # if product ratio is less than .5
        # else if product is greater than or equal to .5
        # else
        if test < .5:
            print('Not so stealable...')
        elif test >= .5:
            print('kind of stealable')
        else:
            print('very stealable')

    def explode(self):
        # calculate boom
        boom = self.flammability * self.weight
        # if boom is greater than 10
        if boom < 10:
            print('...fizzle')
        elif (boom >= 10) & (boom <= 50):
            print('...boom!')
        else:
            print('...BABOOM!!')

class BoxingGlove(Product):

    def __init__(self, name, price=10.00, weight=10, flammability=.5):
        super().__init__(name,price,weight,flammability)

    def explode(self):
        #print explode for BoxingGlove
        print('... it is a glove')

    def punch(self):
        #if weight < 5, then it tickles.
        #if weight (5,15), then Hey that hurts
        #if 15> infinite, ouch
        if self.weight < 5:
            print('that tickles')
        elif (self.weight >= 5) & (self.weight <= 5):
            print('Hey that hurts!')
        else :
            print('OUCH!')