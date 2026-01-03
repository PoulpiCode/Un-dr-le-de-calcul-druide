# Fonction de lecture depuis un fichier texte
def lireExpression(nom_fichier):
    try:
        with open(nom_fichier, "r") as f:
            return f.read().split()  # retourne une liste de nombres et opérateurs
    except FileNotFoundError:
        print("Erreur : fichier non trouvé")
        return []

# Fonction d'évaluation
def evaluerExpression(tokens):
    pile = []
    for token in tokens:
        if token.isdigit():  # si c'est un nombre
            pile.append(int(token))
        else:  # c'est un opérateur
            if len(pile) < 2:
                raise ValueError("Erreur : opérateur sans assez d'opérandes")
            b = pile.pop()
            a = pile.pop()
            if token == '+':
                pile.append(a + b)
            elif token == '-':
                pile.append(a - b)
            elif token == '*':
                pile.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Erreur : division par zéro")
                pile.append(a / b)
            else:
                raise ValueError(f"Erreur : opérateur inconnu {token}")
    if len(pile) != 1:
        raise ValueError("Erreur : expression invalide")
    return pile[0]

# Programme principal
if __name__ == "__main__":
    nom_fichier = "C:\\Users\\Adrien\\Desktop\\Code\\Un drôle de calcul druide\\code.txt"  # Changer le nom du fichier !!!!!
    tokens = lireExpression(nom_fichier)
    if tokens:
        try:
            resultat = evaluerExpression(tokens)
            print("Résultat :", resultat)
        except Exception as e:
            print(e)
