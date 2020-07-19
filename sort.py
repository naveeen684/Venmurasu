import numpy
import operator
import time
import tamil


with open("combined/total.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n') for line in file]


word_array = numpy.array(words)

start = time.time()

word_array = sorted(word_array, reverse=True,
                    key=lambda x: len(tamil.utf8.get_letters(x)))

end = time.time()

print(f"Runtime of the sorting is {end - start}")

with open("result/sorted.txt", "w", encoding="utf-8") as f:
    for s in word_array:
        f.write(str(s) + " - "+str(len(tamil.utf8.get_letters(s))) + "\n")

print('Find N Largest Words')
n = int(input('Enter N:'))


with open("result/Top10LongestWords.txt", "w", encoding="utf-8") as f:
    i = 0
    for s in word_array[:n]:
        print(i, " "+str(s) + " - "+str(len(tamil.utf8.get_letters(s))))
        f.write(str(s) + " - "+str(len(tamil.utf8.get_letters(s))) + "\n")
        i += 1

print('Find M Most Occurring Words')
m = int(input('Enter M:'))
frequency = {}
for word in word_array:
    frequency[word] = 1 + frequency.get(word, 0)


with open("result/Top10MostOccurringWords.txt", "w", encoding="utf-8") as f:
    for l in sorted(frequency.items(), reverse=True, key=operator.itemgetter(1))[:m]:
        print(i, " "+str(l[0])+':'+str(l[1]))
        f.write(str(l[0])+':'+str(l[1]) + "\n")
        i += 1
