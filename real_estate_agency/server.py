from flask import Flask, request, jsonify
import pickle
import numpy as np

# загружаем модель из файла
with open('lr_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Test message. The server is running"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json)
    features = features.reshape(1, 8)
    prediction = model.predict(features)
    return  jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run('localhost', 5000)