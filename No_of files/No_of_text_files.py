#! usr/bin/python3.5
import os
count=0
for(dirname,dirs,files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.txt'):
			count=count+1
			print('Files:')
			print(count)




