a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for i in a:
	if i < num:
		new_list.append(i)
new_list.sort()
new_list.reverse()
print (new_list[0])
print (new_list[1])
print (new_list[2])
