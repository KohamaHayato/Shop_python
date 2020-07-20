from Shop import *

class Shop2(Shop):
    def __init__(self,shop_name,tel_no):
        super().__init__(shop_name,tel_no)
        self.__goods_list = []

    def add_goods(self,goods_name,tel_no):
        self.__goods = Goods(goods_name,tel_no)
        self.__goods_list.append(self.__goods)
    
    def print_shop(self):
        #print('(Shop2) ' + self.shop_name + 'です。 ' + 'TEL:' + self.tel_no)
        for i in range(len(self.__goods_list)):
            self.goods.print_goods()
    
    def sale_goods(self,goods_name,shopping_bag):
        for goods in len(self.__goods_list):
            if(goods.find(goods_name)):
                super.set_goods(goods)
                super.sale_goods(goods_name,shopping_bag)
            else :
                super.set_goods(goods_name)
                super.sale_goods(goods_name,shopping_bag)