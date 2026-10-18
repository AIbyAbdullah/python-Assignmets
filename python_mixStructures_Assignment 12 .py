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
    # 1. total processed records  basic method
pipeline_1=pipelines["pipeline_1"]["records"][0] + pipelines["pipeline_1"]["records"][1] + pipelines["pipeline_1"]["records"][2]
pipeline_2=pipelines["pipeline_2"]["records"][0] + pipelines["pipeline_2"]["records"][1] + pipelines["pipeline_2"]["records"][2]
pipeline_3=pipelines["pipeline_3"]["records"][0] + pipelines["pipeline_3"]["records"][1] + pipelines["pipeline_3"]["records"][2]

print("method 1 for total procced\n")

print(f"total of pipeline 1 : {pipeline_1}")
print(f"total of pipeline 2 : {pipeline_2}")
print(f"total of pipeline 3 : {pipeline_3}")
print("\n")
  # 1. total procced records expert method
print("method 2 for total procced\n")

pipe_1=sum(pipelines["pipeline_1"]["records"])
pipe_2=sum(pipelines["pipeline_2"]["records"])
pipe_3=sum(pipelines["pipeline_3"]["records"])

print(f"total of pipeline 1 is {pipe_1}")
print(f"total of pipeline 1 is {pipe_2}")
print(f"total of pipeline 1 is {pipe_3}")
print("\n")
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

print(f"avg P1 : {pip_1} , avg P2 : {pip_2} , avg P3 : {pip_3}")


print("End of Question no: 47  \n")



# Q48. Banking Transactions
# accounts = {
#  "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
#  "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
#  "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
# }
# Assuming zero starting balances, calculate final balances, highest balance, total withdrawals, and largest single
# deposit.
accounts = {
 "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
 "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
 "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
}
   # 1. calculate final balane of each
final_A101= sum(accounts["A101"]["transactions"])
final_A102= sum(accounts["A102"]["transactions"])
final_A103= sum(accounts["A103"]["transactions"])

print(f"final_A101 : {final_A101}") # 5000
print(f"final_A102 : {final_A102}") # 5000
print(f"final_A103 : {final_A103}") # 8000

   # 2. Highest balance 
balances= {
    "A101":final_A101 , 
    "A102":final_A102,
    "A103":final_A103
}
high_balance=max(balances ,key=balances.get)
print(f"Highest balance {balances[high_balance]} by {high_balance}")

  # 4. largest single deposit

# Saare transactions ek list me
all_trans = accounts["A101"]["transactions"] + accounts["A102"]["transactions"] + accounts["A103"]["transactions"]
print(all_trans) # [5000, -2000, 3000, -1000, 10000, -3000, -2000, 7000, -1500, 2500]

high_deposite=max(all_trans)
print(high_deposite) # 10000


# 3. Total withdrawals
negative_only_2 = []
for amount in all_trans:
    if amount < 0:
        negative_only_2.append(amount)

print(f"negative amounts {negative_only_2} and sum of that amount is {sum(negative_only_2)}") # [-2000, -1000, -3000, -2000, -1500]


print("End of Question no: 48  \n")


# Q49. Product Recommendations
# users = {
#  "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
#  "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
#  "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
# }
# Find products bought by at least two users, Ali wishlist minus purchases, shared wishlist products, and all products.
users = {
 "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
 "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
 "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
}
  # purchase ke sets sabke
Ali_P= users["Ali"]["purchased"]
Sara_P= users["Sara"]["purchased"]
Ahmed_P= users["Ahmed"]["purchased"]

  # wishlist ke sets sabke
Ali_W= users["Ali"]["wishlist"]
Sara_W= users["Sara"]["wishlist"]
Ahmed_W= users["Ahmed"]["wishlist"]

 # 1. Products bought by at least two users
bought_atleast_2=(Ali_P & Sara_P) | (Ali_P & Ahmed_P) | (Ahmed_P & Sara_P)
print(f"Atleast 2 user buy {bought_atleast_2} \n") # {'Keyboard', 'Laptop'}

 # 2. Ali wishlist minus purchases
ali_wish_minus=Ali_W - Ali_P
print(f"Ali wish minus from purchase {ali_wish_minus} \n")  # {'Monitor', 'Keyboard'}

 # 3.shared wishlist product ("Woh product jo kam se kam 2 logon ki wishlist me hai")
shared_wishlist = (Ali_W & Sara_W) | (Ali_W & Ahmed_W) | (Ahmed_W & Sara_W)
print(f"Shared wishlist {shared_wishlist} \n")

# 4.All products (purchased + wishlist sab mila ke) jo sab ke pass hai wo sare.
all_product= Ali_W | Sara_W | Ahmed_W | Ali_P | Sara_P | Ahmed_P
print(f"All prdducts : {all_product}") # {'Headphones', 'Laptop', 'Mouse', 'Keyboard', 'Monitor'}


print("End of Question no: 49  \n")


# Q50. Final Company Analysis
# company = {
#  "departments": {
#  "Engineering": {
#  "employees": [
#  ("Ali", 120000, {"Python", "AWS", "SQL"}),
#  ("Sara", 150000, {"Python", "Databricks", "SQL"})
#  ],
#  "budget": 500000
#  },
#  "Analytics": {
#  "employees": [
#  ("Ahmed", 100000, {"SQL", "Power BI"}),
#  ("Zain", 130000, {"Python", "SQL", "Tableau"})
#  ],
#  "budget": 400000
#  }
#  }
# }
# 1. Payroll per department. 2. Company payroll. 3. Highest-paid employee. 4. Skills shared by all. 5. Engineering-only
# skills. 6. Remaining budget per department. 7. Department with higher average salary. 8. Name-to-salary dictionary. 9.
# All unique skills. 10. Is combined budget sufficient?
company = {
 "departments": {
 "Engineering": {
 "employees": [
 ("Ali", 120000, {"Python", "AWS", "SQL"}),
 ("Sara", 150000, {"Python", "Databricks", "SQL"})
 ],
 "budget": 500000
 },
 "Analytics": {
 "employees": [
 ("Ahmed", 100000, {"SQL", "Power BI"}),
 ("Zain", 130000, {"Python", "SQL", "Tableau"})
 ],
 "budget": 400000
 }
 }
}
  # 1. payroll per departement (har dept ke employe ke salary ka total) without loop
dept_eng= company["departments"]["Engineering"]["employees"][0][1] + company["departments"]["Engineering"]["employees"][1][1]
dept_ana = company["departments"]["Analytics"]["employees"][0][1] + company["departments"]["Analytics"]["employees"][1][1]

print(dept_eng) # 270000
print(dept_ana) # 230000

  # 1. payroll per departement (har dept ke employe ke salary ka total) method 2 using loop
# Engineering
dep_eng = 0
for emp in company["departments"]["Engineering"]["employees"]:
    dep_eng += emp[1]

# Analytics
dep_ana = 0
for emp in company["departments"]["Analytics"]["employees"]:
    dep_ana += emp[1]

print(dep_eng) # 270000
print(dep_ana) # 230000
print("\n")

    # 2. Company payroll (company ka total)
company_payroll=(dept_ana + dept_eng)
print(f"company payroll : {company_payroll} \n")


   # 3. Highest paid employee  method 1: (isme name ko lana difficult or bhaut lamba code hojaiga)
All_salaries= [
    company["departments"]["Engineering"]["employees"][0][1], # Ali 120k
    company["departments"]["Engineering"]["employees"][1][1], # Sara 150k
    company["departments"]["Analytics"]["employees"][0][1],   # Ahmed 100k
    company["departments"]["Analytics"]["employees"][1][1]    # Zain 130k
]
highest_salary=max(All_salaries)
print(f"Highest Salary {highest_salary} \n")

   # 3. Highest paid employee  method 2: lopp with name
high_salary=0
high_name=""
for dept_name in company["departments"]:
    for name,salary,skills in company["departments"][dept_name]["employees"]:
        if salary > high_salary:
            high_salary = salary
            high_name = name
print(f"Highest paid {high_name} - {high_salary} \n")


    # 4. Skills shared by all = sab me common skill method 1 
ali_skills= company["departments"]["Engineering"]["employees"][0][2]
sara_skills= company["departments"]["Engineering"]["employees"][1][2]
ahmed_skills= company["departments"]["Analytics"]["employees"][0][2]
zain_skills= company["departments"]["Analytics"]["employees"][1][2]
common= ali_skills & sara_skills & ahmed_skills & zain_skills
print(common ,"\n")

  # 4. Skills shared by all = sab me common skill method 2 (loop advance and proffesional method)
common=None
for dept_name in company["departments"]:
    for name,salary,skills in company["departments"][dept_name]["employees"]:
        if common is None :
            common=skills
        else:
            common=common & skills
            
print(f"common course {common} \n")


   # 5. Engineering-only skills (wo skill jo eng mai hai or analytic mai nhi) method 1
ali_skill= company["departments"]["Engineering"]["employees"][0][2] 
sara_skill= company["departments"]["Engineering"]["employees"][1][2]
ahmed_skill= company["departments"]["Analytics"]["employees"][0][2]
zain_skill= company["departments"]["Analytics"]["employees"][1][2] 

enginee_skills= ali_skill | sara_skill
analytic_skills= ahmed_skill | zain_skill

eng_only= enginee_skills - analytic_skills
print(f"Engineering Skills : {eng_only} \n")


   # 5. Engineering-only skills (wo skill jo eng mai hai or analytic mai nhi) method 2:loop

# Engineering ki saari skills 
eng_skills=set()
for emp in company["departments"]["Engineering"]["employees"]:
    eng_skills=eng_skills | emp[2]

# Analytics ki saari skills 
ana_skills = set()
for emp in company["departments"]["Analytics"]["employees"]:
    ana_skills=ana_skills | emp[2]

only_eng= eng_skills - ana_skills
print(only_eng , "\n")
  

# 6. Remaining budget per department method 1: (without loop)
eng_budget = company["departments"]["Engineering"]["budget"]
eng_salary = company["departments"]["Engineering"]["employees"][0][1] + company["departments"]["Engineering"]["employees"][1][1]
eng_remaining = eng_budget - eng_salary

ana_budget = company["departments"]["Analytics"]["budget"]
ana_sal = company["departments"]["Analytics"]["employees"][0][1] + company["departments"]["Analytics"]["employees"][1][1]
ana_remaining = ana_budget - ana_sal

print(f"Engineering Remaining: {eng_remaining}")  # Engineering Remaining: 230000
print(f"Analytics Remaining: {ana_remaining} \n") # Analytics Remaining: 170000 

# 6. Remaining budget per department mehtod 2: (with loop)
for dept_name in company["departments"]:
    budget=company["departments"][dept_name]["budget"]  
    total_salary=0
    for name, salary, skills in company["departments"][dept_name]["employees"]:
        total_salary = total_salary + salary  # --> ya total_salary += salary 

    remaining=budget - total_salary
    print(f"{dept_name} Remaining {remaining}")

    


# 7. Department with higher average salary mehtod 1: (without loop)
eng_avg = (company["departments"]["Engineering"]["employees"][0][1] + company["departments"]["Engineering"]["employees"][1][1]) / 2
ana_avg = (company["departments"]["Analytics"]["employees"][0][1] + company["departments"]["Analytics"]["employees"][1][1]) / 2
print("\n")
print(f"Engineering Avg: {eng_avg}")
print(f"Analytics Avg: {ana_avg}")
   # check which one is higher average
if eng_avg > ana_avg:
    print("Engineerint avg is Higher \n")
else:
    print("Analytic avg is Higher")


# 7. Department with higher average salary method 2: using loop 
avg_dict={}
for dept_name in company["departments"]:
    total=0
    count=len(company["departments"][dept_name]["employees"])
    for name, salary, skills in company["departments"][dept_name]["employees"]:
        total += salary
        avg_dict[dept_name]= total/count

# Kaunsa zyada hai?
if avg_dict["Engineering"] > avg_dict["Analytics"]:
    print("Engineering ki average zyada hai")
else:
    print("Analytics ki average zyada hai")
print(avg_dict)


# 8. Name-to-salary dictionary method 1: without loop
name_salary = {
    company["departments"]["Engineering"]["employees"][0][0]: company["departments"]["Engineering"]["employees"][0][1],
    company["departments"]["Engineering"]["employees"][1][0]: company["departments"]["Engineering"]["employees"][1][1],
    company["departments"]["Analytics"]["employees"][0][0]: company["departments"]["Analytics"]["employees"][0][1],
    company["departments"]["Analytics"]["employees"][1][0]: company["departments"]["Analytics"]["employees"][1][1]
}
print(f"Salary of employees with name {name_salary}")

# 8. Name-to-salary dictionary method 2: using loop
name_salary={}
for dept_name in company["departments"]:
    for name,salary, skills in company["departments"][dept_name]["employees"]:
        name_salary[name] = salary

print(f"name_salary {name_salary}") # {'Ali': 120000, 'Sara': 150000, 'Ahmed': 100000, 'Zain': 130000}


# 9. All unique skills method 1 : (without loop)
ali = company["departments"]["Engineering"]["employees"][0][2]
sara = company["departments"]["Engineering"]["employees"][1][2]
ahmed = company["departments"]["Analytics"]["employees"][0][2]
zain = company["departments"]["Analytics"]["employees"][1][2]

unique_skills= ali | sara | ahmed | zain
print(unique_skills)

# 9. All unique skills method 2: using loop
unq_skills=set()
for dept_name in company["departments"]:
    for name, salary,skills in company["departments"][dept_name]["employees"]:
        unq_skills=unq_skills | skills
print(unq_skills)

# 10. Is combined budget sufficient? (without loop)  --> # Matlab total budget vs total salaries
combine_budget=company["departments"]["Engineering"]["budget"] + company["departments"]["Analytics"]["budget"]
combine_salary=company["departments"]["Engineering"]["employees"][0][1]  + company["departments"]["Engineering"]["employees"][1][1] + company["departments"]["Analytics"]["employees"][0][1] + company["departments"]["Analytics"]["employees"][1][1]

print(combine_budget >= combine_salary) # True 
print("yes budget is sufficient")

# Is combined budget sufficient?  method 2: using loop 
total_budget=0
total_salary=0
for dept_name in company["departments"]:
    total_budget += company["departments"][dept_name]["budget"]
    for name,salary,skills in company["departments"][dept_name]["employees"]:
        total_salary += salary

if total_budget >= total_salary:
        print("budget is sufficient")
else:
        print("budget is not sufficinet")
print("End of Question no: 50  \n")


