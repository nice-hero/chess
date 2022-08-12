

import subprocess
import json
import ast
import re

import subprocess
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel




app = FastAPI()


class Post(BaseModel):
   pgn: str
 #   content: str
#    published: bool = True
 #   rating: Optional[int] = None


# request get method url: "/"








@app.get("/")
async def root():
    return {"message": "تم تهكيرك بنجاح ^_^ welcome to my api!!!!ghkuhkljh!!!1"}




@app.get("/posts")
def get_posts():
    return {"data": "this is a post"}





# terminal >> uvicorn --host 0.0.0.0 test22:app --reload
@app.post("/pgntofen")
def create_posts(get_pgn: Post):
    pgn_str = get_pgn.pgn
    print(pgn_str)
    print(type(get_pgn.pgn))
    #print(get_pgn.dict())


    pgn_list=eval(pgn_str)
    print(pgn_list)
    print(type(pgn_list))

    #list_length=len(pgn_list)
    #everyitem=0
    for everyitem in pgn_list :
        pgn_str = pgn_str + everyitem + " "     #change from list to Str (without "") with space between each move and append it to pgn_str
    pgn_str = pgn_str + "*"                      # append * to the end of pgn moves (to be compatible with our pgn-extract app)



    #File = open(r"B:/Programs_Installed_Here/pycharm_project/fastapi/payload.pgn","w")  # open a file to save pgn payload data in it ... and open it later from terminal
    File = open(r"/app/./payload.pgn","w")  # open a file to save pgn payload data in it ... and open it later from terminal # server compatible path
    File.write(pgn_str)
    # File_object.writelines(L) for L = [str1, str2, str3]   # write Multible lines to file
    print(pgn_str,"str")
    File.close()




    # todo : we need to edit this path/command to be compatible/executed with terminal/linux rather than cmd/windows
    #result = subprocess.check_output(["B:/Programs_Installed_Here/pycharm_project/fastapi/pgn-extract.exe", "-F", "payload.pgn", "--json", "-s"],encoding='ascii', stderr=subprocess.STDOUT, shell=False)
    result = subprocess.check_output(
        ["/app/./pgn-extract.exe", "-F", "payload.pgn", "--json", "-s"],encoding='ascii', stderr=subprocess.STDOUT, shell=False) # server compatible path

    # TODO:
    result = re.findall(r'(?<=\")[^"]*\/.*?\/.*?\/.*?\/.*?\/.*?\/.*?\/[^"]*(?=\")', result)[0] # RegEx (Regular Expression) to Extract FEN From json Data


    print("fen is : " ,result)
    return {"fen": result}


























