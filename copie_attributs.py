import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QBrush
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView
from PyQt5.uic import loadUi

from .constantes import *
COLOR_LIGNE_COMMUNE = "#46a200"
COLOR_LIGNE_DIFF = "#dfdfdf"

class CopieAttributsDialog(QDialog):
    def __init__(self, parent=None,iface=None):
        self.layer = None
        self.iface = iface
        self.selection_order = []  # Liste pour stocker l'ordre de sélection des entités

        super().__init__(parent)
        ui_path = os.path.join(os.path.dirname(__file__), "dial", "copie_attributs.ui")
        loadUi(ui_path, self)

        self.label_nbsel.setStyleSheet("color: red;font-weight: bold;")

        self.layer = self.iface.activeLayer()
        if self.layer and self.layer.type() == self.layer.VectorLayer:
            self.iface.currentLayerChanged.connect(self.on_layer_changed)
            # ne se declenche pas si changement de couche
            self.layer.selectionChanged.connect(self.actualiserSelection)
            self.actualiserSelection([], [], False)

        self.pushButton_copier.clicked.connect(self.copier_attributs)

        self.ini_tabwidget()

    def on_layer_changed(self,layer):
        self.layer = layer
        self.selection_order = []
        self.actualiserSelection()

        if self.layer and self.layer.type() == self.layer.VectorLayer:
            # Déconnecte les anciens signaux pour éviter les doublons
            try:
                self.layer.selectionChanged.disconnect(self.actualiserSelection)
            except TypeError:
                pass
            # Reconnecte le signal sur la nouvelle couche
            self.layer.selectionChanged.connect(self.actualiserSelection)

            # Mise à jour immédiate si la nouvelle couche a déjà une sélection
            if self.layer.selectedFeatureCount() > 0:
                self.actualiserSelection([], [], False)


    def ini_tabwidget(self):
        self.tableWidget.verticalHeader().setDefaultSectionSize(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setHorizontalHeaderLabels(["Champs", "Objet référence", "Objets cibles"])

        # Personnaliser les headers : rouge et gras
        header_font = QFont()
        header_font.setBold(True)
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.horizontalHeaderItem(col)
            item.setFont(header_font)
            item.setForeground(QBrush(QColor("black")))
            item.setBackground(QColor("#9b9b9b"))

        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet(STYLE_TABLEWIDGET[0])
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    def get_champs(self):
        # Récupérer les champs de la couche active
        if not self.layer:
            return []
        return [field.name() for field in self.layer.fields() if field.name() not in CHAMPS_INTERDIT]

    def get_first_selected_feature(self):
        if not self.layer:
            return None
        # Si aucune sélection, on retourne le premier element vraiment sélectionné
        if not self.selection_order:
            selected_features = self.layer.selectedFeatures()
            if not selected_features:
                return None
            return selected_features[0]

        # Récupère le premier fid dans l'ordre de sélection
        first_fid = self.selection_order[0]
        # Récupère la feature correspondant à ce fid
        feature = next((f for f in self.layer.selectedFeatures() if f.id() == first_fid), None)
        return feature


    def get_other_selected_features(self):
        if not self.layer:
            return []
        if not self.selection_order:
            return []
        # On récupère tous les fids sauf le premier
        other_fids = self.selection_order[1:]
        # Récupérer les features correspondant aux fids restants
        selected_features = self.layer.selectedFeatures()
        other_features = [f for f in selected_features if f.id() in other_fids]
        return other_features

        # selected_features = self.layer.selectedFeatures()
        # if not selected_features:
        #     return []
        # # retourne tout sauf le premier
        # return selected_features[1:]

    def get_attributs_commun(self, list_entites):
        # if not list_entites or len(list_entites) == 1
        if not list_entites:
            return {}
        champs = self.get_champs()
        attributs_commun = {}
        for champ in champs:
            valeur_champ = list_entites[0][champ]
            if all(entite[champ] == valeur_champ for entite in list_entites):
                attributs_commun[champ] = valeur_champ
            else:
                attributs_commun[champ] = "****"
        return attributs_commun

    def get_ordre_selection(self,selected, deselected, clear_and_select):
        for fid in selected:
            if fid not in self.selection_order:
                self.selection_order.append(fid)
        # retirer les entités désélectionnées
        for fid in deselected:
            if fid in self.selection_order:
                self.selection_order.remove(fid)


    def actualiserSelection(self, selected=None, deselected=None, clear_and_select=None):
        if not self.isVisible():
            return

        if selected is None:
            selected = []
        if deselected is None:
            deselected = []
        if clear_and_select is None:
            clear_and_select = False
        if self.layer is None:
            self.layer = self.iface.activeLayer()
        if self.layer is None:
            return

        self.get_ordre_selection(selected, deselected, clear_and_select)

        nb_sel = self.layer.selectedFeatureCount()
        self.label_nbsel.setText(f"Sélection : {nb_sel}")
        if nb_sel <2:
            self.tableWidget.setRowCount(0)
            return
        champs = self.get_champs()

        self.tableWidget.setRowCount(len(champs))
        self.tableWidget.clearSelection()

        attributs_commun = self.get_attributs_commun(self.get_other_selected_features())


        for i, champ in enumerate(champs):
            item_champ = QTableWidgetItem(champ)
            # item_champ.setBackground(QColor(COLOR_LIGNE_DIFF))
            item_first = QTableWidgetItem(str(self.get_first_selected_feature()[champ]))
            # item_first.setBackground(QColor(COLOR_LIGNE_DIFF))
            item_autre = QTableWidgetItem(str(attributs_commun[champ]))

            if self.get_first_selected_feature()[champ] != attributs_commun[champ]:
                self.tableWidget.selectRow(i)
            # else:
                # item_autre.setBackground(QColor(COLOR_LIGNE_DIFF))


            self.tableWidget.setItem(i, 0, item_champ)

            self.tableWidget.setItem(i, 1, item_first)
            self.tableWidget.setItem(i, 2, item_autre)

    def copier_attributs(self):
        print("sel order = ",self.selection_order)
        # TODO : ne pas copier les attributs en lecture seuls.
        # gerer la selection de la ligne entiere
        # par defaut les lignes vertes sont considerés comme sélectionnées
        # si on selectionne d'aitres lignes , faut les passer en vert

