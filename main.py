import sys
from neuromix import *

class Manager:

    def __init__(self):

        self.chain = []
        self.current = 0
        self.counter = 0

        self.depth = 0

    def initialize(self, query: list):
        
        """ intialize a query process

        -----------------------------
        :param query: list, [reference_class, [isclass: bool, query_name: str]
        :return: None
        """

        # check input
        assert isinstance(query, list), "<query> is not a list"
        assert isinstance(query[0], str), "<reference_class> is not a string"
        assert isinstance(query[1], list), "<queried_instance> is not a list"
        assert isinstance(query[1][0], bool), "<isclass> not a bool)"
        assert isinstance(query[1][1], str), "<query_name> not a string"

        # clean precedent activity
        self.reset()

        # set new query
        query[1].append(0)  # append query timestep
        self.chain = [query]

        print(f"- initialize new query: {self.chain}") 

    def run(self):

        """completion of the traceback of the given query 

        ------------------------------
        :return: None
        """

        assert self.depth == 0, "non-zero depth"

        self.depth = 0
        print('structure:\n')

        # first traceback
        #self.display()
        #self.counter = 1
        #self.depth += 1

        while 1:
            #print('\nchain: ', self.chain, ' | counter=', self.counter, self.depth)
            self.traceback()

            if len(self.chain) == self.counter:
                break

        print()

    def traceback(self):

        """ traceback next queried instance """
        
        current = self.chain[self.counter]
        #print(f'traceback [{self.counter}]: ', current)
        reference_class = current[0]
        iscell, query_name, k = current[1]

        # a cell is queried
        if iscell:
            results = classes_dict[query_name]
            
        else:
            results = classes_dict[reference_class][query_name]

        # end of a branch
        if results == 0:
            self.display()
            self.depth -= 1 * (k == 0)
            self.counter += 1
            return

        # adjust size
        size = len(results)  
    
        # create new branches
        new_branch = []
        for i, result in enumerate(results): 
            new_branch += [[result[0], [0, result[1], size-i-1]]]
    
        # append new branches at the current counter timestep
        self.chain = self.chain[:self.counter+1] + new_branch + self.chain[self.counter+1:]

        self.display()

        # increase depth
        self.depth += 1

        # increase counter
        self.counter += 1

        return 
        
    def display(self):

        """ display a new line of the resulting chain

        -----------------------------
        :param reference: str, the reference class currently handled
        :param query_name: str, the query
        :return: None
        """

        current = self.chain[self.counter]
        if not self.depth:
            print(f"{current[0]}.{current[1][1]}()")
            return

        print('-------'*self.depth, f"{current[0]}.{current[1][1]}()")

    def reset(self):

        """ reset the activity
        
        ------------------------------
        :return None
        """

        self.chain = []
        self.counter = 0
        self.depth = 0



if __name__ == '__main__':

    args = sys.argv[1:]

    manager = Manager()

    manager.initialize(query=[args[0], [False, args[1]]])

    manager.run()
