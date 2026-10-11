tasks = ['wash the dishes', 'clean the house', 'do the laundry']

print("Options:")
print("(1) to add an item")
print("(2) to delete an item at index")
print("(3) to remove the last item")
print("(4) to sort the list")
print("(5) To print the list")

choice = int(input("Choose an option: "))

if choice == 1:
  task = input("Enter a task: ")
  tasks.append(task)
  print(tasks)

elif choice == 2:
  index = int(input("Enter the index to delete: "))
  if 0 <= index < len(tasks):
    del tasks[index]
    print(tasks)
  else:
    print("Invalid index")

elif choice == 3:
  if tasks:
    tasks.pop()
    print(tasks)
  else:
    print("List is empty")

elif choice == 4:
  tasks.sort()
  print(tasks)

elif choice == 5:
  print(tasks)

else:
  print("Invalid choice")
