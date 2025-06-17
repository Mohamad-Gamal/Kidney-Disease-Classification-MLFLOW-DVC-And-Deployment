# Kidney-Disease-Classification-Deep-Learning-Project-With-MLFLOW-DVC-And-Deployment
## This project applies deep learning for classifying kidney disease using Convolutional Neural Networks (CNN), with integrated tools like **MLFLOW** for experiment tracking, **DVC** for data version control, and **Flask** for deployment.

---

## Workflows
   1. Update config.yaml
   2. Update secrets.yaml [Optional]
   3. Update params.yaml
   4. Update the entity
   5. Update the configuration manager in src config
   6. Update the components
   7. Update the pipeline
   8. Update the main.py
   9. Update the dvc.yaml
   10. app.py

## 🚀 How to Run the Project

### ✅ STEP 1: Clone the Repository

```bash
git clone https://github.com/Mohamad-Gamal/Kidney-Disease-Classification-MLFLOW-DVC-And-Deployment.git
cd Kidney-Disease-Classification-MLFLOW-DVC-And-Deployment
```
### ✅ STEP 2: Create a Conda Environment

```bash
conda create -n kidney python=3.8 -y
conda activate kidney
```
### ✅ STEP 3: Install Required Packages

```bash
pip install -r requirements.txt
```
### ✅ STEP 4: Run the Application

```bash
python app.py
```
### 🌐 Access the App
#### Open your browser and go to:

```bash
http://localhost:5000/
```