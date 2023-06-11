from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
import joblib

app = FastAPI()


#Load your saved model and components
def load_model():
  num_imputer = joblib.load('numerical_imputer.joblib')
  scaler = joblib.load('scaler.joblib')
  model = joblib.load('sepsis_model.joblib')
  return num_imputer, scaler, model

#Create a class for taking inputs
class UserInput(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance:int

@app.get('/')
async def index():
    return {"Sepsis API": "Sepsis Prediction"}

#get data and make predictions
@app.post('/predict/')
async def predict(UserInput: UserInput):

  data = {
           'PRG': UserInput.PRG, 
           'PL': UserInput.PL,
           'PR': UserInput.PR,
           'SK': UserInput.SK,
           'TS': UserInput.TS,
           'M11': UserInput.M11,
           'BD2': UserInput.BD2,
           'Age': UserInput.Age,
           'Insurance': UserInput.Insurance,
                }
  df = pd.DataFrame(data, index=[0])
  num_col =  [ 'PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age','Insurance']
  num_imputer, scaler, model = load_model()
     #Scale numerical colums
  scaled_col = scaler.transform(df[num_col])
  df2 = pd.DataFrame(scaled_col)                  
  prediction = model.predict(df2).tolist()

  if (prediction[0] == 1):
    result = "Positive Sepsis"
  else:
    result = "Negative Sepsis"

  return{"result":result}