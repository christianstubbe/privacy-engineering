from opa_python_client import Client
# TODO: add dotenv import

# Initialize OPA Client
opa_client = Client()

# Load policy
with open('rbac_policy.rego', 'r') as file:
    policy = file.read()
    opa_client.create_policy("mypolicy", policy)

def serverless_function(request):
    # Example input data
    input_data = {"method": request.method}
    
    # Evaluate policy
    result = opa_client.evaluate_policy("mypolicy", input_data)
    
    # Take action based on policy evaluation result
    if result["result"]:
        return "Request allowed"
    else:
        return "Request denied", 403
