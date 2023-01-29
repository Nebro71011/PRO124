from flask import Flask,jsonify,request
app = Flask(__name__)

tasks=[
    {
        "Contact":"9769670604",
        "Name":"Advik",
        "done":"false",
        "id":1
    },
    {
        "Contact":"94026759",
        "Name":"Raj",
        "done":"false",
        "id":2
    }
]
contact={
    'id': tasks[-1]['id']+1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact',""),
    'done': False
}

@app.route("/add-data",methods=["POST"])
def add_task():
    if request.json:
        return jsonify({
            "tasks":tasks,
            "status":"successfull",
            "message":"Tasks added successfully"
        })
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

if __name__ == "__main__":
  app.run(debug=True)