
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify
import shutil
import os
import base64
from PIL import Image
import demo as dm




app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)



class shopClassifier_api(Resource):
    @app.route('/',methods=['POST'])
    def post(self):

        receivedData = request.get_json()
      
        text = receivedData['text']
        print()
        byte_check = text[0:2]
        if byte_check == "b'":            
            text = text[2:len(text)-1]
            img = base64.b64decode(text)
        else:
            img = base64.b64decode(text)
        

        with open("E:\\Sachuu\\Read Text\\Final\\demo_image\\test2.jpg",'wb') as f:
            f.write(img)
        

        try:            
            res = dm.run()#os.system("!CUDA_VISIBLE_DEVICES=0 python3 demo.py --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --image_folder /content/deep-text-recognition-benchmark/demo_image/ --saved_model TPS-ResNet-BiLSTM-Attn.pth")
        	
            returnJson = {
            	'result': res,
            	'status': 200 
	        }
            return jsonify(returnJson) 
        except Exception as e:
        	returnJson = {
            	'msg': e,
            	'status': 500
        	}
        	return jsonify(returnJson)
       

api.add_resource(shopClassifier_api,'/expression/')

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5001, debug=False)
    
# Home route
@app.route('/api')
def welcome():
    return 'Text Summarization & Grammar Checking API'