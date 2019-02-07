'''
Fichier principal
'''

from geometry import random_line
from svg import SVG


def generate_random_lines(nb_lines=7):
    '''
    Fonction permettant de générer un nombre n de lignes aléatoires
    Entrée:
        nb_lines: nombre n de lignes à générer aléatoirement
    Sortie:
        lines: un tableau contenant les objets lignes précédemment générés
    '''
    return [random_line() for _ in nb_lines]


def main():
    '''
    Fonction principale
    '''
    drawing = SVG("dessin.svg", 1000, 1000)
    drawing.header()

    lines = generate_random_lines()
    for line in lines:
        drawing.draw_line(line)

    drawing.footer()
    drawing.write_file()

if __name__ == '__main__':
    main()
