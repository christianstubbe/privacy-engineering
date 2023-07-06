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