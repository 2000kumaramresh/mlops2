from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/hello/<user>")
def hello_world(user):
    return f"<p>Hello {user}!</p>"

@app.route("/sum/<x>/<y>")
def sum(x,y):
    return str(int(x) + int(y))

def load_model():
    model_svm = joblib.load("models/M23CSA004_svm_gamma:0.1_C:100.joblib")
    model_tree = joblib.load("models/M23CSA004_tree_max_depth:20.joblib")
    model_lr = joblib.load("models/M23CSA004_lr_solver:lbfgs.joblib")
    return model_svm,model_tree,model_lr

@app.route("/predict/<type>", methods=['POST'])
def pred_model(type):
    if(type=='svm'):
        model = load_model()[0]
    elif(type=='tree'):
        model = load_model()[1]
    elif(type=='lr'):
        model = load_model()[2]


    js = request.get_json()
        
    image = js['image']
    model = joblib.load('models/svm_gamma:0.0005_C:1.joblib')
    predict = model.predict([image])
    return str(predict)

@app.route("/compare", methods=['POST'])


def compare_images():
    js = request.get_json()
    image1 = np.array(js['image1'])
    image2 = np.array(js['image2'])

    image1.reshape(1, -1)
    image2.reshape(1, -1)
    model = joblib.load('Models/svm_gamma:0.0005_C:1.joblib')
    predict = model.predict([image1,image2])
    # predict2 = model.predict(image2)

    if( (predict[0] == predict[1])):
        return f"True"
    else:
        return f"False"