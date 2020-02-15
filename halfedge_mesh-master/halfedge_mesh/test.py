#!/usr/bin/env python
# -*- coding: utf-8 -*-

import halfedge_mesh

#===================================================================#
#   Fichier de test sur la classe halfedge_mesh            
#   Date    :   14/02/2020                                                
#   github  :   https://github.com/locky12/algo_geo.git
#===================================================================#

# .off are supported
mesh = halfedge_mesh.HalfedgeMesh("model_off/tetris.off")

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

print( test_v[0].Voisin() )
test_v[0].descendre()
print("retour parcour : ")
for i in test_v :
    print( i.poids , i.index ) 


print("=============================")
print("test Halfedge")

print( mesh.halfedges[0].all_voisin_index() )
print( mesh.halfedges[0].all_vertex_voisin_of_edges() )
for i in mesh.halfedges :
    continue
