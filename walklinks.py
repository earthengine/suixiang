import os
import re

rootdir = 'D:/work/suixiang'

for subdir,dirs,files in os.walk(rootdir):
	for file in files:
		m = re.match('.*[.]md$',file)
		if m == None:
			continue
		f=open(subdir + '/' + file,'r')
		lines=f.readlines()
		for line in lines:
			m = re.findall('https?[:][/][/][^\'\"<]*[.]md', line);
			if len(m) == 0:
				continue
			for mm in m:
				print mm
		f.close()		