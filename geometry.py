'''
Fichier contenant les différentes classes représentant les différents éléments
graphiques du dessin
'''

from random import randint
from math import sqrt, cos, sin, pi


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
        Entrée:
            point: point de symétrie
        Sortie:
            un objet point symétrique au point de symétrie
        '''
        return self.rotate(point, 180)

    def rotate(self, center, angle):
        '''
        Fonction retournant un point qui est l'image de la rotation du 
        point courant par rapport à un centre et un angle passés en 
        paramètres.
        '''
        angle = angle * (pi / 180)
        new_x = (self.x - center.x) * cos(angle) - (self.y - center.y) * sin(angle) + center.x
        new_y = (self.x - center.x) * sin(angle) + (self.y - center.y) * cos(angle) + center.y

        return Point(new_x, new_y)


class Line:
    '''
    Classe Line permettant d'effectuer des opérations sur les différentes
    lignes du dessin
    '''

    def __init__(self, point_1, point_2):
        '''
        Constructeur de la classe line
        Entrée:
            point_1: première extrémité du segment
            point_2: seconde extrémité du segment
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
        Entrée:
            point: point par rapport auquel on veut le symétrique de la ligne
        Sortie:
            symétrique de la ligne courante par rapport au point passé en
            argument
        '''
        point_1 = self.point_1.get_symmetrical(point)
        point_2 = self.point_2.get_symmetrical(point)

        return Line(point_1, point_2)
    
    def rotate(self, center, angle):
        '''
        Méthode permettant d'effectuer une rotation de la ligne courante selon un
        point central et un angle passés en paramètres
        '''
        point_1 = self.point_1.rotate(center, angle)
        point_2 = self.point_2.rotate(center, angle)
        return Line(point_1, point_2)


def random_point(x_interval=(0, 300), y_interval=(0, 300)):
    '''
    Fonction permettant de générer un point aléatoire
    Entrée:
        x_interval: intervalle dans lequel on veut tirer un x au hasard
        y_interval: intervalle dans lequel on veut tirer un y au hasard
    Sortie:
        un point aléatoire
    '''

    x = randint(x_interval[0], x_interval[1])
    y = randint(y_interval[0], y_interval[1])
    return Point(x, y)


def random_line(x_interval=(0, 300), y_interval=(0, 300)):
    '''
    Fonction permettant de générer une ligne aléatoire
    Entrée:
        x_interval: intervalle dans lequel on veut tirer les abscisses des
                    extrémités au hasard
        y_interval: intervalle dans lequel on veut tirer les ordonnées des
                    extrémités au hasard
    '''

    return Line(random_point(x_interval, y_interval),
                random_point(x_interval, y_interval))
