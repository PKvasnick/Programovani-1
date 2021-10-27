# int is immutable type
integer = 10
print(f"integer: {integer}; address: {hex(id(integer))}")
# integer: 10; address: 0x7f7a7b35fa50
integer = 20
print(f"integer: {integer}; address: {hex(id(integer))}")
# integer: 20; address: 0x7f7a7b35fb90

# str is immutable type
string = "hello"
print(f"string: {string}; address: {hex(id(string))}")
# string: hello; address: 0x7f7a7b205370
string = "world"
print(f"string: {string}; address: {hex(id(string))}")
# string: world; address: 0x7f7a7b205470

# list is mutable type
list_var = [1, 2, 3]
print(f"list_var: {list_var}; address: {hex(id(list_var))}")
# list_var: [1, 2, 3]; address: 0x7f7a7b259840
list_var.append(4)
print(f"list_var: {list_var}; address: {hex(id(list_var))}")
# list_var: [1, 2, 3, 4]; address: 0x7f7a7b259840

# dictionary is mutable type
dict_var = {"key1": "value1"}
print(f"dict_var: {dict_var}; address: {hex(id(dict_var))}")
# dict_var: {'key1': 'value1'}; address: 0x7f7a7b2cf500
dict_var["key2"] = "value2"
print(f"dict_var: {dict_var}; address: {hex(id(dict_var))}")
# dict_var: {'key1': 'value1', 'key2': 'value2'}; address: 0x7f7a7b2cf500
