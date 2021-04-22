# -*- coding: utf-8 -*-
import boto3
import numpy as np
import scipy
import sklearn
import json
import pickle



class Classifier:
    def __init__(self):
        with open("model.pkl", "rb") as f:
            self.model = pickle.load(f)
    def predict(self, data):
        z = self.model.predict([data])
        return z[0]

# We are using classification this time
#classifier = Classifier()
client = boto3.client('iot-data', region_name='us-east-2')


def lambda_handler(event, context):
    #TODO1: Get your data
    data = np.array(event['features'])
    out = classifier.predict(data)

    print(out)
    #Get your maximum of CO2 data 

    #TODO2: Send response back to your device

    response = client.publish(
       topic=event['device_id'],
        qos=1,
        payload=json.dumps({"prediction": out})
    )
    
    #TODO3: Send the results to IOT analytics for aggregation
    response = client.publish(
       topic="data/result",
        qos=0,
        payload=json.dumps({"prediction": out})
    )

    #TODO4: Send results to a monitor client
    

