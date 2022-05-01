#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
from server.service.instance import server
# Now we have to import all the controllers we create:
from server.controllers.app import *

#======================================================#
# Create a Flask application:
server.run()