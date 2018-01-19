"""
一个 block 的例子
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
"""

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