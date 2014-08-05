#10.2
name = raw_input("Enter file:")
if len(name) == 0 : name = "c:/Python27/homeworks/mbox-short.txt"

handle = open(name)

counts = dict()
list = list()

for line in handle:
	if not line.startswith('From '): continue
	words = line.split()
	time = words[5].split(':')
	hours = time[0]
	counts[hours] = counts.get(hours, 0) + 1
	
for key, value in counts.items():
    list.append((key,value))

for key, value in sorted(counts.items()):
    print key, value

#10.2 again
name = raw_input("Enter file:")
if len(name) < 1 : name = "c:/Python27/homeworks/mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle :
    if line.startswith("From "):
        words = line.split()[5].split(':')[0]
        counts[words] = counts.get(words[1],0) + 1

lst = list()
for key, val in counts.items():
    lst.append( (key, val) )

for key, val in sorted(counts.items()):
    print key, val




#hw10.2 sample
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
		
list = list()
for key, val in counts.items():
	list.append((val, key))
	
lst.sort(reserse = True)

for val, key in lst[:10]:
	print key, val



#hw9.4
name = raw_input("Enter file:")
if len(name) < 1 : name = "c:/Python27/homeworks/mbox-short.txt"
handle = open(name)
lst = list()
#count = 0
for line in handle:
	line = line.rstrip()
	if not line.startswith('From:'): continue
	words = line.split()
	lst.append(words[1])
	#print words[1]
	#count = count + 1
#print "There were", count, "lines in the file with From as the first word"

#print lst
counts = dict()
for word in lst:
	counts[word] = counts.get(word, 0) + 1
#print counts

bigcount = None
bigword = None
for word, count in counts.items():
	if bigcount == None or count > bigcount:
		bigword = word
		bigcount = count
		
print bigword, bigcount


#hw9.1
#name = raw_input("Enter file:")
#handle = open(name)
#text = handle.read()
#words = text.split()

#counts = dict()
#for word in words:
#	counts[word] = counts.get(word, 0) + 1
	
#bigcount = None
#bigword = None
#for word, count in counts.item():
	#if bigcount == None or count > bigcount
	#	bigword = word
	#	bigcount = count
		
#print bigword, bigcount

#cou = dict()
#for wrd in words:
#	if wrd in cou:
#		cou[wrd] = cou[wrd] + 1
#	else:
#		cou[wrd] = 1
#	print wrd, cou[wrd]
	





#hw8.4
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip()
	words = line.split()
	#print words
	for word in words:
		lst.append(word)
lst = list(set(lst))
lst.sort()
print lst

#hw8.5
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "c:/Python27/Homeworks/mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
	line = line.rstrip()
	if not line.startswith('From:'): continue
	words = line.split()
	print words[1]
	count = count + 1
print "There were", count, "lines in the file with From as the first word"



#abc = 'With three words'
#stuff = abc.split()
#print stuff
#print len(stuff)
#print stuff[0]
#
#fhand = open('c:/Python27/Homeworks/mbox-short.txt')
#for line in fhand:
#	line = line.rstrip()
#	if not line.startswith('From'): continue
#	words = line.split()
#	print words[2]






