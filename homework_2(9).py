title = 'eat_more_meat'

title_idx = title.split('_')

w1 = title_idx[0].capitalize()
w2 = title_idx[1].capitalize()
w3 = title_idx[2].capitalize()
w4 = ''.join([w1, w2, w3])


print('it was like this:', title, 'But It Has Become Like This:', w4)
