import sys
import re
state={}
def parse(statement,pos,statements,s1,s2):
	c=0
	for i in range (pos,len(statements)):
		if s1 in statements[i]:
			c=c+1
		elif s2 in statements[i]:
			c=c-1
			if c==0:
				index=i
				break
	return index			

class Program:
	def __init__(self,code):
		self.code=code
	def eval(self):
		cstatement=CompoundStatement(self.code.split("\n"))     
		cstatement.eval()

class CompoundStatement:
	def __init__(self,code):
		self.statements=code
	def eval(self):
		pos=0
		for i in range(0,len(self.statements)):
			if "print" not in self.statements[i]: 
				self.statements[i]=re.sub(r'\s+','',self.statements[i])	
			

		while pos<len(self.statements):
			string=self.statements[pos] 
			#print(state)
			if "while" in string:
				index=parse(string,pos,self.statements,"while","done")
				obwhile=While(self.statements[pos:index+1])  	
				obwhile.eval()
				pos=index
			elif "if" in string:
				index=parse(string,pos,self.statements,"if","fi")
				ifelse=IfElse(self.statements[pos:index+1])  	
				ifelse.eval()
				pos=index
			
			if ":=" in string:
				ass=Assignment(string)
				ass.eval()

			elif "println" in string:
				obprintln=Println(string)
				obprintln.eval()
			elif "print" in string:	
				obprintln=Print(string)
				obprintln.eval()

			pos=pos+1


class While:
	def __init__(self,statements):
		self.statements=statements
	def eval(self):
		condition=self.statements[0]
		#print(condition)
		l=len(self.statements)
		i=condition.find("do")
		condition=condition[len("while"):i]
		#print(condition)
		while Expression.eval(condition):
			c=CompoundStatement(self.statements[1:l-1])
			c.eval()


class IfElse:
	def __init__(self,statements):
		self.statements=statements
	def eval(self):
		condition=self.statements[0]
		#print(condition)
		l=len(self.statements)
		i=condition.find("then")
		condition=condition[len("if"):i]
		#print(condition)
		if Expression.eval(condition):
			c=CompoundStatement(self.statements[1:self.statements.index('else')])
			c.eval()

		if (not Expression.eval(condition)): 	
			c=CompoundStatement(self.statements[self.statements.index('else'):self.statements.index('fi;')])
			c.eval()

class Assignment:
	def __init__(self,statement):
		self.text=statement         
	def eval(self):
		left=""
		right=""
		i=self.text.find(":")
		j=self.text.find(";")
		right=self.text[i+2:j]
		result=Expression.eval(right)
		left=self.text[:i]      
		state[left]=result        
	




#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
##Each of expression evaluationss$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class Constant:
	def eval(text):
		#print(text)
		if(text.isalnum()):
			return int(text)
		else:
			return float(text)

class Var:
	def eval(text):
		if text in state:
			return state[text]


class Plus():
	def eval(text):
		idx=text.index('+')  
		return(Expression.eval(text[:idx])+Expression.eval(text[idx+1:]))


class Minus():
	def eval(text):
		idx=text.index('-')
		return(Expression.eval(text[:idx])-Expression.eval(text[idx+1:]))

class Multiply():
	def eval(text):
		idx=text.index('*')
		return(Expression.eval(text[:idx])*Expression.eval(text[idx+1:]))

class Divide():
	def eval(text):
		idx=text.index('/')
		return(Expression.eval(text[:idx])//Expression.eval(text[idx+1:]))


class Greater():
	def eval(text):
		return(Expression.eval(text.split('>')[0])>Expression.eval(text.split('>')[1]))
	
class Less():
	def eval(text):
		return(Expression.eval(text.split('<')[0])<Expression.eval(text.split('<')[1]))

class Greaterequal():
	def eval(text):
		return(Expression.eval(text.split('>=')[0],)>=Expression.eval(text.split('>=')[1]))

class Lessequal():
	def eval(text):
		return(Expression.eval(text.split('<=')[0])<=Expression.eval(text.split('<=')[1]))

class Notequal():
	def eval(text):
		return(Expression.eval(text.split('!=')[0])is not Expression.eval(text.split('!=')[1]))

class Equal():
	def eval(text):
		return(Expression.eval(text.split('==')[0]) is Expression.eval(text.split('==')[1]))



class Expression(Constant):
	
	def eval(text):
		#print(text)
		if '!=' in text:
			return Notequal.eval(text)
		elif '==' in text:
			return Equal.eval(text)
		elif '>=' in text:
			return Greaterequal.eval(text)
		elif '<=' in text:
			return Lessequal.eval(text)	 
		elif '>' in text:
			return Greater.eval(text)
		elif '<' in text:
			return Less.eval(text)  
		elif text.isalpha(): 
			return Var.eval(text)
		elif text.isnumeric():
			return Constant.eval(text)                 
		elif "+" in text:
			return Plus.eval(text)
		elif "-" in text:
			return Minus.eval(text)
		elif "*" in text:
			return Multiply.eval(text)
		elif "/" in text:
			return Divide.eval(text)               
		



class Println:
	def __init__(self,text):
		self.text=text
	def eval (self):
		br=self.text.index('(')
		cb=self.text.index(')')
		val=self.text[br+1:cb]
		if len(val)==0:
			print()
		else:	
			words=val.split(",")        
			for i in range (0,len(words)):
				self.recprint(words[i])


	def recprint(self,word):
		c=""                
		if word[0]=='"':
			for i in range (1,len(word)-1):
				c+=word[i]
			print(c)
		else:
			result=Expression.eval(word)
			print(result)
	



class Print:
	def __init__(self,text):
		self.text=text
	def eval (self):
		br=self.text.index('(')
		cb=self.text.index(')')
		val=self.text[br+1:cb]
		if len(val)==0:
			print(end="")
		else:
			words=val.split(",")        
			for i in range (0,len(words)):
				self.recprint(words[i])


	def recprint(self,word):
		c=""                
		if word[0]=='"':
			for i in range (1,len(word)-1):
				c+=word[i]
			print(c,end="")
		else:
			result=Expression.eval(word)
			print(result,end="")



filename = "code.imp"        
code = open(filename).read()
prog=Program(code)
prog.eval()
