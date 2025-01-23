# Flask Application

This is a simple Flask application that demonstrates a basic "Hello World" functionality.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   └── routes.py
├── venv
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:

```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app`.

## License

This project is licensed under the MIT License.