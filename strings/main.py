# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#1-1
from gettext import find


goal_name_1 = 'Ruud Gullit'
goal_name_2 = 'Marco van Basten'
#1-2
goal_0 = 32
goal_1 = 54
#1-3
scorers = f'{goal_name_1} {goal_0}, {goal_name_2} {goal_1}'
#1-4
report = f'{goal_name_1} scored in the {goal_0}nd minute\n{goal_name_2} scored in the {goal_1}th minute'
#2
player = 'Erwin Koeman'
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find(' ') +1:len(player)])
name_short = first_name[0]+'.'+player[player.find(' '):len(player)]
chant = (first_name +'! ') * (len(first_name) -1) + (first_name+'!') 
good_chant = chant[len(chant):] != ' '
print(chant)
print(good_chant)