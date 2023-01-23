# https://github.com/clarketm/pprintjson
    
import json
from pprintjson import pprintjson as ppjson
class JsonWork:
    def Example():
        mockedJson = [
            {"book":  {"Id": 1, "Title": "Learn EF Core","Price": 19.0000}},
            {"book":  {"Id": 2, "Title": "C# Basics","Price": 18.0000 }},
            {"book":  {"Id": 3, "Title": "ASP.NET Core advance","Price": 30.0000 }},
            {"book":  {"Id": 4, "Title": "VB.NET To C#","Price": 9.0000}} ,
            {"book":  {"Id": 5, "Title": "Basic Azure","Price": 59.0000 }},
            {"book":  {"Id": 6, "Title": "Adnance Azure","Price": 69.0000 }},
            {"book":  {"Id": 7, "Title": "Basic Entity Framework Core","Price": 45.0000 }}
        ]

        # display to console will be formatted
        # display to terminal will be formatted and colorized
        #ppjson(mockedJson) 

        #with open('books.json', 'w+') as fileToSave:
        #        json.dump(mockedJson, fileToSave, ensure_ascii=True, indent=4, sort_keys=True)



        with open("books1.json", "r") as read_file:
            data = json.load(read_file)[:2]

        print(json.dumps(data, indent=4))
        text_file = open("booksExported.json", "w")
        n = text_file.write(json.dumps(data, indent=4))
        text_file.close()