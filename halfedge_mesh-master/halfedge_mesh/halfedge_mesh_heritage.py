import halfedge_mesh
import random


class HalfedgeMeshHerited(halfedge_mesh.HalfedgeMesh):
    def __init__(self,arg):
        halfedge_mesh.HalfedgeMesh.__init__(self,arg)
        self.nb_composante = 1

    def write_file(self, filename) :
        with open(filename, 'w') as file:
            file.write("COFF\n")

            file.write(str(len(self.vertices)) + " " +  str(len(self.facets)) + " " + str(len(self.halfedges)/2)+ "\n" )
            for vertice in self.vertices :
                file.write(str(vertice.x) + " " + str(vertice.y) + " " + str(vertice.z)+" "+ str(vertice.couleurs[0]) + " " + str(vertice.couleurs[1]) + " " + str(vertice.couleurs[2]) + "\n")
            for facet in self.facets :
                file.write("3" + "  " +str(facet.a) + " " + str(facet.b) + " " + str(facet.c)+" "+ str(facet.couleurs[0]) + " " + str(facet.couleurs[1]) + " " + str(facet.couleurs[2]) +"\n")



    def parcours (self,vertex,num_marq =  1) :
        pile = []
        vertex.marq = num_marq
        pile.append(vertex)
        while (pile != []) :
            vertex = pile.pop(len(pile) -1)
            voisins = vertex.Voisin()
            for voisin in voisins :
                if (voisin[0].marq == 0) :
                    voisin[0].marq = num_marq
                    pile.append(voisin[0])

    def verification_marq (self) :
        out = []
        for vertex in self.vertices :
            if vertex.marq == 0 :
                out.append(vertex)
        return out


    def composante_connexes (self) :
        vertices = self.verification_marq()
        nb_composante = 0
        while (vertices != []) :
            self.parcours(vertices[0],nb_composante + 1)
            vertices = self.verification_marq()
            nb_composante += 1
        self.nb_composante = nb_composante
        print("nombe de composante_connexes : ", nb_composante)

    def colorie_composante_connexe (self) :
        couleurs = genere_x_couleur(self.nb_composante)
        for vertex in self.vertices :
            vertex.couleurs = couleurs[vertex.marq - 1]



    def vertex_all_composante(self) :
        list_vertex = []
        index = 1
        for vertex in self.vertices :
            if (vertex.marq == index ) :
                list_vertex.append(vertex)
                index += 1
            if(index == self.nb_composante +1):
                return list_vertex
        return list_vertex


    def calcule_genre (self, num_composante = 1) :
        list = [[],[],[]]
        for halfedge in self.halfedges :
            if(halfedge.vertex.marq == num_composante):
                if (chercheListe(halfedge.index, list[0]) == False):
                    list[0].append(halfedge)
                if (chercheListe(halfedge.vertex.index, list[1]) == False):
                    list[1].append(halfedge.vertex)
                if (chercheListe(halfedge.facet.index, list[2]) == False):
                    list[2].append(halfedge.facet)

        return list

    def genre_composantes(self):
        list = []
        for i in range(self.nb_composante) :
            list.append(self.calcule_genre(i+1))
        return list

    def genre(self) :
        lists = self.genre_composantes()
        list_genre = []
        for list in lists :
            list_genre.append(int(g(list[0],list[1], list[2])))
            print("genre de la CC ", 0, "est : " , g(list[0],list[1], list[2])  )
        return lists, list_genre

    def colorie_genre(self) :
        listes_compososantes, liste_genre = self.genre()
        couleurs = genere_x_couleur(max(liste_genre) + 1)
        list_vertices = []
        for composante, genre in zip(listes_compososantes, liste_genre) :
            for vertex in composante[1]:
                vertex.couleurs = couleurs[genre]
                # list_vertices.append(vertex)

            print("genre de la CC ", 0, "est : " , genre  )
        # self.vertices = list_vertices

    # new 1.3

    def colorie_distance_coposantes (self) :
        vertices = self.vertex_all_composante()
        for index,vertex in enumerate(vertices) :
            self.colorie_bis(vertex,index+1)

    # def colorie(self,index_a):
    #
    #     if( index_a >= len(self.vertices) or index_a < 0 ):
    #         print(">>> Erreur : index non valide pour la coloration ")
    #         return -1
    #
    #     min_find = 0
    #     max_find = 0
    #
    #     # Parcour pour crée la distance au point
    #     self.vertices[index_a].descendre()
    #
    #     for i in self.vertices :
    #         if( max_find < i.poids ) :
    #             max_find = i.poids
    #
    #     for i in self.vertices :
    #         print(i.poids, "poi")
    #         i.couleurs[0] = int( 255 * (( i.poids - min_find ) / ( max_find - min_find )) )
    #         if( i.poids == 0 ):
    #             # Le point de départ visible en bleu
    #             i.couleurs[0] = 0
    #             i.couleurs[1] = 0
    #             i.couleurs[2] = 255

    def colorie_bis (self, vertex, index_composante_connexe = 0) :
            min_find = 0
            max_find = 0

                # Parcour pour crée la distance au point
            vertex.descendre()

            for i in self.vertices :
                if( max_find < i.poids ) :
                    max_find = i.poids

            for i in self.vertices :
                if(i.marq == index_composante_connexe) :
                    i.couleurs[0] = int( 255 * (( i.poids - min_find ) / ( max_find - min_find )) )
                    if( i.poids == 0 ):
                        # Le point de départ visible en bleu
                        i.couleurs[0] = 0
                        i.couleurs[1] = 0
                        i.couleurs[2] = 255


def chercheListe (objet, list) :
    for i in list :
        if ( i.index == objet):
            return True
    return False

def g (halfedge, vertices, facets):
    x = len(vertices) - (len(halfedge)/2) + len(facets)
    return (2-x)/2

def genere_x_couleur (nb) :
    print(nb)
    list = []
    for i in range(nb):
        list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    return list
