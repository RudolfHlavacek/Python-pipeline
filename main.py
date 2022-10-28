"""
Just simply python file.
"""
from logguru import logger
import sys

def hello():
    """Func hello()"""
    print("hello")

def bye():
    """Func bye()"""
    print("bye")

if __name__ == '__main__':
    print(hello())
    for i, arg in enumerate(sys.argv):
        logger.debug('sys.argv[{}]: {}', i, arg)
        print('sys.argv[{}]: {}'.format( i, arg))
        
