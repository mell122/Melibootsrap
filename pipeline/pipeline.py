import subprocess
from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel
import hmac, hashlib , os 

app = FastAPI()

# Replace with your GitHub secret
SECRET = ""

if SECRET is None:
    print("set the github secret in your env using key : GITHUB_SECRET")

# Data Model
class GitHubEvent(BaseModel):
    action: str
    repository: dict
    # Add more fields as needed

# API Endpoints
@app.post("/webhook")
async def github_webhook(request: Request):

    # Handle different GitHub events
    payload = await request.json()
    event_type = request.headers.get("X-Github-Event")
    if event_type == "push":
        # Handle "push" event
        repo_name = event.repository.get("name")

        path = find_file("Dockerfile")
        if path != None:
            if ci(path, "api-py:latest"):
                cd()

        print({"message": f"starting Ci/Cd for {repo_name}"})
        
    # Add more event handling as needed

    return {"message": "Unhandled GitHub event"}

@app.get("/test/{service}")
def test(service):
    if service == "ci":
        path = find_file("Dockerfile")
        if path != None:
            if ci(path, "api-py:latest") :
                return {"build succeed"}
            else:
                return {"build failed"}
        else:
            return{"Dockerfile Not Found"}
        
    elif service == "cd":
        try:
            cd()
            return {"message": "Deployment completed successfully"}
        except Exception as e:
            return {"message": f"Error during deployment: {str(e)}"}

    else:
        return{"test case not found."}

# GLOBAL / Helper FUNCTIONS

# Continious Integration Docker image build
def ci(path, tag):
    try:
        command = f"docker build -t {tag} -f {path} ."
        subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
# Continious Delivery Kubernetes deployment  
def cd():
    path = find_file("yml")
    if path != None:
      apply_kubectl(path)
    else:
        return {"Error:", "kubernetes deployment file not found!"}

# Kubectl Apply -f 
def apply_kubectl(file_path):
    command = f"kubectl apply -f {file_path}"

    try:
        status = os.system(command)
        if status == 0:
            print("kubectl apply completed successfully.")
        else:
            print(f"Error executing kubectl apply. Exit code: {status}")
    except Exception as e:
        print(f"Error executing kubectl apply: {e}")  

# Find a specific file based on a extension passed to the function
def find_file(x):
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)

    for root, dirs, files in os.walk(parent_directory):
        for file in files:
            if file.endswith(x):
                return os.path.join(root, file)
    return None
    
# Validation function for github secret
def validate_signature(signature: str, payload: bytes):
    secret = bytes(SECRET, 'utf-8')
    expected_signature = "sha1=" + hmac.new(secret, payload, hashlib.sha1).hexdigest()

    if not hmac.compare_digest(signature, expected_signature):
        raise HTTPException(status_code=400, detail="Invalid GitHub signature")

# Run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)