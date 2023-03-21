alien_0= {
    'color':'green',
    'points':5,
    }


print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")
print(alien_0)

# adding key - value pairs to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print(f"The colour of the alien is {alien_0['color']}.")

# changing the colour of the alien
alien_0['color'] = 'yellow'

print(f"The colour of the alien is now {alien_0['color']}.")

print(alien_0)

alien_0['speed'] = 'medium'

print(alien_0)

print()

#  show the initial position of the alien
print(f"Original position: x = {alien_0['x_position']}, y = {alien_0['y_position']}")

#  move the alien to the right
#  determine how far it should move based on it's speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New position is equal to old position plus increment
alien_0['x_position'] += x_increment
print(alien_0)

# deleting a key - value pair
del alien_0['points']
print(alien_0)

# we use to get method to assign a string that will be displayed if a key requested for doesn't exist in that dictionary
print(alien_0.get('points', 'No point value assigned here'))


favourite_language = {
    'majesty':'python',
    'taofeek':'c++',
    'ransome':'javascript',
    'chizor':'typescript',
    'isaac':'php',
}
print(favourite_language)
print(favourite_language.keys())
print(favourite_language.values())
print(favourite_language.items())