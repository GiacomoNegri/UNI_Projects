# Loan Approval Prediction Using LightGBM

## Project Overview
This project implements a machine learning solution for predicting loan approval status using LightGBM, a gradient boosting framework. The model achieves a high accuracy of 95.25% on the validation set, making it a reliable tool for loan approval decision support.

## Performance Metrics
- **Overall Accuracy**: 95.25%
- **Class-wise Performance**:
  - Class 0 (Loan Rejected):
    - Precision: 0.96
    - Recall: 0.99
    - F1-score: 0.97
  - Class 1 (Loan Approved):
    - Precision: 0.91
    - Recall: 0.73
    - F1-score: 0.81

## Dataset Information
- Training data size: 46,916 samples
- Features used: 12
- Class distribution:
  - Negative cases (Class 0): 40,208
  - Positive cases (Class 1): 6,708
  - Imbalance ratio: ~6:1

## Technical Implementation
### Dependencies
```python
numpy
pandas
matplotlib
seaborn
scikit-learn
lightgbm
```

### Data Preprocessing
1. Handles missing values:
   - Numeric columns: Filled with median values
   - Categorical columns: Filled with mode values
2. Categorical encoding: All categorical variables are encoded to numeric values
3. Feature selection: Implemented using all available features

### Model Configuration
- Algorithm: LightGBM Classifier
- Train-Test Split: 80-20 ratio
- Random State: 42
- Threading: Row-wise multi-threading (auto-chosen by LightGBM)

## File Structure
- `train.csv`: Training dataset
- `test.csv`: Test dataset
- `submission.csv`: Output file containing predictions

## Usage
1. Ensure all dependencies are installed
2. Place the training and test datasets in the project directory
3. Run the main script to:
   - Preprocess the data
   - Train the model
   - Generate predictions
   - Create submission file

## Results
The model shows strong performance with a high accuracy of 95.25%. It performs particularly well in identifying rejected loans (Class 0) with an F1-score of 0.97. For approved loans (Class 1), the model achieves a respectable F1-score of 0.81, despite the class imbalance.

## Notes
- The model uses automatic row-wise multi-threading for optimization
- Total number of bins used: 1,095
- Initial score: -1.790765

## Future Improvements
1. Address class imbalance using techniques like SMOTE or class weights
2. Experiment with feature engineering
3. Implement cross-validation for more robust evaluation
4. Fine-tune model hyperparameters
5. Consider ensemble methods for improved performance

## Author
Giacomo Negri
