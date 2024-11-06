import heapq 


class node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		
		self.freq = freq 
		self.symbol = symbol 
		self.left = left 
		self.right = right 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 

 
def printNodes(node, val=''): 

	# huffman code for current node 
	newVal = val + str(node.huff) 

	# if node is not an edge node 
	# then traverse inside it 
	if(node.left): 
		printNodes(node.left, newVal) 
	if(node.right): 
		printNodes(node.right, newVal) 

		# if node is edge node then 
		# display its huffman code 
	if(not node.left and not node.right): 
		print(f"{node.symbol} -> {newVal}") 


 
chars = ['a', 'b', 'c', 'd'] 
freq = [12,13,24,74] 
nodes = [] 

# converting characters and frequencies 
# into huffman tree nodes 
for x in range(len(chars)): 
	heapq.heappush(nodes, node(freq[x], chars[x])) 

while len(nodes) > 1: 

	# sort all the nodes in ascending order 
	# based on their frequency 
	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 

	# assign directional value to these nodes 
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create 
	# new node as their parent 
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

	heapq.heappush(nodes, newNode) 

printNodes(nodes[0]) 
