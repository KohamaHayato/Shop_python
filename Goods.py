class Goods:
    def __init__(self,goods_name='??',price=0):
        self.__goods_name = goods_name                                  
        self.__price = price

    def print_goods(self):
        print('?(Goods) ' + self.__goods_name + ' ' + str(self.__price) + '円')

    def set_goods_name(self,goods_name):
        self.__goods_name = goods_name
    
    def get_goods_name(self):
        return self.__goods_name
    
    def set_price(self,price):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_goods(self,goods):
        self.__goods = goods
    
    def get_goods(self):
        return self.__goods
    
    goods_name = property(set_goods_name,get_goods_name)

    price = property(set_price,get_price)

    goods = property(set_goods,get_goods)