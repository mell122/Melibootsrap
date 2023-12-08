from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import hmac, hashlib , os , docker

app = FastAPI()

# Replace with your GitHub secret
SECRET = "your_github_secret"

class GitHubEvent(BaseModel):
    action: str
    repository: dict
    # Add more fields as needed

@app.post("/github-webhook")
async def github_webhook(event: GitHubEvent, signature: str = Header(...)):
    # Ensure the request comes from GitHub by validating the signature
    validate_signature(signature, await request.body())

    # Handle different GitHub events
    if event.action == "push":
        # Handle "opened" event
        repo_name = event.repository.get("name")

        path = find_file("Dockerfile")
        if path != None:
            ci(path)
            cd()

        return {"message": f"starting Ci for {repo_name}"}
        


    # Add more event handling as needed

    return {"message": "Unhandled GitHub event"}


def validate_signature(signature: str, payload: bytes):
    secret = bytes(SECRET, 'utf-8')
    expected_signature = "sha1=" + hmac.new(secret, payload, hashlib.sha1).hexdigest()

    if not hmac.compare_digest(signature, expected_signature):
        raise HTTPException(status_code=400, detail="Invalid GitHub signature")

def ci(path):
    docker.client.ImageCollection.build(path)

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

def find_file(x):
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    
    dockerfile_path = os.path.join(parent_directory, x)
    


    if os.path.exists(dockerfile_path):
        return dockerfile_path
    else:
        return None


def cd ():
    path = find_file("yml")
    if path != None:
      
      apply_kubectl(path)


    

@app.get("/test")
def test():
    path = find_file("Dockerfile")
    if path != None:
        ci(path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
