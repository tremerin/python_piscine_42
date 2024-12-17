# var name
import inspect
import math

x, y, z = 1, 2, 3

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

print(retrieve_name(y))


def NULL_not_found(object: any) -> int:
    print(type(object))
    #if isinstance(object, str):
    #    print("string")
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif type(object) is float:
        print(f"Chesse: nan {type(object)}")
    return 0

print(type(math.nan))
print(math.nan)

Nothing = None
Garlic = float("NaN")
my_float = 0.1
Zero = 0
Empty = ""
Fake = False
print("test_01")
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(my_float)
#NULL_not_found(Zero)
#NULL_not_found(Empty)
#NULL_not_found(Fake)
#print(NULL_not_found("Brian"))
