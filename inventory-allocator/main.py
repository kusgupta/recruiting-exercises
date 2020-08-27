# Checks if a single warehouse contains sufficient quantity of all items
def check_if_contains_all(items, warehouses):
    output = {}
    for warehouse in warehouses:
        name = warehouse['name']
        inventory = warehouse['inventory']
        for item, amount in items.items():
            if item in warehouse['inventory'] and inventory[item] >= amount:
                output[item] = [(name, amount)]
                inventory[item] -= amount
            else:
                output = {}
                break
        if output:
            return output


# Creates dict for each warehouse and associated items
def create_dicts(unformatted_output):
    dict_output = {}
    for item, warehouses in unformatted_output.items():
        for warehouse in warehouses:
            warehouse_name = warehouse[0]
            quantity = warehouse[1]
            if warehouse_name not in dict_output:
                dict_output[warehouse_name] = {item: quantity}
            else:
                dict_output[warehouse_name][item] = quantity
    return dict_output


# Allocates inventory for given items, returns empty list if not possible to complete all of order
def allocate_inventory(items, warehouses):
    # Unformatted output looks like {item: [(warehouse1, quantity), (warehouse2, quanitity)...]}
    unformatted_output = check_if_contains_all(items, warehouses) or {}
    if not unformatted_output:
        for item, amount in items.items():
            unformatted_output[item] = []
            # tracks the remaining amount needed to fulfill order
            remainder = amount
            for warehouse in warehouses:
                name = warehouse['name']
                inventory = warehouse['inventory']
                if item in warehouse['inventory']:
                    if inventory[item] >= amount:
                        unformatted_output[item] = [(name, amount)]
                        inventory[item] -= amount
                        remainder = 0
                        # So that current warehouse isn't overwritten by a more pricey one later
                        break
                    elif inventory[item] >= remainder:
                        inventory[item] -= remainder
                        unformatted_output[item].append((name, remainder))
                        remainder = 0
                    else:
                        remainder -= inventory[item]
                        inventory[item] = 0
                        unformatted_output[item].append((name, remainder))
            if remainder != 0:
                return []

    dict_output = create_dicts(unformatted_output)
    # List comprehension that puts the current dictionaries into a list
    return [{warehouse_name: inventory} for warehouse_name, inventory in dict_output.items()]
