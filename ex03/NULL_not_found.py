"""
import inspect
x, y, z = 1, 2, 3

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

print(retrieve_name(y))
"""

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif type(object) is float and str(object) == "nan":
        print(f"Chesse: nan {type(object)}")
    elif object == "":
        print(f"Empty: {type(object)}")
    elif type(object) is bool and object is False:
        print(f"Fake: False {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0

Nothing = None
Garlic = float("NaN")
my_float = 0.0
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
