ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

print()

#list
ft_list[1] = "World!"
#tuple
aux = list(ft_tuple)
aux[1] = "Spain!"
ft_tuple = tuple(aux)
#set
ft_set.remove("tutu!")
#ft_set.discard("tutu!")
ft_set.add("Málaga!")
#dict
ft_dict["Hello"] = "42 Málaga!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
