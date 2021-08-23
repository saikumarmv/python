shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#  if item == "spam":
#      continue
#  print("buy " + item)
# print("-"*30)
# for item in shopping_list:
#   if item == "spam":
#       break
#   print("buy " + item)
item_to_find = "spam"
found_at = None
# for index in range(6);
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("item found at position {}".format(found_at))
item_to_find = "sai"
found_at = None
# for index in range(6);
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("item  {} not found".format(item_to_find))


if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("item  {} not found".format(item_to_find))
