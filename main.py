from archcode import *
import sys

if __name__ == '__main__':

    args = sys.argv[1:]

    manager = Manager()

    manager.initialize(query=[args[0], [False, args[1]]])

    manager.run()
