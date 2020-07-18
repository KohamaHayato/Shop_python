from Goods import *

class Shop:
    def __init__(self,shop_name,tel_no):
        self.shop_name = shop_name
        self.tel_no = tel_no

    def create_goods(self,goods_name,price):
        self.goods = Goods(goods_name,price)

    def print_shop(self):
        print('(Shop) ' + self.shop_name + 'TEL:' + self.tel_no)
        self.goods.print_goods()

    '''
    def set_shop_name(self,shop_name):
        self.shop_name = shop_name
    
    def get_shop_name(self):
        return self.shop_name
    
    def set_tel_no(self,tel_no):
        self.tel_no = tel_no
    
    def get_tel_no(self):
        return self.tel_no
    
    shop_name = property(set_shop_name,get_shop_name)

    tel_no = property(set_tel_no,get_tel_no)
    '''
