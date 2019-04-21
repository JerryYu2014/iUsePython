f_l = {
    'jen':['python','ruby'],
    'sarah':['C'],
    'edward':['ruby','go'],
    'phli':['python','haskell'],
}

for name,languages in f_l.items():
    if len(languages)==1:
        print(name.title()+"'s favorite language is " +  languages[0])
    else:
        print("\n" + name.title() + "'s favorite languages are: ")
        for language in languages:
            print(language)
