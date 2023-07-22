

class Test:
    def __init__(self):
       self.test_var = 0
       self.test_var2 = 0

    def testMethod(self, nomeVariavel):
        self.nomeVariavel = 1
        print(self.nomeVariavel)


test = Test()
test.testMethod('test_var')
