# Fast API skeleton

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

1. Define a model layer.
2. Create fakes for testing and building logic
3. Create service layer, that connects data/fakes to web layer.
4. Create web layer, defining router endpoints.
5. Connect the web layer to the app defined in main.
6. Create tests.
7. Create data layer - this should include an init.py that handles creating databases as necessary.