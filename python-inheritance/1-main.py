#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)        # Should print the original list: [1, 4, 2, 3, 5]
my_list.print_sorted() # Should print the sorted list: [1, 2, 3, 4, 5]
print(my_list)        # Should print the original list again: [1, 4, 2, 3, 5]

