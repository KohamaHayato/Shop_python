from Goods import *

class Shop:
    def __init__(self,shop_name,tel_no):
        self.__shop_name = shop_name
        self.__tel_no = tel_no

    def create_goods(self,goods_name,price):
        self.__goods = Goods(goods_name,price)    

    def print_shop(self):
        print('(Shop) ' + self.__shop_name + 'TEL?' + self.__tel_no)
        self.__goods.print_goods()

    def set_shop_name(self,shop_name):
        self.__shop_name = shop_name
    
    def get_shop_name(self):
        return self.__shop_name
    
    def set_tel_no(self,tel_no):
        self.__tel_no = tel_no
    
    def get_tel_no(self):
        return self.__tel_no
    
    goods_name = property(set_shop_name,get_shop_name)

    price = property(set_tel_no,get_tel_no)
