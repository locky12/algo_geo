import halfedge_mesh
import random
# Nouveau lib disponnible
import numpy as np
from sklearn.cluster import KMeans

#===============================================================================#
# Fichier de la classe HalfedgeMeshHerited
# Date : 19/02/2020
#
#===============================================================================#

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
            # quit()
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


    def estimation_diametre(self) :
        list_poids = []
        ind_s1 = random.randint( 0 , len( self.vertices ) - 1 )
        self.vertices[ind_s1].descendre()
        s1 = self.vertices[ind_s1]
        for vertex in self.vertices :
            list_poids.append(vertex.poids)
            vertex.init_Dijkstra()

        maxi = max(list_poids)
        s2 = self.vertices[list_poids.index(maxi)]
        list_poids = []
        s2.descendre()
        for vertex in self.vertices :
            list_poids.append(vertex.poids)
            vertex.init_Dijkstra()
        maxi = max(list_poids)
        s3 = self.vertices[list_poids.index(maxi)]

        return halfedge_mesh.distance(s2,s3)


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

    #Renvoie le volume de l'objet
    def Volume_mesh(self):
        res = []
        for t in self.facets :
            res.append( t.SignedVol() )
        return abs( sum(res) )


    def min_max_xyz() :
        list_x = []
        list_y = []
        list_z = []
        for vertex in self.vertices :
            list_x.append(vertex.x)
            list_x.append(vertex.y)
            list_x.append(vertex.z)

        return ([[min(list_x), max(list_x)],[min(list_y), max(list_y)],[min(list_z), max(list_z)]])


    #____________________________________________________________#
    #
    #   Partie : Segmentation
    #____________________________________________________________#

    # Coloration des faces du maillage
    def start_segmentation(self):
        print( self.facets[0].halfedge.adjacente_face() )
        print("")
        liste_p = []
        for i in self.facets :
            liste_p.append( i.perimetre() )
        moy = moyenne(liste_p)
        for i in range(len(self.facets)):
            if( liste_p[i] <= moy ) :
                self.facets[i].categorie = 1
                self.facets[i].give_couleur([250,0,0])
            else :
                self.facets[i].categorie = 2
                self.facets[i].give_couleur([0,0,250])
        return moy

    #
    def parcours_face (self,face_i,num_marq =  1) :
        pile = []
        face_i.marq = num_marq
        face_cat = face_i.categorie
        pile.append(face_i)
        while (pile != []) :
            face_i = pile.pop(len(pile) -1)
            voisins = face_i.halfedge.adjacente_face()
            for voisin in voisins :
                if (voisin.marq == 0 and voisin.categorie == face_cat) :
                    voisin.marq = num_marq
                    pile.append(voisin)

    def verification_marq_face (self) :
        out = []
        for f in self.facets :
            if f.marq == 0 :
                out.append(f)
        return out

    def composante_connexes_face (self) :
        faces = self.verification_marq_face()
        nb_composante = 0
        while (faces != []) :
            self.parcours_face(faces[0],nb_composante + 1)
            faces = self.verification_marq_face()
            nb_composante += 1
        self.nb_composante = nb_composante
        print("nombe de composante_connexes : ", nb_composante)

    def colorie_composante_connexe_face (self) :
        couleurs = genere_x_couleur(self.nb_composante)
        for f in self.facets :
            f.couleurs = couleurs[f.marq - 1]

    def colorie_categorie (self,k) :
        couleurs = genere_x_couleur(k)
        for f in self.facets :
            f.couleurs = couleurs[f.categorie]
    #____________________________________________________________#
    #
    #   Partie : Segmentation par k-mean
    #____________________________________________________________#

# Cette méthode utlise le k-mean

    def test_learn( self,nb_cluster = 2):
        liste_p = []
        for i in self.facets :
            liste_p.append( i.perimetre() )
        X = np.array(list(zip(liste_p,liste_p)))
        kmeans = KMeans(n_clusters=3)
        kmeans = kmeans.fit(X)
        labels = kmeans.predict(X)
        for i,j in zip(self.facets,labels) :
            i.categorie = j


    def test_learn_2D( self, nb_cluster ):

        liste_p = []
        liste_aire = []
        for i in self.facets :
            liste_p.append( i.perimetre() )
            liste_aire.append(i.aire_tri())
        X = np.array(list(zip(liste_p,liste_aire)))
        kmeans = KMeans(nb_cluster)
        kmeans = kmeans.fit(X)
        labels = kmeans.predict(X)
        for i,j in zip(self.facets,labels) :
            i.categorie = j

# Méthode D'Otsu

def Otsu( liste_p , n ):

    maxi = max(liste_p)
    taille = maxi/n
    tab = []
    for j in range(n) :
        tab.append( [] )
        for i in liste_p :
            #print("ici",maxi/(j+1),maxi/(j+2),i," m = ",maxi)
            if( i <= taille*i and i > taille*(i+1) ):
                #print("oui")
                tab[j].append( i )
    return tab


#===============================================================================#
# Fonction externe #

def chercheListe (objet, list) :
    for i in list :
        if ( i.index == objet):
            return True
    return False

def g (halfedge, vertices, facets):
    x = len(vertices) - (len(halfedge)/2) + len(facets)
    return (2-x)/2

def genere_x_couleur (nb) :
    list = []
    for i in range(nb):
        list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    return list

def moyenne(liste):
    return sum(liste)/len(liste)
