from Shop import *
from Goods import *
from ShoppingBag import *

class Shop2(Shop):
    def __init__(self,shop_name,tel_no):
        super().__init__(shop_name,tel_no)
        self.__goods_list = []

    def add_goods(self,goods_name,tel_no):
        self.__goods = Goods(goods_name,tel_no)
        self.__goods_list.append(self.__goods)
    
    def print_shop(self):
        #print('(Shop2) ' + self.shop_name + 'です。 ' + 'TEL:' + self.tel_no)
        for goods in self.__goods_list:
            goods.print_goods()
    
    def sale_goods(self,goods_name,shopping_bag):
        for goods in self.__goods_list:
            if(goods_name == goods.get_goods_name()):
                if(shopping_bag.get_money() > goods.get_price()):
                    charge = shopping_bag.get_money() - goods.get_price()
                    shopping_bag.set_money(charge)
                    shopping_bag.set_goods(goods)
                    print('  (Shop2) まいどあり！　おつりは' + str(charge) + 'です。')
                else :
                    print('  (Shop2) お金がたりません。')
                
            else :
                print('  (Shop2) ' + goods_name + 'は取り扱っていません。')
                