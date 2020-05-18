from func import *


with open('booking.txt') as f:
    z = f.readlines()
q = []
for i in z:
    par = i[:-1]
    par_ = par.split(' ')
    q.append(par_)
for s in q:
    user = User_info(s[0], f'{s[1]} {s[2]} {s[3]}', s[4], s[5], s[6], s[7])
    q = open('output.txt', 'r')
    q.write(user.client_status)




