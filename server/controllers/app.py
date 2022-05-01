#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
from flask import jsonify, request
from flask_cors import cross_origin
import json

from server.service.instance import server
from server.service.control_file import File
from server.service.pca_service import PCAService
#======================================================#
# Endpoint creation:
app, api = server.app, server.api

#======================================================#
@app.route("/home", methods=['GET'])
@cross_origin(supports_credentials=True)
def home():
    return True

#======================================================#
@app.route("/save_file", methods=["POST", "GET", "OPTIONS"])
# @cross_origin(origin='*', headers=['Content-Type', 'multipart/form-data'])
def save_file():
    
    if request.method == 'POST':
        upload_file = request.files['file']
        
        try:
            if upload_file.filename != "":
                File(upload_file)
#======================================================#        
            return jsonify(success=True)
        except Exception as e:
            print(e)
            return jsonify(success=False)
#======================================================#    
@app.route("/dashboard", methods=["GET"])
@cross_origin(supports_credentials=True)
def dashboard():
    # Function to execute the PCA:
    pca_service = PCAService()
    np_array = pca_service.get_pca_plot()

    return json.dumps(np_array)

#======================================================#  
@app.route("/about", methods=["GET"])
@cross_origin(supports_credentials=True)
def about():
    return "True"