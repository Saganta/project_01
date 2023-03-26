import random
random.randint(1, 9)
random_songs = []
i = 0
while i < 3 : 
    var = random.randint(1, 9)
    if var in random_songs:
        i -= 1
    else: random_songs.append(var)
    i += 1
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
songs_time = 0
songs_name = ' '
i = 1
y = 1
r = 0
while (r < 3):
    for song in my_favorite_songs_dict.keys():
        if (i in random_songs):
            songs_time += my_favorite_songs_dict[song]
            songs_name += song
            if (y < 3): 
                songs_name += ', '
            else :
                songs_name += ' '
            y += 1
        i += 1
    r += 1
print('Три песни' + songs_name + 'звучат '  + str(songs_time) + ' минут')
