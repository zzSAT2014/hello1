from random import random
from bisect import bisect
#weighted choices generator
def separate(lis):
	'''input: a list of tuples (weights , values)

	output : weights_list and value_list'''
	weights = []
	values = []
	for atom in lis:
		values.append(atom[1])
		weights.append(atom[0])
	return (weights,values)


def weighted_choice(lis,num = 1):
	'''input: a list of tuples (values , weights), 
		num --> number of output words, indexes

	note: repitiion is disallowed			
	output: a list of output words'''
	weights, values = separate(lis)
	total = 0
	cum_weights = []
	output = set()
	for w in weights:
		total += w
		cum_weights.append(total)

	while len(output) < num:
		x = random() * total
		i = bisect(cum_weights, x)
		output.add(values[i])
	return list(output)



def test_weighted_choices():
	lis = [(1,'jiba'),(1,'fuck'),(1,'simple'),(7,'dick')]
	count = 0
	for i in xrange(1000000):
		#print weighted_choice(lis,num = 1)
		if 'dick' in weighted_choice(lis,num = 2): count+=1
	return count/float(1000000)


#print test_weighted_choices()