import re

'''--- fonction pour ajouter un mots---
cette fonction prend en paramettre 4 elements dont entries qui est du type liste
qui va recevoir une listes mot, lookup_counter qui est un contaire qui va nous servir
tout au long de ce projet pour compter les mots, word qui est le mot lui meme et definition qui va stocker sa defnition'''

def add_word(entries, lookup_counter, word, definition):
    
    # on verifie si le mot exist deja dans le dictionnaire pour l'ajouter
    if word in entries:
        return False
    entries[word] = definition
    lookup_counter[word] = 0
    return True

'''fonction pour avoir la definition du mot
cette fonction prend 3 paramettre pour mieux comprendre ce paramettre 
voir le commentaire sur le fonction add_Word'''

def get_definition(entries, lookup_counter, word):
    if word in entries:
        lookup_counter[word] += 1
        return entries[word]
    return None

'''onction pour mettre a jour une definition
elle prend aussi 3 paramettre dont un nouveau que nous n'avons pas encore expliquer 
new_definition comme sont nom l'indique va permettre de recuprere une nouvelle definition du mot'''

def update_definition(entries, word, new_definition):
    if word not in entries:
        return False
    entries[word] = new_definition
    return True

# fonction permettant de supprimer un mot du dictionnaire

def delete_word(entries, lookup_counter, word):
    if word in entries:
        del entries[word]
        del lookup_counter[word]
        return True
    return False

# fonction pour afficher la liste de mots 

def list_words(entries):
    return sorted(entries.keys())

# fonction pour chercher une definition dans le dictionnaire

def search_in_definitions(entries, keyword):
    return [word for word, definition in entries.items()
            if keyword.lower() in definition.lower()]

# fonction pour suggerer des motss similaire a l'utilisateur

def suggest_similar_words(entries, word, n=3):
    pattern = rf".*{re.escape(word)}.*"
    matches = [w for w in entries.keys() if re.match(pattern, w)]
    return matches[:n]

# foncttion pour voir le mot le plus consulter

def get_lookup_stats(entries, lookup_counter):
    if not lookup_counter:
        return None
    most_consulted = max(lookup_counter, key=lookup_counter.get)
    return {
        'total_words': len(entries),
        'most_consulted': most_consulted,
        'most_consulted_count': lookup_counter[most_consulted],
        'longest_word': max(entries, key=len),
        'shortest_word': min(entries, key=len),
    }

# fonction pour rechercher le mot commençant par une (x) lettre

def get_words_starting_with(entries, letter):
    return sorted([word for word in entries if word.startswith(letter)])

# fonction pour avoir le mot qui contienne une sequence des mots

def get_words_containing(entries, sequence):
    return sorted([word for word in entries if sequence in word])

