                 # Python Practice: Tuples

# Q11. Tuple Indexing
# colors = ("red", "green", "blue", "yellow", "purple")
# Extract second, last, and middle three elements.
colors = ("red", "green", "blue", "yellow", "purple")
second=colors[1]
last=colors[-1]
middle_three_elements=colors[1:4]
print(second)
print(last)
print(middle_three_elements)

print("END of Question 11 \n")


# Q12. Tuple Unpacking
# employee = ("Ali", 28, "Data Engineer", 150000)
# Unpack into four variables and display name and salary
employee = ("Ali", 28, "Data Engineer", 150000)
Name,Age,Departement,Salary = employee
print(f"Name: {Name}")
print(f"Salary: {Salary}")

print("END of Question 12 \n")



# Q13. Tuple Concatenation
# tuple1 = (10, 20, 30)
# tuple2 = (40, 50, 60)
# Combine tuples, then create another tuple in reverse order
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
combine1_2=tuple1 + tuple2
reverse_tuple=combine1_2[::-1]
print(combine1_2)
print(reverse_tuple)

print("END of Question 13 \n")

# LEVEL: INTERMEDIATE

# Q14. Count and Locate
# numbers = (10, 20, 30, 20, 40, 20, 50)
# Count occurrences of 20 and find the first index.
numbers = (10, 20, 30, 20, 40, 20, 50)
count_20=numbers.count(20)
print(count_20)
first_index=numbers.index(20)
print(first_index)

print("END of Question 14 \n")



# Q15. Extended Tuple Unpacking
# data = (100, 200, 300, 400, 500, 600)
# Unpack first two and last into variables; put all 
# remaining elements into a list.
data = (100, 200, 300, 400, 500, 600)
first ,second ,*remaining ,last=data
print(first)
print(second)
print(remaining)
print(last)

print("END of Question 15 \n")


# Q16. Modify an Immutable Tuple
# numbers = (10, 20, 30, 40, 50)
# Create a new tuple replacing 30 with 300.
   # Tareeqa 1: Slicing wala
numbers = (10, 20, 30, 40, 50)
new_no=numbers[:2] + (300,) + numbers[3:] # [:2] matlab 0,1 tk OR [3:] 3 se start
print(new_no)

  # Tareeqa 2: List me badal ke
numbers = (10, 20, 30, 40, 50)
 #  tuple ko list mai convert kya
temp_list=list(numbers)
 #  index 2 par 300 update kya
temp_list[2]=300
 #  list ko dubara tuple convert kya
list_to_tuple=tuple(temp_list)
 # tuple list ko print kya
print(list_to_tuple)

print("END of Question 16 \n")



# Q17. Nested Tuple Access
# students = (
#  ("Ali", (85, 90, 88)),
#  ("Sara", (92, 87, 95)),
#  ("Ahmed", (78, 84, 80))
# )
# Extract Sara second score, Ali average, and Ahmed
# highest score.
students = (
 ("Ali", (85, 90, 88)),
 ("Sara", (92, 87, 95)),
 ("Ahmed", (78, 84, 80))
)
# 1. Sara ka second score
# students[1] -> ("Sara", (92, 87, 95))
# [1] -> (92, 87, 95)
# [1] -> 87
Sara_second_score=students[1][1][1]  
print(Sara_second_score)

Ali_score=students[0][1] # (85, 90, 88)
ali_avg=sum(Ali_score) / len(Ali_score)
print(round(ali_avg,2))

Ahmed_high_score=students[2][1][1]
print(Ahmed_high_score)

print("END of Question 17 \n")


  # LEVEL: ADVANCED

# Q18. Tuple Sorting
# employees = (
#  ("Ali", 80000),
#  ("Sara", 120000),
#  ("Ahmed", 95000)
# )
# Sort by salary descending without loops, comprehensions, or lambda.
 # Method 1 : using itemgetter
from operator import itemgetter
employees = (
 ("Ali", 80000),
 ("Sara", 120000),
 ("Ahmed", 95000)
)
sorted_employees =tuple(sorted(employees ,key=itemgetter(1) , reverse=True))
print(sorted_employees)

# Method 2 : Lambda 
employes = (
 ("Ali", 80000),
 ("Sara", 120000),
 ("Ahmed", 95000)
)
sorted_employes=tuple(sorted(employes ,key=lambda x: x[1] ,reverse=True))
print(sorted_employes)

print("END of Question 18 \n")


# Q19. Tuple Matrix
# matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
# Extract diagonal, calculate its product, and build a tuple of row sums.
matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
     # diagonal of matrix
diagonal=(matrix[0][0], matrix[1][1], matrix[2][2])
print(diagonal)  # (2,10,18)

    # product of diagonal values
product=matrix[0][0] * matrix[1][1] * matrix[2][2]
print(product)   # 2*10*18= 360

    # sum of single rows of matrix
row_sum=(sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))
print(row_sum)

print("END of Question 19 \n")


# Q20. Inventory Tuple Challenge
# records = (
#  ("Laptop", 120000, 5),
#  ("Mouse", 1500, 20),
#  ("Keyboard", 3500, 10)
# )
# Calculate inventory value, find most expensive product, and build reversed tuple of names.
  # Method 1: using index and method
record = (
 ("Laptop", 120000, 5),
 ("Mouse", 1500, 20),
 ("Keyboard", 3500, 10)
)
  # 1. Inventory Value = Price * Qty ka sum
  # Laptop ka value = records[0][1] * records[0][2] -> 120000*5
  # Mouse ka value = records[1][1] * records[1][2] -> 1500*20
  # Keyboard ka = records[2][1] * records[2][2] -> 3500*10
total_value= sum((
    record[0][1] * record[0][2],
    record[1][1] * record[1][2],
    record[2][1] * record[2][2]    
))
print(total_value)  # 665000

  # max price nikala
max_price=max(record[0][1], record[1][1], record[2][1])  #120000
  # ye max price kis ka hai
most_expensive=(
    record[0] if record[0][1] == max_price else
    record[1] if record[1][1] == max_price else
    record[2]
)
print(most_expensive)

name=record[0][0], record[1][0] ,record[2][0]
reverse_name=name[::-1]
print(reverse_name)

print("\n")
  

  # Methond 2 : Using lambda and comprehension
records = (
 ("Laptop", 120000, 5),
 ("Mouse", 1500, 20),
 ("Keyboard", 3500, 10)
)
total_value=sum(price * qty for _, price ,qty in records)
print(total_value)  # 665000

max_price=max(records ,key=lambda x: x[1])
print(max_price) # ('Laptop', 120000, 5)
print(max_price[0]) # laptop

names=tuple(name for name,_ ,_ in records)
revers_name=names[::-1]
print(revers_name)


print("END of Question 20 \n")



