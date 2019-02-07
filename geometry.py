'''
Fichier contenant les différentes classes représentant les différents éléments
graphiques du dessin
'''

from random import randint
from math import sqrt


class Point:
    '''
    Classe point permettant de représenter des points sur le dessin
    '''

    def __init__(self, abscisse, ordonnee):
        '''
        Constructeur de la classe
        '''
        self.x = abscisse
        self.y = ordonnee


class Line:
    '''
    Classe Line permettant d'effectuer des opérations sur les différentes
    lignes du dessin
    '''

    def __init__(self, point_1, point_2):
        '''
        Constructeur de la classe line
        '''
        self.point_1 = point_1
        self.point_2 = point_2

    def get_symmetrical(self, point):
        '''
        Méthode permettant de récupérer le symétrique du trait par rapport à la
        ligne formée entre un point passé en argument et l'axe des abscisse
        '''
        intersect_1 = Point(point.x, self.point_1.y)
        intersect_2 = Point(point.x, self.point_2.y)

        distance_1 = sqrt((self.point_1.x - intersect_1.x)**2 +
                          (self.point_1.x - intersect_1.x)**2)
        distance_2 = sqrt((self.point_2.x - intersect_2.x)**2 +
                          (self.point_2.x - intersect_2.x)**2)

        new_point_1 = Point(intersect_1.x - distance_1, self.point_1.y)
        new_point_2 = Point(intersect_2.x - distance_2, self.point_2.y)

        return Line(new_point_1, new_point_2)


def random_line(max_abscisse=300, max_ordonnee=300):
    '''
    Fonction permettant de générer une ligne aléatoire
    '''
    x_1 = randint(0, max_abscisse)
    x_2 = randint(0, max_abscisse)

    y_1 = randint(0, max_ordonnee)
    y_2 = randint(0, max_ordonnee)

    point_1 = Point(x_1, y_1)
    point_2 = Point(x_2, y_2)

    return Line(point_1, point_2)
