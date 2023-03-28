# Naloga 1: Razvoj enostavne napovedne storitve

## Opis naloge
V sklopu naloge boste z uporabo programskega jezika Python razvili REST spletno storitev za napovedovanje onesnaženosti zraka. Napovedna storitev mora temeljiti na poljubnem algoritmu strojnega učenja (namig: spomnite se vaj iz predmeta RIRSU).

## Vzpostavitev okolja
Razvojno okolje naj zajema sledeče:
- Verzioniranje programske kode (uporabite GitHub platformo)
    - Definirajte tudi .gitignore
- Poetry za upravljanje s knjižnicami
    - Namestite knjižnice za izvajanje razvite programske kode (pandas, scikit-learn, flask...)
    - Namestite knjižnice za pomoč pri razvoju (pytest)
    - Opcijsko lahko dodate v poetry tudi vtičnik poe, za pomoč pri zagonu opravil s poetry
- Pripravite sledečo strukturo projekta:

├── README.md <- Datoteka z opisom projekta in navodili za vzpostavitev okolja in zagon skript

├── data

    ├── processed <- Procesirani podatki, pripravljeni za učenje

    └── raw <- Prenešeni podatki v originalni obliki

├── models <- Naučeni in serializirani modeli, napovedi modelov ali povzetki modelov

├── notebooks <- Jupyter zvezki

├── reports <- Generirane datoteke analiz

    └── figures <- Generirani grafi in slike, uporabljene pri analizi

├── pyproject.toml <- Datoteka, ki definira odvisnosti, verzije knjižnic...

├── src <- Izvorna koda projekta

    ├── __init__.py <- Ustvari direktorij "src" kot Python module

    ├── data <- Skripte za prenos, procesiranje, itd. podatkov

    ├── models <- Skripte za učenje napovednih modelov in uporabo modelov za napovedovanje

    ├── serve <- Skripte za serviranje modelov v obliki spletnih storitev

    └── visualization <- Skripte za vizualizacijo
## Podatki
- Podatke za namen učenja napovednega modela pridobite tukaj.
- Podatke pridobite programsko (spišite skripto fetch_data.py), jih uredite in pripravite za učenje napovednega modela.
- Neobdelane prenešene podatke shranite v mapo "data/raw", procesirane oz. pripravljene za učenje pa v mapo "data/processed".
## Napovedni model
- Naučite napovedni model (skripta train_model.py), ki bo na podlagi prejetih podatkov za izbran kraj skušal čim bolje napovedati (skripta predict_model.py) vrednost parametra (pm10).
- Naučen model shranite v mapo "models".
- V datoteko "reports/train_metrics.txt" shranite vrednosti metrik nad učnimi podatki, v datoteko "reports/metrics.txt" pa vrednosti metrik na testnimi podatki.
## Spletna storitev
- Cilj naloge je naloge je naučen napovedni model izpostaviti v obliki REST API spletne storitve.
- Za pomoč pri razvoju lahko uporabite kateregakoli izmed Python ogrodij za razvoj spletnih storitev (flask, FastAPI...).
- Potrebno je implementirati REST končno točko s sledečimi specifikacijami:
    - POST: /air/predict/ - V telesu zahtevka prejme podatke v obliki, ki jo sami definirate
    - Odgovor storitve naj bo v sledeči JSON obliki:
    {"prediction": 22}
- Razvito spletno storitev testirajte z uporabo orodja Postman ali katerim izmed podobnih orodij.
- Za razvito spletno storitev osnovne teste (pytest), ki se naj ob vsakem "pushu" na GitHub samodejno izvedejo (GitHub Actions).
- Končno razvito rešitev zapakirajte v obliko Docker slike.

primer poslanega json request:

            {
                "no2":36.255351616,
                "pm2.5":78.0,
                "o3":44.0,
                "leto_od":2023.0,
                "mesec_od":2.0,
                "dan_od":15.0,
                "ura_od":19.0,
                "min_od":0.0,
                "leto_do":2023.0,
                "mesec_do":2.0,
                "dan_do":15.0,
                "ura_do":20.0,
                "min_do":0.0
            }

            {
                "pm2.5": 8.0,
                "o3": 57.0,
                "no2": 25.0,
                "temps": 11.3
            }

{\"no2\":22,\"pm2.5\":35,\"nadm_visina\":56,\"datum_od\":\"2023-02-24 15:00\",\"merilno_mesto\":\"Koper\",\"o3\":35,\"ge_sirina\":45.54329,\"pm10\":46,\"sifra\":\"E423\",\"datum_do\":\"2023-02-24 16:00\",\"ge_dolzina\":13.718135}

dvc add data\processed\merged.csv
git add data\processed\merged.csv.dvc
git commit -m "test s data"
dvc push
dvc pull

Avtomatsko dodano:- Avtomatsko dodano iz fetch air data
- Avtomatsko dodano iz fetch air data

## Vaja 4
- great_expetations init 
- y
- great_expetation datasource new
- 1
- 1 pandas
- data\processed
- se odpre jupyter notebook
- cell>run all
- mas konfiguracijo v great_expetations.yml
- lahko ustavis notebook

- great_expetations suite new
- 3 data assist
- (izberes reference data) 
- lahko poimenujes
- odpre notebook
- zakomentiamo vse stolpce ker zelimo da vse pregleda ali zbrisemo 
- cell run all
- odpre avtomatsko dokumentacijo
- se ti zgenerira json in lahko spreminjas vrednosti not npr max_value: null

- great_expetations checkpoint new my_checkpoint
- notebook
- nastavis data_asset_name: current_data.csv 
- (lahko odkumentiramo da zazene checkpoint in odpre report)
- run all

- lahko zbrises tota zelo stroga pravila 
- popravis preko edit suite

- generate python script to trigger checkpoint
- great_expetations checkpoint script my_checkpoint (ime checkpointa)
- v uncommitted imamo run_my_checkpoint.py 
- moremo spremenit context_root_dir
- prestavi si jo nekak npr expetations ker uncommitted je ignore

------

- na dagshub remote experiments
- mlflow 
- train_model moremo dopolnit s mlflow knjiznico
- mores ustvarit train.csv in test.csv
- import mlflow
- copy tracking uri from remote experiment das v ""
- mlflow.set_tracking_uri()
- mlflow.set_experiment("ime") pogledas na dagshub
- mlflow.sklearn.autolog() ali mlflow.autolog()(avtomatsko logiranje)
- ce dodamo not parameter exclusive=False dodamo se da je rocno
- damo vse v with mlflow.start_run()
- dodamo not lastne metroce mlflow.log_metric("name ali key", value)
- na koncu izven start_run() imamo autolog_run= mlflow.last_active_run()
- ce rocno pozenemo python src/models/train_model.py pride do tezave ker nimamo mlflow_tracking s dasghub
- preden pozenemo dodamo setx PATH "name:value"
- mlflow credentials python ali mlflow authentications python


