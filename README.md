# CreoDAMO

```
creodamo/
├── creodamo/
|   ├── __init__.py
|   ├── settings.py
|   ├── urls.py
|   ├── wsgi.py
|   ├── asgi.py 
|   └── ...
├── apps/
|   ├── blockchain/
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── views.py
|   |   └── ...
|   ├── ai_ml/
|   |   ├── __init__.py
|   |   ├── models.py
|   |   ├── services.py
|   |   └── ...
|   └── ...
├── frontend/
|   ├── build/
|   ├── public/
|   ├── src/
|   └── ...  
├── docs/
├── tests/
├── tools/
├── scripts/
├── config/
├── pyproject.toml
├── README.md
└── ...
```

Here are some key points about the structure:

- The `creodamo/` folder is the main Django project folder.
- Inside the `creodamo/` folder, you will find the Django project files such as `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`, and others.
- The `apps/` folder contains the Django apps for each component or functionality. Each app has its own set of files, including `models.py`, `views.py`, and other files specific to that app.
- The `frontend/` folder is where you can find the frontend code, which could be built using React or Vue.js, for example. It can have subfolders such as `build/`, `public/`, `src/`, and others, depending on the frontend framework or build system used.
- The `docs/` folder is for documentation related to the project.
- The `tests/` folder is where you can place your test scripts.
- The `tools/` folder can contain any helper scripts or tools used in the project.
- The `scripts/` folder is for any additional scripts needed for the project.
- The `config/` folder can hold configuration files for the project.
- The `pyproject.toml` file specifies the project dependencies using the Poetry package manager.
- The `README.md` file provides instructions or information about the project.
- Other files and folders not specified explicitly are left open for the specific needs and requirements of the project.

# CreoDAMO
## Decentralized Asset Management and Optimization

CreoDAMO is a blockchain-based platform for securely managing digital assets. 

## Getting Started

To run CreoDAMO locally:

```
git clone https://github.com/creodamo/creodamo_platform.git
cd creodamo_platform
pip install poetry
cd creodamo_plaform
python creodamo.py --debug
```

This will start the CreoDAMO backend on http://localhost:8000.

## Documentation

See the `docs` folder for API documentation and tutorials.

## Features

- Digital asset management 
- Algorithmic trading strategies
- Decentralized storage on IPFS
- Built on Ethereum and Chainlink oracles

## Technology

The backend uses Django and Python and integrates with:

- Web3.py for Ethereum 
- IPFS HTTP API
- PostgreSQL database

The frontend is a single page app built with React.

## Development

To contribute, see `CONTRIBUTING.md`. Pull requests are welcome!
