TITRE = "Boite à outils"
CLEABS = "cleabs"

PLUGIN_LISTE = "IGN_assistant-liste"

CHAMPS_INTERDIT = ["id_sqlite_1gnQg1s","gcms_fingerprint"]

# COLOR_LIGNE_COMMUNE = "#46a200"
# COLOR_LIGNE_DIFF = "#dfdfdf"
HAUTEUR_BTN = 30

# style des lignes sélectionnées
# STYLE_TABLEWIDGET = ["""QTableWidget::item:selected {background-color: #46a200;}"""]
STYLE_TABLEWIDGET = ["""QTableWidget::item:selected {background-color: #ff9f28;}"""]

# 0  : pas de bordure, pas de marge, pas de padding
# 1
CUSTOM_WIDGET = ["""QTabWidget::pane {border: 0px;margin: 0px;padding: 0px;}
                 QTabBar::tab {background: lightblue;color: black;padding: 5px;border: 1px solid gray;}
                    QTabBar::tab:selected {background: #44a3c3;color: white;}"""
                 ]