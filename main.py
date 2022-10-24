# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = f'{player_one} {goal_0}, {player_two} {goal_1}'
print(scorers)

report = f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute'
print(report)

player = player_two
find_space = player.find(" ")
first_name = player[:find_space]
print(first_name)
first_name_len = len(first_name)

last_name = player[find_space:]
last_name_len = len(last_name)-1
print(last_name_len)

initial = player[0] + '.'
name_short = initial + last_name
print(name_short)

chant = ((first_name + '! ') * first_name_len)[:-1] 
print(chant)

good_chant = chant[len(chant)-1] != " "
print(good_chant)