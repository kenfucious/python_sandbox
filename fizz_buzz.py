#FizzBuzz 
#Ken Prchal

target = open("fizz_buzz.txt", 'w')

for i in range(1,101):
	if i % 15 == 0:
		print "FizzBuzz"
		target.write("FizzBuzz")
		target.write("\n")
	elif i % 3 == 0:
		print "Fizz"
		target.write("Fizz")	
		target.write("\n")
	elif i % 5 == 0:
		print "Buzz"
		target.write("Buzz")
		target.write("\n")		
	else:
		print i
		target.write(str(i))	
		target.write("\n")


target.close()
