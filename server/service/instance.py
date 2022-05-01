#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
from flask import Flask
from flask_restx import Api
from flask_cors import CORS
#======================================================#
# Create a class that will be used to create the Flask application:

class Server:
    def __init__(self, ):
        self.app = Flask(__name__)
        self.app.config['CORS_HEADER'] = 'Content-Type'
        
        self.cors = CORS(self.app, supports_credentials=True, resources={r'/*': {"origins": '*'}})
        
        self.api = Api(self.app, 
            version='1.0', 
            title='PCA maker', 
            description='A Web app that execute PCA and return the results.', 
            doc='/docs'             # Documentation URL
        )
    
    # Turn debug to False to production mode:    
    def run(self, ):
        self.app.run(
            debug=False              # Debug mode    
        )
        
#======================================================#
# Create the server:

server = Server()