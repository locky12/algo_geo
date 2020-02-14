import halfedge_mesh


class HalfedgeMeshHerited(halfedge_mesh.HalfedgeMesh):

    def __init__(self,arg):
        halfedge_mesh.HalfedgeMesh.__init__(self,arg)

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

    def parcours (self,vertex) :
        pile = []
        vertex.marq = True
        pile.append(vertex)
        while (pile != []) :
            vertex = pile.pop(len(pile) -1)
            voisins = vertex.Voisin()
            for voisin in voisins :
                if (voisin[0].marq == False) :
                    voisin[0].marq = True
                    pile.append(voisin[0])
    def verification_marq (self) :
        out = []
        for vertex in self.vertices :
            if vertex.marq == False :
                out.append(vertex)
        return out

            
    def composante_connexes (self) :
        vertices = self.verification_marq()
        nb_composante = 0
        while (vertices != []) :
            self.parcours(vertices[0])
            vertices = self.verification_marq()
            nb_composante += 1

        print("nombe de composante_connexes : ", nb_composante)






# class VertexHerited (halfedge_mesh.Vertex) :
#     def __init__() :
#         halfedge_mesh.Vertex.__init__(self)
