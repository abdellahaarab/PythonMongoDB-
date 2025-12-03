"""
main.py
-------

Interface console professionnelle pour gérer les trajets
utilisant la classe GST (MongoDB).

Auteur : Abdellah
Version : Pro
"""

from logic import GST


def afficher_menu():
    """
    Affiche le menu principal du programme.
    """
    print("""
==============================================
           GESTION DES TRAJETS (GST)
==============================================
1 - Ajouter un trajet
2 - Afficher tous les trajets
3 - Rechercher par ville de départ
4 - Supprimer par nom
5 - Sauvegarder un trajet dans un fichier
6 - Afficher le trajet avec la distance minimale
0 - Quitter
==============================================
""")


def demander_entier(message: str) -> int:
    """
    Demande un entier à l'utilisateur avec gestion d'erreur.

    :param message: Texte affiché pour la saisie.
    :return: Valeur entière saisie par l'utilisateur.
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("⚠ Erreur : veuillez entrer un nombre valide.")


def ajouter_trajet(gst: GST):
    """
    Collecte les informations d'un trajet et l'ajoute à la base.

    :param gst: Instance de la classe GST.
    """
    print("\n--- AJOUT D'UN TRAJET ---")

    tb = {
        "nom": input("Nom : "),
        "dist": demander_entier("Distance : "),
        "viled": input("Ville de départ : "),
        "vileA": input("Ville d'arrivée : ")
    }

    gst.Ajouter(tb)
    print("✔ Trajet ajouté avec succès.\n")


def rechercher_trajet(gst: GST):
    """
    Recherche et affiche les trajets à partir d'une ville.

    :param gst: Instance de la classe GST.
    """
    print("\n--- RECHERCHE PAR VILLE DE DÉPART ---")
    v = input("Ville de départ : ")
    print(gst.rechercher(v))


def supprimer_trajet(gst: GST):
    """
    Supprime un trajet selon son nom.

    :param gst: Instance de la classe GST.
    """
    print("\n--- SUPPRESSION D'UN TRAJET ---")
    nom = input("Nom du trajet à supprimer : ")
    print(gst.suprimer(nom))


def sauvegarder_trajet(gst: GST):
    """
    Sauvegarde un trajet dans un fichier texte.

    :param gst: Instance de la classe GST.
    """
    print("\n--- SAUVEGARDER UN TRAJET ---")
    nom = input("Nom du trajet à sauvegarder : ")
    gst.sof(nom)
    print(f"✔ Le trajet '{nom}' a été sauvegardé dans {nom}.txt\n")


def afficher_plus_court(gst: GST):
    """
    Affiche le trajet ayant la distance minimale.

    :param gst: Instance de la classe GST.
    """
    print("\n--- TRAJET LE PLUS COURT ---")
    print(gst.ShortRout())


def main():
    """
    Fonction principale du programme.
    Gère le menu, les choix et l'exécution des commandes.
    """
    gst = GST()  # Instance principale de gestion

    while True:
        afficher_menu()
        choix = demander_entier("Votre choix : ")

        if choix == 1:
            ajouter_trajet(gst)

        elif choix == 2:
            print("\n--- LISTE DES TRAJETS ---")
            print(gst)

        elif choix == 3:
            rechercher_trajet(gst)

        elif choix == 4:
            supprimer_trajet(gst)

        elif choix == 5:
            sauvegarder_trajet(gst)

        elif choix == 6:
            afficher_plus_court(gst)

        elif choix == 0:
            print("\n👋 Merci d'avoir utilisé GST. À bientôt !")
            break

        else:
            print("⚠ Choix invalide. Veuillez réessayer.\n")


if __name__ == "__main__":
    main()
