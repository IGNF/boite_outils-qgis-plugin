from PyQt5.QtCore import Qt, QTimer
from qgis.gui import QgsHighlight


def clignoter_feature(layer, feature, canvas, duree=1000, intervalle=300):
    """
    layer : QgsVectorLayer contenant la feature
    feature : QgsFeature à faire clignoter
    canvas : QgsMapCanvas
    duree : durée totale du clignotement en ms
    intervalle : intervalle entre visible/invisible en ms
    """
    highlight = QgsHighlight(canvas, feature.geometry(), layer)
    highlight.setColor(Qt.yellow)
    highlight.setWidth(5)

    # pour clignoter
    timer = QTimer()
    compteur = 0
    max_count = duree // intervalle
    def toggle():
        nonlocal compteur
        highlight.setVisible(not highlight.isVisible())
        compteur += 1
        if compteur >= max_count:
            highlight.hide()
            timer.stop()

    timer.timeout.connect(toggle)
    timer.start(intervalle)