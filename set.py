# 1.Write a Python program to create a set.

# s = {10,20,30,40,50}
# print(s)


#2.Write a Python program to iterate over sets.

# s = {10,20,30,40,50}
# for i in s:
#     print(i)


#3.Write a Python program to add member(s) to a set.

# s = {10,20,30,40,50}
# print(s)
# s.add(101)
# print(s)


#4.Write a Python program to remove item(s) from a given set.

# s = {10,20,30,40,50}
# print(s)
# s.remove(20)
# print(s)


#5.Write a Python program to remove an item from a set if it is present in the set.

# s = {10,20,30,40,50}
# print(s)
# s.discard(201)
# print(s)


#6.Write a Python program to create an intersection of sets.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.intersection(s2))


#7.Write a Python program to create a union of sets.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.union(s2))


#8.Write a Python program to create set difference.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.difference(s2))
# print(s2.difference(s1))


#9.Write a Python program to create a symmetric difference.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# print(s1.symmetric_difference(s2))


#10.Write a Python program to check if a set is a subset of another set.

# a = {10,20,30}
# b = {10,20,30,40,60}
# print(a.issubset(b))


#11.Write a Python program to create a shallow copy of sets.

# s1 = {10,20,30,40,50}
# print(s1,id(s1))
# s2 = s1.copy()
# print(s2,id(s2))


#12.Write a Python program to remove all elements from a given set.

# s1 = {10,20,30,40,50}
# print(s1)
# s1.clear()
# print(s1)


#13.Write a Python program that uses frozensets.

# s = frozenset([10,20,30,40,50])
# print(s)


#14.Write a Python program to find the maximum and minimum values in a set.

# s = {10,20,0,40,230,543,22,-34,234,5321}
# print(min(s))
# print(max(s))


#15.Write a Python program to find the length of a set.

# s = {10,20,30,40,50}
# print(len(s))


#16.Write a Python program to check if a given value is present in a set or not.

# s1 = {10,20,30,40,50}
# if(100 in s1):
#     print("Value is present")
# else:
#     print("Value not found")


#17.Write a Python program to check if two given sets have no elements in common.

# s1 = {10,20,30,40,50}
# s2 = {60,70,80,90,100}
# print(s1.isdisjoint(s2))


#18.Write a Python program to check if a given set is a superset of itself and a superset of another given set.

# s1 = {10,20,30,40,50}
# s2 = {10,20,30}
# print(s1.issuperset(s2))


#19.Write a Python program to find elements in a given set that are not in another set.

# s1 = {10,20,30,40,50}
# s2 = {50,60,40,30,20,10}
# for i in s2:
#     if(i not in s1):
#         print(i)


#20.Write a Python program to remove the intersection of a second set with a first set.

# s1 = {10,20,30,40,50}
# s2 = {40,50,60,70,80}
# s1.difference_update(s2)
# print(s1)


#21.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

# words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
# d = {}
# for i in words:
#     if(i not in d):
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


#22.Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# target = 35
# for i in nums:
#     for j in nums:
#         if((i+j) == target):
#             print(i,j)

