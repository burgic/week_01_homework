# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name


def get_total_cash(pet_shop):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    return pet_shop

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    return pet_shop    

# def get_pets_sold(pet_shop):
#     pet_shop = ["admin"]["pets_sold"]
#     return pet_shop

def get_stock_count(pet_shop):
    stock_count = len(pet_shop["pets"])
    return stock_count

# def get_pets_by_breed(pet_shop):
#     pet = len(pet_shop.get("british shorthair"))
#     return pet_shop

