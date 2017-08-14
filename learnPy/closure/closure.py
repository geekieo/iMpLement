'''
有点像 lamdba 演算
'''
def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)
    return greeting

mGreeting = greeting_conf("Good morning")
mGreeting("Wilber")
mGreeting("Will")

aGreeting = greeting_conf("Good afternoon")
aGreeting("Wilber")
aGreeting("Will")
