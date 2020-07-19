from Goods import *
from ShoppingBag import *

class Shop:
    def __init__(self,shop_name,tel_no):
        self.__shop_name = shop_name
        self.__tel_no = tel_no

    def create_goods(self,goods_name,price):
        self.goods = Goods(goods_name,price)

    def print_shop(self):
        print('(Shop) ' + self.__shop_name + 'TEL:' + self.__tel_no)
        self.goods.print_goods()
    
    def sale_goods(self,goods_name,shopping_bag):
        if(self.goods.get_goods_name() == goods_name):
            if(shopping_bag.get_money() > self.goods.get_price()):
                charge = shopping_bag.get_money() - self.goods.get_price()
                shopping_bag.set_money(charge)
                shopping_bag.set_goods(self.goods)
                print('まいどあり！ おつりは' + str(charge) + '円です。')
            else :
                print('お金が足りません。')
        else :
            print(goods_name + 'は取り扱っていません。申し訳ありません。')

    def set_shop_name(self,shop_name):
        self.__shop_name = shop_name
    
    def get_shop_name(self):
        return self.__shop_name
    
    def set_tel_no(self,tel_no):
        self.__tel_no = tel_no
    
    def get_tel_no(self):
        return self.__tel_no
    
    shop_name = property(set_shop_name,get_shop_name)

    tel_no = property(set_tel_no,get_tel_no)