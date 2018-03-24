class Queue(object):
	'''Queue data structure(First In First Out)'''
	def __init__(self):
		'''Creates a python list to maintain the q elements'''
		self.q_elements = []
	def __len__(self):
		'''returns integer -> no of elements in list'''
		return len(self.q_elements)
	def enqueue(self, data):
		'''Add elements to the queue'''
		self.q_elements.extend(data) if type(data) is list else self.q_elements.extend([data])
	def dequeue(self):
		'''Dequeue elements one by one'''
		return self.q_elements.pop(0) if self.q_elements else None
	def IsQueueEmpty(self):
		'''check if q is empty'''
		return False if self.q_elements else True
	def clear(self):
		'''remove all elements in q'''
		del self.q_elements[:]
	def __str__(self):
		'''print q elements'''
		return "The elements in the queue are: {}".format(self.q_elements) if self.q_elements else "The queue is empty"

	

if __name__ == "__main__":
	testq = Queue()
	print Queue.__dict__['__dict__']
	print Queue.__dict__['__dict__'].__get__(testq)
	print testq, len(testq)
	print testq.dequeue()
	testq.enqueue(10)
	print testq.IsQueueEmpty()
	print testq, len(testq)
	testq.enqueue([20,30,40])
	print testq, len(testq)
	testq.dequeue()
	print testq, len(testq)
	print Queue.__dict__['__dict__'].__get__(testq)
	testq.clear()
	print testq.IsQueueEmpty(), len(testq)





'''
Notes: 
------
Why class name(object) is necessary? object - just denotes it is a new style calss in python. and object is the moteher of all classes. So, it inerits from that. 
https://stackoverflow.com/questions/7375595/class-with-object-as-a-parameter?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
How to use format 
https://pyformat.info/

https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

Queue.__dict__

https://stackoverflow.com/questions/6020960/python-dictionary-as-instance-variable
'''
