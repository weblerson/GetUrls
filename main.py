from config import *
from utils import Utils

app: FastAPI = Config().app


@app.post('/urls')
def get_urls(body: Body):
    results: Results = Utils.find_urls_str(body.html)

    return {
        'success': True,
        'body': results
    }
