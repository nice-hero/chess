import re
import subprocess
import json
import ast

test = [{
    "test": 'test'
}]

# todo : we need to edit this path/command to be compatible/executed with terminal/linux rather than cmd/windows


# B:/Programs_Installed_Here/pycharm_project/fastapi/pgn-extract.exe -F 3.pgn --json -s

result = subprocess.check_output(
    ["B:/Programs_Installed_Here/pycharm_project/fastapi/pgn-extract.exe", "-F", "3.pgn", "--json", "-s"]
    ,encoding='ascii', stderr=subprocess.STDOUT, shell=False)

# ,encoding='ascii'
# ,encoding='utf-8'  --> decode error


#print(result)
print("-0------------------------------")
print(re.findall(r'(?<=\")[^"]*\/.*?\/.*?\/.*?\/.*?\/.*?\/.*?\/[^"]*(?=\")', result)[0]) # RegEx (Regular Expression) to Extract FEN From json Data


#result = result.replace('\n', '')
#result = result.replace('\r', '')



# print(json.detect_encoding(result))
# result = eval(result)
# result = ast.literal_eval(result)           # to convert from str to list

# result = result.replace(result[-2:],'')
# result = result.replace(result[:1],'')

# = result.strip()


# x = ast.literal_eval(result)
# print(type(x),"2")


result = result[0]
# result[0]


# print(result["Moves"])
# result = dict(result)
# print(result.Moves.dict())
# x = result.split("\r\n")

# print(x)
