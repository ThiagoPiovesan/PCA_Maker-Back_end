#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
import os
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from server.utils.PCA import PCA
    
DEBUG = False                                                   # Set True to Grafic debug
#======================================================#
class PCAService:
    UPLOAD_DIR = './server/data/'                               # Where the file will be saved
    
    def __init__(self) -> None:
        pass
    
#======================================================#
    def get_data(self) -> pd.DataFrame:
        """
        Return dataframe
        """
        try:
            for f in os.listdir(self.UPLOAD_DIR):               # Get the file inside the folder
                
                if f.endswith('.csv') or f.endswith('.data'):   # if it is a CSV file:
                    df = pd.read_csv(self.UPLOAD_DIR + f)
                
                elif f.endswith('.xlsx'):                       # if it is a XLSX file:
                    df = pd.read_excel(self.UPLOAD_DIR + f)                    
                
        except Exception as e:                                  # If there is an error:
            print('Failed to get data. Reason: %s' % e)
            
        return df                                               # Return the dataframe

#======================================================#
    def prepare_data(self) -> pd.DataFrame:
        """
            Execute the data preparation to make the PCA
        """
        dataFrame = self.get_data()                                     # Get the dataframe
        
        # Considering that the first column and line are consecutively the features
        # names [lines] (can be empty) and the number of experiment [columns]
        new_dataFrame = dataFrame.select_dtypes(exclude='object')       # Select only numeric data
        
        if 'target' in dataFrame:                                       # If the target column exists:
            target = dataFrame['target']                                # Get the target column
            new_dataFrame = new_dataFrame.drop(['target'], axis = 1)    # Drop the target column

            return new_dataFrame, target
        else:                                                           # If the target column does not exist:
            return new_dataFrame, None
        
#======================================================#
    def get_pca(self, n_components: int = 2) -> pd.DataFrame:
        """
        Return PCA and infos by and CSV or XLSX that was given by user
        """
    
        # Step 1 & 2: Prepare the data and target:
        x, target = self.prepare_data()

        # Step 3: Applying it to PCA function
        mat_reduced = PCA.execute_PCA(x, n_components)

        # Step 4: Creating a Pandas DataFrame of reduced Dataset
        principal_df = pd.DataFrame(mat_reduced, columns = ['PC1','PC2'])

        print(target)
        # Step 5: Concat it with target variable to create a complete Dataset
        if target is not None:
            principal_df = pd.concat([principal_df, pd.DataFrame(target)], axis = 1)
        else:
            principal_df = pd.concat([principal_df], axis = 1)
            
        return principal_df, target
    
#======================================================#     
    def get_pca_plot(self) -> np.array:
        
        principal_df, target = self.get_pca(n_components=2)
        
        if DEBUG:
            
            plt.figure(figsize = (6,6))
            
            if target is not None:
                sb.scatterplot(data = principal_df, x = 'PC1', y = 'PC2', hue = 'target', s = 60, palette= 'icefire')
            else:
                sb.scatterplot(data = principal_df, x = 'PC1', y = 'PC2', s = 60, palette= 'icefire')
                
            plt.show() 
            
        return principal_df.to_numpy().tolist()
#======================================================#


    
