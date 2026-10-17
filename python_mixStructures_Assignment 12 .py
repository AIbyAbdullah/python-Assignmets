            # Python Practice: Mixed Data Structures
# LEVEL: ADVANCED
# Q41. Student Performance System
# students = [
#  {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
#  {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
#  {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
# ]
# Calculate each average, top student, tuple of names, and set of unique marks.
students = [
 {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
 {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
 {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
]
     # Calculate each average
Ali_avg= round(sum(students[0]["marks"]) / len(students[0]["marks"]),2)
Sara_avg= round(sum(students[1]["marks"]) / len(students[1]["marks"]),2)
Ahmed_avg= round(sum(students[2]["marks"]) / len(students[2]["marks"]),2)

print(f"Ali Average : {Ali_avg}")  # Ali Average : 87.67
print(f"Sara Average : {Sara_avg}")  # Sara Average : 92.67
print(f"Ahmed Average : {Ahmed_avg}")  # Ahmed Average : 80.67

    # Top Student name with average
Average={"Ali" : Ali_avg, "Sara" : Sara_avg, "Ahmed" : Ahmed_avg} 
top_student=max(Average ,key=Average.get)
print(f"Topper student: {top_student} with {Average[top_student]}") # Topper student: Sara with 92.67

    # Tuple of names
name_tuple=students[0]["name"], students[1]["name"], students[2]["name"]
print(f"tuple of names : {name_tuple}")  # tuple of names : ('Ali', 'Sara', 'Ahmed')

    # sets of unique marks
all_marks=students[0]["marks"] + students[1]["marks"] + students[2]["marks"]
unique_marks=set(all_marks)
print(f"unique marks set : {unique_marks}")  # unique marks set : {78, 80, 84, 85, 88, 90, 91, 92, 95}


print("End of Question no: 41  \n")


# Q42. Employee Skills
# employees = {
#  "Ali": {"Python", "SQL", "AWS"},
#  "Sara": {"Python", "Databricks", "SQL"},
#  "Ahmed": {"AWS", "Snowflake", "SQL"}
# }
# Find common skills, Ali-only skills, all team skills, and employees meeting Python + SQL requirements.
employees = {
 "Ali": {"Python", "SQL", "AWS"},
 "Sara": {"Python", "Databricks", "SQL"},
 "Ahmed": {"AWS", "Snowflake", "SQL"}
}
   # common skills
common_skills=employees["Ali"] & employees["Sara"] & employees["Ahmed"]
print(f"common skills : {common_skills}")  # common skills : {'SQL'}

print("\n")
   # Ali-only skills
other_skills=employees["Sara"] | employees["Ahmed"]
only_Ali_skills= employees["Ali"] - other_skills
print(only_Ali_skills)  # set()  empty set aya islye ke jo skills ali ke pass hai wo baqi ke pass bhi hai, "only-ali ka matlab jo kisi or ke pass na ho"

print("\n")
   # All team skills
all_team_skills= employees["Ali"] | employees["Sara"] | employees["Ahmed"]
print(f"All Team Skills : {all_team_skills}")  # {'Snowflake', 'Databricks', 'SQL', 'Python', 'AWS'}

print("\n")
  # Employees meeting Python + SQL requirements
requirement={"Python", "SQL"}
  # Har ek ko check karna
ali_meets=requirement.issubset(employees["Ali"])
sara_meets=requirement.issubset(employees["Sara"])
ahmed_meets=requirement.issubset(employees["Ahmed"])

print(f"Ali meets Python+SQL? {ali_meets}") # True
print(f"Sara meets Python+SQL? {sara_meets}") # True
print(f"Ahmed meets Python+SQL? {ahmed_meets}") # False

qualify=[]
if ali_meets:
    qualify.append("Ali")
if sara_meets:
    qualify.append("Sara")
if ahmed_meets:
    qualify.append("Ahmed")

print(f"Qualify employees {qualify}")


print("End of Question no: 42  \n")


# Q43. Sales Data
# sales = [
#  ("Laptop", 120000, 2),
#  ("Mouse", 1500, 5),
#  ("Keyboard", 3500, 3)
# ]
# Calculate revenue, top-revenue product, name-to-revenue dictionary, and set of prices.
sales = [
 ("Laptop", 120000, 2),
 ("Mouse", 1500, 5),
 ("Keyboard", 3500, 3)
]
  # Each revenue
laptop_revenue=sales[0][1] * sales[0][2]
mouse_revenue=sales[1][1] * sales[1][2]
keyboard_revenue=sales[2][1] * sales[2][2]

print(f"laptop revenue : {laptop_revenue}")
print(f"mouse revenue : {mouse_revenue}")
print(f"keyboard revenue : {keyboard_revenue}")
    # total revenue
total_revenue=laptop_revenue + mouse_revenue + keyboard_revenue
print(f"Total revenue of all products : {total_revenue}")

  # top revenue
revenues= {
 sales[0][0]:laptop_revenue,
 sales[1][0]:mouse_revenue,
 sales[2][0]:keyboard_revenue
}    
top_product=max(revenues, key=revenues.get)
print(f"Top revenue : {top_product} with {revenues[top_product]}")

  # name to revenues dict
print(f"Name to revenue dict : {revenues}")

  # set of prices
prices = (sales[0][1], sales[1][1], sales[2][1])
price_set = set(prices)
print(f"set of prices : {price_set}")

print("End of Question no: 43  \n")


# Q44. Customer Orders
# customers = {
#  "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
#  "C102": {"name": "Sara", "orders": [3000, 4500]},
#  "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
# }
# Calculate spending per customer, top customer, and tuple of totals in customer ID order.
customers = {
 "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
 "C102": {"name": "Sara", "orders": [3000, 4500]},
 "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
}
   # calculate spending per customer
spnt_c101=sum(customers["C101"]["orders"])
spnt_c102=sum(customers["C102"]["orders"])
spnt_c103=sum(customers["C103"]["orders"])

print(f"Spend of C101 is : {spnt_c101}")
print(f"Spend of C102 is : {spnt_c102}")
print(f"Spend of C103 is : {spnt_c103}")

   # Top customer
spnt={
    customers["C101"]["name"] :spnt_c101,
    customers["C102"]["name"] :spnt_c102,
    customers["C103"]["name"] :spnt_c103
}
top_customer=max(spnt, key=spnt.get)
print(f"Top spend {top_customer} with {spnt[top_customer]} dollors")


   # Tuple of totals in customer ID order
totals_tuple = (spnt_c101, spnt_c102, spnt_c103)
print(f"Tuple of totals of (C101, C102, C103 order) : {totals_tuple}")

print("End of Question no: 44  \n")


# Q45. Course Enrollment
# courses = {
#  "Python": {"Ali", "Sara", "Ahmed"},
#  "SQL": {"Sara", "Ahmed", "Zain"},
#  "AWS": {"Ali", "Ahmed", "Zain"}
# }
# Find students in exactly two, all three, and exactly one course; count unique students.
courses = {
 "Python": {"Ali", "Sara", "Ahmed"},
 "SQL": {"Sara", "Ahmed", "Zain"},
 "AWS": {"Ali", "Ahmed", "Zain"}
}
    # Exactly in two courses students
py_sql_only=(courses["Python"] & courses["SQL"]) - courses["AWS"]
py_aws_only=(courses["Python"] & courses["AWS"]) - courses["SQL"]
sql_aws_only=(courses["SQL"] & courses["AWS"]) - courses["Python"]
Exactly_two= py_sql_only | py_aws_only | sql_aws_only
print(f"Exactly in two course students are : {Exactly_two}")  # {'Ali', 'Sara', 'Zain'}

   # student in All Courses
Student_in_All_Courses=courses["Python"] & courses["SQL"] & courses["AWS"]
print(f"Student in all three courses: {Student_in_All_Courses}")  # Ahmed

   # only in one course student
py_only= courses["Python"] - (courses["AWS"] | courses["SQL"])
sql_only= courses["SQL"] - (courses["AWS"] | courses["Python"])
aws_only= courses["AWS"] - (courses["Python"] | courses["SQL"])
Exactly_one= py_only | sql_only | aws_only
print(f"Exactly in one course student is : {Exactly_one}")  # set()  noone in only one course

  # count unique students
unique_students = courses["Python"] | courses["SQL"] | courses["AWS"]
print(f"unique Students : {unique_students}")  # {'Zain', 'Sara', 'Ali', 'Ahmed'}

'''
TRICK:
  All three using : A & B & C
  Exactly two using : (A&B)-C + (A&C)-B + (B&C)-A
  Exactly one using : A-(B|C) + B-(A|C) + C-(A|B)
'''

print("End of Question no: 45  \n")


# LEVEL: EXPERT

# Q46. E-Commerce Transactions
# transactions = [
#  {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
#  {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
#  {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
# ]
# Calculate total revenue, Ali spending, largest transaction, and unique product names.
transactions = [
 {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
 {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
 {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
]
    # 1. Calculate total revenue
# total 101 = Laptop + Mouse
spnt_101=transactions[0]["items"][0][1] * transactions[0]["items"][0][2] + transactions[0]["items"][1][1] * transactions[0]["items"][1][2]
# 120000*1 + 1500*2 = 123000

# total 102 = Laptop + Mouse
spnt_102=transactions[1]["items"][0][1] * transactions[1]["items"][0][2] + transactions[1]["items"][1][1] * transactions[1]["items"][1][2]
# 3500*2 + 1500*1 = 8500

# Transaction 103 ka total
spnt_103=transactions[2]["items"][0][1] * transactions[2]["items"][0][2]
# 45000*1=45000

print(f"ID 101 Spend is : {spnt_101}")
print(f"ID 102 Spend is : {spnt_102}")
print(f"ID 103 Spend is : {spnt_103}")

total_spnt=spnt_101 + spnt_102 + spnt_103
print(f"total spnt of all ids : {total_spnt}")


    # 2. Ali spending
Ali_spnt=spnt_101 + spnt_103
print(f"Ali total spend : {Ali_spnt}")

   # 3. largest transaction
transaction={
    transactions[0]["id"] : spnt_101,
    transactions[1]["id"] : spnt_102,
    transactions[2]["id"] : spnt_103
}
large_transaction=max(transaction ,key=transaction.get)
print(f"large transaction ID : {large_transaction} with amount {transaction[large_transaction]}")

   # 4. unique product names
unique_items={
  transactions[0]["items"][0][0],
  transactions[0]["items"][1][0],
  transactions[1]["items"][0][0],
  transactions[1]["items"][1][0],
  transactions[2]["items"][0][0]
}
print(f"uniques products {unique_items}")  # {'Mouse', 'Monitor', 'Laptop', 'Keyboard'} -> duplicate nhi aye kyunke set mai duplicate remove hojate hai.

print("End of Question no: 46  \n")


# Q47. Pipeline Monitoring
# pipelines = {
#  "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
#  "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
#  "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
# }
# Find total processed records, failed pipelines, largest pipeline total, and average records per run for each.
pipelines = {
 "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
 "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
 "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
}
    # 1. total processed records
pipeline_1=pipelines["pipeline_1"]["records"][0] + pipelines["pipeline_1"]["records"][1] + pipelines["pipeline_1"]["records"][2]
pipeline_2=pipelines["pipeline_2"]["records"][0] + pipelines["pipeline_2"]["records"][1] + pipelines["pipeline_2"]["records"][2]
pipeline_3=pipelines["pipeline_3"]["records"][0] + pipelines["pipeline_3"]["records"][1] + pipelines["pipeline_3"]["records"][2]

print(f"total of pipeline 1 : {pipeline_1}")
print(f"total of pipeline 2 : {pipeline_2}")
print(f"total of pipeline 3 : {pipeline_3}")
  # 1. total processed records (sirf success walon ka)
total_procceed= {}
if pipelines["pipeline_1"]["status"] == "success":
    total_procceed["pipeline_1"] = pipeline_1
if pipelines["pipeline_2"]["status"] == "success":
    total_procceed["pipeline_2"] = pipeline_2
if pipelines["pipeline_3"]["status"] == "success":
    total_procceed["pipeline_3"] = pipeline_3
    
print(f"Total success piplines : {total_procceed}")

  # 2. failed pipelines
failed=[]
if pipelines["pipeline_1"]["status"] == "failed":
    failed.append("pipeline_1")
if pipelines["pipeline_2"]["status"] == "failed":
    failed.append("pipeline_2")
if pipelines["pipeline_3"]["status"] == "failed":
    failed.append("pipeline_3")

print(f"failed pipelines : {failed}")

  # 3. largest pipeline total
total={
    "pipeline1": pipeline_1,
    "pipeline2": pipeline_2,
    "pipeline3": pipeline_3
}
largest_pip=max(total ,key=total.get)
print(f"largest pipeline total value is {largest_pip} with {total[largest_pip]}")

   # 4. average records per run for each
pip_1= round(pipeline_1 / 3)
pip_2= round(pipeline_2 / 3)
pip_3= round(pipeline_3 / 3)

print(f"avg P1 : {pip_1} ,avg P2 : {pip_2} , avg P3 : {pip_3}")

    
    
    


print("End of Question no: 47  \n")



