from Shop2 import *
from Customer import *

tokyo = Shop2('東京店','03-1234-5678')
tokyo.add_goods('海洋深層水',1200)
tokyo.add_goods('ビタミンABC',350)
tokyo.add_goods('天然黒酢',890)
tokyo.add_goods('アガリクス',2000)
tokyo.add_goods('アロエはちみつ',650)

tokyo.print_shop()

yamada = Customer('山田')
yamada.create_shopping_bag(1000)

yamada.print_customer()

yamada.buy_goods(tokyo,'海洋深層水')
yamada.buy_goods(tokyo,'青汁一杯')

yamada.buy_goods(tokyo,'青汁一杯')

yamada.print_customer()
