# JSON格式的API

- 视图 返回一个 dict ，那么它会被转换为一个 JSON 响应。

- 使用 jsonify() 函数会序列化任何支持的 JSON 数据类型。
    ```
    @app.route("/me")
    def me_api():
        user = get_current_user()
        return {
            "username": user.username,
            "theme": user.theme,
            "image": url_for("user_image", filename=user.image),
        }
    
    @app.route("/users")
    def users_api():
        users = get_all_users()
        return jsonify([user.to_json() for user in users])
    ```