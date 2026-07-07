def remove_duplicates(s):
  return "".join(dict.fromkeys(s))

input = "programming"
print(f"Output: {remove_duplicates(input)}")