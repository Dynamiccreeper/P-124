from flask import Flask,jsonify,request

# creating a list of tasks

data = [
    {
        'id': 1,
        'title': 'Raju',
        'description': '9987644456', 
        'done': False
    },
    {
        'id': 2,
        'name': 'Rahul',
        'Contact': '9876543222', 
        'done': False
    }
]

app=Flask(__name__)



@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message":"Please provide the data!"
        }, 400)

    Contact={
        'id': data[-1]['id'] + 1,
        'Name': request.json['title'],
        'Contact': request.json.get('Contact', ""),
        'done':False
    }
    data.append(data)
    return jsonify({
        "status":"Success",
        "message": "Task added successfully!"
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data": data
    })

if(__name__=="__main__"):
    app.run(debug=True)