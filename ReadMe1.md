# Aceest Fitness Flask Application

This is a simple Flask application for managing items with add and delete functionality.  
It includes unit and functional tests, Docker support, and CI/CD via GitHub Actions.

## Features

- Add items (`/add`)
- Delete items (`/delete/<id>`)
- List items (`/items`)
- RESTful API with auto-generated IDs

## Getting Started

### Prerequisites

- Python 3.10+
- Docker (optional for containerization)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aceest_fitness_flask.git
   cd aceest_fitness_flask
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

### Running Tests

```bash
pytest tests/
```

### Docker Usage

Build and run the Docker container:

```bash
docker build -t aceest_fitness_flask .
docker run -p 5000:5000 aceest_fitness_flask
```

### Continuous Integration

GitHub Actions workflow is provided in `.github/workflows/ci.yml` to:

- Install dependencies
- Run tests
- Build Docker image

## API Endpoints

- `POST /add`  
  Add an item.  
  **Body:** `{ "name": "Item Name" }`  
  **Response:** `{ "id": 1, "success": true }`

- `DELETE /delete/<id>`  
  Delete an item by ID.  
  **Response:** `{ "deleted": true }`

- `GET /items`  
  List all items.

## Project Structure

```
EC1/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
└── tests/
    └── test_app.py
```

## License