def f(phrase):
    phrase = phrase + "petite "
    return g(h(phrase))

def g(phrase):
    phrase = phrase + "brise "
    return h(phrase)

def h(phrase):
    if phrase[0] == "L":
        phrase = phrase + "la "
        return k(phrase)
    else:
        return "La " + phrase

def k(phrase):
    return phrase + "glace."

phrase_test = ""
phrase_test = f(phrase_test)
print(phrase_test)
