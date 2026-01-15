# import libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware # CORS - Cross-Origin Resource Sharing (used for the domain to access the API)
import nest_asyncio


# create the instance of the fastAPI
app = FastAPI()

# give the formations for the CORS
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# format to pass the data
class model_input(BaseModel):
    age : int
    sex : int
    cp  : int
    trestbps : int
    chol : int
    fbs : int
    restecg : int
    thalach : int
    exang : int
    oldpeak : float
    slope : int
    ca : int
    thal : int

    # load the saved model
heart_disease_model = pickle.load(open("/Users/macbookpro/Desktop/Heart_Disease_Predictive System/ML API in Heroku/HeartDiseasePrediction.sav", "rb"))

# post - it means we've to post a value to the API
# create the model api
@app.post('/heart_disease_prediction')

# create a function for the input parameters
def heart_disease_pred(input_parameters : model_input):
    input_data = input_parameters.model_dump_json() # convert the json data into a dictionary
    
    input_dictionary = json.loads(input_data)
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    cp  = input_dictionary['cp']
    trestbps = input_dictionary['trestbps']
    chol = input_dictionary['chol']
    fbs = input_dictionary['fbs']
    restecg = input_dictionary['restecg']
    thalach = input_dictionary['thalach']
    exang = input_dictionary['exang']
    oldpeak = input_dictionary['oldpeak']
    slope = input_dictionary['slope']
    ca = input_dictionary['ca']
    thal = input_dictionary['thal']

    # store the variables in a list
    input_lists = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

    # pass the list into a mode to make predictions
    prediction = heart_disease_model.predict([input_lists])

    # comditional statements to predict the outcome
    if prediction[0] == 0:
        return 'This person DOES NOT have a Heart Disease'
    else:
        return 'This person HAS a Heart Disease'