from ShoppingBag import *

class Customer:
    def __init__(self,customer_name):
        self.__customer_name = customer_name

    def create_shopping_bag(self,money):
        self.shopping_bag = ShoppingBag(money)
    
    def print_customer(self):
        print('(Customer) ' + self.__customer_name + 'さんの買い物かご')
        self.shopping_bag.print_shopping_bag()
    
    def query_shop(self,shop):
        print('(Customer) ' + self.__customer_name + '「この店は何店ですか？」')
        shop.print_shop()
    
    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name
    
    def get_customer_name(self):
        return self.__customer_name
    
    customer_name = property(set_customer_name,get_customer_name)