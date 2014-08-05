#hw2.1
inp = raw_input("Enter Hours:")
rates = raw_input("Enter Rates:")
print float(inp)*float(rates)

fh = open("c:/Python27/Homeworks/romeo.txt", "r")

count = 0
for line in fh:
    print line.strip()
    count = count + 1

print count,"Lines in the file."

#hw3.1
try:
	inp = raw_input("Enter Hours:")
	h = float(inp)
	inp = raw_input("Enter Rate: ")
	r = float(inp)
except:
	print "Error, please enter numeric input"
	quit()
	
if h > 40 :
	pay = 40*r +(h-40)*r*1.5
else :
	pay = h*r
print "Finished with computepay", pay

#hw3.2
grade = raw_input("Enter Grades: ")
g = float(grade)
if g >= 0.9 :
	print "A"
elif g >= 0.8 :
	print "B"
elif g >= 0.7 :
	print "C"
elif g >= 0.6 :
	print "D"
else :
	print "F"
	
	
	
#hw4
def computepay(h, r) :
	print "In computepay", h, r
	if h > 40 :
		pay = 40*r +(h-40)*r*1.5
	else :
		pay = h*r
	print "Finished with computepay", pay
	return pay

try:
	inp = raw_input("Enter Hours:")
	hours = float(inp)
	inp = raw_input("Enter Rate: ")
	rate = float(inp)
except:
	print "Error, please enter numeric input"
	quit()
	
print "In the main code", hours, rate
pay = computepay(hours, rate)
print "we are back", pay

#hw5
print "Hello"
count = 0
total = 0
while True:
	inp = raw_input("Enter a number:")
	
	#Handle the edge cases
	if inp == "done" : break
	if len(inp) <  1 : break # Check for empty line
	
	#Do the work
	try: 
		num = float(inp)
	except: 
		print "Invalid input"
		continue
	count = count + 1
	total = total + num
	print num, total, count

print "Average = ", total / count

#hw5.2
largest = 6
smallest = 4
while True:
    num = raw_input("Enter a number: ")           
        
    if num == "done" : break
    if len(num) <  1 : break # Check for empty line    
    
    try:
        number = float(num)
    except:
        print "Invalid input"
        continue

    if number >= largest :
    	largest = number 
    elif number < smallest :
        smallest = number 
            	
print "Maximum is", int(largest)
print "Minimum is", int(smallest)

#hw6.2
x = "X-DSPAL-Confidence:   0.84576"
print x
pos = x.find(':')
print pos
print x[pos+1:]
num = float(x[pos+1:])
print num, type(num)

#hw7.2
#fhand = open('mbox.txt')
#for line in fhand:
#	line = line.rstrip()
#	if not line.startswith('Front:'):
#		continue
#	print line
	
#try:
#	fhand = open(fname)
#except:
#	print 'File cannot be opened:', fname
#	exit()
#count = 0 
#for line in fhand:
#	if line.startswith('Subject:'):
#		count = count + 1
#print 'There were', count, 'subject lines in', fname

#hw7.1
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fhand:
	print line.upcase()
	 


