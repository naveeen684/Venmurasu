import glob

score = []

# get all text files from data folder and combine it into single list
for file in glob.glob("data/*.txt"):
    print(file)
    with open(file, 'r', encoding="utf-8") as f:
        score = score+[line.rstrip('\n') for line in f]


with open("combined/total.txt", "w", encoding="utf-8") as f:
    for s in score:
        f.write(str(s) + "\n")


print("Total no of blog entries: ", len(glob.glob("data/*.txt")))
print("Total no of words: ", len(score))
