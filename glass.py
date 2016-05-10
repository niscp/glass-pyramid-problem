__author__ = 'Nishank Singh'

def findWater(h,x,c):
	""" Function to calculate water in each glass. This function returns a list with the values of
	water value in each glass.
	This function accepts three inputs:
	h -- number of levels of glass
	x -- total amount of water in a jug
	c -- capacity of water in a glass
	""" 

	# find the total number of elements in a pyramid of glass.
	num = h*(h+1)/2

	#initialise this list of glass with the value of zero for each glass. 
	glass_list = [0]*num
	index = 0
	glass_list[index] = x
	level =1 

	# Loop for all levels or until the water is finished
	while level <= h and x != 0.0:
		col =1
		while col <= level:
			x = glass_list[index]
	

	#Assign the water equals to capacity of glass if it is available in jug else put it completely.
			if x >= c:
				glass_list[index] = c
			else:
				glass_list[index] = x
			if x >=c:
				x = x-c
			else:
				x = 0
	

	#Avoid the out of range glasses  			
			if index+level+1 <= num:	
				glass_list[index+level] = glass_list[index+level] + x/2
				glass_list[index+level+1] = glass_list[index+level+1] + x/2
			col = col + 1
			index = index + 1
		level =level + 1
	return glass_list
			
h = int(raw_input('Enter number of levels \n'))
x = float(raw_input('Enter total water in jug \n'))
c =float(raw_input('Enter capacity of glass \n'))
print findWater(h,x,c)				

