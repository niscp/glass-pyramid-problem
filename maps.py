__author__ = 'Nishank Singh'

def nValue(exp):
	"""
	returns the value of north movement (+1 for north and -1 for south)
	"""
	if exp == 'N' or exp == 'n':
		return 1
	elif exp == 'S' or exp == 's':
		return -1
def eValue(exp):
	"""
	returns the value of east movement(+1 for east and -1 for west)
	"""
	if exp == 'E' or exp == 'e':
		return 1
	elif exp == 'W' or exp == 'w':
		return -1

def getDirection(exp):
	"""
	returns the list  which provide shortest possible route to reach back to starting place. 
	"""
	east = 0
	north = 0
	l = len(exp)
	s_list = []

	for i in exp:
	
	#Compute the value of north/south movement for the whole sequence
		if (i =='N' or i == 'n') or (i =='S' or i == 's'):
			north = north + nValue(i)
	
	#Compute the value of east/west movement for the whole sequence
		if (i =='E' or i == 'e') or (i =='w' or i == 'W'):
			east = east + eValue(i)
	
	if east > 0:
		for i in range(east):
			s_list.append('W')
	elif east < 0:
		east = -east
		for i in range(east):
			s_list.append('E')
	if north>0:
		for i in range(north):
			s_list.append('S')
	elif north < 0:
		north = -north
		for i in range(north):
			s_list.append('E')
	return s_list



a = raw_input('Please enter long distance map including only N,E,W,S\n')

n = getDirection(a)
print 'Shortst Possible route is \n'
print ''.join(n)
