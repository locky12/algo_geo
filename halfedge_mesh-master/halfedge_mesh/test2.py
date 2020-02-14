import halfedge_mesh_heritage
mesh = halfedge_mesh_heritage.HalfedgeMeshHerited("bonhomme.off")
# mesh.parcours_largeur()
# mesh.parcours(mesh.vertices[0])
# # mesh.write_file("cubeColor2.off")
# print(mesh.verification_marq())
mesh.composante_connexes()
