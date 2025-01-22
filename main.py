import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph  # Pour générer une séquence d'images (schéma dynamique)

# Fonction pour créer le graphe complexe représentant le flux de patients
def create_problem_graph():
    G = nx.DiGraph()

    # Ajout des nœuds et arcs avec capacités (flux possibles)
    G.add_edge("Admission", "Consultation Générale", capacity=70)
    G.add_edge("Consultation Générale", "Radiologie", capacity=40)
    G.add_edge("Consultation Générale", "Laboratoire", capacity=50)
    G.add_edge("Radiologie", "Traitement Radiologique", capacity=30)
    G.add_edge("Laboratoire", "Consultation Spécialiste", capacity=35)
    G.add_edge("Consultation Spécialiste", "Traitement Médical", capacity=45)
    G.add_edge("Traitement Radiologique", "Sortie", capacity=20)
    G.add_edge("Traitement Médical", "Sortie", capacity=50)

    return G

# Fonction pour dessiner un graphe avec des styles améliorés
def draw_graph(G, title=""):
    plt.figure(figsize=(14, 12))
    pos = nx.spring_layout(G, seed=42)  # Position fixe pour cohérence
    capacities = nx.get_edge_attributes(G, 'capacity')
    nx.draw(
        G, pos, with_labels=True, node_size=3000, node_color='#4CAF50',
        font_size=8, font_weight='bold', font_color="white"
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities, font_color="#ff5722", font_size=9)
    plt.title(title, fontsize=16, color="#333333", fontweight="bold")
    st.pyplot(plt)

def generate_sequence_diagram():
    from graphviz import Digraph  # Import ici si non global

    dot = Digraph(format='png', engine='dot')
    dot.attr(rankdir='LR', size='35' ,dpi="500")  # Augmenter la taille du diagramme

    # Ajouter des nœuds avec descriptions
    dot.node("Admission", "Admission\n(Entrée des patients)", width="2", height="1")
    dot.node("Consultation Générale", "Consultation Générale\n(Médecin généraliste)", width="2.5", height="1")
    dot.node("Radiologie", "Radiologie\n(Examens d'imagerie)", width="2", height="1")
    dot.node("Laboratoire", "Laboratoire\n(Analyses biologiques)", width="2", height="1")
    dot.node("Consultation Spécialiste", "Consultation Spécialiste\n(Expertise spécialisée)", width="2.5", height="1")
    dot.node("Traitement Radiologique", "Traitement Radiologique\n(Traitement ciblé)", width="2.5", height="1")
    dot.node("Traitement Médical", "Traitement Médical\n(Suivi et soins)", width="2.5", height="1")
    dot.node("Sortie", "Sortie\n(Fin du parcours)", width="2", height="1")

    # Ajouter des arcs avec annotations
    dot.edge("Admission", "Consultation Générale", label="70 patients/h")
    dot.edge("Consultation Générale", "Radiologie", label="40 patients/h")
    dot.edge("Consultation Générale", "Laboratoire", label="50 patients/h")
    dot.edge("Radiologie", "Traitement Radiologique", label="30 patients/h")
    dot.edge("Laboratoire", "Consultation Spécialiste", label="35 patients/h")
    dot.edge("Consultation Spécialiste", "Traitement Médical", label="45 patients/h")
    dot.edge("Traitement Radiologique", "Sortie", label="20 patients/h")
    dot.edge("Traitement Médical", "Sortie", label="50 patients/h")

    # Générer et afficher l'image
    filepath = "sequence_diagram"
    dot.render(filepath, format='png', cleanup=True)
    st.image(f"{filepath}.png", caption="Schéma explicatif du parcours patient", use_container_width=True)

# Fonction pour calculer et afficher le flot maximal
def generate_solution_graph(G):
    flow_value, flow_dict = nx.maximum_flow(G, "Admission", "Sortie")
    st.write(f"**Flot maximal calculé :** {flow_value} patients par heure")

    # Modifier les étiquettes d'arc pour montrer le flot réalisé
    flow_labels = { (u, v): f"{flow}/{d['capacity']}" for u, v, d in G.edges(data=True)
                    if (flow := flow_dict[u][v]) > 0 }

    # Dessiner le graphe avec les flots
    plt.figure(figsize=(14, 12))
    pos = nx.spring_layout(G, seed=42)  # Position fixe pour cohérence
    nx.draw(
        G, pos, with_labels=True, node_size=3000, node_color='#1E88E5',
        font_size=8, font_weight='bold', font_color="white"
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=flow_labels, font_color="green", font_size=10)
    plt.title("Solution optimisée (Flot maximal)", fontsize=16, color="#333333", fontweight="bold")
    st.pyplot(plt)

# Interface principale Streamlit
st.title("🔄 Optimisation des flux de patients dans un hôpital")

# Navigation par étapes
st.sidebar.title("📋 Navigation")
steps = ["Introduction", "Création du graphe", "Schéma explicatif", "Calcul du flot maximal", "Analyse des résultats"]
step = st.sidebar.radio("Étapes", steps)

if step == "Introduction":
    st.header("Étape 1 : Introduction")
    st.write("""
    ## **Contexte et problématique**  
    Les hôpitaux jouent un rôle essentiel dans la prise en charge des patients, mais ils font souvent face à des défis majeurs liés aux temps d'attente prolongés. Ces délais peuvent être causés par :  
    - Une mauvaise organisation des parcours des patients.  
    - Des ressources limitées, comme un nombre insuffisant de médecins ou de salles.  
    - Une demande croissante de soins, dépassant les capacités disponibles.  

    Ces problèmes entraînent non seulement une expérience frustrante pour les patients, mais aussi une surcharge pour le personnel médical.  

    ## **Objectif du projet**  
    L'objectif principal de ce projet est d'optimiser le flux des patients à travers différentes étapes de leur parcours à l'hôpital, en utilisant des outils et algorithmes issus de la recherche opérationnelle. Cela permettra de :  
    - **Réduire les temps d'attente** : Identifier et supprimer les goulets d'étranglement.  
    - **Maximiser le nombre de patients traités** : Assurer une meilleure utilisation des ressources.  
    - **Améliorer la qualité des soins** : Permettre au personnel de se concentrer sur les traitements.  

    ## **Comment allons-nous procéder ?**  
    Ce projet modélisera le parcours des patients comme un graphe où :  
    - Les **nœuds** représentent les étapes du parcours patient (par exemple, admission, radiologie, traitement).  
    - Les **arcs** représentent les connexions entre ces étapes avec une capacité maximale (nombre de patients pouvant transiter par heure).  

    Un algorithme de recherche opérationnelle, tel que **l'algorithme de flot maximal**, sera appliqué pour optimiser ce flux, tout en respectant les contraintes des ressources disponibles.  

    ## **Exemple concret :**  
    Prenons l'exemple d'un patient arrivant à l'hôpital :  
    1. Il commence par **l'admission**, où ses informations sont enregistrées.  
    2. Ensuite, il passe par une **consultation générale**, où un médecin évalue son état.  
    3. Selon ses besoins, il peut être dirigé vers :  
        - **Radiologie** pour un examen d'imagerie, ou  
        - **Laboratoire** pour une analyse biologique.  
    4. Après les examens, il peut avoir une **consultation spécialisée** ou directement un traitement.  
    5. Une fois le traitement terminé, il quitte l'hôpital.  

    Ce parcours, bien qu'apparemment simple, peut devenir un véritable casse-tête en cas de surcharge. Notre projet vise à résoudre ce problème pour rendre le système plus fluide et efficace.  
    """)

# Étape 2 : Création du graphe
elif step == "Création du graphe":
    st.header("Étape 2 : Création du graphe")
    st.write("""
    ## **Création du graphe représentant le parcours patient**  
    Pour mieux comprendre et optimiser le parcours des patients dans un hôpital, nous avons modélisé ce processus sous forme d’un graphe.  

    ### **Qu’est-ce qu’un graphe ?**  
    Un graphe est un ensemble de **nœuds** (ou sommets) reliés par des **arcs** (ou liens). Dans notre cas :  
    - **Les nœuds** représentent les différentes étapes que les patients suivent dans l’hôpital.  
    - **Les arcs** montrent comment les patients passent d’une étape à l’autre, avec une capacité indiquant le nombre maximal de patients pouvant transiter par heure.  

    ### **Les étapes du parcours patient (nœuds du graphe) :**  
    1. **Admission** :  
       L'étape d'entrée où les informations du patient sont collectées et son passage à l’étape suivante est organisé.  
    2. **Consultation Générale** :  
       Une rencontre initiale avec un médecin généraliste pour évaluer l’état du patient et déterminer les examens ou soins nécessaires.  
    3. **Radiologie** :  
       Réalisation d’examens d’imagerie médicale (rayons X, IRM, scanners) pour aider à diagnostiquer le problème du patient.  
    4. **Laboratoire** :  
       Analyse d’échantillons biologiques (sang, urine, etc.) pour fournir des informations complémentaires au diagnostic.  
    5. **Consultation Spécialiste** :  
       Une rencontre avec un médecin spécialiste qui examine les résultats des analyses et propose des traitements spécifiques.  
    6. **Traitement** :  
       Cette étape regroupe différents types de soins, comme des interventions médicales, des traitements radiologiques ou d’autres suivis nécessaires.  
    7. **Sortie** :  
       L'étape finale où le patient quitte l’hôpital après avoir reçu les soins requis.  

    ### **Les transitions entre les étapes (arcs du graphe) :**  
    Les arcs représentent les connexions entre les étapes avec des capacités maximales :  
    - Entre **Admission** et **Consultation Générale**, un maximum de 70 patients par heure peut être admis.  
    - Entre **Consultation Générale** et les étapes d’examen (**Radiologie** et **Laboratoire**), les capacités sont respectivement de 40 et 50 patients par heure.  
    - Entre **Laboratoire** et **Consultation Spécialiste**, la capacité est de 35 patients par heure.  
    - Entre les traitements (**Radiologique** ou **Médical**) et **Sortie**, la capacité varie entre 20 et 50 patients par heure.  

    Ce graphe nous permet de visualiser le flux des patients et d'identifier les goulets d'étranglement (par exemple, une étape où les capacités sont insuffisantes).  
    """)

    # Création et affichage du graphe
    G = create_problem_graph()
    draw_graph(G, title="Graphe représentant le parcours patient")


# Étape 3 : Schéma explicatif
elif step == "Schéma explicatif":
    st.header("Étape 3 : Schéma explicatif")
    st.write("""
    ## **Schéma explicatif : Visualisation du parcours patient**  

    Ce schéma dynamique illustre le parcours des patients à travers différentes étapes de l'hôpital. Il aide à comprendre :  
    - **Les étapes principales** que les patients traversent.  
    - **Les connexions entre les étapes**, montrant comment les patients transitent d'une étape à l'autre.  
    - **Les limites de capacité** des ressources, comme le nombre maximum de patients pouvant être pris en charge par heure dans chaque étape.

    ### **Détail des étapes représentées dans le schéma :**  
    1. **Admission :**  
       - C'est le point de départ où les patients sont enregistrés.  
       - Les informations sont collectées et les patients sont dirigés vers les étapes suivantes.  
    2. **Consultation Générale :**  
       - Un médecin généraliste évalue l’état initial du patient.  
       - Le médecin décide des examens ou traitements nécessaires, en orientant les patients vers la Radiologie ou le Laboratoire.  
    3. **Radiologie :**  
       - Étape où les patients réalisent des examens d’imagerie (comme des scanners, IRM ou rayons X).  
    4. **Laboratoire :**  
       - Analyses biologiques comme des tests sanguins ou urinaires pour compléter le diagnostic médical.  
    5. **Consultation Spécialiste :**  
       - Un médecin spécialiste examine les résultats des analyses et propose un plan de traitement adapté.  
    6. **Traitement :**  
       - Cette étape regroupe différents soins, tels que des traitements radiologiques ou médicaux.  
    7. **Sortie :**  
       - Les patients quittent l’hôpital une fois tous les soins nécessaires réalisés.  

    ### **Pourquoi ce schéma est important ?**  
    - Il donne une vue claire et structurée du parcours hospitalier.  
    - Il met en évidence les **goulets d’étranglement** potentiels où les capacités peuvent être dépassées (par exemple, Radiologie ou Traitement).  
    - Il sert de base pour optimiser les flux en identifiant les étapes critiques.  

    Regardez ci-dessous pour une illustration détaillée générée dynamiquement :  
    """)

    st.image("sequence_diagram.png", caption="Schéma explicatif du parcours patient", width=900)

# Étape 4 : Calcul du flot maximal
elif step == "Calcul du flot maximal":
    st.header("Étape 4 : Calcul du flot maximal")
    st.write("""
    ## **Qu'est-ce que le flot maximal ?**  
    Le **flot maximal** est une méthode de recherche opérationnelle qui permet de déterminer la quantité maximale d'un flux (ici, les patients) qui peut traverser un système (le parcours hospitalier) tout en respectant les capacités des ressources disponibles (médecins, salles, équipements).  

    ### **Pourquoi le calculer ?**  
    Le calcul du flot maximal nous aide à :  
    - Identifier combien de patients peuvent être pris en charge simultanément à travers toutes les étapes de l'hôpital.  
    - Détecter les étapes ou transitions où les ressources sont insuffisantes (goulets d'étranglement).  
    - Proposer des améliorations pour rendre le parcours plus efficace.  

    ### **Comment est-il calculé ?**  
    1. Nous utilisons un algorithme de **flot maximal**, qui suit les arcs du graphe (les connexions entre les étapes) et respecte leurs capacités maximales.  
    2. Le flot est calculé entre un point d'entrée (**Admission**) et un point de sortie (**Sortie**).  
    3. Chaque arc indique combien de patients peuvent transiter à un moment donné.  

    Voici le graphe mis à jour avec le **flot maximal calculé** :  
    """)
    G = create_problem_graph()
    generate_solution_graph(G)

# Étape 5 : Analyse des résultats
elif step == "Analyse des résultats":
    st.header("Étape 5 : Analyse des résultats")
    st.write("""
    ## **Analyse des résultats obtenus**  

    Une fois le flot maximal calculé, nous pouvons analyser les données pour identifier les **points critiques** et proposer des améliorations.  

    ### **Les goulets d'étranglement**  
    Les goulets d’étranglement sont des étapes où les ressources disponibles sont insuffisantes pour gérer tous les patients qui transitent. Dans notre cas :  
    - **Radiologie** : L'étape est limitée à 40 patients par heure, ce qui peut entraîner des retards.  
    - **Traitement Radiologique** : La capacité est limitée à 30 patients par heure, ce qui peut freiner la progression des flux.  

    ### **Propositions d'amélioration**  
    Pour résoudre ces goulets d'étranglement et améliorer le système :  
    1. **Augmenter les ressources humaines** : Ajouter du personnel (médecins, techniciens, infirmiers) pour augmenter la capacité des étapes critiques.  
    2. **Augmenter les équipements** : Ajouter des machines (appareils de radiologie ou équipements de laboratoire) pour traiter plus de patients simultanément.  
    3. **Optimiser les priorités** : Mettre en place un système qui donne la priorité aux patients les plus urgents ou ceux nécessitant des soins critiques.  
    4. **Réorganiser les flux** :  
        - Réduire les étapes inutiles pour certains patients.  
        - Diviser les flux pour éviter que trop de patients passent par les mêmes étapes (par exemple, répartir les patients entre plusieurs services).  

    ### **Conclusion**  
    En appliquant ces propositions, nous pouvons :  
    - **Réduire significativement les temps d’attente.**  
    - **Maximiser l’efficacité des ressources disponibles.**  
    - **Améliorer la qualité des soins offerts aux patients.**  
    """)

