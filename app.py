from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

workouts = []
items = []
next_id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        workout = request.form.get('workout')
        duration_str = request.form.get('duration')

        if not workout or not duration_str:
            flash('Please enter both workout and duration.', 'error')
            return redirect(url_for('index'))

        try:
            duration = int(duration_str)
            workouts.append({"workout": workout, "duration": duration})
            flash(f"Workout '{workout}' added successfully!", 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Duration must be a number.', 'error')
            return redirect(url_for('index'))

    return render_template('index.html', workouts=workouts)

@app.route('/clear', methods=['POST'])
def clear_workouts():
    workouts.clear()
    flash('All workouts cleared.', 'success')
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_item():
    global next_id
    data = request.get_json()
    item = {
        'id': next_id,
        'name': data.get('name')
    }
    items.append(item)
    next_id += 1
    return jsonify({'id': item['id'], 'success': True}), 201

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({'deleted': True}), 200

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)