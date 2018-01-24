import sys
print(sys.version)

"""
先启动server:

$ python blockchain.py * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

让我们尝试通过get请求挖一块 http://localhost:5000/mine

让我们在body里包含交易结构发起post请求到 http://localhost:5000/transactions/new 创建一次新的交易：

如果你没有用postman，也可用curl发起相同的请求：

$ curl -X POST -H “Content-Type: application/json” -d ‘{ “sender”: “d4ee26eee15148ee92c6cd394edd974e”, “recipient”: “someone-other-address”, “amount”: 5 }’ “http://localhost:5000/transactions/new"

我重启我的server，挖2个块出来，总共3块了。看一下完整的链条 http://localhost:5000/chain ：

例如
{ “chain”:
“index”:1,“previoushash”:1,“proof”:100,“timestamp”:1506280650.770839,“transactions”:[],
“index”:2,“previoushash”:“c099bc…bfb7”,“proof”:35293,“timestamp”:1506280664.717925,“transactions”:[“amount”:1,“recipient”:“8bbcb347e0634905b0cac7955bae152b”,“sender”:“0”],
“index”:3,“previoushash”:“eff91a…10f2”,“proof”:35089,“timestamp”:1506280666.1086972,“transactions”:[“amount”:1,“recipient”:“8bbcb347e0634905b0cac7955bae152b”,“sender”:“0”]
“index”:1,“previoushash”:1,“proof”:100,“timestamp”:1506280650.770839,“transactions”:[],
“index”:2,“previoushash”:“c099bc…bfb7”,“proof”:35293,“timestamp”:1506280664.717925,“transactions”:[“amount”:1,“recipient”:“8bbcb347e0634905b0cac7955bae152b”,“sender”:“0”],
“index”:3,“previoushash”:“eff91a…10f2”,“proof”:35089,“timestamp”:1506280666.1086972,“transactions”:[“amount”:1,“recipient”:“8bbcb347e0634905b0cac7955bae152b”,“sender”:“0”]
, “length”: 3 }
"""