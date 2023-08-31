text = input("Enter Text: ")
words = len(text.split())
sentences = text.count('.') + text.count('!') + text.count('?') + text.count(',') + 1

L = (len(text) / words) * 100
S = (sentences / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8

grade = round(index)

if grade >= 16:
  print("Grade 16+")
elif grade < 1:
  print("Before Grade 1")
else:
  print("Grade", grade)