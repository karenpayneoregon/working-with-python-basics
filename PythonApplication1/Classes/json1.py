# https://github.com/clarketm/pprintjson

import json
from pprintjson import pprintjson as ppjson

# No different than obtaining data from a file or end-point, here cutting out the middle man
mockedJson = [{"Id": 1,"Title": "Learn EF Core","Price": 19.0000},{"Id": 2,"Title": "C# Basics","Price": 18.0000},{"Id": 3,"Title": "ASP.NET Core advance","Price": 30.0000 },{"Id": 4,"Title": "VB.NET To C#","Price": 9.0000}, {"Id": 5, "Title": "Basic Azure","Price": 59.0000 }]

# display to console will be formatted
# display to terminal will be formatted and colorized
ppjson(mockedJson) 

with open('books.json', 'w+') as fileToSave:
        json.dump(mockedJson, fileToSave, ensure_ascii=True, indent=4, sort_keys=True)