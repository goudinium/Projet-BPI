'''
Fichier permettant d'effectuer différents tests au fur et à mesure du
développement
'''

from svg import SVG
from geometry import random_line, random_point
from geometry import Point

dessin = SVG("dessin.svg", 1000, 1000)


def test_line():
    ligne = random_line()
    dessin.draw_line(ligne)


def test_multiple_random():
    for _ in range(7):
        ligne = random_line((500, 1000), (0, 1000))
        dessin.draw_line(ligne)


def test_symmetrical_point():
    point_of_symmetry = Point(500, 500)
    point_test = random_point()
    dessin.draw_point(point_test)
    dessin.draw_point(point_of_symmetry)
    dessin.draw_point(point_test.get_symmetrical(point_of_symmetry))


def test_symmetrical_line():
    point_of_symmetry = Point(500, 500)
    ligne = random_line((500, 700), (0, 500))
    dessin.draw_line(ligne)
    dessin.draw_point(point_of_symmetry)
    print(ligne.get_symmetrical(Point(500, 500)))
    dessin.draw_line(ligne.get_symmetrical(point_of_symmetry))


def main():
    '''
    Fonction principale
    '''
    dessin.header()
    test_symmetrical_line()
    dessin.footer()
    dessin.write_file()

if __name__ == '__main__':
    main()
