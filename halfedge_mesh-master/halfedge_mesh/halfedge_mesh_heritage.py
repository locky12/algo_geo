import halfedge_mesh
import random


class HalfedgeMeshHerited(halfedge_mesh.HalfedgeMesh):
    def __init__(self,arg):
        halfedge_mesh.HalfedgeMesh.__init__(self,arg)
        self.nb_composante = 0

    def write_file(self, filename) :
        with open(filename, 'w') as file:
            file.write("COFF\n")

            file.write(str(len(self.vertices)) + " " +  str(len(self.facets)) + " " + str(len(self.halfedges)/2)+ "\n" )
            for vertice in self.vertices :
                file.write(str(vertice.x) + " " + str(vertice.y) + " " + str(vertice.z)+" "+ str(vertice.couleurs[0]) + " " + str(vertice.couleurs[1]) + " " + str(vertice.couleurs[2]) + "\n")
            for facet in self.facets :
                file.write("3" + "  " +str(facet.a) + " " + str(facet.b) + " " + str(facet.c)+" "+ str(facet.couleurs[0]) + " " + str(facet.couleurs[1]) + " " + str(facet.couleurs[2]) +"\n")


    def parcours_largeur (self) :
        vertex = self.vertices[0]
        pile = []
        pile.append(vertex)
        vertex.marq = True
        while pile != [] :
            if(vertex in pile):
                pile.remove(vertex)
            print("en cours de traitement : ", vertex.index)

            voisin = vertex.halfedge.next.vertex
            # if (voisin.marq == False) :
            vertex = voisin
            print("voisin1 : ", voisin.index)

            while voisin.marq == False :
                print("voisin : ", voisin.index)
                pile.append(voisin)
                voisin.marq = True
                voisin = voisin.halfedge.next.vertex
        for i in self.vertices :
            if(i.marq == True) :
                print("True : ",i.index)
            else :
                print("False : ",i.index)

    def test (self) :
            pile = []
            pile.append("A")
            pile.append("B")
            pile.append("C")
            r = pile.pop(len(pile)-1)
            print(pile)
            print(r)

    def parcours (self,vertex,num_marq) :
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
        couleurs = self.genere_x_couleur()
        for vertex in self.vertices :
            vertex.couleurs = couleurs[vertex.marq -1]


    def genere_x_couleur (self) :
        list = []
        for i in range(self.nb_composante):
            list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
        return list

<<<<<<< HEAD
    def calcule_genre (self, num_composante = 1) :
        list = [[],[],[]]
        print(list)
        for halfedge in self.halfedges :
            if(halfedge.vertex.marq == num_composante):
                if (chercheListe(halfedge.index, list[0]) == False):
                    list[0].append(halfedge)
                if (chercheListe(halfedge.vertex.index, list[1]) == False):
                    list[1].append(halfedge.vertex)
                if (chercheListe(halfedge.facet.index, list[2]) == False):
                    list[2].append(halfedge.facet)

        print(len(list[0]), len(list[1]) ,len(list[2]))
        print(list)
        return list

    def genre_composantes(self):
        list = []
        for i in range(self.nb_composante) :
            list.append(self.calcule_genre(i+1))
        print(list)
        return list

    def genre(self) :
        lists = self.genre_composantes()
        for list in lists :
            print(g(list[0],list[1], list[2]))
            print("genre de la CC ", 0, "est : " , g(list[0],list[1], list[2])  )

def chercheListe (objet, list) :
    for i in list :
        print("compare",i.index, objet)
        if ( i.index == objet):
            print("true")
            return True
    return False

def g (halfedge, vertices, facets):
    x = len(vertices) - (len(halfedge)/2) + len(facets)
    return (2-x)/2
=======


    # new 1.3
    def colorie(self,index_a):

        if( index_a >= len(self.vertices) or index_a < 0 ):
            print(">>> Erreur : index non valide pour la coloration ")
            return -1
        
        min_find = 0
        max_find = 0
        
        # Parcour pour crée la distance au point
        self.vertices[index_a].descendre()
        
        for i in self.vertices :
            if( max_find < i.poids ) :
                max_find = i.poids
                
        for i in self.vertices :
            i.couleurs[0] = int( 255 * (( i.poids - min_find ) / ( max_find - min_find )) )
            if( i.poids == 0 ):
                # Le point de départ visible en bleu
                i.couleurs[0] = 0
                i.couleurs[1] = 0
                i.couleurs[2] = 255
>>>>>>> 6b9564e924897b8ed8442e4963b8447715af054e
