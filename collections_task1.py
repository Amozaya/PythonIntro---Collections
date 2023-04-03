
millionaire_list = ["sportcar", "Rolex", "mansion", "yacht", "helicopter"]

print(millionaire_list)
print(type(millionaire_list))

print(millionaire_list[0])
print(millionaire_list[1])
print(millionaire_list[-1])

millionaire_list[0] = "Ferrari"
millionaire_list[3] = "casino"
print(millionaire_list)

millionaire_list.append("suit")
print(millionaire_list)

millionaire_list.remove("Rolex")
print(millionaire_list)

millionaire_list.pop()
print(millionaire_list)