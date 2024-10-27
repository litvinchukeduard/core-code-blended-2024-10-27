from enum import Enum, StrEnum, auto
from collections import defaultdict, UserDict
'''
Створити структуру класів, яка буде керувати апаратом для продуктів
'''

'''
Product: name, price, type (snack, drink)
'''

# types_list = ["drink", "snack"]
class ProductType(StrEnum):
    DRINK = auto()
    SNACK = auto()

class Product:

    def __init__(self, name: str, price: int, product_type: ProductType):
        self.name = name
        self.price = price
        self.product_type = product_type

    def __str__(self):
        return f'Product(name={self.name}, price={self.price}, product_type={self.product_type})'
    
    # def __eq__(self, value):
    #     return self.price == value.price
        
    
    def __repr__(self):
        return str(self)


class VendingMachine(UserDict):
    
    def __init__(self, product_list: list[Product], money: int):
        products = sort_products(product_list)

        self.__money = None
        self.money = money

        super().__init__(products)

    @property
    def money(self):
        raise Exception("Access to money restricted")
    
    @money.setter
    def money(self, new_value):
        if type(new_value) != int:
            raise TypeError("Money should be an int")
        if new_value < 0:
            raise ValueError("Money should be greater than or equals to zero")
        self.__money = new_value

    def find_product(self, name: str, product_type: ProductType):
        products_for_type = self.data[product_type]
        for product in products_for_type:
            if product.name == name:    
                return product

    def buy_product(self, name: str, product_type: ProductType, money_amount: int):
        product = self.find_product(name, product_type)
        change_amount = money_amount - product.price
        if self.__money < change_amount:
            raise ValueError("Not enough money in the machine")
        
        self.__money -= change_amount
        return (product, change_amount)
        

"""
{
    ProductType.SNACK: ['Snickers', 'Mars'],
    ProductType.DRINK: ['Coca Cola', 'Sprite']
}
"""
def sort_products(product_list: list[Product]):
    result_dict = defaultdict(list)

    for product in product_list:
        result_dict[product.product_type].append(product)
        
        # for product_type in ProductType:
        #     if product.product_type == product_type:
        #         result_dict[product_type].append(product)


    # for product in product_list:
    #     if product.product_type == ProductType.SNACK:
    #         result_dict[ProductType.SNACK].append(product)
    #     elif product.product_type == ProductType.DRINK:
    #         result_dict[ProductType.DRINK].append(product)
    
    return result_dict

product_list = []

# for product_type in ProductType:
#     print(product_type.name)
product_list.append(Product("Snickers", 20, ProductType.SNACK))
product_list.append(Product("Mars", 20, ProductType.SNACK))
product_list.append(Product("Bounty", 20, ProductType.SNACK))
product_list.append(Product("Snickers", 20, ProductType.SNACK))

product_list.append(Product("Coca Cola", 35, ProductType.DRINK))
product_list.append(Product("Coca Cola", 35, ProductType.DRINK))
product_list.append(Product("Coca Cola", 35, ProductType.DRINK))

# print(sort_products(product_list))

machine = VendingMachine(product_list, 10000)

print(machine.buy_product("Snickers", ProductType.SNACK, 50))

print(machine._VendingMachine__money)
# print(machine.data[ProductType.SNACK])

# print(dir(machine))
# print(machine._VendingMachine__money)
# machine.money = -10000

# machine.money += 1000

# print(machine.money)

# print(machine.data)

# print(machine[ProductType.SNACK])
# print(machine.products)
# product_two = Product("Snickers", 30, "snack")
# product = Product("Snickers", 20, "snacc")
# product_two = Product("Snickers", 30, "snack")
# print(product.price)
# print(product_two.price)

# print(ProductType.DRINK.value)
# print(ProductType.SNACK.value)

# my_dict = dict()
# my_default_dict = defaultdict(str)

# my_default_dict['hello'] += "world!"
# print(my_default_dict)

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# my_list.remove(3)
# print(my_list)

# print(Product("Coca Cola", 35, ProductType.DRINK) == Product("Coca Cola", 35, ProductType.DRINK))

# my_list = [Product("Coca Cola", 35, ProductType.DRINK), Product("Snickers", 20, ProductType.SNACK)]
# for product in my_list:
#     if product.name == 'Snickers':
#         my_list.remove(product)

# print(my_list)