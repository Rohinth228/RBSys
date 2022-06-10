# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import pickle

app = Flask(__name__)
api = Api(app)

@app.route('/prediction',methods=['POST'])
def post():
    pred=None
    data1 = request.get_json()	 # status code
    line = list(data1.values())
    for a in range(len(data1)):
        if(line[a] == 'Yes'):
            line[a] = 1
        if(line[a] == 'No'):
            line[a] = 0
    line.pop(0)
    line.pop(0)
    line.pop(1)
    if line[0]<24:
        if line[7]==1 or line[8]==1 or line[9]==1:
            if line[10]==1 or line[11]==1 or line[12]==1:
                return {"class":"Screen Immediately"}
        if line[1]==1 or line[2]==1:
            if line[3]==1 or line[4]==1 or line[5]==1 or line[6]==1:
                return {"class":"Screen After 1 month"}
        return {"class":"No Risk"}
    if line[0]<36:
        if line[6]==1 or line[7]==1 or line[8]==1 or line[9]==1 or line[10]==1 :
            if line[11]==1 or line[12]==1 or line[13]==1 or line[14]==1:
                return {"class":"Screen Immediately"}
        if line[1]==1:
            if line[2]==1 or line[3]==1 or line[4]==1 or line[5]==1:
                return {"class":"Screen After 1 month"}
        return {"class":"No Risk"}
    if line[0]<48:
        if line[7]==1 or line[8]==1 or line[9]==1 or line[10]==1 or line[11]==1:
            if line[12]==1:
                return {"class":"Screen Immediately"}
        if line[1]==1:
            if line[2]==1 or line[3]==1 or line[4]==1 or line[5]==1 or line[6]==1:
                return {"class":"Screen After 1 month"}
        return {"class":"No Risk"}



if __name__ == '__main__':
	app.run(debug=True)
