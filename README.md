# Iris Flower Classification

## 📌 Project Overview
This project is a Machine Learning pipeline for classifying Iris flower species based on their sepal and petal measurements. The project follows an end-to-end machine learning workflow, incorporating data preprocessing, model training, evaluation, and inference.

This project is designed to demonstrate skills in:
- Data Preprocessing and Feature Engineering
- Exploratory Data Analysis (EDA)
- Model Training and Hyperparameter Tuning
- Model Evaluation and Interpretation
- Deployment with DVC and CI/CD using GitHub Actions

## 🚀 Tech Stack
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Version Control**: Git, GitHub
- **Data Version Control**: DVC
- **CI/CD**: GitHub Actions
- **Environment Management**: Virtualenv
- **Containerization**: Docker (optional for deployment)

---

## 📂 Project Structure
```
Iris Flower Classification/
│── data/
│   ├── raw/                # Raw dataset
│   ├── processed/          # Cleaned and processed dataset
│── notebooks/
│   ├── exploratory_data_analysis.ipynb  # EDA and visualization
│   ├── model_training.ipynb             # Model training and evaluation
│── src/
│   ├── data_processing.py   # Functions for cleaning and preprocessing data
│   ├── train_model.py       # Training script
│   ├── evaluate_model.py    # Model evaluation metrics
│   ├── inference.py         # Model inference
│── .gitignore
│── dvc.yaml                 # DVC pipeline
│── requirements.txt
│── README.md
```

---

## 📊 Data Pipeline
The pipeline follows these steps:
1. **Data Ingestion**: Load and clean the raw data (`data/raw/iris.csv`).
2. **Data Processing**: Cleaned data is stored in `data/processed/iris_cleaned.csv`.
3. **EDA & Visualization**: Conducted in `notebooks/exploratory_data_analysis.ipynb`.
4. **Model Training**: Trains and saves a classification model (`notebooks/model_training.ipynb`).
5. **Evaluation**: Model performance is assessed using accuracy, precision, recall, and F1-score (`src/evaluate_model.py`).
6. **Inference**: Deploy the trained model for real-time predictions (`src/inference.py`).
7. **Versioning & Automation**: DVC tracks data/model versions, and GitHub Actions automates tests and deployments.

---

## ⚡ Quick Start
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/iris-classification.git
cd iris-classification
```

### 2️⃣ **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Initialize DVC**
```bash
dvc init
dvc pull  # Pull latest data and model version
```

### 5️⃣ **Run Exploratory Data Analysis**
```bash
jupyter notebook notebooks/exploratory_data_analysis.ipynb
```

### 6️⃣ **Train the Model**
```bash
python src/train_model.py
```

### 7️⃣ **Evaluate the Model**
```bash
python src/evaluate_model.py
```

### 8️⃣ **Run Inference**
```bash
python src/inference.py --input "5.1,3.5,1.4,0.2"
```

---

## 🎯 Model Performance
| Metric  | Score |
|---------|-------|
| Accuracy | 97% |
| Precision | 96% |
| Recall | 98% |
| F1-Score | 97% |

---

## 🔧 CI/CD with GitHub Actions & DVC
- **GitHub Actions** automates model testing and evaluation on every push.
- **DVC** ensures versioning of datasets and models.
- **Docker** (optional) for deploying the model as an API.

---

## 🤝 Contributing
Feel free to fork the repository and submit a pull request with improvements.

---

## 📜 License
This project is licensed under the MIT License.

---

## ✨ Contact
For questions, reach out at: [surakiat.0723@gmail.com] or connect on [LinkedIn](https://www.linkedin.com/in/surakiat-kansa-ard-171942351/)

---

🔹 **Showcasing this project in job applications?** Include a link to this repository in your resume or portfolio!

---

