'''
Fichier permettant d'effectuer différents tests au fur et à mesure du
développement
'''

from svg import SVG
from point import Point

dessin = SVG("dessin.svg", 300, 300)


def test_line():
    '''
    Fonction permettant de tester l
    '''
    point_1 = Point(100, 100)
    point_2 = Point(200, 200)
    dessin.draw_line(point_1, point_2)


def main():
    '''
    Fonction principale
    '''
    dessin.header()
    test_line()
    dessin.footer()
    dessin.write_file()

if __name__ == '__main__':
    main()
