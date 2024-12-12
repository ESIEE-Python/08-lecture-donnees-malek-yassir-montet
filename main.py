"""Script de Lecture de Données"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r', encoding='utf-8') as f:
        for row in f:
            l.append([int(cell) for cell in row.split(";")])
    return l


def get_list_k(data, k):
    """Fonction accesseur liste d'indice k"""
    return data[k]

def get_first(l):
    """Fonction accesseur du premier élément"""
    return l[0]

def get_last(l):
    """Fonction accesseur du dernier élément"""
    return l[-1]

def get_max(l):
    """Fonction calcul du maximum de la liste"""
    return max(l)

def get_min(l):
    """Fonction calcul du minimum de la liste"""
    return min(l)

def get_sum(l):
    """Fonction calcul de la somme de la liste"""
    return sum(l)


#### Fonction principale

def main():
    """Fonction main"""
    read_data("listes.csv")


if __name__ == "__main__":
    main()
