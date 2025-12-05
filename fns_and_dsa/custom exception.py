
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""
    pass

    

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  
    "grapes": 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except OutOfStockError:
        print( f"Sorry, the item '{item}' is out of stock.")
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception

purchase_item("apple", 3)  # Purchase successful
purchase_item("orange", 1)  # Raises OutOfStockError
purchase_item("watermelon", 1)  # Item not available
purchase_item('coke',5)
print(product_inventory["apple"])