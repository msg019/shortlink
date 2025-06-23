from flask import Flask
from flask_cors import CORS
from adapters.api.api import bp
from services.db_services import createSimpleTable

app= Flask(__name__)

CORS(app)

app.register_blueprint(bp)
        
if '__main__'==__name__:
    createSimpleTable()
    app.run(debug=True, port=5000)