from flask import Flask
from flask import request
from waitress import serve
import controller as controller

app = Flask(__name__)

# TODO - Remove this function and adjust
#@app.route('/product',methods = ['GET'])
#def product():
#    productList = controller.retrieveProductList(request)
#    return { "products": productList }, 200

@app.route('/productStream',methods = ['GET'])
def productStream():
    """Receives a HTTP Get request and return a list of Products.

    Returns:
        dict: Dict with discounted Products List
    """
    print(request)
    print(type(request))
    productList = controller.retrieveProductListStream(request)
    return { "products": productList }, 200

if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=5000)