#!/usr/bin/env python
# -*- coding: utf-8 -*-

import halfedge_mesh

# .off are supported
mesh = halfedge_mesh.HalfedgeMesh("tetris.off")

# Returns a list of Vertex type (in order of file)--similarly for halfedges,
# and facets
mesh.vertices

# The number of facets in the mesh
len(mesh.facets)

# Get the 10th halfedge
mesh.halfedges[10]

print("=============================")

print("test facets")
for i in mesh.facets:
    #print(i.adjacent_halfedges_index())
    t = i.adjacent_vertices_obj()
    for j in t :
        continue
        #print( j.get_vertex() )
    #print( i.aire_tri())
print("=============================")

print("test vertices")
test_v = mesh.vertices
for i in mesh.vertices:
    #print( i.distance( test_v[1] ) )
    #print( i.produit_vectoriel( test_v[1] ) )
    #print( i.Voisin() )
    continue

test_v[0].descendre()
for i in test_v :
    print( i.poids , i.index ) 


print("=============================")
