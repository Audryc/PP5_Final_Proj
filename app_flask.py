from flask import Flask
import flask
from flask import request
from flask import Response
import pandas as pd
import operator

bus_data = pd.read_csv("ny_bus_new.csv")
score_data = pd.read_csv("result.csv")

app = Flask(__name__)


@app.route('/nyc-zip-code-tabulation-areas-polygons.geojson')
def map_data():
    with open("nyc-zip-code-tabulation-areas-polygons.geojson","r") as json_map:
        return json_map.read()



@app.route('/')
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("ny_map.html", 'r') as viz_file:
        return viz_file.read()

@app.route('/score')
def score_route(zip_code=""):
    print "type = ", type(request.args.get('postal_code'))
    print "postal code = ", request.args.get('postal_code')
    
    try:
        zip_code = int(request.args.get('postal_code'))
    except:
        zip_code = 10030
    
    print "zip_code = {}".format(zip_code)
    data = score_data[score_data["postal_code"]==zip_code].iloc[0].to_dict()
    data2 = sorted(data.items(),key=operator.itemgetter(1),reverse=True)[2:7]
    print sorted(data.items(),key=operator.itemgetter(1),reverse=True)
    data4 = []
    for j in range(len(data2)):
        if data2[j][1]<1:
            data4.append(data2[j])
    for vae in data4:
        data2.remove(vae)
    print data2
    return flask.jsonify(data2)

@app.route('/bus')
def bus_route():
    zip_code = request.args.get('zip_code')
    cat = request.args.get('new_categories')
    zip_code=int(zip_code)
    
    data = bus_data.loc[(bus_data['postal_code'] == zip_code) &(bus_data['new_categories'] == cat)]
    data = data.to_dict(orient="records")
    print(data)
    data_dict={'res':data}
    #resp = Response(response=data_dict,
    #status=200, \
    #mimetype="application/json")
    
    #return(resp)
    return flask.jsonify(data_dict)





if __name__ == '__main__':
    app.run(debug=True, port=5051, host='0.0.0.0')

