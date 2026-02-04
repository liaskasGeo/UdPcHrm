a = "George"
# b = a + 10 #ERROR string + int
b = a + str(10) # CORRECT
print(b * 5)
# int("Hi") ERROR
print(int(10.5)) #PRINTS 10
print(float("10")) #PRINTS 10.0
print("====================================================================")
my_list = ["a","b","c"]
my_tuple = ("d","e","f")
my_set = {"g","h","i"}
z = my_list[1]
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(z)
print(type(z))
print(my_list.index("b"))
print("My old list: ",my_list)
my_list.__setitem__(1, "d") # mylist[1] = "d" <- PREFERED
print("My new list: ",my_list)
print(my_list.__getitem__(2)) #prints C
print(my_list[2]) # PREFERED and its calling the method to do that , the getitem method

my_list = ["a","b","c"]
print(my_list)
my_list[1] = "c"
print(my_list)

my_tuple = ("a","b","c")
print(my_tuple)
# my_list[1] = "c" ERROR Tuples does not support item assignment