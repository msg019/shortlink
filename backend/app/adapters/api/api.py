from flask import Blueprint,request,jsonify,redirect
from services.db_services import saveURL,readDB
from services.verify_services import is_valid_short, is_valid_url
import uuid

bp=Blueprint("api",__name__)

# Generate link
@bp.route('/generate', methods=['POST'])
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
@bp.route('/<route>', methods=['GET'])
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