# Optimisation des Flux de Patients dans un Hôpital à l'Aide de la Recherche Opérationnelle

## 1. Contexte

Dans de nombreux hôpitaux, des problèmes récurrents se posent en raison de temps d'attente excessifs et d'une surcharge du personnel médical. Ces difficultés résultent souvent d'une gestion inefficace des flux de patients et de ressources limitées (médecins, salles, équipements). Ce projet a pour ambition d'utiliser des techniques de recherche opérationnelle, en particulier l'algorithme de flot maximal, pour optimiser le parcours des patients dans un environnement hospitalier.

## 2. Objectifs

L’objectif principal est de modéliser et d’optimiser le parcours des patients dans un hôpital en tenant compte des contraintes liées aux ressources disponibles. Les objectifs spécifiques sont :

- **Maximiser le nombre de patients traités par heure.**
- **Réduire les temps d’attente** à chaque étape du parcours.
- **Améliorer l’utilisation des ressources** (humaines et matérielles) pour une gestion plus efficace de l’activité hospitalière.

## 3. Modélisation du Projet

Le parcours patient est représenté sous la forme d’un **graphe orienté** :

- **Nœuds** : Chaque nœud correspond à une étape du parcours patient (par exemple, Admission, Consultation, Radiologie, etc.).
- **Arcs** : Les arcs relient ces étapes et indiquent, par le biais de capacités maximales, le nombre de patients pouvant passer d'une étape à l'autre par heure.

L’algorithme de **flot maximal** est ensuite appliqué pour déterminer le flux optimal de patients à travers l'ensemble du système hospitalier, en respectant les contraintes de capacité de chaque service.

## 4. Installation

### Prérequis

- **Python 3.x**

- Bibliothèques Python requises :
  - **Streamlit** : Pour la création de l'interface graphique.
  - **NetworkX** : Pour la modélisation du graphe et l’implémentation de l'algorithme de flot maximal.
  - **Matplotlib** : Pour la visualisation des graphes.
  - **Graphviz** (optionnel) : Pour générer et afficher des schémas explicatifs. Assurez-vous que Graphviz est installé et correctement configuré sur votre machine.

### Installation des Dépendances

Pour installer les bibliothèques nécessaires, exécutez la commande suivante :

```bash
pip install streamlit networkx matplotlib graphviz
5. Exécution du Projet
Pour lancer le projet :

Téléchargez le projet et placez-le dans le répertoire de votre choix.

Dans un terminal, exécutez la commande suivante pour démarrer l'application avec Streamlit :
streamlit run main.py

Naviguez dans l'application, qui se compose des étapes suivantes :

Étape 1 : Introduction
Présente le contexte et la problématique.

Étape 2 : Création du graphe
Affiche un graphe représentant le parcours patient avec ses capacités.

Étape 3 : Schéma explicatif
Fournit une illustration détaillée du parcours du patient, étape par étape.

Étape 4 : Calcul du flot maximal
Applique l’algorithme de flot maximal pour déterminer le flux optimal de patients.

Étape 5 : Analyse des résultats
Analyse les goulets d’étranglement identifiés et propose des améliorations pour optimiser le flux.

6. Structure du Projet
Le dépôt est organisé comme suit :
project-directory/
│
├── main.py                    # Script principal de l'application
├── schema_parcours_patient.png # Image illustrant le parcours patient (optionnel)
├── README.md                   # Ce fichier de documentation
└── requirements.txt            # Liste des dépendances Python (facultatif)
7. Résultats
L'application permet de :

Calculer le flot maximal, c'est-à-dire le nombre de patients pouvant être traités par heure à travers l'ensemble de l'hôpital.
Identifier les goulets d'étranglement dans des étapes clés, telles que la Radiologie et le Traitement Radiologique.
Proposer des pistes d'amélioration pour optimiser le flux des patients en ajustant les ressources ou en réorganisant le parcours.
8. Remerciements
Nous souhaitons exprimer notre profonde gratitude à Mme Zineb Tabbakh, professeur de recherche opérationnelle, pour son soutien précieux et ses conseils avisés tout au long de ce projet.

9. Auteurs
Ce projet a été réalisé par :

Haitham El Abdioui
