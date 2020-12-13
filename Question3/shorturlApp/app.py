# app.py - a minimal flask api using flask_restful
from flask import Flask, render_template, request, redirect, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json
import string
import secrets
app = Flask(__name__)
api = Api(app)

## SQLALchemy
# Source: https://pypi.org/project/Flask-SQLAlchemy/
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

# Define the Url's Model
# For the long url, shortUrl
class UrlModel(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    url = db.Column(db.String(1000), unique=True, nullable=False)
    shorturl = db.Column(db.String(1000), unique=True, nullable=False)
    # def __repr__(self):
    #     return {'id':self.id, 'url':self.url, 'shorturl':self.shorturl}

    def __str__(self):
        return 'UrlModel(id='+str(self.id)+', url='+str(self.url)+',shorturl='+str(self.shorturl)+ ')'
# Create the DB before the request
@app.before_request
def createTheUrlModel():
    db.create_all()
    
    # url = "https://www.google.com/"
    # testUrl = "test"
    # model = UrlModel(url=url, shorturl="testUrl")
    # db.session.add(model)
    # db.session.commit()

    

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')
@app.route('/home', methods=["GET", "POST"])
def index():
    urlLists = None
    if request.method == "POST":
        if request.form:
            try:
                existingRecord = UrlModel.query.filter_by(url=request.form.get("url")).first()
                if existingRecord is not None:
                    print("")
                else:
                    alphabet = string.ascii_letters + string.digits
                    shortUrl = ''.join(secrets.choice(alphabet) for i in range(8))
                    print(shortUrl)
                    urlModel = UrlModel(url=request.form.get("url"),shorturl=shortUrl)
                    db.session.add(urlModel)
                    db.session.commit()
                    #return "Created the new shortUrl :" + urlModel
            except Exception as e:
                print("Failed to add urlModel")
                print(e)
    urlLists = UrlModel.query.all()
    return render_template('/home.html', entries=urlLists)

@app.route('/newurl',methods=["POST"])
def newurl():
    if request.method == "POST":
        data = request.data
        jsonRequest = json.loads(data)
        print(jsonRequest)
        try:
            if jsonRequest['url'] is not None:
                existingRecord = UrlModel.query.filter_by(url=jsonRequest['url']).first()
                if existingRecord is not None:
                    return "ShortUrl is already created previously as: " + existingRecord.shorturl
                else:
                    alphabet = string.ascii_letters + string.digits
                    shortUrl = ''.join(secrets.choice(alphabet) for i in range(8))
                    print(shortUrl)
                    urlModel = UrlModel(url=jsonRequest['url'],shorturl=shortUrl)
                    db.session.add(urlModel)
                    db.session.commit()
                    remote_addr = request.remote_addr
                    jsonResult = {
                        "url" : jsonRequest['url'],
                        "shortUrl": shortUrl,
                        "remote_addr": remote_addr
                    }
                    return jsonify(jsonResult)
        except Exception as e:
            print("Eorr ocurrances!")
            print(e)
    else:
        return "Not valid request."

@app.route('/<path:path>')
def redirectUrl(path):
    if request.method == "GET":
        try:
            existingShortUrl = UrlModel.query.filter_by(shorturl=path).first()
            print(existingShortUrl)
            if existingShortUrl is not None and existingShortUrl.url is not None:
                return redirect(existingShortUrl.url)
            else:
                return "The shortUrl doesn't exist!"
        except Exception as e:
            print("Eorr ocurrances!")
            print(e)
    else:
        return "Not valid request."
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)