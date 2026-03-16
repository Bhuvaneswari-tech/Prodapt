#1. Create a list of product list
inventory = ["Laptop", "Mouse", "Keyboard"]
print("Initial Inventory:", inventory)

# 2. append() - adds an item to the end of the list
inventory.append("Monitor")
print(inventory) # ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

# 3. insert() - adds an item at a specific index
inventory.insert(1, "Printer")
print(inventory) # ['Laptop', 'Printer', 'Mouse', 'Keyboard', 'Monitor']

#4. Combine Products from Another Warehouse (extend())
new_inventory = ["Webcam", "Headset"]
inventory.extend(new_inventory)
print(inventory) # ['Laptop', 'Printer', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headset']

#5. Remove Discontinued Product (remove())
inventory.remove("Mouse")
print(inventory) # ['Laptop', 'Printer', 'Keyboard', 'Monitor', 'Webcam', 'Headset']

#6. Process Shipped Product (pop())
shipped_product = inventory.pop(2) # removes 'Keyboard'
print("Shipped Product:", shipped_product) # Keyboard

#7.Count Product Occurrence (count())
inventory.append("Laptop") # Adding another Laptop for counting
laptop_count = inventory.count("Laptop")
print("Number of Laptops in Inventory:", laptop_count) # 2

#8. Find Product Position (index())
monitor_index = inventory.index("Monitor")
print("Index of Monitor:", monitor_index) # 3

#9. Sort Inventory Alphabetically (sort())
inventory.sort()
print("Sorted Inventory:", inventory) # ['Headset', 'Laptop', 'Laptop', 'Monitor', 'Printer', 'Webcam']

#10. Reverse Inventory Order (reverse())
inventory.reverse()
print("Reversed Inventory:", inventory) # ['Webcam', 'Printer', 'Monitor', 'Laptop', 'Laptop', 'Headset']

#11. Backup Inventory (copy())
backup_inventory = inventory.copy()
print("Backup Inventory:", backup_inventory) # ['Webcam', 'Printer', 'Monitor', 'Laptop', 'Laptop', 'Headset']

#12. Clear Inventory (clear())
inventory.clear()
print("Cleared Inventory:", inventory) # []




