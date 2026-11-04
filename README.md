# Légszennyezettségi Adatfelemző Projekt (Air Quality Analysis)

Ez a Python-projekt egy légszennyezettségi adatsor (`air_quality_dataset.csv`) átfogó statisztikai és vizuális elemzését végzi el a `pandas`, `numpy` és `matplotlib` könyvtárak segítségével.

A program 5 összetett analitikai kérdésre ad választ a terminálban szövegesen, valamint egy közös elrendezésben 5 grafikont jelenít meg.


## Használt Teknológia és Könyvtárak

- **Python 3.2**
- **Pandas**: Adatkezelés, adattisztítás, csoportosítás és gördülő átlagok.
- **NumPy**: Matematikai számítások, Z-score, átlag- és szórásszámítás.
- **Matplotlib**: Grafikonok és kördiagramok rajzolása.
- **OS**: Dinamikus fájlútvonal-kezelés


## Telepítés és Futtatás

1. Győződj meg róla, hogy a `air_quality_dataset.csv` adatfájl és a Python kód ugyanabban a mappában található.
2. Telepítsd a szükséges csomagokat a terminálban:
   ```bash
   pip install pandas numpy matplotlib
   ```
   
## A 5 Vizsgált Szempont Részletes Magyarázata

### 1. Vizsgált Szempont: PM2.5 / PM10 Arány (Szennyezettségi Szintek Szerint)
  A kód kiszámolja a veszélyes finompor (PM2.5) és a durvább szállópor (PM10) hányadosát (`PM2.5 / PM10`). Ezután a levegőminőségi értékeket 4 egyenlő kategóriára osztja: *Tiszta*, *Mérsékelt*, *Szennyezett*, és *Erősen szennyezett*.
  Megmutatja, hogy a teljes porszennyezésből mekkora arányt képvisel a legkisebb, tüdőbe lejutó porszemcse.


### 2. Vizsgált Szempont: Z-Score és Anomália-detektálás
  A NumPy segítségével kiszámoljuk a PM2.5 értékek átlagát és szórását, majd minden egyes mérési pontra kiszámítjuk a Z-score értéket:
  Ha a Z-score absolute értéke nagyobb 3-nál, azt extrém mérésnek/anomáliának tekintjük.
  - **Negatív Z-score (pl. -1, -2):** Az átlagnál lényegesen tisztább, alacsonyabb szennyezettségű napokat jelöli (a tengely ezért indul -2-ről).
  - **0 Z-score:** Az átlagos napokat jelöli.
  - **Pozitív Z-score (pl. +1, +2, +3):** Az átlagnál szennyezettebb napokat jelöli.


### 3. Vizsgált Szempont: Rövid és Hosszú Távú Levegőminőség (Gördülő Átlagok)

  Az eljárással kiszámolunk egy **30 napos** és egy **1 éves** gördülő átlagot a napi PM2.5 értékekre.
  A napi mérésekben sok a véletlenszerű ingadozás ("zaj"). A gördülő átlag kisimítja ezeket a tüskéket:
  - **30 napos átlag (piros):** A rövid távú, hetente fellépő változásokat mutatja.
  - **1 éves átlag (kék):** A hosszabb távú, szezonális trendeket ábrázolja.


### 4. Vizsgált Szempont: Hibás Adatok Feltöltése
  A szemléltetés érdekében a CSV-ben mesterséges hiányok lettek létrehozva, majd a hiányzó cellákat a meglévő adatok **mediánjával** tölti fel.
  Megmutatja, hogy az adathiányok pótlása hogyan módosítja a statisztikai mutatókat


### 5. Vizsgált Szempont: Az 5 Fő Szennyezőanyag Aránya (Kördiagram)

  Kiszámolja az 5 kulcsfontosságú légszennyező gáz és por (`PM2.5`, `PM10`, `NOx`, `NO2`, `SO2`) átlagos koncentrációját, és azok egymáshoz viszonyított százalékos arányát.
