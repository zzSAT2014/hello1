import re
from les3 import *
from copy import copy
import os
import string
from word_bank import dictionary


dictionary = dictionary()


def print_dict(dic):
	separator = '-->'
	indentation = '    '
	#@trace
	def inner(dic,inlevel=0):
		if type(dic) is not dict: print indentation*inlevel+repr(dic)
		else:
			for key in dic:
				print indentation*inlevel + repr(key) + separator
				
				inner(dic[key],inlevel+1)
	inner(dic)

class data(object):
	def __init__(self,filename,mode = 'r+'):
		'''opens up the file in r+ mode, unless otherwise specified, i.e use a+ to create file'''
		self.file = open(filename,mode)
		self.name = filename
		string=self.file.read().strip()
		self.info =  eval(string)
		self.file.close()

	def update(self, func, output = 'newmaster'):
		'''modify the input and save it'''
		func(self.info)
		#print_dict(self.info)
		self.file = open(output,'a+')
		os.remove(output)
		self.file = open(output,'a+')
		#print self.info
		self.file.write(repr(self.info))
		self.file.close()

	def get_student(self,name):
		'''return all information about the student'''
		#print_dict(self.info[name])
		return self.info[name]
	def __str__(self):
		print_dict(self.info)
		return 'end'

def csub_dict(dic,lis,value):
	'''create a subdictionary if there there is not one'''
	#print '\t\tvalue in c_sub\t%s'%value
	if len(lis) == 0:
		return value
	else:
		dic[lis[0]] = {} 
		dic[lis[0]] = csub_dict(dic[lis[0]],lis[1:],value)
		#print '\t\tindide c_sub \t %s'%(dic)
		return dic
#@trace
def sub_dict(dic,lis,func=lambda x:x,value=None,copy=None):
	'''dic target dicttionary
		lis --> target directory
		mutate the bottom value using func'''
	#print lis
	#print '\tvalue in sub\t%s' %(value)
	if lis[0] not in dic: 
		#print 'creat'
		csub_dict(dic,lis,value)
		#print 'inside sub_dic%s\t'%(dic)
	#print dic
	if len(lis) == 1:
		dic[lis[0]] = func(dic[lis[0]])
	else: sub_dict(dic[lis[0]],lis[1:],func,value)

def sub_test():
	a = {1:{2:{3:'b'}},2:{3:4,5:6}}
	f = lambda x: 1
	b=sub_dict(a,[1,2,3],func = f,value='a')
	b = sub_dict(a,[2,3],func=f)
	b = sub_dict(a,[3,4])
	print a
#sub_test()
splitter= lambda string: re.split(',',string)
input_proce = lambda line: map(splitter,line.split())


class txt_parser(object):
	'''return a parser function which mutates the info stored''' 
	def __init__(self,txtfile):
		'''parse a the input txt file into a list of tuples directory,value pair [(directory,value),(),()]
		directory a list of strings'''
		self.file = open(txtfile,'r')
		self.info = []
		for index,line in enumerate(self.file):
			if index == 0:
				#print line 
				#print 'hi'
				dirs = input_proce(line)
			else:
				line = input_proce(line)
				for i2,atom in enumerate(line):
					if i2 == 0: name = atom
					else:
						self.info.append((name+dirs[i2],atom))
		#print self.info
	def parser(self):
		return None


def test_txt_parser():
	input= 'input.txt'
	a=txt_parser(input)
	print a.info
#test_txt_parser()

class basic_parser(txt_parser):
	'''parse level 1 information,i.e only one element like name, age, sex etc'''
	def parser(self):
		def inner(dic):
			'''merely mutate value, does not return anything'''
			for directory,value in self.info:
				sub_dict(dic,directory,func = lambda x: value[0])
		return inner
 
def phoneix(filename):
	'''destory a file and create an empty file with the same name

	return --> the new file object'''
	os.remove(filename)
	return open(filename,'a+')


def word_add(date):
	def inner(tup):
		'''change the inner tuple corresponding to each word'''
		num, lis = tup
		lis.append(date)
		num = len(lis)
		return (num,lis)
	return inner


def appender(x):
	'''appending function with stuff to be appended as function constructor'''
	def inner(y):
		y.append(x)
		return y
	return inner






def index_2_word(lisNum):
	def inner(coor):
		return dictionary.get_w((lisNum,coor))
	return inner
# l_trans=index_2_word('l5')
# print l_trans('D2')

class vocab_parser(txt_parser):
	def __init__(self,filename):
		'''custom designed vocab template processing toool'''
		self.file = open(filename,'r')
		self.temp = {}
		self.info = []#(flag(wheter it is append),directory,result)


	def parser(self):
		def inner(dic):
			for index,line in enumerate(self.file):
				if index == 0: date=line.split()[1]
				elif index == 1: continue
				else:
					print line 
					name,listNum,tested,wrong = line.split()
					l_trans = index_2_word(listNum)
					tested = map(l_trans,re.split(',',tested) ) 
						
					if wrong == 'None': wrong = []
					
					if len(wrong) >0: wrong = map(l_trans,re.split(',',wrong))	
					correct = [a for a in tested if a not in wrong]#maybe i will add untested word later
					correctRate = len(correct)/float(len(tested))
					sub_dict(dic,[name,'vocab','date',date],func = appender((listNum,correctRate)),value=[])
					#print dic
					sub_dict(dic,[name,'vocab','list',listNum],func = appender((date,correctRate)) ,value=[])
					#print dic
					for cate,identi,flag in [(wrong,'wrong',False),(correct,'correct',True)]:
						for word in cate:
							#translate(word)
							sub_dict(dic,[name,'vocab','word',word,identi],func=word_add(date) ,value = (0,[]))
							sub_dict(dic,[name,'vocab','word',word,'mostRecent'],func =lambda x: (flag,date),value=())
		return inner



def test_v_parser():
	filename = 'sb12014.7.11'
	a = 'zhe		  	   l1			   E1,E2,E3,E4,E5								E1,E2'
	my_info = {}
	#parser = vocab_parser(filename).parser()
	# parser(my_info)
	# print_dict(my_info)
	a = data('test')
	#a.update(parser)
	print a
	print_dict(a.get_student('zhe'))
	# name,date,listNum,correctRate ='zhe','11.11','l1',0.9
	# sub_dict(my_info,[name,'vocab','list',listNum],func = appender((date,correctRate)),value=[])
	# print my_info
	# sub_dict(my_info,[name,'vocab','date',date],func = appender((listNum,correctRate)),value=[])
	# print my_info
test_v_parser()
#def update_file(target,*inputs):


filename = 'test'
allData = data(filename)


