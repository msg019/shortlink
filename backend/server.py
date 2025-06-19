from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from function.db import saveURL, readDB, createSimpleTable
from function.verify import is_valid_url,is_valid_short
import uuid

app= Flask(__name__)

CORS(app)

# Create redirection

@app.route('/generate', methods=['POST'])
def generate():
    if request.method=='POST':
        try:
            url=request.json['url']

            valid_url= is_valid_url(url)

            if not valid_url:
                return jsonify({"error":"Invalid URL"}),400
                
            id=str(uuid.uuid4())
            saveURL(id,valid_url)

            shortURL=f'http://localhost:5000/{readDB(valid_url,True)}'

            return jsonify(shortURL), 200
        except:
            return jsonify({'error':'Internal Server Error'}), 500


# Redirect
@app.route('/<route>', methods=['GET'])
def redi(route):
    if request.method=='GET':
        if route and is_valid_short(route):
            try:
                link=readDB(route,False)[0][0]
                return redirect(link, code=302)
            except:
                return "Internal server Error", 500
        else:
            return "Invalid URL",400
        

if '__main__'==__name__:
    createSimpleTable()
    app.run(debug=True, port=5000)