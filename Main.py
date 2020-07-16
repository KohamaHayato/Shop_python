from Shop import *
from Customer import *
from Goods import *
from ShoppingBag import *

tokyo = Shop('東京店','03-1234-5678')
goods = Goods('海洋深層水',1200)
shopping_bag = ShoppingBag(1000)
yamada = Customer('山田')

tokyo.print_shop(goods)
yamada.print_customer(shopping_bag)
yamada.query_shop(tokyo)
