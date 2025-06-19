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

## 🧠 MLOps Workflow Breakdown
### 1. Update config.yaml
✅ Purpose: Central configuration file with all high-level paths, URLs, filenames, etc.

📁 Example:

yaml
Copy
Edit
data_ingestion:
  source_url: "https://..."
  download_dir: "artifacts/data"
🔄 Role: Allows dynamic control of behavior across all components without changing code.

### 2. Update secrets.yaml [Optional]
🔐 Purpose: Securely store sensitive info like:

API keys

Database credentials

Access tokens

🔒 Role: Keeps sensitive data separate from code/configs for security and flexibility.

### 3. Update params.yaml
🛠 Purpose: Stores model/training-specific hyperparameters like:

Learning rate

Epochs

Batch size

💡 Role: Keeps ML tuning decoupled from code for easier experiments & reproducibility.

### 4. Update the entity
🧱 Purpose: Define structured objects (e.g., configs) using data classes.

🧾 Example:

python
Copy
Edit
@dataclass
class DataIngestionConfig:
    source_url: str
    local_file: str
🧠 Role: Creates a consistent schema to pass config data into components cleanly.

### 5. Update the configuration manager in src/config
🧭 Purpose: This class reads the YAML files (config.yaml, params.yaml) and maps them to the entity classes.

🔄 Role: Bridges raw YAML data to Python objects used in your code.

### 6. Update the components
⚙️ Purpose: Core functional logic for pipeline stages:

Data ingestion

Data transformation

Model training

Evaluation

🔨 Role: Modular, testable code units that do the real work.

### 7. Update the pipeline
🧵 Purpose: Orchestrates the order and interaction between components.

📌 Example:

python
Copy
Edit
data = ingest()
clean_data = transform(data)
model = train(clean_data)
🔁 Role: Connects all steps into a repeatable ML workflow.

### 8. Update the main.py
🚀 Purpose: Entry point of the project — triggers the pipeline.

🔄 Role: Runs the full process end-to-end:

python
Copy
Edit
if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run()
### 9. Update dvc.yaml
🧬 Purpose: Defines the pipeline stages and their dependencies using DVC (Data Version Control).

📁 Example:

yaml
Copy
Edit
stages:
  train:
    cmd: python src/train.py
    deps:
      - data/train.csv
    outs:
      - model.pkl
🧠 Role: Enables reproducible, version-controlled ML pipelines.

### 10. app.py
🌐 Purpose: Used to create an API (usually via Flask or FastAPI) to serve the model.

🚀 Role: Turns your ML model into a web service for real-time predictions.

🗂️ Summary Table
Step	Purpose	Role
config.yaml	General configuration	Central settings
secrets.yaml	Sensitive credentials	Security
params.yaml	ML hyperparameters	Reproducible tuning
Entity	Data schema classes	Structured configs
Config manager	Reads YAMLs into entities	Connection layer
Components	Actual logic	Functional ML steps
Pipeline	Orchestrates components	Workflow logic
main.py	Entry point	Runs the pipeline
dvc.yaml	Versioned stages	Reproducibility
app.py	Model API	Deployment

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