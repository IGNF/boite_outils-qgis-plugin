<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/image1.jpeg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="font-size: 24px;text-align: center;"><p><strong>Manuel utilisateur du plugin
« Boîte à outils »</strong></p>
<p><strong>V0.2.1</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>


## Sommaire

- [1. Prérequis](#prerequis)

- [2. Résumé](#resume)

- [3 Présentation](#presentation)

- [4 Onglet « Topo »](#onglet-topo)

	- [4.1 Fusion](#fusion)

	- [4.2 <img src="images/image2.png" style="width:0.62509in;height:0.3438in" />](#section)

- [5 Onglet « Attr »](#onglet-attr)

	- [5.1 Copie d’attributs](#copie-dattributs)

- [6 Recherche](#recherche)

	- [6.1 « Recherche par CLEABS »](#recherche-par-cleabs)

	- [6.2 « Recherche »](#recherche_1)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>

- Version de QGIS : 3.28 ou supérieur

- Le plugin « maitre » doit préalablement être installé : 
[maitre-qgis-plugin sur GitHub](https://github.com/IGNF/maitre-qgis-plugin)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="resume" style="color: white;margin:0;" >2. Résumé</h2>
</div>

Ce plugin regroupe diverses fonctionnalités accessibles via des onglets

- Topologie (fusion d’entités, mode d’accrochage des sommets pour
  déplacer des entités)

- Attr (copie d’attributs d’une entité à un autre)

- Recherche (recherche par cleabs, recherche via des requêtes sql)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >3. Présentation</h2>
</div>

<img src="images/image3.png"
style="width:2.78164in;height:1.37519in" />

Chaque onglet regroupe plusieurs fonctionnalités


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="onglet-topo" style="color: white;margin:0;" >4. Onglet « Topo »</h2>
</div>


<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="fusion" style="color: white;margin:0;" >4.1 Fusion</h2>
</div>

Pas encore implémenté

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="via" style="color: white;margin:0;" >4.2	<img src="images/image2.png" style="width:0.62509in;height:0.3438in" /></h2>
</div>

C’est un outil « d’accrochage »

<img src="images/image2.png"
style="width:0.62509in;height:0.3438in" /> : Accrochage désactivé

<img src="images/image4.png"
style="width:0.63135in;height:0.35075in" /> : Accrochage activé

On a une entité sélectionnée et elle partage un même sommet avec
d’autres entités dans QGIS :

- Lorsque l’accrochage est désactivé :

Le déplacement du sommet commun ne déplace que le sommet de l’objet
sélectionné.

- Lorsque l’accrochage est activé :

Le déplacement du sommet commun déplace ce sommet pour toutes les
entités.


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="onglet-attr" style="color: white;margin:0;" >5. Onglet « Attr »</h2>
</div>


<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="copie-dattributs" style="color: white;margin:0;" >5.1 Copie d’attributs</h2>
</div>

Cette interface permet la copie d’attributs d’une entité vers une ou
plusieurs autres.

<img src="images/image5.png"
style="width:4.15811in;height:2.62752in" />

<span class="mark">À l’ouverture, cette interface est vide. Elle
s’initialise dès lors qu’au moins deux entités sont sélectionnées.\
La première entité sélectionnée sert de référence, les autres
constituent les entités cibles.</span>

Attention à la sélection par rectangle, main levée ou polygone (l’objet
cible sera aléatoire).

Apres sélection de 2 entités :

<img src="images/image6.png"
style="width:5.77845in;height:3.65141in" />

En rouge : les champs en lecture seuls

En orange : les attributs différents entre l’entité de référence et
l’entité cible.

Apres sélection de plus de 2 entités :

<img src="images/image7.png"
style="width:6.45099in;height:4.07639in" />

Idem que pour la sélection de 2 entités sauf :

Les « \*\*\* » correspondent à des valeurs d’attributs différents entre
les entités cibles.

La copie ne s’effectue que sur les attributs en orange ;

Il est possible de sélectionner/désélectionner d’autres attributs.


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="recherche" style="color: white;margin:0;" >6. Recherche</h2>
</div>

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="recherche-par-cleabs" style="color: white;margin:0;" >6.1 « Recherche par CLEABS »</h2>
</div>

<img src="images/image8.png"
style="width:4.72983in;height:1.25017in" />

Cette recherche s’effectue de la CLEABS vers id QGIS

On renseigne une CLEABS et on clique sur « Recherche » :

<img src="images/image9.png"
style="width:4.72983in;height:1.25017in" />

L’entité correspondante est sélectionnée.

QGIS fait clignoter et zoom sur cette entité.

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="recherche_1" style="color: white;margin:0;" >6.2 « Recherche »</h2>
</div>

Pas encore implémenté
