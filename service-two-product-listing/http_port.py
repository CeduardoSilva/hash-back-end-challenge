from flask import Flask
from flask import request
from waitress import serve
import controller as controller

app = Flask(__name__)

@app.route('/product',methods = ['GET'])
def product():
    headers = request.headers
    if(headers.get("X-User-Id")):
        print("Received Id!")
    else:
        print("Didn't receive Id!")

    productList = controller.retrieveProductList()
    return productList, 200

if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=5000)