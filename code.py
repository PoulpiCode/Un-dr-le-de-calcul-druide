"""
Module : Calcul druide de Zarhbic
Description : Lit une expression en notation postfixée depuis un fichier et calcule le résultat.
"""

def lireExpression(nom_fichier):
    """
    Lit le contenu d'un fichier texte et retourne une liste de nombres et opérateurs.
    """
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read().split()
    except FileNotFoundError:
        print(f"Erreur : fichier '{nom_fichier}' non trouvé")
        return []

def evaluerExpression(tokens):
    """
    Évalue une expression en notation postfixée.
    """
    pile = []
    for token in tokens:
        if token.isdigit():
            pile.append(int(token))
        else:
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
                raise ValueError(f"Erreur : opérateur inconnu '{token}'")
    if len(pile) != 1:
        raise ValueError("Erreur : expression invalide")
    return pile[0]

def main():
    """
    Programme principal : lit le fichier, évalue l'expression et affiche le résultat.
    """
    nom_fichier = "C:\\Users\\Adrien\\Desktop\\Code\\Un drôle de calcul druide\\code.txt"
    tokens = lireExpression(nom_fichier)
    if not tokens:
        return

    try:
        resultat = evaluerExpression(tokens)
        print("Résultat :", resultat)
    except ValueError as ve:
        print("Erreur dans le calcul :", ve)
    except ZeroDivisionError as zde:
        print("Erreur de division par zéro :", zde)

if __name__ == "__main__":
    main()
