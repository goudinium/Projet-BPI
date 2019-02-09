'''
Fichier permettant d'effectuer différents tests au fur et à mesure du
développement
'''

from svg import SVG
from math import pi
from geometry import random_line, random_point
from geometry import Point

dessin = SVG("dessin.svg", 1000, 1000)


def test_line():
    '''
    Test affichant une ligne aléatoire sur le dessin svg
    '''
    ligne = random_line()
    dessin.draw_line(ligne)


def test_multiple_random():
    '''
    Test affichant 7 lignes aléatoires sur le dessin svg
    '''
    for _ in range(7):
        ligne = random_line((500, 1000), (0, 1000))
        dessin.draw_line(ligne)


def test_symmetrical_point():
    '''
    Test permettant d'afficher le symétrique d'un point tiré au hasard par
    rapport à un point de symétrie
    '''
    point_of_symmetry = Point(500, 500)
    point_test = random_point()
    dessin.draw_point(point_test)
    dessin.draw_point(point_of_symmetry)
    dessin.draw_point(point_test.get_symmetrical(point_of_symmetry))


def test_symmetrical_line():
    '''
    Test permettant d'afficher le symétrique d'une ligne aléatoire par rapport
    à un point de symétrie
    '''
    point_of_symmetry = Point(500, 500)
    ligne = random_line((500, 700), (0, 500))
    dessin.draw_line(ligne)
    dessin.draw_point(point_of_symmetry)
    print(ligne.get_symmetrical(Point(500, 500)))
    dessin.draw_line(ligne.get_symmetrical(point_of_symmetry))

def test_rotation_point():
    '''
    Test permettant de vérifier que la rotation d'un point se passe correctement
    '''
    center = Point(500, 500)
    rnd_point = random_point((500, 700), (0,500))
    angle = 90
    dessin.draw_point(center)
    dessin.draw_point(rnd_point)
    dessin.draw_point(rnd_point.rotate(center, angle))


def main():
    '''
    Fonction principale
    '''
    dessin.header()
    test_rotation_point()
    dessin.footer()
    dessin.write_file()

if __name__ == '__main__':
    main()
