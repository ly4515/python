current_users = ['admin', 'mary', 'john', 'Eric', 'TGD']
new_users = ['mary', 'hoho', 'eric', 'tgd', 'rdt']
c_users = []
for current_user in current_users:
    c_users.append(current_user.lower())
for user in new_users:
    if user.lower() in c_users:
        print(user + " is used")
    else:
        print(user + ' is not used')