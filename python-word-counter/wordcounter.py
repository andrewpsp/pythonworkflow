article = raw_input("Enter File Name:")
if len(article) < 1 : article = "healtharticle.txt"
fileopener = open(article, "r")
text = fileopener.read()
words = text.split()


counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
    	bigword = word
        bigcount = count

print bigword, bigcount
