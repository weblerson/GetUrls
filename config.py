from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from re import Pattern

from pydantic import BaseModel

from typing import List, Tuple, Dict

Matches = List[Tuple[str]]
Results = List[Dict[str, str]]

__all__: List[str] = ['Config', 'FastAPI', 'Body', 'Matches', 'Results', 'Pattern']


class Body(BaseModel):
    html: str


class Config:
    def __init__(self):
        self._app: FastAPI = FastAPI()
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['POST'],
            allow_headers=['Content-Type', 'Accept']
        )

    @property
    def app(self) -> FastAPI:
        return self._app
