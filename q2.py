def find_and_replace(lst, find_val, replace_val):
  """
  Searches for all occurrences of a value (find_val) in a given list (lst)
  and replaces them with a new value (replace_val).

  Args:
    lst: The input list.
    find_val: The value to find.
    replace_val: The value to replace with.

  Returns:
    The modified list.
  """
  if not isinstance(lst, list):
    raise TypeError("The first argument 'lst' must be a list.")

  modified_lst = []
  for item in lst:
    if item == find_val:
      modified_lst.append(replace_val)
    else:
      modified_lst.append(item)
  return modified_lst


#Invoke the find_and_replace function

# scenario 1: replacing 2 with 5 in the list
lst =[1,2,3,4,2,2]
print(f"Original list: {lst}")
newlist = find_and_replace(lst, 2, 5)
print(f"Modified list: {newlist}")

# scenario 2: replacing 'apple' with 'orange' in the list
lst = ['apple', 'banana', 'apple']
print(f"Original list: {lst}")
newlist = find_and_replace(lst, 'apple', 'orange')
print(f"Modified list: {newlist}")