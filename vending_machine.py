from enum import Enum, StrEnum, auto
from collections import defaultdict
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
    
    def __repr__(self):
        return str(self)


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
product_list.append(Product("Snickers", 20, ProductType.SNACK))
product_list.append(Product("Snickers", 20, ProductType.SNACK))
product_list.append(Product("Snickers", 20, ProductType.SNACK))

product_list.append(Product("Coca Cola", 35, ProductType.DRINK))
product_list.append(Product("Coca Cola", 35, ProductType.DRINK))
product_list.append(Product("Coca Cola", 35, ProductType.DRINK))

print(sort_products(product_list))
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
