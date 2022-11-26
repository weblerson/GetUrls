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
    lines: List[bytes] = file.file.readlines()

    results: Results = [Utils.find_urls_str(line.decode()) for line in lines if len(line) != 0][0]

    return {
        'success': True,
        'body': results
    }
