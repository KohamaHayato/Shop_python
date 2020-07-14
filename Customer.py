from ShoppingBag import *

class Customer:
    def __init__(self,customer_name):
        self.__customer_name = customer_name
    
    def set_customer_name(self,customer_name):
        self.__customer_name = customer_name
    
    def get_customer_name(self):
        return self.__customer_name