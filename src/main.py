import os
import sys
import xml.sax

# High: Code_Injection
@app.route('/execute')
def execute_user_code_unsafe(): 
    user_code = request.args.get('code')
	result = eval(user_code)
	
	return result['value']

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
