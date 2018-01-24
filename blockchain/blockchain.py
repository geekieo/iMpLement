import hashlib
import json
from time import time
from uuid import uuid4
from urllib.parse import urlparse

from flask import Flask, jsonify, request

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		# 创建起源区块
		self.new_block(previous_hash = 1, proof = 100)
		
		self.nodes = set()

	def new_block(self, proof, previous_hash = None):
		"""
		在链条中创建新区块

		param proof: <int> 靠 PoW 算法给出来的 proof 值
		param previous_hash:(Optional) <str> 前一区块的 hash 值
		return: <dict> 新块

		block 的一个例子：
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


	def proof_of_work(self, last_proof):
		"""
		Simple Proof of Work Algorithm:
		简单的工作证据（PoW）算法
			- 找到一个数字 p' ，使得 hash(pp') 的结果里以4个0开头，p是上一块里的p'
			- p是上一块的proof值，p'是新的proof

		:param last_proof: <int>
		:return: <int>
		"""

		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof



	@staticmethod
	def valid_proof(last_proof, proof):
		"""
		验证proof：hash(last_proof,proof)是否以4个0开头

		:param last_proof: <int> 上一个roof
		:param proof: <int> 当前的 Proof
		:return: <bool> True为正确.
        """
		guess = f'{last_proof}{proof}'.encode()	# PEP498 in python 3.6
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000"

	"""
	达成共识
	"""
	def register_node(self, address): 
		"""
        添加新节点到节点列表中
		网络上的每个节点都应该保存其他节点的登记信息。这样的话我们需要更多的http请求节点：
			1./nodes/register 通过url接收一系列的新节点
			2./nodes/resolve 实现我们的共识算法，解决冲突－－确保每个节点都有正确的链条
        
		:param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc)


'''
Blockchain API
描述：使用 flask web 微框架，让我们容易将端口映射到 python 函数的框架，
让我们同我们的区块链通过 web 的 http 请求来通讯.
目标:将一个 server 在区块链网络里成为一个单独节点。

创建三个方法：
/transactions/new 给一个区块创建一个新的交易
/mine 告诉服务器挖出来一个新块
/chain 返回整个区块链
'''
# Instantiate our Node 实例化节点
app = Flask(__name__)

# Generate a globally unique address for this node 给节点取一个随机名字
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain 实例化 Blockchain 类
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    '''
	挖矿节点
	创建 /mine 节点，接收 get 请求
	描述：计算PoW；
		靠给交易信息里加同意给我们1个币来奖励矿工；
		靠把老的加到链条里来组织新的块。
	'''
    # 这里跑pow算法取到下一个proof值
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # 因为找到proof我们必须接收一个奖励 
    # 发送方写0表示这个节点挖了新币
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # 把块加到链条中完成组装
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
	'''
	交易节点
	接收post请求，因为我们要给它发数据

	这是一次交易看起来的样子，用户发给server下面的数据：
	{ “sender”: “my address”, “recipient”: “someone else’s address”, “amount”: 5 }
	'''
	values = request.get_json()
	
	# Check that the required fields are in the POST'ed data
	required = ['sender', 'recipient', 'amount']
	if not all(k in values for k in required):
		return 'Missing values', 400

	# Create a new Transaction
	index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

	response = {'message': f'Transaction will be added to Block {index}'}
	return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    '''
	创建/chain节点，返回全部的区块链
	'''
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
