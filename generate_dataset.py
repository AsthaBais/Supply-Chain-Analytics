from generators.suppliers import generate_suppliers
from generators.warehouses import generate_warehouses
from generators.products import generate_products
from generators.customers import generate_customers
from generators.orders import generate_orders
from generators.inventory import generate_inventory
from generators.shipments import generate_shipments
from generators.deliveries import generate_deliveries

suppliers = generate_suppliers()
warehouses = generate_warehouses()
products = generate_products()

print("\n===== Suppliers =====")
print(suppliers.head())

print("\n===== Warehouses =====")
print(warehouses.head())

print("\n===== Products =====")
print(products.head())
suppliers.to_csv("../Dataset/suppliers.csv", index=False)
warehouses.to_csv("../Dataset/warehouses.csv", index=False)
products.to_csv("../Dataset/products.csv", index=False)

print("\nDatasets saved successfully!")

customers = generate_customers()

print("\n===== Customers =====")
print(customers.head())

customers.to_csv("../Dataset/customers.csv", index=False)

orders = generate_orders()

print("\n===== Orders =====")
print(orders.head())

orders.to_csv("../Dataset/orders.csv", index=False)
inventory = generate_inventory()

print("\n===== Inventory =====")
print(inventory.head())

inventory.to_csv("../Dataset/inventory.csv", index=False)
shipments = generate_shipments(orders)
deliveries = generate_deliveries(shipments)

print("\n===== Shipments =====")
print(shipments.head())

print("\n===== Deliveries =====")
print(deliveries.head())

shipments.to_csv("../Dataset/shipments.csv", index=False)
deliveries.to_csv("../Dataset/deliveries.csv", index=False)

print("\n✅ All datasets generated successfully!")