#This program used to remove redundant words in a sentence.
s = input("Please input you text:   ")
w = s.split(" ")
print (" ".join(sorted(list(set(w)))))