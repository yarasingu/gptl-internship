list = [2,4,5,6,7,8,9,10]
#print list length and list elements 
print(len(list))
print(list)

#print last index
num = list[-1]
print(num)

#print first index
num= list[0]
print(num)

#pritn list from fist index to fourth index
num = list[0:4]
print(num)

#print list from  index given by user arrguments 
num = list[5:]
print(num)

# this line of code num = list[0:4] and given code work same it takes default as 0
num = list[:4]
print(num)

#this will give the staring to end index as same as this line num = list[0:4]
num = list[1:-1]
print(num)