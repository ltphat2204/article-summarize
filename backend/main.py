import uvicorn
from fastapi import FastAPI, Response
from model import CrawlRequest, WordCloudRequest
from fastapi.middleware.cors import CORSMiddleware
from crawl import searchGoogle
from datetime import datetime
from gen_wordcloud import generateWordCloud
import pandas as pd
import os
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/crawl")
async def crawl(req: CrawlRequest):
    print("New crawl")

    fullSearch = ' + '.join(req.search)
    result = searchGoogle(fullSearch, req.quantity)

    df = pd.DataFrame(result)
    filePath = f'temp-{datetime.now().strftime("%Y-%m-%d-%H-%M")}.xlsx'
    df.to_excel(filePath)

    if os.path.exists(filePath):
        os.remove(filePath)

    print("Crawl done")
    return result

@app.post("/wordcloud")
async def wordcloud(req: WordCloudRequest):
    print("New Wordcloud")

    plt = generateWordCloud(req.text)
    temp_file = io.BytesIO()
    plt.savefig(temp_file, format='png')

    temp_file.seek(0)
    plt.close()

    print("Gen WC done")
    return Response(content=temp_file.read(), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="debug", reload=True)