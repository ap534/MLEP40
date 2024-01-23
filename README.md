# MLE P40 Submission Background

This is my solution to the MLE P40 challenge and instructions for deployment. The files included show a detailed solution to the problem of creating a movie recommendation system.

## Data Analysis Report
### Found in <a href="./Data Analysis Report.ipynb">Data Analysis Report.ipynb</a>

## Modeling and Evaluation Report
### Found in <a href="./Modeling and Evaluation Report.ipynb">Modeling and Evaluation Report.ipynb</a>

## Business Evaluation Report amnd Additional Recommendations
### Found in <a href="./Business Evaluation Report and Additional Recommendations.ipynb">Business Evaluation Report and Additional Recommendations.ipynb</a>

## Deployment

#### How to deploy with docker streamlit app:
#### After git cloning the respository run in the cloned folder: 
#### ```docker-compose up --build```
#### Then browse to http://localhost:8051 which loads the steamlit app that connects to the flask based backend, or directly query flask using curl
#### ```curl http://localhost:5001/recommend\?user_id=4```

## Community Recommendation Engine Experiment
### Found in <a href="./Community Recommendation Engine Experiment.ipynb">Community Recommendation Engine Experiment.ipynb</a>
