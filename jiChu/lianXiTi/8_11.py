def show_magicians(magicians_names):
    for name in magicians_names:
        print(name.title())
    return name


def make_great(magicians_names):
    while m_names:
        name = m_names.pop()
        name = 'the Great' + name
    return name


m_names = ['dd', 'ww', 'qq']
show_magicians(m_names)
make_great(m_names)

# 8_11
name_list = ['mag1', 'mag2', 'mag3']
name_change = []


def make_great(name_list, name_change):
    while name_list:
        cur = name_list.pop()
        cur = 'the Great ' + cur
        name_change.append(cur)


def show_magicians(name_change):
    for name in name_change:
        print(name)


make_great(name_list[:], name_change)
show_magicians(name_list)
show_magicians(name_change)
