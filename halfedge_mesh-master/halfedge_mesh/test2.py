#!/usr/bin/env python
# -*- coding: utf-8 -*-

import halfedge_mesh_heritage

#===================================================================#
#   Fichier de test sur la classe halfedge_mesh_heritage
#   Date    :   14/02/2020
#   github  :   https://github.com/locky12/algo_geo.git
#===================================================================#

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/cube2.off")


print("=============================")
print("Test parcours")


# mesh.parcours_largeur()
mesh.parcours(mesh.vertices[0])
mesh.colorie_composante_connexe()
mesh.write_file("model_off/bonhommeColorieComposante.off")

# print(mesh.verification_marq())

print("=============================")
print("Test coloration")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/tetris.off")
# mesh.colorie_bis(mesh.vertices[0])
mesh.colorie_distance_coposantes()
print("volume = ", mesh.Volume_mesh() )
# quit()
# Sauvegarde du fichier
mesh.write_file("model_off/Retour_coloration.off")
print('ok')


print("=============================")
print("Test composante connexes")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/bonhomme.off")

mesh.composante_connexes()
# mesh.calcule_genre()
# mesh.colorie_genre()
mesh.colorie_distance_coposantes()

mesh.write_file("model_off/CC_genre_colorie.off")


# mesh.write_file("model_off/bonhommeColorie.off")

print("=============================")
print("Test genre")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/bitore.off")
mesh.composante_connexes()
mesh.colorie_composante_connexe()
mesh.calcule_genre()
mesh.genre()

