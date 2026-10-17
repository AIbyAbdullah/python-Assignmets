        # Python Practice: Dictionaries
# LEVEL: BEGINNER

# Q31. Dictionary Access
# student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
# Extract name and marks; retrieve missing city with default Karachi.
student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
# 1. Extract name and marks
name = student["name"]   # ya student.get("name")
marks = student["marks"] # ya student.get("marks")
print(f"Name: {name}")
print(f"Marks: {marks}")

# 2. Missing city with default Karachi
city = student.get("city", "Karachi")
print(f"City: {city}") 

print("End of Question 31: \n")


# Q32. Update Dictionary
# employee = {"name": "Sara", "salary": 100000, "department": "IT"}
# Raise salary by 20%, add bonus 15000, change department to Data Engineering.
employee = {"name": "Sara", "salary": 100000, "department": "IT"}
    # Departement update to Data Engennering
employee.update({"department": "Data Engennering"})
print(employee)
    # Salary 20% raise and plus 15000 bonus
employee["salary"]=employee["salary"] * 1.2 + 15000
print(employee)

   # percent find karne ka tareeqa
''' 
20% increase = 1 + 20/100 = 1 + 0.2 = 1.2
30% increase = 1 + 30/100 = 1 + 0.3 = 1.3
15% increase = 1 + 15/100 = 1.15
50% increase = 1 + 50/100 = 1.5
20% decrease = 1 - 20/100 = 0.8
10% decrease = 1 - 10/100 = 0.9
'''

print("End of Question 32: \n")


# Q33. Dictionary Methods
# product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
# Extract keys, values, items; remove stock and retain its value.
product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}

  # keys nikalne ke liye
print(product.keys())
  # values nikalne ke liye
print(product.values()) 
  # items nikalne ke liye
print(product.items())
  # stock remove ke liye
remove_stocks= product.pop("stock") 
print(f"remove stock : {remove_stocks}") # 5
  # check dict
print(product) # {'id': 101, 'name': 'Laptop', 'price': 120000}

print("End of Question 33: \n")


# LEVEL: INTERMEDIATE
# Q34. Merge Dictionaries
# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 50, "d": 40}
# Merge so dict2 overrides overlapping keys.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}
 # method 1 using union |  jo last wala same hoga uski value select hogi jo b:50 hai
merged= dict1 | dict2
print(merged)  # {'a': 10, 'b': 50, 'c': 30, 'd': 40}
 # method 2 jo purana tareeqa hai ** wala 
merge= {**dict1, **dict2}
print(merge) # {'a': 10, 'b': 50, 'c': 30, 'd': 40}

print("End of Question 34: \n")



# Q35. Student Marks
# marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
# Find highest, lowest, average, and top-scoring student without loops or lambda.
marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

highest_value = max(marks.values())
lowest_value = min(marks.values())
avg = sum(marks.values()) / len(marks)  
top_student = max(marks, key=marks.get) # items() nahi ayega warna "zain" show hoga islye ke max alpha ko dekta hai 'z' sab se bara hai

print(highest_value) # 92
print(lowest_value)  # 78
print(avg)           # 85.75
print(top_student)   # Sara

print("End of Question 35: \n")


# Q36. Nested Employee Records
# employees = {
#  "E101": {"name": "Ali", "salary": 80000},
#  "E102": {"name": "Sara", "salary": 120000},
#  "E103": {"name": "Ahmed", "salary": 95000}
# }
# Extract Sara salary, increase Ali salary 15%, and calculate total payroll.
employees = {
 "E101": {"name": "Ali", "salary": 80000},
 "E102": {"name": "Sara", "salary": 120000},
 "E103": {"name": "Ahmed", "salary": 95000}
}
  # Extract sara salary
sara_salary=employees["E102"]["salary"]
print(f"Sara Salary: {sara_salary}")

 # Increase Ali salary 15%  (1 + 15/100 = 1.15 )
Ali_salary=employees["E101"]["salary"] * 1.15
print(f"Ali_salary increase 15% : {Ali_salary}")

  # caluclate total salaries of all  method 1:
total_payroll=employees["E101"]["salary"] + employees["E102"]["salary"] + employees["E103"]["salary"]
print(f"total payroll : {total_payroll}")  

  # caluclate total salaries of all  method 2:
total_salary=sum(emp["salary"] for emp in employees.values())
print(f"total payroll : {total_salary}")

print("End of Question 36: \n")


# Q37. Dictionary Inversion
# data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
# Create inverse dictionary without loops or comprehensions.
data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
  # method 1 using map
inverse=dict(map(reversed ,data.items()))
print(f" using map : {inverse}")  
  # method 2 using zip
inverse2=dict(zip(data.values() ,data.keys()))
print(f" using zip : {inverse2}")
   # method 3 using loop
inverse_loop={v : k for k,v in data.items()}
print(f" using_loop : {inverse_loop} ")

print("End of Question 37: \n")


# LEVEL: ADVANCED


# Q38. Order Calculation
# order = {
#  "laptop": {"price": 120000, "quantity": 2},
#  "mouse": {"price": 1500, "quantity": 5},
#  "keyboard": {"price": 3500, "quantity": 3}
# }
# Calculate subtotals, grand total, and amount after 10% discount.
order = {
 "laptop": {"price": 120000, "quantity": 2},
 "mouse": {"price": 1500, "quantity": 5},
 "keyboard": {"price": 3500, "quantity": 3}
}
    # subtotal (price * Quantity)
laptop_total= order["laptop"]["price"] * order["laptop"]["quantity"]
mouse_total= order["mouse"]["price"] * order["mouse"]["quantity"]
keyboard_total= order["keyboard"]["price"] * order["keyboard"]["quantity"]

print(f"subtotal of laptop is : {laptop_total}")
print(f"subtotal of mouse is : {mouse_total}")
print(f"subtotal of keyboard is : {keyboard_total}")

  # Grand total
Grand_total= laptop_total + mouse_total + keyboard_total
print(f"Grand_total is : {Grand_total}")

 # After 10% discount yani decrease (1 - 10/100)=0.9
discounted= Grand_total * 0.9
print(f"After 10% Discount : {discounted}")


print("End of Question 38: \n")


# Q39. Employee Performance
# employees = {
#  "Ali": {"python": 90, "sql": 85, "aws": 88},
#  "Sara": {"python": 95, "sql": 92, "aws": 90},
#  "Ahmed": {"python": 80, "sql": 87, "aws": 84}
# }
# Calculate each average, top performer, and highest SQL score
employees = {
 "Ali": {"python": 90, "sql": 85, "aws": 88},
 "Sara": {"python": 95, "sql": 92, "aws": 90},
 "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}
   # Calculate Each average
Ali_avg= round(sum(employees["Ali"].values()) / len(employees["Ali"]),2)
Sara_avg= round(sum(employees["Sara"].values()) / len(employees["Sara"]),2)
Ahmed_avg= round(sum(employees["Ahmed"].values()) / len(employees["Ahmed"]),2)

print(f"Average of Ali marks is : {Ali_avg}")
print(f"Average of Sara marks is : {Sara_avg}")
print(f"Average of Ahmed marks is : {Ahmed_avg}")

  # Top performer
average={"Ali":Ali_avg, "Sara":Sara_avg, "Ahmed":Ahmed_avg}
top_performer=max(average ,key=average.get)
print(f"top_performer is : {top_performer}")

 # Top highest score in sql  mehtod 1:
top_sql_score=max(employees["Ali"]["sql"] , employees["Sara"]["sql"] , employees["Ahmed"]["sql"])
print(top_sql_score) # 92
 
print("End of Question 39: \n")
 
 # Top highest score in sql  mehtod 2 with name:
  
   # SQL KA SCORE SAB STUDENTS KA
sql_score={name : data["sql"] for name,data in employees.items()}
print(sql_score) # {'Ali': 85, 'Sara': 92, 'Ahmed': 87} => ye sql ka score hai

  # HIGH score
top_sql_name=max(sql_score, key=sql_score.get)
highest_score=sql_score[top_sql_name]
print(f"highest SQL is {highest_score} by {top_sql_name}")  # highest SQL : 92 by Sara

'''
    why "key=sql_score.get"  this is imp because:
    if:
    sql_score = {'Ali': 99, 'Sara': 92, 'Ahmed': 87}
    Ali ka 99 sab se zyada hai

    print(max(sql_score)) # Sara dega ! (kyunki S > A)  kyunke max jo hia wo alphabet dekhta hai nake values jisme 's' bara hai jo s ayegacls
    Lekin topper Ali hona chahiye tha

    print(max(sql_score, key=sql_score.get)) # Ali dega - YE SAHI HAI
'''

print("End of Question 39: \n")



# Q40. Inventory Management
# inventory = {
#  "P101": {"name": "Laptop", "price": 120000, "stock": 5},
#  "P102": {"name": "Mouse", "price": 1500, "stock": 20},
#  "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
# }
# Calculate total value, most valuable item by price x stock, and update stock after selling two laptops and five mice.
inventory = {
 "P101": {"name": "Laptop", "price": 120000, "stock": 5},
 "P102": {"name": "Mouse", "price": 1500, "stock": 20},
 "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}
    # 1. Total value = price * stock ka sum
# Each item ke value (price * stock)
p101=inventory["P101"]["price"] *  inventory["P101"]["stock"]
p102=inventory["P102"]["price"] *  inventory["P102"]["stock"]
p103=inventory["P103"]["price"] *  inventory["P103"]["stock"]
total= p101 + p102 + p103
print(f"total value : {total}")

    # 1.2 total value
total_value=sum(items["price"] * items["stock"] for items in inventory.values())
print(f"total value : {total_value}")

    # 2. # 2. Most valuable item by price x stock
values={
    "P101":inventory["P101"]["price"] *  inventory["P101"]["stock"],
    "P102":inventory["P102"]["price"] *  inventory["P102"]["stock"],
    "P103":inventory["P103"]["price"] *  inventory["P103"]["stock"]
}
most_valuable_ID=max(values, key=values.get)
print(f"Most valuable ID: {most_valuable_ID} -> {inventory[most_valuable_ID]['name']} with {values[most_valuable_ID]}") # Most valuable ID: P101 -> Laptop with 600000
 
    # 3. Update stock after selling 2 laptops and 5 mice
inventory["P101"]["stock"] -=2
inventory["P102"]["stock"] -=5
print(f"After selling: {inventory}")

print("End of Question 40: \n")

