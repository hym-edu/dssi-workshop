## Data Product Development and Deployment with Streamlit

### Step 1: Train and Save Model
1. Perform EDA and model development on Jupyter notebook.
2. Develop training and model registry scripts to automate model training and persistance respectively.
3. Run the training script to train a loan approval model:
```
python src/training.py --data_path data/churn.csv --model_path models/ --f1_criteria 0.7
```
Sample model training notebook: [DSSI_ChurnModel.ipynb](https://github.com/hym-edu/dssi-workshop/blob/main/notebooks/DSSl_ChurnModel.ipynb)  

Sample training script: [training.py](https://github.com/hym-edu/dssi-workshop/blob/main/src/training.py)
  
Sample model registry script: [model_registry.py](https://github.com/hym-edu/dssi-workshop/blob/main/src/model_registry.py)

### Step 2: Create App and Load Model
1. Develop an inference script to serve predictions.
2. Create a loan approval application with Streamlit that automates decisions with user inputs and trained model.  

Sample inference script: [inference.py](https://github.com/hym-edu/dssi-workshop/blob/main/src/inference.py)  

Sample application code: [app.py](https://github.com/hym-edu/dssi-workshop/blob/main/app.py)

### Step 3: Test App Locally
Run and test the application locally:
```
streamlit run app.py
```

### Step 4: Deploy App Online
1. Commit repository to GitHub
2. Deploy on Streamlit community cloud (example: https://dssi-workshop-submission.streamlit.app/)