from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup

import decouple

from pydantic import BaseModel

from typing import List, Tuple, Dict

Results = List[Dict[str, str]]

__all__: List[str] = ['Config', 'FastAPI', 'Body', 'Results', 'UploadFile', 'File', 'List',
                      'BeautifulSoup']


class Body(BaseModel):
    html: str


class Config:
    def __init__(self):
        self._app: FastAPI

        if decouple.config('PROD', cast=bool):
            self._app = FastAPI(docs_url=None, redoc_url=None)
        else:
            self._app = FastAPI()

        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['POST'],
            allow_headers=['*']
        )

    @property
    def app(self) -> FastAPI:
        return self._app
