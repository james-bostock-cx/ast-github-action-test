import os
import sys
import xml.sax

# Random comment
# High: OS_Access_Violation
path = sys.stdin.readline()[:-1]
os.remove(path)

# Medium
class TestHandler(xml.sax.ContentHandler):
    """A simple class"""
    pass

parser = xml.sax.make_parser()
parser.setContentHandler(TestHandler())
with open(sys.argv[1]) as f:
    parser.parse(f)

# Low
# Password: secret

print('Done!')
