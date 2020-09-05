def first_occurrence(input_string):
  char_count = {}
  
  # Build the character count dicitonary
  for c in str.lower(input_string):
    if c not in char_count:
      char_count[c] = 1
    else:
      char_count[c] += 1
  
  # Rewrite the string in order of number of occurrences and order from the inputted string
  char_to_count_mapping = map(lambda x: (x, char_count[str.lower(x)]), input_string)
  sorted_map = sorted(char_to_count_mapping, key = lambda x:x[1])
  rewritten_chars = [c for c,_ in sorted_map]
  
  # Print the first character that is not repeated
  print(rewritten_chars[0])

  # Print the rewritten string
  print("".join(rewritten_chars))

def main():
  s = str(input("Enter the string:"))
  first_occurrence(s)

if __name__ == "__main__":
    main()