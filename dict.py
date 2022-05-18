import json # file eka import karagannawa
from difflib import get_close_matches # mema module eken puluwan file ekakai api depu input fotm ekakai wenas kam thiyeda kiyala adura ganna

data = json.load(open("data.json"))# json.load walin karanne kiyawanna puluwan thathwayata file eke data hadaganna eka


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.key())) > 0:
        yesno = input("Did you mean %s insted? Enter y if yes, or n if no:"%get_close_matches(w, data.key())[0])
        if yesno == "Y":
            return data[get_close_matches(w, data.key())[0]]
        elif yesno == "N":
            return "The word doen't matched.please double check your input"
        else:
            return "we don't understand your input"
    else:
        return "The word doesn't Exist.Please double check your input"

word = input("Enter your word:")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)











































