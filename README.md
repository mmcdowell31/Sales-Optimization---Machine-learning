# Sales Optimization - Machine Learning

A comprehensive sales analysis and prediction project using machine learning techniques to optimize retail sales across different store locations and market segments.

## 📊 Project Overview

This project analyzes retail sales data across multiple locations (College towns, New York City, Philadelphia, and St. Louis) to identify patterns, optimize promotional strategies, and predict future sales using advanced machine learning models.

### Key Features
- **Multi-location Analysis**: Comparative analysis across 4 different market types
- **Weather Integration**: Incorporating weather data for seasonal trend analysis
- **Machine Learning Models**: XGBoost, Random Forest, and other ML algorithms
- **Interactive Visualizations**: Comprehensive data visualization and reporting
- **SHAP Analysis**: Model interpretability and feature importance analysis

## 🗂️ Project Structure

```
├── 📁 Data Files
│   ├── location_class_college.csv      # College town sales data
│   ├── location_class_newyork.csv      # NYC sales data
│   ├── location_class_philly.csv       # Philadelphia sales data
│   ├── location_class_stlouis.csv      # St. Louis sales data
│   ├── city_weather_data.csv           # Weather data for analysis
│   └── sales_seasonality.csv           # Seasonal trend data
│
├── 📁 Analysis Notebooks
│   ├── Exploratory Analysis.ipynb      # Main exploratory data analysis
│   ├── Sales_Seasonality.ipynb         # Seasonal trend analysis
│   ├── Seasonality_Weather_Joined.ipynb # Weather impact analysis
│   └── Correlation Matrix Heatmap.ipynb # Feature correlation analysis
│
├── 📁 Machine Learning Models
│   ├── XGBoost Sales Prediction_Colleges.ipynb
│   ├── XGBoost Sales Prediction_NYC.ipynb
│   ├── XGBoost Sales Prediction_PHI.ipynb
│   ├── XGBoost Sales Prediction_STL.ipynb
│   └── Shap Plots.ipynb               # Model interpretability
│
├── 📁 Utility Modules
│   ├── Encoder.py                     # Custom encoding functions
│   ├── Standardizer.py                # Data standardization utilities
│   ├── Interaction.py                 # Feature interaction functions
│   └── NOAA.py                        # Weather data processing
│
├── 📁 Documentation
│   ├── ISYE_7406_Project_Group_64.pdf # Final project report
│   ├── Project Presentation.pdf       # Project presentation
│   └── Project Proposal V2.docx       # Initial project proposal
│
└── 📁 Visualizations
    ├── Sales Histogram by Location Class.png
    ├── Average Sales by Total Promotions.png
    ├── Combined_Seasonality_Trends.png
    └── [Various SHAP and model performance plots]
```

## 🔧 Technical Stack

- **Programming Language**: Python 3.11+
- **Data Analysis**: pandas, numpy
- **Machine Learning**: scikit-learn, XGBoost
- **Visualization**: matplotlib, seaborn, plotnine
- **Model Interpretability**: SHAP
- **Statistical Analysis**: statsmodels
- **Weather Data**: NOAA API integration

## 📈 Key Analyses

### 1. Exploratory Data Analysis
- Sales distribution across different location types
- Promotional effectiveness analysis
- Channel and segment performance comparison
- Feature correlation and relationship identification

### 2. Seasonal and Weather Analysis
- Seasonal sales trend identification
- Weather impact on sales performance
- Day-of-year sales patterns
- Geographic weather correlation analysis

### 3. Machine Learning Models
- **XGBoost Regression**: Primary prediction model for each location
- **Random Forest**: Ensemble method for comparison
- **Cross-validation**: Robust model evaluation
- **Hyperparameter Tuning**: Optimized model performance

### 4. Model Interpretability
- SHAP (SHapley Additive exPlanations) analysis
- Feature importance ranking
- Individual prediction explanations
- Global model behavior understanding

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost plotnine statsmodels shap tqdm
```

### Quick Start
1. Clone the repository
2. Install required packages
3. Run the notebooks in the following order:
   - `Exploratory Analysis.ipynb` - Start here for data understanding
   - `Sales_Seasonality.ipynb` - Seasonal trend analysis
   - `XGBoost Sales Prediction_[Location].ipynb` - Location-specific models
   - `Shap Plots.ipynb` - Model interpretability

## 📊 Key Findings

### Sales Performance Insights
- **Location Impact**: College towns show different promotional effectiveness compared to urban markets
- **Channel Optimization**: E-commerce vs in-store performance varies by location type
- **Seasonal Patterns**: Clear seasonal trends identified across all locations
- **Weather Correlation**: Weather conditions significantly impact sales in certain categories

### Model Performance
- **XGBoost Models**: Achieved high predictive accuracy across all locations
- **Feature Importance**: Promotional activities, location type, and seasonality are top predictors
- **Cross-validation**: Models show consistent performance across different time periods

## 📁 Data Sources

- **Sales Data**: Retail transaction data across multiple locations
- **Weather Data**: NOAA weather API for historical weather information
- **Store Information**: Location classifications and operational details
- **Promotional Data**: Marketing campaign and promotional activity records

## 🔍 Model Interpretability

The project includes comprehensive SHAP analysis providing:
- Global feature importance across all predictions
- Local explanations for individual predictions
- Interaction effects between features
- Model decision boundary visualization

## 📄 Documentation

Detailed documentation available in:
- `ISYE_7406_Project_Group_64.pdf` - Complete project report
- `Project Presentation.pdf` - Executive summary and key findings
- Individual notebook markdown cells - Step-by-step analysis documentation

## 🤝 Contributing

This project was developed as part of ISYE 7406 coursework. For questions or suggestions, please open an issue.

## 📝 License

This project is for educational purposes. Please respect data privacy and usage guidelines.

## 🏆 Acknowledgments

- Georgia Tech ISYE 7406 course materials
- NOAA for weather data access
- Open-source Python data science community

---

*This project demonstrates the application of machine learning techniques to real-world business problems, showcasing the end-to-end process from data exploration to model deployment and interpretation.*