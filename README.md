# Project Name
> Toolbox for enforcing purpose-based access control in cloud native applications.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)
[![Terraform](https://github.com/christianstubbe/usability-engineering/actions/workflows/terraform.yml/badge.svg)](https://github.com/christianstubbe/usability-engineering/actions/workflows/terraform.yml)

## Table of Contents
- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Installation

### Prerequisites

- Google Cloud CLI
- Terraform
- Serverless CLI

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Setup

```sh
pip install -r requirements.txt
```

## Development

### API Testing

FastAPI comes with built-in support for automatic generation of API documentation, thanks to its use of Python type hints and the underlying Starlette framework. The built-in docs use OpenAPI and JSON Schema under the hood, so you can make use of any tooling that supports these standards.

You can use these OpenAPI specifications to automatically create Postman requests. 

Follow these steps:

1. **Run your FastAPI application**: Run your FastAPI app using `uvicorn`. If your app is in a file called `main.py`, you would do:

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the OpenAPI docs**: Open your browser and go to `http://localhost:8000/docs` (adjust the URL as necessary for your environment). This will display the Swagger UI, which is a visual representation of your API derived from the OpenAPI spec.

3. **Get the OpenAPI JSON**: You can get the actual OpenAPI JSON used to generate this page by going to `http://localhost:8000/openapi.json`.

4. **Import into Postman**: 

   - Open Postman
   - Click on `Import`
   - Paste the URL from step 3 (i.e., `http://localhost:8000/openapi.json`)
   - Select `Import as API`

Postman will create a new collection with all your API endpoints, including parameters, request bodies, etc. Please note that the application needs to be running in order to access the OpenAPI JSON spec.

## Testing

Explain how to run the automated tests for this system.

```sh
example commands to run tests
```

## Deployment

Add additional notes about how to deploy this on a live system or a platform.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- Dr. Frank Pallas
