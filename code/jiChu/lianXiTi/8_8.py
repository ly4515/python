def make_album(name, music, num=''):
    album = {'name': name, 'music': music}
    if num:
        album['num'] = num
    return album
while True:
    print("if you input 'q' will quit")
    name = input('please input a singer name:')
    if name == 'q':
        break
    # print("if you input 'q' will quit")
    music = input("please input the singer's music:")
    if music == 'q':
        break
    a = make_album(name, music)
    print(a)
