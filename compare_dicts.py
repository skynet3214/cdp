

def compare_dicts(a,b):
	for c in b.keys():
		if b[c] == a[c]:
			pass
		else:
			return None
	return True

if __name__ == "__main__":
	a = {1:0,2:0,3:0}
	b = {1:0,2:1}

	d = {'a':0,'b':0,'c':0}
	e = {'a':0,'b':1}
	print compare_dicts(d,e)


