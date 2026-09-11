from models.subject import Sujet


DUREE_TRAVAIL = 25 * 60
DUREE_PAUSE = 5 * 60


class Minuteur(Sujet):

    def __init__(self):
        super().__init__()
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"   # "Travail" ou "Pause"
        self._sessions_completees = 0

    def tick(self) -> None:
        """Avance le minuteur d'une seconde et notifie les observateurs."""
        # À compléter :
        # 1. Si en pause, ne rien faire
        if self._en_pause:
            return
        # 2. Si temps_restant > 0, décrémenter
        if self._temps_restant > 0:
            self._temps_restant -= 1
        # 4. Notifier les observateurs
        self.notifier_observateurs()
        # À compléter :
        # Si état == "Travail" : incrémenter sessions, passer en "Pause", reset temps
    def changer_etat(self) -> None:
        if self._etat == "Travail" and self._temps_restant == 0:
            self._sessions_completees += 1
            self._etat = "Pause"
            self._temps_restant = DUREE_PAUSE
        # Sinon : passer en "Travail", reset temps
        elif self._etat == "Pause" and self._temps_restant == 0:
            self._etat = "Travail"
            self._temps_restant = DUREE_TRAVAIL

    def basculer_pause(self) -> None:
        """Met en pause ou reprend le minuteur."""
        # À compléter
        self._en_pause = not self._en_pause
        pass

    def reinitialiser(self) -> None:
        """Réinitialise le minuteur à l'état initial et notifie les observateurs."""
        # À compléter
        self._temps_restant = DUREE_TRAVAIL
        self._en_pause = False
        self._etat = "Travail"
        self._sessions_completees = 0

        # N'oubliez pas de notifier les observateurs à la fin
        self.notifier_observateurs()
        pass

    def get_donnees(self) -> dict:
        # À compléter : retourner un dictionnaire avec :
        dict(
            temps_restant=self._temps_restant,
            etat=self._etat,
            en_pause=self._en_pause,
            sessions_completees=self._sessions_completees,
            duree_totale=DUREE_TRAVAIL + DUREE_PAUSE
        )

        pass
