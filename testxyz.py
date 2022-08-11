

import subprocess
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import pgntofen

get_pgn = ''

app = FastAPI()


class Post(BaseModel):
   pgn: str
 #   content: str
#    published: bool = True
 #   rating: Optional[int] = None


# request get method url: "/"


@app.get("/")
async def root():
    return {"message": "welcome to my api!!!!ghkuhkljh!!!!!!1"}


@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}


@app.post("/pgntofen")
def create_posts(get_pgn: Post):
    pgn_str = get_pgn.pgn
    print(pgn_str)

    print(type(get_pgn.pgn))

    subprocess.check_output(["B:/Programs_Installed_Here/pycharm_project/fastapi","1.pgn -Wfen"])
 #r"C:/Windows/System32/cmd C:/temp/calc.exe"


'''
pgnConverter = pgntofen.PgnToFen()
pgnConverter.move(pgn_str)
fen = pgnConverter.getFullFen()
# fen will be 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'
'''




    print("fen is : ",fen)
    return {"fen": fen}






