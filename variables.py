#! C:\Python27
hello_str = "Hello World"
hello_int = True
hello_tuple = (21, 32)

hello_list = ["Hello,", "this", "is", "a", "list"]
hello_list = list()
hello_list.append("Hello,")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

hello_dict = {"first_name": "Tejas",
              "last_name": "Gokhale",
              "eye_color": "brown"}

print(hello_list[4])

hello_list[4] += "!"
print(hello_list[4])

print(str(hello_tuple[0]))
print(hello_dict["first_name"] + " " + hello_dict["last_name"] + "has" + hello_dict["eye_color"] + "eyes.")
print("{0} {1} has {2} eyes".format(hello_dict["first_name"], hello_dict["last_name"], hello_dict["eye_color"]))


