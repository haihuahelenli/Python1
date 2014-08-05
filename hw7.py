#hw8.1
abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]

fhand = open('c:/Pyhton27/Homeworks/mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	print words[2]






#hw7.1
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
	line = line.rstrip()
	print line.upper()

#hw7.2	
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0.0
sum = 0.0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	#print line
	count = count + 1
		#print count
	pos = line.find(':')
	sum = sum + float(line[pos+1:])

print "Average spam confidence:", sum/count




	
	
	
