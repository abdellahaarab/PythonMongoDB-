"""
logic.py
--------

Module de gestion des routes (trajets) avec MongoDB.
La classe GST fournit des méthodes professionnelles pour :

- Ajouter un trajet
- Afficher tous les trajets
- Rechercher par ville de départ
- Supprimer par nom
- Sauvegarder un trajet dans fichier texte
- Trouver le trajet avec la distance minimale

Auteur : Abdellah
Version : Pro
"""

from pymongo import MongoClient
from pymongo.collection import Collection


class GST:
    """
    Classe GST permettant la gestion des trajets dans une base MongoDB.
    """

    def __init__(self, db_name: str = "routs", collection_name: str = "rout") -> None:
        """
        Constructeur :
        Initialise la connexion MongoDB et sélectionne la base + collection.

        :param db_name: Nom de la base MongoDB.
        :param collection_name: Nom de la collection MongoDB.
        """
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.col: Collection = self.db[collection_name]

    # ----------------------------------------------------------------------
    # AJOUT
    # ----------------------------------------------------------------------
    def Ajouter(self, tb: dict) -> None:
        """
        Ajoute un trajet dans la base.

        :param tb: Dictionnaire contenant les champs :
                   nom, dist, viled, vileA
        """
        self.col.insert_one(tb)

    # ----------------------------------------------------------------------
    # AFFICHAGE
    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        """
        Retourne une chaîne formatée de tous les trajets.

        :return: String listant tous les trajets.
        """
        res = list(self.col.find({}))

        if not res:
            return "⚠ Aucun trajet disponible dans la base."

        output = "\n===== LISTE DES TRAJETS =====\n"
        for x in res:
            output += (
                f"\nNom : {x.get('nom')}"
                f"\nDistance : {x.get('dist')}"
                f"\nVille Départ : {x.get('viled')}"
                f"\nVille Arrivée : {x.get('vileA')}\n"
                "------------------------------\n"
            )

        return output

    # ----------------------------------------------------------------------
    # RECHERCHE
    # ----------------------------------------------------------------------
    def rechercher(self, viled: str) -> str:
        """
        Recherche les trajets ayant une ville de départ donnée.

        :param viled: Ville de départ recherchée.
        :return: Tous les trajets correspondants formatés.
        """
        res = list(self.col.find({"viled": viled}))

        if not res:
            return "⚠ Aucun trajet trouvé pour cette ville de départ."

        output = f"\n=== TRAJETS DÉPART {viled.upper()} ===\n"
        for x in res:
            output += (
                f"\nNom : {x.get('nom')}"
                f"\nDistance : {x.get('dist')}"
                f"\nVille Départ : {x.get('viled')}"
                f"\nVille Arrivée : {x.get('vileA')}\n"
                "--------------------------\n"
            )

        return output

    # ----------------------------------------------------------------------
    # SUPPRESSION
    # ----------------------------------------------------------------------
    def suprimer(self, nom: str) -> str:
        """
        Supprime un trajet à partir de son nom.

        :param nom: Nom du trajet à supprimer.
        :return: Message de confirmation ou d’erreur.
        """
        result = self.col.delete_one({"nom": nom})

        if result.deleted_count > 0:
            return "✔ Trajet supprimé avec succès."
        return "⚠ Aucun trajet trouvé avec ce nom."

    # ----------------------------------------------------------------------
    # SAUVEGARDER DANS FICHIER
    # ----------------------------------------------------------------------
    def Sauvgarder(self, nom: str) -> str:
        """
        Récupère un trajet et retourne son format texte.

        :param nom: Nom du trajet.
        :return: Contenu formaté pour sauvegarde.
        """
        x = self.col.find_one({"nom": nom})

        if not x:
            return "⚠ Trajet introuvable."

        return (
            f"Nom : {x.get('nom')}\n"
            f"Distance : {x.get('dist')}\n"
            f"Ville Départ : {x.get('viled')}\n"
            f"Ville Arrivée : {x.get('vileA')}\n"
        )

    def sof(self, nom: str) -> None:
        """
        Sauvegarde un trajet dans un fichier .txt.

        :param nom: Nom du trajet à sauvegarder.
        """
        content = self.Sauvgarder(nom)
        with open(f"{nom}.txt", "w", encoding="utf-8") as file:
            file.write(content)

    # ----------------------------------------------------------------------
    # PLUS COURTE DISTANCE
    # ----------------------------------------------------------------------
    def ShortRout(self) -> str:
        """
        Retourne le trajet ayant la plus petite distance.

        :return: Chaîne formatée contenant le trajet minimum.
        """
        shortest = self.col.find_one({}, sort=[("dist", 1)])

        if not shortest:
            return "⚠ Aucun trajet disponible."

        return (
            "\n===== TRAJET LE PLUS COURT =====\n"
            f"Nom : {shortest.get('nom')}\n"
            f"Distance : {shortest.get('dist')}\n"
            f"Ville Départ : {shortest.get('viled')}\n"
            f"Ville Arrivée : {shortest.get('vileA')}\n"
            "================================\n"
        )
