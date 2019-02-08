'''
Fichier contenant les fonctions permettant de générer le code SVG
servant à l'affichage des différents éléments graphiques
Auteur: François Goudineau
'''


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

    def draw_line(self, line_object):
        '''
        Méthode permettant de tracer une ligne
        Entree:
            line_object: objet line représentant la ligne à tracer
        Sortie:
            ajout d'une ligne dans le dessin
        '''

        (point_1, point_2) = (line_object.point_1, line_object.point_2)
        line = '<line x1="{}" y1="{}" x2="{}" y2="{}"\
                style="stroke:rgb(255,0,0);stroke-width:2" />\n'.format(
            point_1.x, point_1.y, point_2.x, point_2.y
        )
        self.data += line

    def draw_point(self, point_object):
        '''
        Méthode permettant de tracer un point
        Entrée:
            point_object: point que l'on veut dessiner
        Sortie:
            ajout du point dans le dessin
        '''
        point = '<circle cx="{}" cy="{}" r="10" stroke="black"\
                 stroke-width="3" fill="red" />\n'.format(point_object.x,
                                                          point_object.y)
        self.data += point

    def write_file(self):
        '''
        Méthode permettant d'écrire le code du dessin dans le fichier
        Sortie:
            écriture du code du dessin dans le fichier
        '''
        with open(self.file, "w+") as dessin:
            dessin.write(self.data)
