 # Python Practice Assignment : lists

# Q1. Accessing List Elements
# numbers = [10, 20, 30, 40, 50, 60, 70]
# Extract the first, middle, and last elements without modifying
#  the original list.
numbers=[10,20,30,40,50,60,70]
result=[numbers[0],numbers[len(numbers)//2],numbers[-1]]
print(result)

print("END OF QUESTION 1 \n")


# Q2. List Slicing
# numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# Create three new lists: first five elements, last four elements,
# and every second element in reverse order.
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

first_five = numbers[:5]          
last_four = numbers[-4:]          
every_second_reverse = numbers[::-2]  

print(first_five)
print(last_four)
print(every_second_reverse)

print("END OF QUESTION 2 \n")


# Q3. List Modification
# fruits = ["apple", "banana", "cherry", "mango"]
# Replace banana with orange, add grapes at index 2, and remove cherry
fruits = ["apple", "banana", "cherry", "mango"]
fruits[1]="banana"
fruits.insert(2,"grapes")
fruits.remove("cherry")
print(fruits)

print("END OF QUESTION 3 \n")



# Q4. Reverse Without reverse()
# numbers = [12, 45, 23, 67, 89, 34]
# Reverse using slicing only; preserve the original list.
numbers = [12, 45, 23, 67, 89, 34]
reversed_numbers=numbers[::-1]
print(numbers)
print(reversed_numbers)

print("END OF QUESTION 4 \n")



# Q5. Second Largest Unique Number
# numbers = [45, 12, 89, 34, 89, 67, 45, 23]
# Find the second-largest unique number. Expected: 67.

numbers = [45, 12, 89, 34, 89, 67, 45, 23]
 # remove duplicate from list
unique_list=set(numbers)
 # sorted the list
sort_number=sorted(unique_list)
 # find second largest number
second_largest=sort_number[-2]
print(second_largest)
print(sort_number)
                    # AND 
SECONT_LARGEST=sorted(set(numbers))[-2]
print(SECONT_LARGEST)

print("END OF QUESTION 5 \n")


# Q6. Rotate a List
# numbers = [10, 20, 30, 40, 50, 60]
# k = 2
# Rotate the list right by k using slicing. Expected: [50, 60, 10, 20, 30, 40].

numbers = [10, 20, 30, 40, 50, 60]
k=2
rotate=numbers[-k:] + numbers[:-k]
print(rotate)
 # preserve actual list
print(numbers)

print("END OF QUESTION 6 \n")

# Q7. Remove Duplicates, Preserve Order
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# Remove duplicates while preserving first-occurrence order.
num = [10, 20, 10, 30, 20, 40, 30, 50]
uniqu_list=list(dict.fromkeys(num))   # jo phele aya num mai wo hi tarteeb rahegi
print(uniqu_list)

print("END OF QUESTION 7 \n")


# Q8. Flatten a Nested List
# data = [[10, 20], [30, 40], [50, 60]]
# Flatten into [10, 20, 30, 40, 50, 60] using list operations.
data = [[10, 20], [30, 40], [50, 60]]

# a ) Method 1:
flattend=sum(data,[])
print(flattend)

# sum(data, []) ka matlab hai [] + [10][20] + [30][40] + [50][60] - 
# Python khud jor deta hai.

# b ) Method 2:
flatten=data[0] + data[1] + data[2]
print(flatten)

print("END OF QUESTION 8 \n")


# # Q9. Extract Data from a Matrix
# matrix = [
#  [10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]
# ]
# Extract main diagonal, secondary diagonal, and middle column;
#  calculate the sum of each
matrix = [
 [10, 20, 30],  # index 0
 [40, 50, 60],  # index 1
 [70, 80, 90]   # index 2
]
main_diagonal= [matrix[0][0], matrix[1][1], matrix[2][2]]
secondary_diagonal= [matrix[0][2], matrix[1][1], matrix[2][0]]
middle_column= [matrix[0][1], matrix[1][1], matrix[2][1]]

print(f"{main_diagonal} sum  {sum(main_diagonal)}")
print(f"{secondary_diagonal} sum  {sum(secondary_diagonal)}")
print(f"{middle_column} sum  {sum(middle_column)}")

# 1. Main Diagonal
# [ 10 ,  x ,  x ]
# [  x , 50 ,  x ]
# [  x ,  x , 90 ]  => [10, 50, 90] sum = 150


# 2. Secondary Diagonal
# [  x ,  x , 30 ]
# [  x , 50 ,  x ]
# [ 70 ,  x ,  x ]  => [30, 50, 70] sum = 150


# 3. Middle Column
# [  x , 20 ,  x ]
# [  x , 50 ,  x ]
# [  x , 80 ,  x ]  => [20, 50, 80] sum = 150

print("END OF QUESTION 9 \n")


# Q10. List Transformation Challenge
# data = [15, 5, 25, 10, 35, 20, 30]
# Build a list of the three largest unique values ascending, then two 
# smallest unique values descending. Expected: [25,30, 35, 10, 5].
data = [15, 5, 25, 10, 35, 20, 30]
 # sort data
sort_data=sorted(data)
 # find 3 largest no from sort_data in ASC order
Three_largest_no=sort_data[-3:] # [25, 30, 350]
 # find 2 smallest no from sort_data 
Two_smallest_no=sort_data[:2]   # OR sort_data[:-5]  => [5, 10]
 # ab isko descending karna hai
reserve_two_no=Two_smallest_no[::-1] # OR list(reversed(Two_smallest_no)) => [10, 5]  
 # combine both lists
final_list=Three_largest_no + reserve_two_no
print(final_list) # [25, 30, 35, 10, 5]


print("END OF QUESTION 10 \n")












