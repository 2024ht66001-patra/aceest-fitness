# ACEest Fitness Flask Application

This project is a simple fitness tracker web application built using Flask. It allows users to log their workouts and view a list of logged workouts.

## Project Structure

```
aceest_fitness_flask
├── app.py                # Main entry point of the Flask application
├── templates
│   └── index.html       # HTML template for the main page
├── static
│   └── style.css        # CSS styles for the application
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd aceest_fitness_flask
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install Flask
   ```

## Usage

1. **Run the application**:
   ```
   python app.py
   ```

2. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Features

- Add workouts with duration.
- View a list of logged workouts.

## License

This project is licensed under the MIT License.