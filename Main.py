from Shop import *
from Customer import *

tokyo = Shop('東京店','03-1234-5678')
tokyo.create_goods("海洋深層水",1200)
yamada = Customer("山田")
yamada.create_shopping_bag(1000)

yamada.print_customer()
yamada.query_shop(tokyo)
