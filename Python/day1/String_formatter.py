#string formatter
name = "Alice"
age = 30
height = 5.5
# Using f-string
print(f"My name is {name}, I am {age} years old and my height is {height} feet.")
# Using str.format()
print("My name is {}, I am {} years old and my height is {} feet.".format(name, age, height))
# Using % operator
print("My name is %s, I am %d years old and my height is %.1f feet." % (name, age, height))

#Format left alignment
print(f"{'Name':<10} {'Age':<5} {'Height':<10}")
print(f"{name:<10} {age:<5} {height:<10}")

#Format right alignment
print(f"{'Name':>10} {'Age':>5} {'Height':>10}")
print(f"{name:>10} {age:>5} {height:>10}")