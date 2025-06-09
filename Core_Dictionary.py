import re

# --- Gestion du dictionnaire ---
def add_word(entries, lookup_counter, word, definition):
    if word in entries:
        return False
    entries[word] = definition
    lookup_counter[word] = 0
    return True

# fonction pour avoir la definition du mot

def get_definition(entries, lookup_counter, word):
    if word in entries:
        lookup_counter[word] += 1
        return entries[word]
    return None
# fonction pour mettre a jour une definition

def update_definition(entries, word, new_definition):
    if word not in entries:
        return False
    entries[word] = new_definition
    return True

def delete_word(entries, lookup_counter, word):
    if word in entries:
        del entries[word]
        del lookup_counter[word]
        return True
    return False

def list_words(entries):
    return sorted(entries.keys())

def search_in_definitions(entries, keyword):
    return [word for word, definition in entries.items()
            if keyword.lower() in definition.lower()]

def suggest_similar_words(entries, word, n=3):
    pattern = rf".*{re.escape(word)}.*"
    matches = [w for w in entries.keys() if re.match(pattern, w)]
    return matches[:n]

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

def get_words_starting_with(entries, letter):
    return sorted([word for word in entries if word.startswith(letter)])

def get_words_containing(entries, sequence):
    return sorted([word for word in entries if sequence in word])
