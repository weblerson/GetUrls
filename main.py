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


@app.post('/files')
async def get_file_urls(file: UploadFile = File()):
    html: bytes = file.file.read()
    results: Results = Utils.find_urls_str(html.decode())

    return {
        'success': True,
        'body': results
    }
