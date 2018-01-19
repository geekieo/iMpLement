class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_trainscations = []
		
	def new_block(self):
		# 创建新块，加入链条
		pass
		
	def new_transaction(self):
		# 添加一次新的交易到交易列表中
		pass
		
	@staticmethod
	def hash(block):
		# 计算一个 bolck 的 hash 值
		pass
	
	@property
	def last_block(self):
	# 返回链条中最后一个 block
		pass