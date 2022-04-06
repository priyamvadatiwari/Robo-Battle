from flask import Flask, render_template, request
from battle import bracketBattle1, winnersR1, bracketBattle2, winnersR2, bracketBattle3, winnerR3, finalBattle, ultimateWinner


app = Flask('app')

@app.route('/')
def game():
    battles = bracketBattle1()
    round1 = winnersR1()
    round2 = bracketBattle2()
    winners_R2 = winnersR2()
    list3 = bracketBattle3()
    winner_R3 = winnerR3()
    finalist = finalBattle()
    ultimate_Winner = ultimateWinner()
    return render_template("index.html",battles=battles, round1 = round1, round2=round2, winners_R2 = winners_R2, list3=list3, winner_R3=winner_R3, finalist=finalist,ultimate_Winner=ultimate_Winner)

app.run(host='0.0.0.0', port=8080)