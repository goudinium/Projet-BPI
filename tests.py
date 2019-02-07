'''
Fichier permettant d'effectuer différents tests au fur et à mesure du
développement
'''

from svg import SVG
from line import random_line

dessin = SVG("dessin.svg", 300, 300)


def test_line():
    '''
    Fonction permettant de tester l
    '''
    ligne = random_line()
    dessin.draw_line(ligne)


def test_multiple_random():
    for _ in range(7):
        ligne = random_line()
        dessin.draw_line(ligne)


def main():
    '''
    Fonction principale
    '''
    dessin.header()
    test_multiple_random()
    dessin.footer()
    dessin.write_file()

if __name__ == '__main__':
    main()
