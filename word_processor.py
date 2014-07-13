from collector import *
from weighted_random import weighted_choice
#sub_dict(dic,lis,func=lambda x:x,value=None,copy=None)
#i have these important information
dictionary = dictionary
data = allData

class student(object):
	'''get all inforamtion about an individual student'''
	def __init__(self,name):
		self.info = data.get_student(name)
		self.name = name
	def __str__(self):
		print_dict(self.info)
		return 'end'

class student_vocab(student):
	def __init__(self,name):
		student.__init__(self,name)
		if 'wocab' not in self.info:
			sub_dict(self.info,['vocab','list'],value=())
			sub_dict(self.info,['vocab','word'],value={})
		self.info = self.info['vocab']

#custom designed functions
###############################################################################################to be changed later
eval_most_recent = lambda flag,date: 1
eval_wrong = lambda num, dates: 1
eval_correct = lambda num, dates: 1

def weight_word(dic ,untested = 10):
	'''evaluate all the contents of the dic and return a weight value
	dic --> sucdictionary belonging to the word, includes {correct'''
	if dic is None:
		return untested
	else: 
		weight = 0
		components = ['correct','wrong','mostRecent']
		evalfuncs = [eval_correct, eval_wrong, eval_most_recent]
		for ele,func in zip(components,evalfuncs):
			if ele in dic:
				#print 'ele is -->%s\t, func  is %s' %(ele,func)
				#print '\t testing weighted_word-->%s' %(func(*(dic[ele])))
				#print type
				weight +=  func(*(dic[ele]))
		return weight

trans = lambda word: dictionary.get_i(word)
get_coor = lambda tu: tu[1]


class student_vocab_list(student_vocab):
	

	def __init__(self,name,lis_num):
		'''return student_specific, list_specific information and probabily process it'''
		student_vocab.__init__(self,name)
		self.rel = dictionary.get_l(lis_num)
		temp = self.info['list']
		if lis_num not in temp: 
			self.basic = {}
		else: self.basic = self.info['list'][lis_num]
		self.lis_num = lis_num
		words = self.info['word']
		self.list = []
		self.words = {}
		for word in self.rel:
			if word in words:
				self.words[word] = words[word]
				self.date = words[word]['mostRecent']
		for word in self.rel:
			if word not in words: self.words[word] = None
		#self.words[word] = None           
				#add the last revised time of when needed
		#get list
		for word in self.words.keys():
			self.list.append((weight_word(self.words[word]),word))


	def generate_list(self , num = 10):   
		#smaller num used to for testing, will change to larger value later
		#print self.list

		output = map(trans,weighted_choice(self.list,num = num))
		coordinates = map(get_coor,output)
		return (self.name ,self.lis_num, coordinates)





	# def generate(self,func):
	# 	'''a list '''
gpNamel = ['zhe','chongzhang','zhouhan']
lis_nums =['l1','l2','l3']
def generate_for_lis_groups(gpNamel,lis_nums):
	'''	input: gp --> a list containing all the names inside a group
				lis_num --> a list containing all numbers to be test_student

		output: list containing all information to be printed
	'''
	output = []
	for name in gpNamel:
		for lis_num in lis_nums:
			a = student_vocab_list(name,lis_num)
			output.append(a.generate_list())
	return output


class vocabulary_tests_data (object):
	"""
	input:data:[(name, listnum, vocab_test), (), () ]

	date will be supplied as an additional parameter

	output: generate txt file, same as vo_input_temp.txt

	"""
	def __init__(self,data,date):
		
		self.data = data
		self.date = date

	def process_line(self,atom):
		name, lis_num, words = atom
		return name + ' '*(20-len(name)) + lis_num + '\t'*4 + ','.join(words)

	def output(self,filename):
		a = open(filename,'a+')
		a.write('date '+self.date)
		a.write('\n')
		a.write('name' +'\t'*4+ 'listnum' + '\t'*4+'vocab,test' +'\t'*12+ 'vocab,false')
		a.write('\n')
		for atom in self.data:
			print atom#iterable
			a.write(vocabulary_tests_data.process_line(self,atom)+'\n')
		a.close()

name_gs =['sb1','sb2']
groups = [['zhe','chongzhang'],['zhouhan','zhe']]
lisnum_gs = [['l1', 'l2' , 'l3'],['l4', 'l5']]
date = '2014.7.11'

def generate_list_specific(name_gs,groups,lisnum_gs,date):
	'''generate all txt files need for testing, with name in name_gs+date  as filename'''
	for identifier, groups, lisnums in zip(name_gs,groups,lisnum_gs):
		data = generate_for_lis_groups(gpNamel,lis_nums)
		print data
		a = vocabulary_tests_data(data,date)
		a.output(identifier+date)



generate_list_specific(name_gs,groups,lisnum_gs,date)


def test_student():
	name='zhe'
	a = student_vocab_list(name,'l1')
	#print print_dict(a.words)
	#print a.generate_list()
	gpNamel = ['zhe','chongzhang','zhouhan']
	lis_nums =['l1','l2','l3']
	print generate_for_lis_groups(gpNamel,lis_nums)
#test_student()


