#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
import os
from werkzeug.utils import secure_filename

#======================================================#
class File:
    UPLOAD_DIR = './server/data/'           # Where the file will be saved
    NEW_NAME = 'datafile'                   # The new name of the file will be saved in the UPLOAD_DIR
    
    def __init__(self, filename):
        self.file_name = filename
        
        self.change_file_name(self.NEW_NAME)
        
        if self.check_folder():
            self.save_file()
            
#======================================================#        
    def save_file(self) -> None:
        self.file_name.save(os.path.join(self.UPLOAD_DIR, secure_filename(self.file_name.filename)))
        
#======================================================#    
    def check_folder(self) -> bool:
        try:
            
            for f in os.listdir(self.UPLOAD_DIR):
                os.remove(os.path.join(self.UPLOAD_DIR, f))
                
            return True                         # Return True after the folder is empty    

        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (self.UPLOAD_DIR, e))    
                

#======================================================#
    def change_file_name(self, new_name) -> None:
        extension = self.file_name.filename.split('.')[-1]
        
        # Change the name of the file
        self.file_name.filename = new_name + "." + extension    
#======================================================#
        