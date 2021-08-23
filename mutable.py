shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
# lists are mutable
# immutable objects value cannot be chenged
print(id(another_list))
print(another_list)
a = b = c = d = e = f = another_list
print(a)
b.append("cream")
print(c)
print(d)
print(a)