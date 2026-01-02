# Air Quality Index (AQI) Prediction Using Machine Learning

## Description
This project predicts the **Air Quality Index (AQI)** based on concentrations of major air pollutants using a **Linear Regression** machine learning model. The dataset consists of daily air quality data from various Indian cities, with pollutants including PM2.5, PM10, NO2, SO2, CO, and O3. The project demonstrates data preprocessing, model training, prediction, and evaluation.

---

## Key Tasks
1. **Data Collection:** Used the `city_day.csv` dataset from Kaggle (Air Quality Data in India).  
2. **Data Preprocessing:** Selected relevant columns and removed missing values.  
3. **Feature Selection:** Used pollutant concentrations (`PM2.5, PM10, NO2, SO2, CO, O3`) as input features and AQI as the target.  
4. **Train-Test Split:** Divided the dataset into 80% training and 20% testing data.  
5. **Model Training:** Trained a Linear Regression model on the training data.  
6. **Prediction:** Predicted AQI for the test data.  
7. **Evaluation:** Measured performance using **Mean Squared Error (MSE)** and **R² Score**.  
8. **Sample Output:** Displayed predicted AQI vs actual AQI for sample data.

---

## Output
**Model Evaluation Metrics:**

Mean Squared Error: ~1096
R2 Score: ~0.7


**Sample AQI Predictions:**
| Actual AQI | Predicted AQI |
|------------|---------------|
| 86         | 73.04         |
| 95         | 86.24         |
| 532        | 601.13        |
| 386        | 347.21        |
| 69         | 70.48         |
| 147        | 171.35        |
| 103        | 69.54         |
| 168        | 144.57        |
| 347        | 296.90        |
| 48         | 53.34         |


---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
