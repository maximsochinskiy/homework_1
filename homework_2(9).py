title = 'eat_more_meat'

ttl_idx = title.split('_')

w1 = ttl_idx[0].capitalize()
w2 = ttl_idx[1].capitalize()
w3 = ttl_idx[2].capitalize()
w4 = ''.join([w1, w2, w3])


print('it was like this:', title, 'But It Has Become Like This:', w4)
