#!/usr/bin/env python3

from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///bos.db")

# OVERVIEW PAGE ROUTE

@app.route("/")
def indexstart():
    return render_template("bos.html")

@app.route("/bos.html")
def indexback():
    return render_template("bos.html")

# 000 ROUTE

@app.route("/indv/000.html")
def show000():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/000.html", rows=rows, chat=chat)

@app.route("/indv/like000")
def addlike000():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 0)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 0))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/000.html", rows=rows, chat=chat)

@app.route("/indv/com000")
def addcom000():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (0, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/000.html", rows=rows, chat=chat)

# 001 ROUTE

@app.route("/indv/001.html")
def show001():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/001.html", rows=rows, chat=chat)

@app.route("/indv/like001")
def addlike001():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 1)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 1))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/001.html", rows=rows, chat=chat)

@app.route("/indv/com001")
def addcom001():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (1, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/001.html", rows=rows, chat=chat)

# 002 ROUTE

@app.route("/indv/002.html")
def show002():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/002.html", rows=rows, chat=chat)

@app.route("/indv/like002")
def addlike002():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 2)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 2))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/002.html", rows=rows, chat=chat)

@app.route("/indv/com002")
def addcom002():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (2, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/002.html", rows=rows, chat=chat)

# 003 ROUTE

@app.route("/indv/003.html")
def show003():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/003.html", rows=rows, chat=chat)

@app.route("/indv/like003")
def addlike003():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 3)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 3))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/003.html", rows=rows, chat=chat)

@app.route("/indv/com003")
def addcom003():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (3, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/003.html", rows=rows, chat=chat)

# 004 ROUTE

@app.route("/indv/004.html")
def show004():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/004.html", rows=rows, chat=chat)

@app.route("/indv/like004")
def addlike004():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 4)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 4))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/004.html", rows=rows, chat=chat)

@app.route("/indv/com004")
def addcom004():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (4, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/004.html", rows=rows, chat=chat)

# 005 ROUTE

@app.route("/indv/005.html")
def show005():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/005.html", rows=rows, chat=chat)

@app.route("/indv/like005")
def addlike005():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 5)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 5))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/005.html", rows=rows, chat=chat)

@app.route("/indv/com005")
def addcom005():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (5, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/005.html", rows=rows, chat=chat)

# 006 ROUTE

@app.route("/indv/006.html")
def show006():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/006.html", rows=rows, chat=chat)

@app.route("/indv/like006")
def addlike006():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 6)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 6))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/006.html", rows=rows, chat=chat)

@app.route("/indv/com006")
def addcom006():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (6, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/006.html", rows=rows, chat=chat)

# 007 ROUTE

@app.route("/indv/007.html")
def show007():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/007.html", rows=rows, chat=chat)

@app.route("/indv/like007")
def addlike007():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 7)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 7))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/007.html", rows=rows, chat=chat)

@app.route("/indv/com007")
def addcom007():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (7, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/007.html", rows=rows, chat=chat)

# 008 ROUTE

@app.route("/indv/008.html")
def show008():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/008.html", rows=rows, chat=chat)

@app.route("/indv/like008")
def addlike008():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 8)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 8))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/008.html", rows=rows, chat=chat)

@app.route("/indv/com008")
def addcom008():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (8, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/008.html", rows=rows, chat=chat)

# 009 ROUTE

@app.route("/indv/009.html")
def show009():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/009.html", rows=rows, chat=chat)

@app.route("/indv/like009")
def addlike009():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 9)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 9))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/009.html", rows=rows, chat=chat)

@app.route("/indv/com009")
def addcom009():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (9, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/009.html", rows=rows, chat=chat)


# 010 ROUTE

@app.route("/indv/010.html")
def show010():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/010.html", rows=rows, chat=chat)

@app.route("/indv/like010")
def addlike010():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 10)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 10))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/010html", rows=rows, chat=chat)

@app.route("/indv/com010")
def addcom010():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (10, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/010.html", rows=rows, chat=chat)

# 011 ROUTE

@app.route("/indv/011.html")
def show011():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/011.html", rows=rows, chat=chat)

@app.route("/indv/like011")
def addlike011():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 11)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 11))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/011.html", rows=rows, chat=chat)

@app.route("/indv/com011")
def addcom011():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (11, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/011.html", rows=rows, chat=chat)

# 012 ROUTE

@app.route("/indv/012.html")
def show012():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/012.html", rows=rows, chat=chat)

@app.route("/indv/like012")
def addlike012():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 12)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 12))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/012.html", rows=rows, chat=chat)

@app.route("/indv/com012")
def addcom012():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (12, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/012.html", rows=rows, chat=chat)

# 013 ROUTE

@app.route("/indv/013.html")
def show013():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/013.html", rows=rows, chat=chat)

@app.route("/indv/like013")
def addlike013():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 13)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 13))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/013.html", rows=rows, chat=chat)

@app.route("/indv/com013")
def addcom013():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (13, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/013.html", rows=rows, chat=chat)

# 014 ROUTE

@app.route("/indv/014.html")
def show014():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/014.html", rows=rows, chat=chat)

@app.route("/indv/like014")
def addlike014():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 14)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 14))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/014.html", rows=rows, chat=chat)

@app.route("/indv/com014")
def addcom014():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (14, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/014.html", rows=rows, chat=chat)

# 015 ROUTE

@app.route("/indv/015.html")
def show015():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/015.html", rows=rows, chat=chat)

@app.route("/indv/like015")
def addlike015():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 15)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 15))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/015.html", rows=rows, chat=chat)

@app.route("/indv/com015")
def addcom015():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (8, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/015.html", rows=rows, chat=chat)

# 016 ROUTE

@app.route("/indv/016.html")
def show016():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/016.html", rows=rows, chat=chat)

@app.route("/indv/like016")
def addlike016():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 16)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 16))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/016.html", rows=rows, chat=chat)

@app.route("/indv/com016")
def addcom016():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (16, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/016.html", rows=rows, chat=chat)

# 017 ROUTE

@app.route("/indv/017.html")
def show017():
    rows = db.execute("SELECT * FROM bos")
    chat = db.execute("SELECT * FROM comments")
    return render_template("/indv/017.html", rows=rows, chat=chat)

@app.route("/indv/like017")
def addlike017():
    tmp = db.execute("SELECT likes FROM bos WHERE imgID = ? ;", 17)
    totlikes = tmp[0]["likes"] + 1
    db.execute("UPDATE bos SET likes = ? WHERE imgID = ? ;", (totlikes, 17))
    rows = db.execute("SELECT * FROM bos")
    chat= db.execute("SELECT * FROM comments")
    return render_template("/indv/017.html", rows=rows, chat=chat)

@app.route("/indv/com017")
def addcom017():
    comment = request.args.get("comment")
    usr = request.args.get("usr")
    db.execute("INSERT INTO comments (imgID, comment, usr) VALUES (?, ?, ?);", (17, comment, usr))
    chat = db.execute("SELECT * FROM comments")
    rows = db.execute("SELECT * FROM bos")
    return render_template("/indv/017.html", rows=rows, chat=chat)
