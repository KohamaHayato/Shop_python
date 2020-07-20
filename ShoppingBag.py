from Goods import *

class ShoppingBag:
    def __init__(self,money = 0):
        self.__money = money
        self.__goods = Goods()

    def print_shopping_bag(self):
        print('  (ShoppingBag) 限度額' + str(self.__money) + '円')
        if self.__goods == None:
            print('  (ShoppingBag) 商品は入っていません。')
        else :
            self.__goods.print_goods()

    def set_money(self,money):
        self.__money = money
    
    def get_money(self):
        return self.__money
    
    def set_goods(self,goods):
        self.__goods = goods
    
    def get_goods(self):
        return self.__goods

    money = property(set_money,get_money)

    goods = property(set_goods,get_goods)