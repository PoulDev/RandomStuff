class AsyncImport(object):
    def __init__(self, lib_name):
        self.library = lib_name
        self.object = None

    def __getattribute__(self, __name: str):
        if __name in ['library', 'object']: return super().__getattribute__(__name)
        if not self.object:
            self.object = __import__(self.library)
        
        return getattr(self.object, __name)

"""
A simple flask app to test the async import.
This is not really a good method to use the async Imports,
they can come in handy in much larger and complex projects,
and not in such a simple program.
"""
 

flask = AsyncImport('flask')
app = flask.Flask(__name__)

@app.route('/')
def helloAsync():
    return 'Hello World from AsyncImport!'

app.run('0.0.0.0', 8000)