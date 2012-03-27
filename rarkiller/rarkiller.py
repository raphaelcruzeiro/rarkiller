import sys
import os
import re

def main(args):
    print 'Searching path: %s' % args[1]
    rar_count = 0

    for dirname, dirnames, filenames in os.walk(args[1]):
         for filename in filenames:
             file, extension = os.path.splitext(filename)
             if extension == '.rar' or re.search(r'\.r\d+$', extension):
                 filepath = os.path.join(dirname, filename)
                 print 'Deleting: %s' % filepath    
                 os.remove(filepath)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
