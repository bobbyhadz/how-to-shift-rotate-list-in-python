# How to shift (rotate) a List in Python

# ✅ Move the first list item to the back
a_list = [1, 2, 3, 4, 5]


new_list = a_list[1:] + a_list[:1]
print(new_list)  # 👉️ [2, 3, 4, 5, 1]


#  -----------------------------------------

# ✅ Move the last list item to the front
a_list = [1, 2, 3, 4, 5]

new_list = [a_list[-1]] + a_list[:-1]
print(new_list)  # 👉️ [5, 1, 2, 3, 4]