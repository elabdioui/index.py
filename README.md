Optimisation des Flux de Patients dans un Hôpital à l'Aide de la Recherche Opérationnelle
1. Contexte
Dans de nombreux hôpitaux, les temps d'attente prolongés pour les patients et la surcharge des professionnels de santé sont des problèmes récurrents. Cela est souvent dû à une gestion inefficace des flux de patients et à des ressources limitées (médecins, salles, équipements). Ce projet se propose d'utiliser des outils de recherche opérationnelle, en particulier l'algorithme de flot maximal, pour optimiser le parcours des patients dans un hôpital.

2. Objectifs
L'objectif de ce projet est de modéliser et d'optimiser le parcours des patients dans un hôpital en respectant les contraintes des ressources disponibles. Plus précisément :

Maximiser le nombre de patients traités par heure.
Réduire les temps d'attente à chaque étape du parcours.
Améliorer l'utilisation des ressources (humaines et matérielles) dans un environnement hospitalier.
3. Modélisation du Projet
Le parcours patient est modélisé sous forme d’un graphe orienté :

Les nœuds représentent les étapes du parcours patient (Admission, Consultation, Radiologie, etc.).
Les arcs représentent les transitions entre ces étapes avec des capacités maximales, indiquant combien de patients peuvent transiter par heure d'une étape à l'autre.
L'algorithme de flot maximal est utilisé pour calculer le nombre maximal de patients pouvant être pris en charge à travers l'ensemble du parcours hospitalier, tout en respectant les contraintes de capacité de chaque service.

4. Installation
Prérequis
Python 3.x
Bibliothèques Python :
Streamlit : pour créer l'interface graphique.
NetworkX : pour la modélisation du graphe et l'application de l'algorithme de flot maximal.
Matplotlib : pour la visualisation des graphes.
Graphviz (optionnel) : pour générer et visualiser des schémas explicatifs (vérifiez que Graphviz est bien installé sur votre machine).
Installation des dépendances
Installez les dépendances nécessaires avec la commande suivante :

bash
Copier
Modifier
pip install streamlit networkx matplotlib graphviz
5. Exécution du Projet
Télécharger le projet et placez-le dans un répertoire de votre choix.
Lancer l'application avec Streamlit en exécutant la commande suivante dans votre terminal :
bash
Copier
Modifier
streamlit run main.py
Naviguer dans l'application :
Étape 1 : Introduction : Présente le contexte et la problématique.
Étape 2 : Création du graphe : Affiche un graphe représentant le parcours patient avec ses capacités.
Étape 3 : Schéma explicatif : Explique le parcours du patient étape par étape.
Étape 4 : Calcul du flot maximal : Applique l'algorithme de flot maximal pour déterminer le flux optimal de patients.
Étape 5 : Analyse des résultats : Analyse les goulets d’étranglement et propose des solutions d'amélioration.
6. Structure du Projet
Le projet est structuré comme suit :

bash
Copier
Modifier
project-directory/
│
├── main.py                    # Script principal du projet
├── schema_parcours_patient.png # Image représentant le parcours patient (optionnel)
├── README.md                   # Fichier de documentation (ce fichier)
└── requirements.txt            # Liste des dépendances Python (facultatif)
7. Résultats
L'application présente les résultats suivants :

Flot maximal calculé, représentant le nombre de patients pouvant être pris en charge à travers tout l’hôpital.
Identification des goulets d'étranglement dans certaines étapes, telles que Radiologie et Traitement Radiologique.
Propositions d'amélioration pour optimiser le flux des patients en ajoutant des ressources ou en réorganisant le parcours.
8. Remerciements
Ce projet a été encadré par Mme Zineb Tabbakh, professeur de recherche opérationnelle, qui nous a fourni un soutien précieux tout au long du développement de ce travail. Nous la remercions pour ses conseils, son expertise et son implication.

9. Auteurs
Le projet a été réalisé par :Haitham El Abdioui
