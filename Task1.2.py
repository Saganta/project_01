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
# print(random_songs)
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
songs_time = 0
songs_name = ' '
i = 1
for song_number in random_songs:
    songs_time += my_favorite_songs[song_number][1]
    if (i < 3): 
        songs_name += my_favorite_songs[song_number][0] + ', '
    else: 
        songs_name += my_favorite_songs[song_number][0] + ' '
    i += 1
print('Три песни' + songs_name + 'звучат '  + str(songs_time) + ' минут')
