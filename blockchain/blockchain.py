import hashlib
import json
from time import time

"""
block 的例子
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
		self.current_transactions = []
		
		# 创建起源区块
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self, proof, previous_hash = None):
		"""
		在链条中创建新区块

		param proof: <int> 靠 PoW 算法给出来的 proof 值
		param previous_hash:(Optional) <str> 前一区块的 hash 值
		return: <dict> 新块

		"""
		block = {
			'index':len(self.chain)+1,
			'timestamp': time(),
			'transactions':self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]), 
		}
		# 重置当前的交易列表
        self.current_transactions = []

        self.chain.append(block)
        return block

	def new_transaction(self,sender, recipient, amount):
		"""
		在交易列表中创建一个新交易，并将交易块的索引，交给下一个创建的区块
		
		param sender: <str> 发出人地址
		param recipient: <str> 接收人地址
		param amount: <int> 金额
		return: <int> 保存这一次交易的块的索引
		"""
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
		})
		
		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		"""
        给一个块创建一个sha-256的hash值

        :param block: <dict> 整个块
        :return: <str>
        """
        # 我们必须确保dict是有序的，否则会得到不一致的hash值
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
	
	@property
	def last_block(self):
		# 返回链条中最后一个 block
		return self.chain[-1]