"""
Generate a list of products then summaries
"""
from random import choice
from random import randint
from random import uniform
from acme import Product
from random import sample


def generateProduct(num_products=30):
#generate a number of products,
#then return a list of products
    products = []
    while num_products>0:
        num_products = num_products-1

        # generate price and weight from 5-100, and flammability from 0.0-2.5
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = round(uniform(0.0, 2.5),2)

        # pick a random word from Adj, and a random from noun, then concatecate Adj + noun
        adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', 'Candy']
        random_name = choice(adj)+ " " + choice(noun)

        #generate name
        x = Product('random_name',price,weight,flammability)
        products.append(x)
        #print out the name
        #print(random_name, weight, price, flammability)
    return products


def inventory_report(products):
    '''orunt a summary of given list of products'''
    mean_price = sum(Product.price for Product in products)/len(products)
    mean_weight = sum(Product.weight for Product in products)/len(products)
    mean_flammability = sum(Product.flammability for Product in products) / len(products)
    return print('unique sample', 30, '. the average price is ', round(mean_price,2), '. average weight is', round(mean_weight,2), '. average flammability is', round(mean_flammability,2))

if __name__=='__main__':
    inventory_report(generateProduct())