from flask import Flask
from flask import request
from waitress import serve
import controller as controller
import config.httpconfig as httpconfig

app = Flask(__name__)

@app.route('/productStream',methods = ['GET'])
def productStream():
    """Receives a HTTP Get request and return a list of Products.

    Returns:
        dict: Dict with discounted Products List
    """
    productList = controller.retrieveProductListStream(request)
    return { "products": productList }, 200

def startServer():
   serve(app, host=httpconfig.host, port=httpconfig.port)