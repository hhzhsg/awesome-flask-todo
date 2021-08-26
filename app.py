from flask import Flask # 导入flask类，通过这个类我们可以创建应用

app = Flask(__name__) # 创建app，也就是一个Flask应用实例


@app.route("/") # 创建index方法，使用app.route装饰器绑定路由规则
def index():
    return "Hello World!"


if __name__ == "__main__": # 运行Flask应用
    app.run()
