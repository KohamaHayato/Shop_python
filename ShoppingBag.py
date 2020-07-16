class ShoppingBag:
    def __init__(self,money):
        self.money = money
    
    def print_shopping_bag(self,goods):
        print('　(ShoppingBag) 限度額' + str(self.money) + '円')
        if goods.get_goods_name() == None:
            print('商品は入っていません。')
        else :
            goods.print_goods()

    def set_money(self,money):
        self.money = money
    
    def get_money(self):
        return self.money
    
    money = property(set_money,get_money)