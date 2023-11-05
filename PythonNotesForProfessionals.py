# a = set('abracadabra')
# print(a)
# import keyword
# print(keyword.kwlist)
# a, b, _ = 1, 2, 3
# print(a, b)
# # Output: 1, 2

x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7, 8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y) # printing the value of the list using its other name