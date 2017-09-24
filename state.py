


class State:

    def isGoalState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def moveToNextState(self):
        raise NotImplementedError("Subclass must implement abstract method")          

    def getSuccessors(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def gOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def hOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def fOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    


