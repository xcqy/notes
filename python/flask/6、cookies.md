# cookies


- 要访问 cookies ，可以使用 cookies 属性。
- 使用set_cookie 方法来设置 cookies
    ```
    读取 cookies:
    from flask import request
    
    @app.route('/')
    def index():
        username = request.cookies.get('username')
        # use cookies.get(key) instead of cookies[key] to not get a
        # KeyError if the cookie is missing.
    
    储存 cookies:
    from flask import make_response
    
    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp
    ```
- cookies 设置在响应对象上
- 使用 延迟的请求回调 方案可以在没有响应对象的情况下设置一个 cookie。