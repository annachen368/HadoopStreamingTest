def mapper(lines):
	for line in lines:
		line = line.strip()
		words = line.split()
		for word in words:
			print('%s\t%s' % (word, 1))
