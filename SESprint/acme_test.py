import unittest
import random
from acme import Product
from acme_report import generateProduct

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_product_weight_default(self):
        #test default product weight being 20
        prod = Product('Test Product')
        self.assertEqual(prod.weight,20)


class AcmeReportTests(unittest.TestCase):
    def test_num_product_default(self):
        #test default product number being 30
        num = len(generateProduct)
        self.assertEqual(num,30)

    #def are_name_legal(self):
    #    adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    #    noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', 'Candy']
    #    select_adj = random.choice(adj)
    #    select_noun = random.choice(noun)
    #    test_name = select_adj + ' ' + select_noun
    #    self.assertMultiLineEqual(test_name,)

if __name__ == '__main__':
    unittest.main()