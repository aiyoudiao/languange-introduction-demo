# import requests
import flask

# 创建Flask应用实例
app = flask.Flask(__name__)

# GET接口，返回200状态码
@app.route('/', methods=['GET'])
def get_hello():
    return 'OK', 200

# POST接口，返回201状态码
@app.route('/', methods=['POST'])
def post_hello():
    return 'Created', 201

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)

