import unittest
from main import allocate_inventory
class TestInventoryAllocator(unittest.TestCase):

    def test_one_item(self):
        inp = ({'apple' : 1}, [{'name' : 'owd', 'inventory': {'apple' : 1}}])
        out = allocate_inventory(inp)
        expected = [{'owd' : {'apple' : 1}}]
        self.assertEqual(out, expected, "Allocates correctly for one item in one warehouse")
    
    def test_one_item_multiple_warehouses(self):
        inp = ({'apple' : 10}, [{'name' : 'owd', 'inventory': {'apple' : 5}}, {'name': 'dm', 'inventory': {'apple': 5}}])
        out = allocate_inventory(inp)
        expected = [{'dm' : {'apple' : 5}}, {'owd' : {'apple': 5}}]
        self.assertEqual(out, expected, "Allocates correctly for one item in multiple warehouses")

    def test_multiple_items_one_warehouse(self):
        inp = ({'apple' : 5, 'banana': 5}, [{'name' : 'owd', 'inventory': {'apple' : 5, 'banana': 10}}, {'name': 'dm', 'inventory': {'apple': 5, 'banana': 10}}])
        out = allocate_inventory(inp)
        expected = [{'owd' : {'apple' : 5, 'banana': 5}}]
        self.assertEqual(out, expected, "Allocates correctly for multiple items in one warehouse")

    def test_multiple_items_in_multiple_warehouse(self):
        inp = ({'apple' : 5, 'banana': 5}, [{'name' : 'owd', 'inventory': {'apple' : 5, 'banana': 3}}, {'name': 'dm', 'inventory': {'apple': 5, 'banana': 10}}])
        out = allocate_inventory(inp)
        expected = [{'owd' : {'apple' : 5, 'banana': 3}, 'dm' : {'banana': 2}}]
        self.assertEqual(out, expected, "Allocates correctly for multiple items in one warehouse")
    
    def test_not_enough_of_an_item(self):
        inp = ({'apple' : 5, 'banana': 14}, [{'name' : 'owd', 'inventory': {'apple' : 5, 'banana': 3}}, {'name': 'dm', 'inventory': {'apple': 5, 'banana': 10}}])
        out = allocate_inventory(inp)
        expected = []
        self.assertEqual(out, expected, "Returns empty list when the items aren't available")

    def test_prioritize_single_warehouse(self):
        inp = ({'apple' : 5, 'banana': 14}, [{'name' : 'owd', 'inventory': {'apple' : 5, 'banana': 3}}, {'name': 'dm', 'inventory': {'apple': 5, 'banana': 12}}, {'name': 'm&m', 'inventory': {'apple': 5, 'banana': 14}}])
        out = allocate_inventory(inp)
        expected = [{'m&m' : {'apple' : 5, 'banana': 14}}]
        self.assertEqual(out, expected, "Returns empty list when the items aren't available")