from flask import Flask, request, jsonify
import pandas as pd
import joblib
import traceback
import os
from flask_cors import CORS
from flask_cors import cross_origin



from preprocessing.cleaning_data import preprocess
from predict.prediction import predict


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home():
    message= jsonify("ALIVE")
    message.headers.add('Access-Control-Allow-Origin', '*')
    return message

@app.route('/predict', methods=['POST'])
@cross_origin()
def price_predict():

    try:
        json_ = request.json
        ds = pd.DataFrame(json_)

        query = preprocess(ds)


        price_pred = list(predict(query))
        response = jsonify({"Price": list(price_pred)})
        
        return response
    except:
        return jsonify({"trace": traceback.format_exc()})


@app.route('/predict', methods=['GET'])
def format_data():
    m= jsonify("""
                data format for the POST request:
                {
                    "data": {"type": "APARTMENT" | "HOUSE" ,"room_number": int,"area": int,"kitchen_equipped": bool 0 | 1,"furnished": bool  0 | 1,"fireplace": bool  0 | 1,"terrace": bool  0 | 1,"terrace_area": int,"garden": bool 0 | 1,"garden_area": int,"land_surface": int,"facade_count": int,"swimming_pool": bool 0 | 1,"building_condition": "TO_BE_DONE_UP" | "TO_RENOVATE" | "GOOD" | "JUST_RENOVATED" | "AS_NEW" | "TO_RESTORE""Province":"LUXEMBOURG" | "HAINAUT" | "FLANDRE-OCCIDENTALE" | "LIEGE" | "FLANDRE-ORIENTALE" | "BRUXELLES" | "BRABANT FLAMAND" | "ANVERS" | "BRABANT WALLON" | "LIMBOURG" | "NAMUR"
                            
                    }
                }
                """)
    m.headers.add('Access-Control-Allow-Origin', '*')        
    return m        

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',threaded=True, port=port, debug=True)