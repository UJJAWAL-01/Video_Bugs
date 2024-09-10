from flask import Flask, render_template, request, redirect, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Replace the following URI with your MongoDB Atlas connection string
app.config["MONGO_URI"] = "mongodb+srv://harshal:Harshal2022@cluster0.u5i2m.mongodb.net/form?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

# Route for rendering the form
@app.route('/')
def index():
    return render_template('form.html')

# Route for handling form submissions
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Extract form data
        form_data = {
            "location": request.form.get('location'),
            "date_time": request.form.get('date_time'),
            "detected_by": request.form.get('detected_by'),
            "description": request.form.get('description'),
            "camera_type": request.form.get('camera_type'),
            "found_by": request.form.get('found_by'),
            "camera_model": request.form.get('camera_model'),
            "camera_color": request.form.get('camera_color'),
            "camera_lens_specs": request.form.get('camera_lens_specs'),
            "battery_status": request.form.get('battery_status'),
            "storage_status": request.form.get('storage_status'),
            "evidence_taken": request.form.get('evidence_taken'),
            "actions_taken": request.form.get('actions_taken'),
            "additional_comments": request.form.get('additional_comments')
        }
        
        # Insert data into MongoDB
        mongo.db.video_bug_detection.insert_one(form_data)

        return redirect('/')

# API route to create a new entry (equivalent to form submission)
@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    if data:
        mongo.db.video_bug_detection.insert_one(data)
        return jsonify({"message": "Data added successfully"}), 201
    return jsonify({"error": "No data provided"}), 400

# API route to retrieve data by ID
@app.route('/api/data/<id>', methods=['GET'])
def get_data(id):
    try:
        data = mongo.db.video_bug_detection.find_one({"_id": ObjectId(id)})
        if data:
            data['_id'] = str(data['_id'])  # Convert ObjectId to string
            return jsonify(data), 200
        return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API route to update data by ID
@app.route('/api/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.json
    if data:
        try:
            result = mongo.db.video_bug_detection.update_one({"_id": ObjectId(id)}, {"$set": data})
            if result.matched_count:
                return jsonify({"message": "Data updated successfully"}), 200
            return jsonify({"error": "Data not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "No data provided"}), 400

# API route to delete data by ID
@app.route('/api/data/<id>', methods=['DELETE'])
def delete_data(id):
    try:
        result = mongo.db.video_bug_detection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Data deleted successfully"}), 200
        return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
