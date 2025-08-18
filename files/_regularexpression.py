import re
text="This is a PROGRAM from regular expression which is python program"
# match= re.search("program",text)
# if match:
#     print("match found")
#     print("Start index", match.start())
#     print("Ending index", match.end())

matches = re.findall("program", text,re.IGNORECASE)
print("Matches Found",matches)


#virtually replace the parttern with another string

with open("data.txt","r",encoding="utf-8") as f:
    text = f.read()
    print("original text:", text)

new_text = re.sub("password","meow",text)
print("New text:",new_text)
