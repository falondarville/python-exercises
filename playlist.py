# this is an example of data modeling using the structure of a Spotify playlist
playlist = {'title': 'eight',
'author': 'Falon','songs': [{'title': 'What If I Go?','artist': ['Mura Masa'],'duration': 2.5},{'title': 'Whippin','artist': ['Kiiara', 'Felix Snow'],'duration': 3},{'title': 'Snow in October','artist': ['Chelsea Cutler'],'duration': 2.9}]}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']
print(total_length)