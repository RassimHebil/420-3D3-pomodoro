import tkinter as tk
from observers.observer import Observateur


class AffichageTemps(Observateur):

    def __init__(self, parent):
        self._label = tk.Label(parent, text="25:00", font=("Arial", 48, "bold"))
        self._label.pack(pady=10)

    def actualiser(self, sujet) -> None:
        # À compléter :
        # Récupérez temps_restant depuis sujet.get_donnees()
        temps_restant = sujet.get_donnees()["temps_restant"]
        # Calculez minutes et secondes
        minutes = temps_restant // 60
        secondes = temps_restant % 60
        # Mettez à jour le label au format "MM:SS"
        self._label.config(text=f"{minutes:02d}:{secondes:02d}")
