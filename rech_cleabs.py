import os
from qgis.PyQt.QtWidgets import QDialog, QApplication
from qgis.PyQt.uic import loadUi
from qgis._core import QgsCoordinateTransform
from qgis.core import QgsProject
from .fonctions import *
from .mapping_version import *


class RechercheCleabsDialog(QDialog):
    def __init__(self, parent=None,iface=None):
        super().__init__(parent)
        self.iface = iface
        ui_path = os.path.join(os.path.dirname(__file__), "dial", "dial_recherche_cleabs.ui")
        loadUi(ui_path, self)

        self.lineEdit_id.setStyleSheet("color: None;font-weight: bold")
        self.lineEdit_cleabs.setStyleSheet("color: None;font-weight: bold")

        # Exemple : connecter le bouton à une méthode interne
        self.pushButton_recherche_cleabs.clicked.connect(self.on_btn_recherche_cleabs)

    def on_btn_recherche_cleabs(self):
        # IMPORTANT : un id est unique pour un layer, pas pour tous les layers du projet
        QApplication.setOverrideCursor(WaitCursor)

        # 1er cas : on connait la cleabs exemple : TRONROUT0000000010804221
        self.lineEdit_id.setText("")
        cleabs = self.lineEdit_cleabs.text()
        layer = self.iface.activeLayer()
        expr = f'"cleabs" = \'{cleabs}\''
        trouve = False
        layers = self.iface.mapCanvas().layers()
        for layer in layers:
            for feat in layer.getFeatures(expr):
                # selection de l'entité trouvée
                # layer.select(feat.id())

                # zomm sur l'entité trouvée
                self.zoom_entite(layer, feat.id(),0)

                # faire clignoter l'entité trouvée
                clignoter_feature(layer, feat, self.iface.mapCanvas(), duree=3000, intervalle=300)

                self.lineEdit_id.setStyleSheet("color: None;font-weight: bold")
                self.lineEdit_id.setText(str(feat.id()))
                trouve = True
                break
        if not trouve:
            self.lineEdit_id.setStyleSheet("color: red;font-weight: bold;")
            self.lineEdit_id.setText("Entité non trouvée")
        QApplication.restoreOverrideCursor()


    def zoom_entite(self,layer,entite_id,buffer):
        feature = layer.getFeature(entite_id)
        geom = feature.geometry()
        if geom is None or geom.isEmpty():
            return
        bbox = geom.boundingBox()
        if buffer:
            bbox.grow(buffer)
        # transformer si CRS différent
        if layer.crs() != self.iface.mapCanvas().mapSettings().destinationCrs():
            transform = QgsCoordinateTransform(layer.crs(), self.iface.mapCanvas().mapSettings().destinationCrs(),
                                               QgsProject.instance())
            bbox = transform.transformBoundingBox(bbox)
        self.iface.mapCanvas().setExtent(bbox)
        self.iface.mapCanvas().refresh()
