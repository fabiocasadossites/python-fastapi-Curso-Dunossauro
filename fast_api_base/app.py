from fastapi import FastAPI

app = FastAPI()

# Documentações
# /redoc
# /docs


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}
