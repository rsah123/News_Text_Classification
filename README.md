# News Text Classification System

A multi-class Natural Language Processing (NLP) project that classifies BBC news articles into five categories:

- Business
- Entertainment
- Politics
- Sport
- Tech

The project compares multiple machine learning models using TF-IDF features and selects the best-performing model based on validation performance, cross-validation, and Macro F1-score.
## Project Workflow

1. Load raw BBC news articles.
2. Check class distribution, missing values, blank articles, and duplicates.
3. Remove duplicate articles to reduce data leakage.
4. Split the dataset into training, validation, and test sets using stratification.
5. Convert text into numerical features using TF-IDF.
6. Train and compare:
   - Logistic Regression
   - Multinomial Naive Bayes
   - Linear SVM
7. Check training vs validation performance for overfitting and underfitting.
8. Tune model hyperparameters.
9. Perform 5-fold stratified cross-validation.
10. Tune TF-IDF and SVM using GridSearchCV.
11. Perform error analysis and inspect influential features.
12. Train the final model using training + validation data.
13. Evaluate once on the untouched test set.
14. Save the complete TF-IDF + SVM pipeline.
15. Deploy the model using Streamlit.
## Model Performance

### Baseline Validation Results

| Model | Train Accuracy | Validation Accuracy | Train-Val Gap | Macro F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 99.66% | 97.49% | 2.17% | 97.48% |
| Multinomial Naive Bayes | 98.66% | 97.18% | 1.48% | 97.08% |
| Linear SVM | 100.00% | 97.49% | 2.51% | 97.42% |

### Tuned Model

The final model was selected using hyperparameter tuning and 5-fold stratified cross-validation.

Best configuration:

- Model: Linear SVM
- SVM C: 0.5
- TF-IDF ngram range: (1, 2)
- TF-IDF min_df: 1

Cross-validation results:

- Mean CV Accuracy: 97.51%
- Mean CV Macro F1: 97.49%

### Final Test Results

The final model was evaluated once on the untouched test set.

- Test Accuracy: **98.75%**
- Test Macro F1: **98.68%**

The test set contained 320 unseen news articles, of which 316 were classified correctly.
## Dataset

This project uses the BBC News dataset containing news articles from five categories:

- Business
- Entertainment
- Politics
- Sport
- Tech

The original dataset contained 2,225 articles.

During preprocessing:

- 98 duplicate articles were identified.
- Duplicate articles were removed to reduce the risk of data leakage.
- The final dataset contained 2,127 unique articles.
- No missing or blank articles were found.

## Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- Matplotlib
- Streamlit
- Joblib
- Jupyter Notebook
- Git
- GitHub
## Project Structure

```text
News_Text_Classification/
│
├── data/
│   └── bbc/
│
├── notebook/
│   └── news_classification.ipynb
│
├── app.py
├── news_classification_model.pkl
├── requirements.txt
├── README.md
└── .gitignore