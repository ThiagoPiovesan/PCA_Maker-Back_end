# PCA maker:
---

## Objective:
-> This project has the main pourpose of understand and test the methods and functions developed to execute an PCA implementation in an "Excel" file (planilha). <br>

---
#### Concepts and Languages used:
- VUE.js
- Flask API;
- Python;
- MVP.

---

## How does it work?
→ You can simply Upload your file on the web application and it will procress the file and get you back the response of that data after the PCA.<br>

---
## A little of theory and concepts included (You can skip if you want to):

<details>
  <summary>PCA - Principal Component Analysis</summary>
  → PCA is used in applications when you have big data that might have some statistical distribution and you want to uncover the low dimensional patterns to build models off of it. <br>

  
#### Steps to execute PCA:
1. Compute mean row. <br>

2. Subtract mean from the main (original) data: B = x_matrix - x_matrix_hat: <br>
→ Subtract the mean of each variable from the dataset so that the dataset should be centered on the origin.  <br>

3. Covariance matrix of the rows of B:
→ Calculate the Covariance Matrix of the mean-centered data. The covariance matrix is a square matrix denoting the covariance of the elements with each other. <br>

4. Compute Eigenvalues and Eigenvectors of C:
→ The Eigenvectors of the Covariance matrix we get are Orthogonal to each other and each vector represents a principal axis. <br>
→ A Higher Eigenvalue corresponds to a higher variability. Hence the principal axis with the higher Eigenvalue will be an axis capturing higher variability in the data. <br>
→ Orthogonal means the vectors are mutually perpendicular to each other. Eigenvalues and vectors seem to be very scary until we get the idea and concepts behind it. <br>

5. Principal component: T = BV

---
→ Essentially what you do is you decompose this matrix into kind of directions of maximal variance just like in the singular value decomposition, called the **Principal component**. And the **Loadings** are king of how much of each of those principal components each of the experiments has the loadings in a particular experiment of those principal componentes columns.

→ Gives the indication of the amount of the variance of this dataset that these principal component capture.

→ How much of the variance is capture by computing kind of how much energy or variances in those first two eigen values of this D matrix.

</details>

<details> 
    <summary> Reference </summary>
    → https://www.youtube.com/watch?v=fkf4IBRSeEc <br>
    → https://www.askpython.com/python/examples/principal-component-analysis <br>
    → https://youtu.be/Oi4SJqJIL2E <br>
    → https://youtu.be/fu7uXxZMzC8 <br>
    → https://youtu.be/p4bvCFygfW0 <br>

</details>

---
## Thanks for the read & I hope you enjoy it!

---

Ass: Thiago Piovesan - 04/2022 -- version: 1.0.0.