numbers = [1,2,3,4,5]
fruits = ["apples", "oranges","strawberry","pears"]

numbers2 = list((1,2,3,4,5))

print(numbers,fruits)

#Get a value of a list- valor  

print(fruits[2])

#get length- longitud

print(len(fruits))

#append to the list 
 
fruits.append("mango")
print(fruits)

#remove from the list

fruits.remove("pears") 

#insert to position 

fruits.insert(2,"watermelon")
print(fruits)

#Remove from a position with pop

fruits.pop(2)
print(fruits)

#reverse the list
fruits.reverse()
print(fruits)

#sort alphbetically
fruits.sort()
print(fruits)

