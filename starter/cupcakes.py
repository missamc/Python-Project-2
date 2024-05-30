# from pprint import pprint

# import csv




# def read_csv(file):
#     with open("sample.csv") as csvfile:
#         reader = csv.DictReader(csvfile)

#         for row in reader:
#             pprint(row)

# read_csv("sample.csv")

# def write_new_csv(file, cupcakes):
#     with open(file, "w", newline "\n") as csvfile:
#         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        
#         writer.writeheader()

#         if hasattr(cupcake, "filling"):
#             cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
#             cupcake1.add_sprinkles("Red", "White", "Blue")
#             cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
#             cupcake2.add_sprinkles("Oreo pieces")
#             cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

#             cupcake_list = [
#                 cupcake1,
#                 cupcake2,
#                 cupcake3
#             ]

# def write_new_csv(file, cupcakes):
#     with open(file, "w", newline= "\n") as csvfile:
#         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.header()

#         for cupcake in cupcakes:
#             if hasattr(cupcake, "filling"):
#                 writer.writenow({"size": cupcake.size, "name":cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles":cupcake.sprinkles})
#             else:
#                 writer.writerow({"size": cupcake.size, "name":cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles":cupcake.sprinkles})

# write_new_csv("sample.csv", cupcake_list)


# def _add_cupcake(file, cupcake):
#     with open(file, "a", newline= "\n") as csvfile:
#         fieldnames = ["size", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         if hasattr(cupcake, "filling"):
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
#         else:
#             writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})





# from abc import ABC, abstractmethod


# class Cupcake(ABC):
#     size = "regular"
#     def __init__(self, name, price, flavor, frosting, filling):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.filling = filling
#         self.sprinkles = []

#     def add_sprinkles(self, *args):
#             for sprinkle in args:
#                 self.sprinkles.append(sprinkle)
#     def calculate_price(self, quantity):
#         return quantity * self.price


# class Mini(Cupcake):
#     size = "mini"
#     def __init__(self, name, price, flavor, frosting):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.sprinkles = []




# my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")
# print(my_cupcake_mini.name)
# print(my_cupcake_mini.price)
# print(my_cupcake_mini.size)

# my_cupcake = Cupcake("Cookies and Cream", 2.99, "Strawberry", "Birthday Cake", "Vanilla")

# my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

# print(my_cupcake.sprinkles)

# my_cupcake.frosting = "Chocolate"
# my_cupcake.filling = "Guava"
# my_cupcake.name = "Cute Cupcake"

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)

import csv

from pprint import pprint



with open("sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
         pprint(row)


def read_csv (file):
     with open(file) as csvfile:
          reader = csv.DictReader(csvfile)

          for row in reader:
               pprint(row)

read_csv("sample.csv")




def write_new_csv(file, cupcakes):
     with open(file, "w", newline = "\n") as csvfile:
          fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
          writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

          writer.writeheader()

          for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

# write_new_csv("sample.csv", cupcake_list)


def add_another_cupcake(file, cupcake):
     with open(file, "a", newline="\n") as csvfile:
          fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

         
          if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
          else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})





from abc import ABC, abstractmethod

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
            for sprinkle in args:
                 self.sprinkles.append(sprinkle)
                 return self.sprinkles

#     @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price


my_cupcake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")

my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

print(my_cupcake.sprinkles)

my_cupcake.frosting = "Chocolate"
my_cupcake.filling = "Chocolate"
my_cupcake.name = "Triple Chocolate"

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)


class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")

print(my_cupcake_mini.name)
print(my_cupcake_mini.price)
print(my_cupcake_mini.size)  


cute_cupcake1 = Cupcake("Stars and Hearts", 2.99, "Vanilla", "Strawberry", "Ganache")
cute_cupcake1.add_sprinkles("Purple", "Pink", "Blue")
cute_cupcake2 = Mini("Heath Bar", .99, "Chocolate", "Reeses")
cute_cupcake2.add_sprinkles("White Chocolate Chips")
# cute_cupcake3 = Large("Red Velvet", 3.99, "Vanilla", "Cream Cheese", None)

cupcake_list = [
     cute_cupcake1,
     cute_cupcake2,
     # cute_cupcake3
]







def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)




def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader