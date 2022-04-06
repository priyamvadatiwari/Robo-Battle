import random
import json

filename = "dataround1.json"  #This will store participants, groups and theirs scores of first round.
filename2 = "dataround2.json" #This will store participants, groups and theirs scores of second round.
filename3 = "dataround3.json"
filename4 = "finalists.json"
# tupRound1 = ()  to check if I can use tuple to avoid the second list from changing. 

#First Battle - Players for first round, their points
def bracketBattle1():

  players_roster = ['Kelly', 'India', 'Canada', 'America', 'Australia', 'Poland', 'Norway', 'Italy', 'Germany', 'Japan', 'China', 'Bhutan', 'Nigeria', 'Phillipines', "New Zealand", "Spain"]
  
  battleRound1 = []
  counter = 1
  

  for player in range(int(len(players_roster)/2)):
    battle = []
    counter += 1
    player1 = random.choice(players_roster) #Round 1 player 1
    
    players_roster.remove(player1)
    # pointsP1 = random.randint(1,1000)
    player2 = random.choice(players_roster) #Round 1 player 2
    # pointsP2 = random.randint(1,1000)
    players_roster.remove(player2)

    battle.append(player1) 
    battle.append(player2)
    
    battleRound1.append(battle)

  for match in battleRound1:
      
      while True:
          points1 = random.randint(1,100)
          points2 = random.randint(1,100)
          if points1 == points2:
            continue 
          else:
            match.insert(1, points1)
            match.insert(3, points2)
            break

  for match in battleRound1:
    if match[1] > match[3]:
      match.append(f"{match[0]} wins!")
    elif match[1] < match[3]:
      match.append(f"{match[2]} wins!")
    else:
       match.append(f"Its a tie!")

  #put the list in json file to reuse it in next function.
  with open(filename, 'w') as jsonFile:
    jsonFile.write(json.dumps(battleRound1, indent=3))
  
  return battleRound1

#Winners for round 1
def winnersR1():
  #read the data from first round json file
  with open(filename) as file_obj:
    round1 = json.load(file_obj)

  round1Winners = []
  for match in  round1:
    if match[1] > match[3]:
      round1Winners.append(f"{match[0]}")
    elif match[1] < match[3]:
      round1Winners.append(f"{match[2]}")
    else:
      round1Winners.append(f"Its a tie!")
  return round1Winners   #return the first round winners.
  
#Battle 2 - Winners from first round will move to round 2, and their points will be calcultaed here
def bracketBattle2():
  round2 = winnersR1()
  battleRound2 = []
  counter = 1

  for r2Player in range(int(len(round2)/2)):
    brktBattle2 = []
    counter += 1
    r2Player1 = random.choice(round2) #round 2 player 1
    round2.remove(r2Player1)

    r2Player2 = random.choice(round2) # round 2 player 2
    round2.remove(r2Player2)

    brktBattle2.append(r2Player1) 
    brktBattle2.append(r2Player2)
  
    battleRound2.append(brktBattle2)
  
  #assign points to each player.
  for match in battleRound2:
    while True:
      r2Points1 = random.randint(1,100)
      r2Points2 = random.randint(1,100)
      if r2Points1 == r2Points2:
        continue 
      else:
        match.insert(1, r2Points1)
        match.insert(3, r2Points2)
        break

  with open(filename2, 'w') as jsonFile:
    jsonFile.write(json.dumps(battleRound2, indent=3))
  return battleRound2

#Winners from round 2 will be stored.
def winnersR2():
  with open(filename2) as file_obj:
    battle2list = json.load(file_obj)
  round2Winners = []
  for game2 in battle2list:
    if game2[1] > game2[3]:
      round2Winners.append(f"{game2[0]}")
    elif game2[1] < game2[3]:
      round2Winners.append(f"{game2[2]}")
    else:
      round2Winners.append(f"Its a tie!")
  
  tupList = tuple(round2Winners)
  print(tupList)        #converting it to tuple to avoid data changes.
  return tupList

#Battle 3 -  Winners from Battle 2 will move to round 3 and will be assigned points randomly. 
def bracketBattle3():
  playersRound3 = list(winnersR2())
  battleRound3 = []
  counter3 = 1

  for r2Player in range(int(len(playersRound3)/2)):
    brktBattle3 = []
    counter3 += 1
    r3Player1 = random.choice(playersRound3) #round 3 player 1
    playersRound3.remove(r3Player1)

    r3Player2 = random.choice(playersRound3) # round 3 player 2
    playersRound3.remove(r3Player2)

    brktBattle3.append(r3Player1) 
    brktBattle3.append(r3Player2) 
  
    battleRound3.append(brktBattle3)
  
  for match3 in battleRound3:
        #print(match)
    while True:
      r3Points1 = random.randint(1,100)
      r3Points2 = random.randint(1,100)
      if r3Points1 == r3Points2:
        continue 
      else:
        match3.insert(1, r3Points1)
        match3.insert(3, r3Points2)
        break

    with open(filename3, 'w') as jsonFile:
      jsonFile.write(json.dumps(battleRound3, indent=3))    
  return battleRound3

#Winners of Round 3 will be selected here and stored in a list.
def winnerR3():

  with open(filename3) as file_obj:
    playersR3 = json.load(file_obj)
  # playersR3 = list(bracketBattle3())
  round3Winners = []
  for game3 in playersR3:
    if game3[1] > game3[3]:
      round3Winners.append(f"{game3[0]}")
    elif game3[1] < game3[3]:
      round3Winners.append(f"{game3[2]}")
    else:
      round3Winners.append(f"Its a tie!")

  return round3Winners

#This will be the last battle between the top 2 winners. 
def finalBattle():
  finalists = winnerR3()
  finalshow = []
  counter4 = 0
  for r4Player in range(int(len(finalists)/2)):
    brktBattle4 = []
    counter4 += 1
    r4Player1 = random.choice(finalists) #Final round player 1
    finalists.remove(r4Player1)

    r4Player2 = random.choice(finalists) # Final round player 2
    finalists.remove(r4Player2)

    brktBattle4.append(r4Player1)  
    brktBattle4.append(r4Player2) 
  
    finalshow.append(brktBattle4)
  
  for match4 in finalshow:
    while True:
      r4Points1 = random.randint(1,100)
      r4Points2 = random.randint(1,100)
      if r4Points1 == r4Points2:
        continue 
      else:
        match4.insert(1, r4Points1)
        match4.insert(3, r4Points2)
        break
  with open(filename4, 'w') as jsonFile:
    jsonFile.write(json.dumps(finalshow, indent=3))  

  return finalshow
 
#Ultimate Winner for the game will be selected. 
def ultimateWinner():
  with open(filename4) as file_obj:
    lastbattle = json.load(file_obj)

  winners = []
  for final in lastbattle:
    if final[1] > final[3]:
      winners.append(f"{final[0]}")
    elif final[1] < final[3]:
      winners.append(f"{final[2]}")
    else:
      winners.append(f"Its a tie!")
  return winners
