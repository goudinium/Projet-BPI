'''
Fichier contenant les fonctions permettant de générer le code SVG
servant à l'affichage des différents éléments graphiques
Auteur: François Goudineau
'''

import point


class SVG:

    def __init__(self, file_path, width, height):
        '''
        Constructeur de la classe SVG
        L'objet SVG contient quatre champs :
            width: la largeur du dessin
            height: la hauteur du dessin
            file: le fichier dans lequel on souhaite écrire le code svg
            data: le code svg du dessin (pour éviter de faire des ouvertures/
                  fermetures de fichier intempestives, on décide de n'écrire
                  que le code final du dessin)
        Entree:
            file_path: chemin vers le fichier svg à écrire
            width: largeur du dessin svg
            height: hauteur du dessin svg
        Sortie :
            self : un objet de classe SVG

        '''
        self.width = width
        self.height = height
        self.file = file_path
        self.data = str()

    def header(self):
        '''
        Méthode permettant d'écrire l'en-tête du fichier svg:
        Sortie:
            ajout de l'en tête dans le fichier
        '''
        header = '<svg height="{}" width="{}">\n'.format(
            self.height, self.width)
        self.data += header

    def footer(self):
        '''
        Méthode permettant d'écrire le pied du fichier svg
        Sortie:
            ajout du pied du fichier svg
        '''
        footer = '</svg>'
        self.data += footer

    def draw_line(self, point_1, point_2):
        '''
        Méthode permettant de tracer une ligne
        Entree:
            point_1: premier point où commence le trait
            point_2: second poin où se finit le trait
        Sortie:
            ajout d'une ligne dans le dessin
        '''
        line = '<line x1="{}" y1="{}" x2="{}" y2="{}"\
                style="stroke:rgb(255,0,0);stroke-width:2" />\n'.format(
            point_1.x, point_1.y, point_2.x, point_2.y
        )
        self.data += line

    def write_file(self):
        '''
        Méthode permettant d'écrire le code du dessin dans le fichier
        Sortie:
            écriture du code du dessin dans le fichier
        '''
        with open(self.file, "w+") as dessin:
            dessin.write(self.data)
