#NOTES CLEANER
#PART - 1 = SNEEK PEEK
n = int(input("How many characters to preview? "))
file = open("classnotes.txt ", "r")
print(file.read(n))
file.close()
print()
#PART -- 2 = ALL LINES AS A LIST
file = open("classnotes.txt ", "r")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range (len(lines)):
 print(i + 1, "->", lines[i].strip())
print()

#PART -- 3 = Filter lines
word = input("Skip items starting with: ")
file = open("classnotes.txt ", "r")
for line in file:
 if line.startswith(word):
  print("Skip ->", line.strip())
 else:
    print("Keep ->", line.strip())
    file.close()
 print()

 #PART -- 4 = copy odd lines to new file
 file = open("classnotes.txt ", "r")
 lines = file.readlines()
 file.close()
 out = open("odd-lines.txt", "w")
 for i in range(0, len(lines), 2):
  out.write(lines[1])
  out.close()
print("Odd lines saved to odd-lines.txt")






    