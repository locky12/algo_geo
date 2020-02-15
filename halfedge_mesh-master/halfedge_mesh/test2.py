#!/usr/bin/env python
# -*- coding: utf-8 -*-

import halfedge_mesh_heritage

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("tore.off")
mesh.composante_connexes()
mesh.colorie_composante_connexe()
mesh.calcule_genre()
mesh.genre()
quit()

#===================================================================#
#   Fichier de test sur la classe halfedge_mesh_heritage
#   Date    :   14/02/2020
#   github  :   https://github.com/locky12/algo_geo.git
#===================================================================#


mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/bonhomme.off")


print("=============================")
print("Test parcours")


# mesh.parcours_largeur()

# mesh.parcours(mesh.vertices[0])

# # mesh.write_file("cubeColor2.off")

# print(mesh.verification_marq())

print("=============================")
print("Test coloration")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/tetris.off")

mesh.colorie(0)

# Sauvegarde du fichier
mesh.write_file("model_off/Retour_coloration.off")

print("=============================")
print("Test composante connexes")

mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("model_off/bonhomme.off")

mesh.composante_connexes()

mesh.colorie_composante_connexe()

# mesh.calcule_genre()
# mesh.genre()
mesh.write_file("bonhommeColorie.off")


mesh.write_file("model_off/bonhommeColorie.off")

print("=============================")
