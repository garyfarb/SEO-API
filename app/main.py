from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'Example' : 'Welcome to SEO API', 'data' : '0'}