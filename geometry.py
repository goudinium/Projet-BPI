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

    def __init__(self, abscisse=0, ordonnee=0):
        '''
        Constructeur de la classe
        '''
        self.x = abscisse
        self.y = ordonnee

    def __str__(self):
        '''
        Méthode srt pour afficher les coordonnées du point
        '''
        result = "{},{}".format(self.x, self.y)
        return result

    def get_symmetrical(self, point):
        '''
        Méthode permettant d'obtenir le symétrique du point en question à
        partir d'un second point passé en argument
        '''
        x_difference = self.x - point.x
        y_difference = self.y - point.y

        new_x = self.x - 2 * x_difference
        new_y = self.y - 2 * y_difference
        symmetrical = Point(new_x, new_y)
        return symmetrical


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

    def __str__(self):
        '''
        Méthode str pour afficher les points constituant les extrémités du
        segment. Sert essentiellement pour debuguer le code
        '''
        result = "Point 1 : {}\nPoint 2 : {}".format(
            self.point_1, self.point_2)
        return result

    def get_symmetrical(self, point):
        '''
        Méthode permettant de récupérer le symétrique du trait par rapport à un
        point passé en argument
        '''
        point_1 = self.point_1.get_symmetrical(point)
        point_2 = self.point_2.get_symmetrical(point)

        return Line(point_1, point_2)


def random_point(x_interval=(0, 300), y_interval=(0, 300)):
    '''
    Fonction permettant de générer un point aléatoire
    '''

    x = randint(x_interval[0], x_interval[1])
    y = randint(y_interval[0], y_interval[1])
    return Point(x, y)


def random_line(x_interval=(0, 300), y_interval=(0, 300)):
    '''
    Fonction permettant de générer une ligne aléatoire
    '''

    return Line(random_point(x_interval, y_interval),
                random_point(x_interval, y_interval))
