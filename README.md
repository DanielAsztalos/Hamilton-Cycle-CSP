# Hamilton-Cycle-CSP

## Feladat leírása

Adott egy N csomópontból és M élből álló gráf. Határozzuk meg, hogy tartalmaz-e Hamilton kört.<br/>
Hamilton kör: egy olyan csomópont sorozat, ami tartalmazza a gráf összes csomópontját egyetlen egyszer úgy, hogy az első és utolsó pont között létezik él.

## Program leírása

Használt Python verzió: 3.6<br/>
Külső csomag: numpy - installálása: pip install numpy<br/>
Program meghívása:
```
python hamilton.py [n] [x]
```
n - a generálandó gráf mérete<br/>
x - a megoldási módszer:
- backtracking
- backtracking + MVR + FC
- backtracking + MVR + AC3
                         
## Eredmények

Előre leszögezett 5 csomópontból álló gráfra<br/>
  - ha tartalmaz Hamilton kört: 
    1. 52 értékadás
    2. 9 értékadás
    3. 
  - ha nem tartalmaz Hamilton kört:
    1. 781 értékadás
    2. 54 értékadás
