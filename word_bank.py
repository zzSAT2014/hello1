import re
from collections import defaultdict

def read_file(file_name):
	"""
	read file and output data in the form of lists.

	"""
	with open(file_name) as f:
		data=f.readlines()
	regex = re.compile(r'[\t;]')
	for i in xrange(len(data)):
		data[i] = regex.sub(' ',data[i])
	return data

#print read_file("word_list")
        


def divide_list(data):
	"""
	Input: word list

	Output: split the word list

	"""
	word_list = []
	temp = []
	for i in xrange(len(data)):
		if "@List" in data[i]:
			word_list.append(temp)
			temp = []
		else:
			temp.append(data[i])
	return word_list

#print divide_list(read_file("word_list"))

def trans(row_num,col_num):
	'''translate column and row number into user_friendly number'''
	coltab = {1:'A',2:'B',3:'C',4:'D'}
	return coltab[col_num]+str(row_num)

def generate_dict(word_lists):
	"""
	input: a list of word list
	Output: a dictionary where the keys are tuples(list_num,row_num,col_num),
	and the values are the words.

	"""
	dict = {}
	ldict = defaultdict(list)
	for i in xrange(len(word_lists)):
	    list_num = i + 1
	    for j in xrange(len(word_lists[i])):
			row_num = j + 1
			words = word_lists[i][j].split()
			for k in xrange(len(words)):
				col_num = k + 1
				dict[('l'+str(list_num),trans(row_num,col_num))] = words[k]
				ldict['l'+str(list_num)].append(words[k])
	return dict,ldict


def reverse_dict(dic):
	new = {}
	for key,value in dic.items():
		new[value] = key
	return new



class dictionary(object):
	def __init__(self):
		self.data,self.ldata = generate_dict(divide_list(read_file("word_list")))
		self.rdata = reverse_dict(self.data)
	def get_w(self,index):
		return self.data[index]
	def get_i(self,word):
		return self.rdata[word]
	def get_l(self,lis):
		return self.ldata[lis]


a = dictionary()
#print len(a.get_l('l4'))
#print a.get_w(('l5','D2'))
# # print a.get_i('na\xc3\xafve')
# # print a.get_i('diffident')

	




















