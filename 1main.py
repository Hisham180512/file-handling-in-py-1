#NOTEBOOK MERGER
import os

#PART -- 1 = Read with Autoclose
print("=== Science Notes ===")
with open("science.txt", "r") as f:
        for line in f:
         print(line.strip())
print()

#PART -- 2 = Count words in each line
print("=== Word Count ===")
with open("maths.txt", "r") as f:
     for line in f:
          words = line.split()
          print(len(words ), "->", line.strip())
     print()

#PART -- 3 = Check and merge
print("=== Merging Notes ===")
if os.path.exists("all-notes.txt"):
     print("all-notes.txt already exists. Overwriting...")
else:
        print("all-notes.txt does not exist. Creating new file...")
        content = ""
with open("science.txt", "r") as f:
        content += "---science-notes.txt---\n"
        content += f.read() + "\n"
        with open("maths-notes.txt", "r") as f:
         content += "---maths-notes.txt---\n"
         content += f.read() + "\n"
         with open("all-notes.txt", "w") as out:
              out.write(content)
              print("saved to all-notes.txt")
              print()

              #PART -- 4 = Delete merged file
              if os.path.exists("all-notes.txt"):
                   os.remove("all-notes.txt")
                   print("all-notes.txt deleted.")
              else:
                   print("all-notes.txt does not exist.") 