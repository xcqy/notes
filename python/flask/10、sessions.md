# sessions

- session 对象，允许在不同请求 之间储存信息。相当于用密钥签名加密的 cookie ，即用户可以查看你的 cookie ，但是如果没有密钥就无法修改它。

- 
    ```
    from flask import Flask, session, redirect, url_for, escape, request
    
    app = Flask(__name__)
    
    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    
    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username']) #  escape() 是用来转义的。如果不使用模板引擎就可以像上例 一样使用这个函数来转义。
        return 'You are not logged in'
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
    
    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))
    ```
- 如何生成一个好的密钥：好的密钥应当有足够的随机性。
