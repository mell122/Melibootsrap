from fastapi import FastAPI, Request

# FastAPI app
app = FastAPI()

@app.post("/webhook_events")
async def webhook_handler(request: Request):
    # handle events
    payload = await request.json()
    event_type = request.headers.get("X-Github-Event")

    # reviews requested or removed
    if event_type == "pull_request":
        action = payload.get("action")
        if action == "review_requested":
            # TODO: store review request
        return "ok" 
        elif action == "review_request_removed":
            # TODO: delete review request 
        return "ok"        
    return "ok"

    # review submitted
    if event_type == "pull_request_review" and payload.get("action") == "submitted":
    # TODO: update review request
        return "ok"

    # ignore other events
    return "ok"