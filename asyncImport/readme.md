# Async Import

`Async Imports in python.`

> ### *Explanation*:
> ```
> this simple code is used to import libraries only when they are used, and not on the startup.
> This can be useful in large projects where, for example, there are many imports that slow down the startup.
> ```
`p.s. using async import unfortunately you will not be able to use the tips of most ides :')`

> ### *Code Example*
> ```py
> flask = AsyncImport('flask')
> app = flask.Flask(__name__)
> 
> @app.route('/')
> def helloAsync():
>     return 'Hello World from AsyncImport!'
> 
> app.run('0.0.0.0', 8000)
> ```
> `This is not really a good method to use the async Imports,
they can come in handy in much larger and complex projects,
and not in such a simple program.`