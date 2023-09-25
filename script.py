import os

entries = os.listdir('.')
f = open('compile.md', 'w')
for entry in entries:
	f.write(entry)
	f.write('\n')
f.close()

