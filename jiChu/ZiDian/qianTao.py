love_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    # 'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in love_languages.items():
    print('\n' + name.title() + "'s love_languages are:")
    for la in languages:
        if len(languages) == 1:
            print(name.title() + "'s love_languages is " + la)
        print('\t' + la.title())

