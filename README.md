![Fast API Skeleton](https://github.com/user-attachments/assets/897da9ea-c0cb-42c1-a746-f8cf72431692)

# Fast API skeleton
Employs the FastAPI pattern explored in Bill Lubanovic's book _FastAPI: Modern Python Web Development_.

## Structure

    .
    ├── data
    │   └── __init__.py
    ├── errors.py
    ├── fake
    │   ├── example.py
    │   └── __init__.py
    ├── main.py
    ├── model
    │   ├── example.py
    │   └── __init__.py
    ├── README.md
    ├── service
    │   ├── example.py
    │   └── __init__.py
    ├── test
    │   ├── full
    │   ├── int
    │   └── unit
    │       └── service
    │           └── example.py
    └── web
        ├── example.py
        └── __init__.py

## Setup

Clone or fork this code then create a virtual environment:

```bash
python3 -m venv .fastapi
source .fastapi/bin/activate
python3 -m pip install -r requirements.txt
```

1. Define a model layer.
2. Create fakes for testing and building logic
3. Create service layer, that connects data/fakes to web layer.
4. Create web layer, defining router endpoints.
5. Connect the web layer to the app defined in main.
6. Create tests.
7. Create data layer - this should include an init.py that handles creating databases as necessary.
