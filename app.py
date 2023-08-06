#We begin with importing the Flask class from the flask module.
from flask import Flask

#Creating an object of Flask called app.
#This helps Flask to locate resources and templates used in making a website.
app = Flask(__name__)


#Route is simply a part of the URL that comes after the domain name
@app.route('/')
def hello():
  return "<h1>hello meet</h1>"


#To run our flask application, we will use the flask command app.run and pass the host name = '0.0.0.0', to run it locally.
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
