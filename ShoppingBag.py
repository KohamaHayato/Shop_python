from Goods import *

class ShoppingBag:
    goods = Goods()
    def __init__(self,money,goods):
        self.__money = money
    
    def print_shopping_bag(self):
        print('　(ShoppingBag) 限度額' + self.__money + '円')
        if goods.get_goods_name() == null:
            print('商品は入っていません。')
        else :
            goods.print_goods()

    def set_money(self,money):
        self.money = money
    
    def get_money(self):
        return self.__money