## Section 1: Software and Platforms Used 

The attached jupyter notebook files were created in VSCode and Google Colab, where Python3 was used to run both of them. There are four main jupyter notebooks for each of the four predictive models we created, as well as one for descriptive analysis (some summary statistics and exploratory visualizations) and a notebook for testing the optimal models and their specific hyperparameters on the test data originally included in this repository. The packages that were used to create these notebooks are pandas, numpy, scikit-learn, matplotlib, seaborn, and PyTorch. Finally, the operating system used to run these notebooks is MacOS.

## Section 2: Documentation Map 

#### Below is a directory tree showing the structure of this repository and the contents of each folder.

```
ds4021-project/
├── Data/
│   ├── train.csv                 # Training data used for all model fitting and tuning
│   └── test.csv                  # Held-out test set for final evaluation only
│
├── data_raw/
│   └── anxiety_depression_data.csv   # Original dataset downloaded from Kaggle (in .gitignore)
│
├── data_working/                 # Intermediate or scratch data files (in .gitignore)
│
├── NOTEBOOKS/
│   ├── 01_eda.ipynb              # Exploratory data analysis and summary statistics
│   ├── 02_ridge.ipynb            # Penalized linear regression (Ridge)
│   ├── 03_svm.ipynb              # Support Vector Machine regression
│   ├── 04_ensemble.ipynb         # Ensemble model (Random Forest)
│   ├── 05_nn.ipynb               # Neural network implemented in PyTorch
│   └── 06_test_evaluation.ipynb  # Final evaluation on held-out test set
│
├── OUTPUT/
│   ├── EDA_age_vs_depression.png
│   ├── EDA_anxiety_distribution.png
│   ├── EDA_correlation_heatmap.png
│   ├── EDA_depression_distribution.png
│   ├── EDA_education_level_vs_anxiety.png
│   ├── nn_anxiety_tuning_results.csv
│   ├── nn_depression_tuning_results.csv
│   ├── ridge_prediction_depression.png
│   ├── ridge_prediction_anxiety.png
│   ├── svm_prediction_depression.png
│   ├── svm_prediction_anxiety.png
│   ├── rf_predictions_depression.png
│   ├── rf_predictions_anxiety.png
│   ├── nn_predictions_depression.png
│   └── nn_predictions_anxiety.png
│
├── src/
│   └── split_data.py             # Script used to create training and test sets
│
├── final_report.pdf              # Final written report
├── README.md                     # Project description, software info, and documentation map
└── .gitignore                    # Files ignored by git

```

