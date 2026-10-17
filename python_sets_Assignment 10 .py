                        # SETS Assignment
# LEVEL: BEGINNER

# Q21. Unique Values
# numbers = [10, 20, 10, 30, 40, 20, 50]
# Convert to a set and count unique elements
numbers = [10, 20, 10, 30, 40, 20, 50]
 # remove duplicate
sets=set(numbers)   
print(sets)
  # unique count
print(f"Total unique elements: {len(sets)}")

print("End of Question 21: \n")


# Q22. Set Operations
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# Find union, intersection, a - b, and symmetric difference.
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a | b)   # union => {1,2,3,4,5,6,7,8}
print(a & b)   # intersection => {4,5} - jo dono mai common hai
print(a - b)  # difference => {1,2,3} - jo sirf a mai hai
print(a ^ b)  # symetric difference => {1,2,3,6,7,8} - jo dono mai common nhi hia

print("End of Question 22: \n")


# Q23. Add and Remove
# skills = {"Python", "SQL", "AWS"}
# Add Snowflake and Databricks; safely remove AWS
skills = {"Python", "SQL", "AWS"}
skills.update(["Snowflake","Databricks"])
print(skills)

skills.discard("AWS")
print(skills)


print("End of Question 23: \n")


 # LEVEL: INTERMEDIATE

# Q24. Common Students
# python_students = {"Ali", "Sara", "Ahmed", "Zain"}
# sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
# Find students taking both and exactly one course.
python_students = {"Ali", "Sara", "Ahmed", "Zain"}
sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}

both = python_students & sql_students
print(both)

only_one = python_students ^ sql_students
print(only_one)

print("End of Question 24: \n")


# Q25. Subset and Superset
# required_skills = {"Python", "SQL"}
# candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
# Check required skills are a subset and candidate skills a superset.
required_skills = {"Python", "SQL"}
candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}

print(required_skills.issubset(candidate_skills))  # True
print(candidate_skills.issuperset(required_skills)) # True
      # AND
print(required_skills <= candidate_skills) # subset => True
print(candidate_skills >= required_skills) # superset => True

print("End of Question 25: \n")


# Q26. Missing Numbers
# numbers = {1, 2, 4, 6, 8, 10}
# Find missing integers from 1 through 10 using set operations.
numbers = {1, 2, 4, 6, 8, 10}
 # 1 se 10 tk ka pura set
full_set=set(range(1,11)) 
 # missing = pura - numbers
missing=full_set - numbers
  # ya 
difference=full_set ^ numbers
print(difference) # {3,5,7,9}

print(full_set) #{1,2,3,4,5,6,7,8,9,10}
print(missing) # {3, 5, 7, 9}


print("End of Question 26: \n")


# Q27. Three-Set Analysis
# python = {"Ali", "Sara", "Ahmed", "Zain"}
# sql = {"Sara", "Ahmed", "Hamza"}
# aws = {"Ahmed", "Zain", "Hamza"}
# Find students in all three, exactly Python and SQL (not AWS), and at least two.
python = {"Ali", "Sara", "Ahmed", "Zain"}
sql = {"Sara", "Ahmed", "Hamza"}
aws = {"Ahmed", "Zain", "Hamza"}
  # all three wale
all_three=python & sql & aws
print(all_three)

# 2. Exactly Python and SQL (not AWS)
# Matlab Python aur SQL dono me ho, lekin AWS me na ho
py_sql_only = (python & sql) - aws
print(py_sql_only) # {'Sara'}

atleast_2=(python & sql) | (python & aws) | (sql & aws)
print(atleast_2)

print("End of Question 27: \n")


  # LEVEL: ADVANCED

# Q28. Transaction Analysis
# day1 = {101, 102, 103, 104}
# day2 = {103, 104, 105, 106}
# day3 = {104, 106, 107, 108}
# Find IDs appearing on all days, exactly one day, and at least two days.
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
day3 = {104, 106, 107, 108}

   # IDs jo har din hai
all_3_days= day1 & day2 & day3
print(all_3_days) # {104}

  # jo sirf 1 din hai
only_day1= day1 - day2 - day3 # {101, 102}
only_day2= day2 - day1 - day3 # {105}
only_day3= day3 - day1 - day2 # {107, 108}
one_day_only= only_day1 | only_day2 | only_day3 
print(one_day_only) # {101, 102, 105, 107, 108}

  # jo atleast 2 din hai
atleast_2_day= (day1 & day2) | (day2 & day3) | (day1 & day3)
print(atleast_2_day) # {104, 106, 103}

  # jo sirf 2 din hai  (2 din hi ho, 3 me na ho)
only_2_days= (atleast_2_day - all_3_days)
print(only_2_days)  # {106, 103}

print("End of Question 28: \n")


# Q29. Access Control
# required_permissions = {"read", "write", "execute"}
# user_permissions = {"read", "write", "delete"}
# Find missing and extra permissions and test full authorization.
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write", "delete"}

    # wo permissions jo user ke pass nhi hai req mai se yani "execute"
missing= required_permissions - user_permissions
print(f"user missing permission: {missing}")

    # extra permission jo user ke pass hai yani "delete"
extra= user_permissions - required_permissions
print(f"user extra permission: {extra}")

   # kya user ke pass sab authorized permissions hai? 
is_authorized=required_permissions.issubset(user_permissions)
print(f"Fully Authorized? {is_authorized}")

print("End of Question 29: \n")


# Q30. Customer Segmentation
# website = {"C1", "C2", "C3", "C4", "C5"}
# mobile = {"C3", "C4", "C6", "C7"}
# store = {"C2", "C4", "C7", "C8"}
# Find customers on exactly one, exactly two, and all three platforms.
website = {"C1", "C2", "C3", "C4", "C5"}
mobile = {"C3", "C4", "C6", "C7"}
store = {"C2", "C4", "C7", "C8"}

  # wo customers jo Exactly one platform (sirf 1 par hai)
only_website = website - mobile - store  # {'C1', 'C5'}
only_mobile = mobile - website - store   # {'C6'}
only_store = store - website - mobile    # {'C8'}
exactly_one = only_website | only_mobile | only_store
print(f"Exactly one: {exactly_one}") # {'C1', 'C5', 'C6', 'C8'}

  # wo customers jo atleast two platform par hai
atleast_two=(website & mobile) | (website & store) | (mobile & store)
  # wo customers jo dino (3) mai platform par hai
all_three= website & mobile & store
  # wo customers jo sirf 2 platforms par hai
only_two=atleast_two - all_three
print(f"Exactly Two : {only_two}")  # {'C3', 'C2', 'C7'}

print(f"All three: {all_three}")  # {'C4'}


print("End of Question 30: \n")
