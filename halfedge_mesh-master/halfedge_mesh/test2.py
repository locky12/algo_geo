#!/usr/bin/env python
# -*- coding: utf-8 -*-

import halfedge_mesh_heritage

#===================================================================#
#   Fichier de test sur la classe halfedge_mesh_heritage
#   Date    :   14/02/2020
#   github  :   https://github.com/locky12/algo_geo.git
#===================================================================#

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/cubes.off")


print("=============================")
print("Test parcours")


# mesh.parcours_largeur()
mesh.parcours(mesh.vertices[0])
mesh.colorie_composante_connexe()
mesh.write_file("model_off/bonhommeColorieComposante.off")

# print(mesh.verification_marq())

print("=============================")
print("Test coloration")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/ico.off")
# mesh.colorie_bis(mesh.vertices[0])
# mesh.composante_connexes()
# mesh.colorie_distance_coposantes()
# for i in mesh.vertices :
#     print(i.poids)
# quit()
print("diametre estimation = ", mesh.estimation_diametre())
print("volume = ", mesh.Volume_mesh() )
quit()# Sauvegarde du fichier
mesh.write_file("model_off/Retour_coloration.off")
print('ok')
# quit()

print("=============================")
print("Test composante connexes")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/CC_genre.off")

mesh.composante_connexes()
mesh.calcule_genre()
mesh.colorie_genre()
# mesh.colorie_distance_coposantes()

mesh.write_file("model_off/CC_genre_colorie.off")


# mesh.write_file("model_off/bonhommeColorie.off")
#
# print("=============================")
# print("Test genre")
#
# mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/CC_genre.off")
# mesh.composante_connexes()
# mesh.colorie_composante_connexe()
# mesh.write_file("model_off/composante_colorie.off")
# mesh.calcule_genre()
# mesh.genre()
