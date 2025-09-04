# ACEest Fitness Flask Application

This project is a simple fitness tracker web application built using Flask. It allows users to log their workouts and view a list of logged workouts.

## Project Structure

```
aceest_fitness_flask
├── app.py                # Main entry point of the Flask application
├── templates
│   └── index.html        # HTML template for the main page
├── static
│   └── style.css         # CSS styles for the application
├── tests
│   └── test_app.py       # Unit and functional tests for the application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
└── README.md             # Documentation for the project
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repository-url>
cd aceest_fitness_flask
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install the required packages
```bash
pip install -r requirements.txt
```

## How to Run the Application Locally

1. **Start the Flask application:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## How to Execute the Tests Locally

1. **Ensure you are in the project root directory.**
2. **Run the tests using pytest:**
   ```bash
   pytest tests/
   ```
   This will discover and run all unit and functional tests in the `tests` folder.

## Docker Usage (Optional)

1. **Build the Docker image:**
   ```bash
   docker build -t aceest_fitness_flask .
   ```
2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 aceest_fitness_flask
   ```
3. **Access the application at:**  
   `http://127.0.0.1:5000/`

## GitHub Actions Pipeline Overview

This project includes a CI/CD pipeline using GitHub Actions, defined in `.github/workflows/ci.yml`.  
On every push or pull request to the `main` branch, the pipeline will:

- **Check out the code**
- **Set up Python**
- **Install dependencies**
- **Run all tests using pytest**
- **Build the Docker image**

This ensures code quality and that the application builds and passes all tests before deployment.

## Features

- Add workouts with duration.
- View a list of logged workouts.

## License

This project is licensed under the MIT License.