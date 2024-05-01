from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from typing import Optional
import uvicorn
import syncedlyrics
import re
import json
# 
app = FastAPI()

@app.get("/")
async def get_index():
    # Đảm bảo rằng đường dẫn đến index.html là đúng
    return FileResponse("templates/index.html")


@app.get("/lyrics/")
async def get_lyrics(song_name: Optional[str] = None):
    if not song_name:
        raise HTTPException(status_code=400, detail="Song name is required")
    
    lrc = syncedlyrics.search(song_name)
    if not lrc:
        return {"error": "Lyrics not found"}

    lines = lrc.split('\n')
    json_data = []
    pattern = r'\[(\d+:\d+\.\d+)\] (.+)'
    for line in lines:
        match = re.match(pattern, line)
        if match:
            timestamp, text = match.groups()
            json_entry = {
                "time": timestamp,
                "lyrics": text
            }
            json_data.append(json_entry)
    
    return json_data

if __name__ == "__main__":
    query = input("Enter Song Name: ")
    print(f"Fetching lyrics for: {query}")
    # Assuming your FastAPI app is running on the default port 8000
    url = f"http://127.0.0.1:8070/lyrics/?song_name={query.replace(' ', '%20')}"
    print("You can view the lyrics at:", url)
    uvicorn.run(app, host="127.0.0.1", port=8070, log_level="info")
