import re
import json
import traceback

dt = {}
file_exceptions = "exceptions.json"
with open(file_exceptions, 'r') as f:
        exceptions = json.load(f)
for i in exceptions:
    dt[i[0]] = {i[1]:{hash(i[2]): i[3]}}
exceptions

def throwException(trace):
    line = re.search("line \d+", trace.split("\n")[1]).group(0)[5:]
    exception = trace.split("\n")[-2].strip()
    print(dt['main.py ' + line][exception][hash(trace)], "check your code on line number", line)

try:
    raise MemoryError()
except:
    throwException(traceback.format_exc())
try:
    raise TypeError()
except:
    throwException(traceback.format_exc())
try:
    raise KeyError()
except:
    throwException(traceback.format_exc())
try:
    raise TimeoutError()
except:
    throwException(traceback.format_exc())