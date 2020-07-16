class Goods:
    def __init__(self,goods_name,price):
        self.goods_name = goods_name                                  
        self.price = price

    def print_goods(self):
        print(' (Goods) ' + self.goods_name + ' ' + str(self.price) + '?')

    def set_goods_name(self,goods_name):
        self.goods_name = goods_name
    
    def get_goods_name(self):
        return self.goods_name
    
    def set_price(self,price):
        self.price = price
    
    def get_price(self):
        return self.price
    
    goods_name = property(set_goods_name,get_goods_name)

    price = property(set_price,get_price)