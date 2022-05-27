import uvicorn
import os

# GCS private key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '[key위치]'

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)