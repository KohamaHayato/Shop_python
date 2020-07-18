from Goods import *

class ShoppingBag:
    def __init__(self,money = 0):
        self.__money = money
    
    def print_shopping_bag(self):
        goods = Goods() #初期化しているので商品が入っていないことになる
        print('　(ShoppingBag) 限度額' + str(self.__money) + '円')
        if goods.get_goods_name() == 'なし':
            print('　(ShoppingBag) 商品は入っていません。')
        else :
            goods.print_goods()

    def set_money(self,money):
        self.__money = money
    
    def get_money(self):
        return self.__money
    
    money = property(set_money,get_money)