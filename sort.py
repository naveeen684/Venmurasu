import numpy
import operator
import tamil


with open("combined/total.txt", "r", encoding="utf-8") as file:
    words = [line.rstrip('\n') for line in file]


word_array = numpy.array(words)
print('Count of the total Words found: ', len(word_array))


print('Find N Most Occurring Words')
n = int(input('Enter N:'))
unique_words = {}
for word in word_array:
    unique_words[word] = 1 + unique_words.get(word, 0)

print('Count of the unique Words found: ', len(unique_words))

with open("result/Top%sMostOccurringWords.txt" % n, "w", encoding="utf-8") as f:
    i = 1
    for l in sorted(unique_words.items(), reverse=True, key=operator.itemgetter(1))[:n]:
        print(i, " "+str(l[0])+':'+str(l[1]))
        f.write(str(l[0])+':'+str(l[1]) + "\n")
        i += 1

word_array = {k: v for k, v in sorted(unique_words.items(
), reverse=True, key=lambda item: len(tamil.utf8.get_letters(item[0])))}

with open("result/sorted.txt", "w", encoding="utf-8") as f:
    for s in word_array.items():
        f.write(str(s[0]) + "-" +
                str(len(tamil.utf8.get_letters(s[0])))+"-"+str(s[1]) + "\n")


print('Find M Longest Words')
m = int(input('Enter M:'))


with open("result/Top%sLongestWords.txt" % m, "w", encoding="utf-8") as f:
    i = 1
    for s in word_array.items():
        if(i <= m):
            print(i, " "+str(s[0]) + " - " +
                  str(len(tamil.utf8.get_letters(s[0]))))
            f.write(str(s[0]) + " - " +
                    str(len(tamil.utf8.get_letters(s[0]))) + "\n")
            i += 1
        else:
            break
