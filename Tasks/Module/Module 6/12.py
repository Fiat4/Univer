str = input()
first = str.find("h")
last = str.rfind("h")
new_string = list(str.replace("h", "H"))
new_string[first], new_string[last] = "h", "h"
print("".join(new_string))