import csv
f = open("eggs.csv", "r")
reader = csv.reader(f, delimiter=',')
for line in reader:
	print(line)

