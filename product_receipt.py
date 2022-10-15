# Store supermart information
super_mart = "super grocery mart"
super_mart_street = "123 Main Street" 
super_mart_location = "Orlando, FL 32803"
super_mart_contact_no = "(407) 555-1234" 
cashier_name = "Jane Smith" 

# import datetime library 
import datetime 
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Items bought 
items_bought = "grocery"

# Product Name and Price 
p1_name, p1_price = "sgm spaghetti sauce", 4.99
p2_name, p2_price = "sgm spaghetti pasta", 1.99
p3_name, p3_price = "mrch inst lunch", 0.96 
p4_name, p4_price = "ee coffee french rst", 5.96 
p5_name, p5_price = "agm evrdy pnt btr", 1.99
p6_name, p6_price = "cub white bread", 1.99
p7_name, p7_price = "par baked rustic rolls", 4.99

# Calculate Sub Total
sub_total = p1_price + p2_price + p3_price + p4_price + p5_price + p6_price + p7_price
# Calculate Food Tax
food_tax = sub_total * 0.06 
# Calculate Grand Total
grand_total = sub_total + food_tax 

# credit, number of items sold, return policy and remark
credit = "credit"
items_sold = 7 
return_policy = "No returns on meat, product, milk products"
remark = "Thank you for your business"


print("*" * 100) 
print(f"\t\t\t\t\t\t{super_mart.title()}")
print(f"\t\t\t\t\t\t{super_mart_street}")
print(f"\t\t\t\t\t\t{super_mart_location}")
print(f"\t\t\t\t\t\t{super_mart_contact_no}")
print("*" * 100)
print(f"Cashier: {cashier_name}")
print(f"{date_time[0:10]}\t\t\t\t\t\t\t    {date_time[10:]}")
print("=" * 100)
print(f"{items_bought.upper()}")
print('') 
print(f"{p1_name.upper()}\t\t\t\t\t\t\t{p1_price}")
print(f"{p2_name.upper()}\t\t\t\t\t\t\t{p2_price}")
print(f"{p3_name.upper()}\t\t\t\t\t\t\t\t{p3_price}")
print(f"{p4_name.upper()}\t\t\t\t\t\t\t{p4_price}")
print(f"{p5_name.upper()}\t\t\t\t\t\t\t{p5_price}")
print(f"{p6_name.upper()}\t\t\t\t\t\t\t\t{p6_price}")
print(f"{p7_name.upper()}\t\t\t\t\t\t\t{p7_price}")
print("\n")
print(f"Subtotal\t\t\t\t\t\t\t      ${sub_total:.2f}")
print(f"Food @ 6%\t\t\t\t\t\t\t       ${food_tax:.2f}")
print(f"GRAND TOTAL\t\t\t\t\t\t\t      ${grand_total:.2f}")
print('')
print(credit)
print('')
print(f"TOTAL NUMBER OF ITEMS SOLD =\t\t\t\t\t\t  {items_sold}")
print("=" * 100)
print(f"\t\t\t{return_policy}")
print(f"\t\t\t{remark}!!")