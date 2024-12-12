def all_thing_is_obj(object: any) -> int:
    if type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object) == list or type(object) == tuple or type(object) == set or type(object) == dict:
        print(f"{object} : {type(object)}")
    else:
        print("Type not found")
    return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
