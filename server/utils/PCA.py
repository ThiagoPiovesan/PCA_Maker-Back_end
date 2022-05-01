#======================================================#
# + Projet: Principal Component Analysis automation    #
# + Date:   04/2022                                    #
# + Description: Return PCA and infos by and CSV or    #
# XLSX that was given by user                          #
# + Author: Thiago Piovesan                            #
#======================================================#
# Libraries importation:
import numpy as np

#======================================================#
class PCA:

    def execute_PCA(X, num_components):      
        # Step 1: Compute mean row and Subtract mean from the main (original) data:
        X_meaned = X - np.mean(X, axis = 0)
        
    #======================================================#
        # Step 2: Covariance matrix of the rows of B:
        cov_mat = np.cov(X_meaned, rowvar = False)
        
    #======================================================#        
        # Step 3: Compute Eigenvalues and Eigenvectors of C:
        eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)
        
    #======================================================#
        # Step 4: Compute Eigenvalues and Eigenvectors of C:
        sorted_index = np.argsort(eigen_values)[::-1]
        sorted_eigenvalue = eigen_values[sorted_index]
        sorted_eigenvectors = eigen_vectors[:, sorted_index]
        
    #======================================================#
        # Step 5: Compute Eigenvalues and Eigenvectors of C:
        eigenvector_subset = sorted_eigenvectors[:, 0:num_components]
        
    #======================================================#
        # Step 6: Principal component:
        X_reduced = np.dot(eigenvector_subset.transpose(), X_meaned.transpose()).transpose()
            
    #======================================================#
        return X_reduced
