class State:
    """Generic Class for representing a State of the search problem.
       A generic search algorithm expects this class structure for the state.
       Any concrete class(for e.g. State for representing TSP Problem) should implement all the methods of the State Class
    """

    def isGoalState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def moveToNextState(self, State):
        raise NotImplementedError("Subclass must implement abstract method")          

    def getSuccessors(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def gOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def hOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def fOfState(self):
        raise NotImplementedError("Subclass must implement abstract method")



    


