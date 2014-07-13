
class vocabulary_tests_data (object):
	"""
	input:data:[(name, listnum, vocab_test), (), () ]

	date will be supplied as an additional parameter

	output: generate txt file, same as vo_input_temp.txt

	"""
	def __init__(self,data,date):
		
		self.vocab_false = None

	def process_line(self,atom):
		name, lis_num, words = atom
		return name + ' '*(20-len(name)) + lis_num + '\t'*4 + repr(words) 


	def content(self,data):
		for i in range(len(data)):#len
			
			for j in range(0,3):
				return data[i][j]	

	def output(self,filename):
		a = open(filename,'a+')
		a.write('date '+date)
		a.write('\n')
		a.write('name' +'\t'*4+ 'listnum' + '\t'*10+'vocab,test' +'\t'*14+ 'vocab,false')
		a.write('\n')
		for atom in data:
			print atom#iterable
			a.write(vocabulary_tests_data.process_line(self,atom)+'\n')
		a.close()





data = [('shenxin','l1',['B1','B2']*5),('christopher','l2',['C1','C2']*5)]
date = '07.11.2014'
a = vocabulary_tests_data(data,date)
filename = 'foo'
a.output(filename)

