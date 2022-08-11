

import subprocess
from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import json




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
    #print(get_pgn.dict())


    #



    # todo : we need to edit this path/command to be compatible/executed with terminal/linux rather than cmd/windows
    result = subprocess.check_output(["B:/Programs_Installed_Here/pycharm_project/fastapi/pgn-extract.exe", "-F", "3.pgn", "--json", "-s"],
        encoding='ascii', stderr=subprocess.STDOUT, shell=False)

    result = json.loads(result)
    result = result[0]
    fen = result["Moves"][0]["FEN"]

    print("fen is : ",fen)
    return {"fen": fen}






