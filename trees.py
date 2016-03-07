class Node():
	def __init__(self,key):
		self.value = key
		self.left = None
		self.right = None
def insert(root,node):
	if root is None:
		root = node
	else:
		if root.value < node.value:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)
def inorder(root):
	if root:
		inorder(root.left)
		print root.value
		inorder(root.right)

def preorder(root):
	if root:
		print root.value
		preorder(root.left)
		preorder(root.right)

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inorder(r)
print "\n"
preorder(r)