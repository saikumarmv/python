# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 180, 185, 187, 188, 191, 350, 360]
data = [12223, 31564564, 531564, 51564]
# del data[:2]
# print(data)
# del data[14:]
# print(data)
min_valid = 100
max_valid = 200
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:  # removing low values
        stop = index
        break
print(stop)
del data[:stop]
print(data)
# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # Set 'start' to the position of the first
        # item to delete which is 1 after index value
        start = index + 1
        break
print(start)
del data[start:]
print(data)
