# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# variable for players that scored.
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

# variable for each minute that a goal was scored.
goal_0 = 32
goal_1 = 54

scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
print(scorers)

report = scorer_1 +' scored in the '+ str(goal_0) + 'nd minute' + "\n" + scorer_2 +' scored in the '+ str(goal_1)+ 'th minute'
print(report)

player = 'Ronald Koeman'

#Use slicing and find-method to isolate player firstname.

first_name = player [0:player.find(" ")]
print(first_name)

#3 use find , slicing and len,
last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)
#4 isolate firstname.
name_short=player[0:1] + "." + player[player.find(" "):]
print(name_short)

# 5 multiply firstname.
chant=(first_name + "!"+" ") * len(first_name)
print(chant)

#6 

good_chant=(chant.strip( ) != chant)

print(chant != good_chant)













# chant = (first_name + '!'+ " ") * len(first_name)
# lenght_chant_1 = len(chant)
# print(lenght_chant_1)

# chant_2 = chant[0:lenght_chant_1 - 1]
# lenght_chant_2= len(chant_2)
# print(lenght_chant_2)



#chant=(first_name + "!"+" ") * len(first_name)
#good_chant= chant.strip()
#print(good_chant)
#print(chant !=good_chant)











 



