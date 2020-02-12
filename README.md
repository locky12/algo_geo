#===============================================#
 Notepatch 1.1
 29/01/2020
 François-Xavier Marcheix
#===============================================#

 Rapport de code :

=> Les commantaires ne sont pas gérer
=> Pas de couleur
=> Espace non gérer

 class HalfedgeMesh

- Correction du chargement des fichiers off
	=> les commentaire '#' sont pris en compte par le programme
	=> modifier : parse_off , parse_build_halfedge_off , read_off_vertices


 class Facet

- nouvelle fonction 

	=> adjacent_vertices(self) renvoie les points du triangles

	=> adjacent_halfedges(self) renvoie les arrêtes du triangles
		to do : renvoie sous forme obj
#
#===============================================#
 Notepatch 1.2
 05/02/2020
 François-Xavier Marcheix
#===============================================#

 Rapport de code :

=> Ajout de l'aire d'une face triangulaire
=> Ajout de l'aire d'un modele


 class Vertex

- nouvelle fonction 

	=> distance(self,other) renvoie la distance a un autre point du plan
	=> produit_vectoriel(self,other) renvoie le produit vecotiel entre l'objet et une autre de même classe
	
	=== Dijkstra

	- Ajout d'un paramétre poids
	- Ajout d'un paramétre drapeau 

	=> Voisin(self) renvoie la liste des voisins 
		// besoin de corectif sur le retour
	=> init_Dijkstra(self)
		// 
	=> descendre(self) fait un dijstra sur le point actuel
		// peut être optimisé par un trie

 class Facet

	=> aire_tri(self) renvoie l'aire de la face

 Autre 

	- le model cube.off ne fonctionne pas sur Voisin()
		// Soit car voisin ne fonctionne pas
		// Soit il est sans bord
#
#===============================================#
 Notepatch 1.3
 12/02/2020
 François-Xavier Marcheix
#===============================================#

 class Facet

	- couleurs = [ 0 , 0 , 0 ]
	- La fonction voisin est modifier

#
#===============================================#
Git :

- git clone adresse
- git add
- git status
- git commit -m "commentaire"
- git push
