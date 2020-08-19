
def head(title):
    return """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>"""+title+"""</title>
</head>"""


def body(body, h, color="black"):
    c = '"'
    return """ <body style = "color:"""+color+c+"""> <"""+h+"""> """+body+""" </"""+h+"""> </body> </html>"""
