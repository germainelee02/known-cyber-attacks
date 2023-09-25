import os

entries = os.listdir('.')
f = open('compile.md', 'w')
for entry in entries:
    if entry[:4].isdigit():
	    f.write(entry)
	    f.write('<br>')
f.close()

