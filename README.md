## Section 1: Software and Platforms Used 

The attached jupyter notebook files were created in VSCode and Google Colab, where Python3 was used to run both of them. There are four main jupyter notebooks for each of the four predictive models we created, as well as one for descriptive analysis (some summary statistics and exploratory visualizations) and a notebook for testing the optimal models and their specific hyperparameters on the test data originally included in this repository. The packages that were used to create these notebooks are pandas, numpy, scikit-learn, matplotlib, seaborn, and PyTorch. Finally, the operating system used to run these notebooks is MacOS.

## Section 2: Documentation Map 

### Below is a directory tree showing the structure of this repository and the contents of each folder.


ds4021-project/
├── Data/
│   ├── train.csv              # Training data used for all model fitting and tuning
│   └── test.csv               # Held-out test set for final evaluation only
│
├── data_raw/
│   └── anxiety_depression_data.csv   # Original dataset downloaded from Kaggle
│
├── data_working/
│   └── ...                    # Intermediate or scratch data files (optional)
│
├── NOTEBOOKS/
│   ├── 01_eda.ipynb           # Exploratory data analysis and summary statistics
│   ├── 02_ridge.ipynb         # Penalized linear regression (Ridge)
│   ├── 03_svm.ipynb           # Support Vector Machine regression
│   ├── 04_ensemble.ipynb      # Ensemble model (e.g., Random Forest / Gradient Boosting)
│   ├── 05_nn.ipynb            # Neural network implemented in PyTorch
│   └── 06_test_evaluation.ipynb   # Final evaluation on the held-out test set
│
├── OUTPUT/
│   └── ...                    # Figures, tables, exported graphics for the report
│
├── src/
│   └── split_data.py          # Script used to create the training and test sets
│
├── final_report.pdf           # Final written report
├── README.md                  # Project description, software info, and repository map
└── .gitignore                 # Files ignored by git

---
