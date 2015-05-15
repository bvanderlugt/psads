class LogicGate(object):
    '''" We are writing a method that will use code that does not exist yet"'''

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
    
