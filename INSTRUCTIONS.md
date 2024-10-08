Za pokretanje testova koristiti komandu:
```
python manage.py test prodavnice.tests --noinput
```
Svaki put se kreira nova test baza.

U ovom primeru koristi se Django modul za implementaciju web aplikacije koja čuva evidenciju o prodavnicama. Za ovaj primer potrebno je imati instaliran pip, setuptools, Django. Preporučljivo je instalirati Django u virtuelnom okruženju sa komandom
```
pip install Django
```
Za novi Django projekat pokrenuti komandu
```
django-admin startproject naziv_projekta
```
Za kreiranje inicijalne šeme baze podataka pokrenuti komandu
```
python manage.py migrate
```
Za admin aplikaciju treba kreirati superuser nalog komandom
```
python manage.py createsuperuser
```
Zatim treba kreirati aplikaciju komandom
```
python manage.py startapp naziv_aplikacije
```
Kada se izmeni models.py modul u direktorijumu prodavnice potrebno je pokrenuti komandu
```
python manage.py makemigrations prodavnice
```
da bi se dobile datoteke za kreiranje tabela u bazi. Sa dobijenim datotekama treba ponovo pokrenuti komandu
```
python manage.py migrate
```
da bi se kreirale nove tabela sa dobijenim datotekama za aplikaciju za rad sa prodavnicama.
Za popunjavanje tabela sa inicijalnim vrednostima pokrenuti komandu
```
python manage.py popuni_bazu
```
Server se moze pokrenuti komandom
```
python manage.py runserver
```
Preporučljivo je da se instaliranje vrši u posebnom virtualnom okruženju. Da bi mogli da koristite pip komandu mozete instalirati po uputstvu sa sajta

https://pip.pypa.io/en/stable/installing/

Zatim treba instalirati virtualenv alat komandom
```
pip install virtualenv
```
Kreirati novo virtualno okruženje koristeci komandu
```
virtualenv NAZIV_OKRUZENJA
```
Kreirano virtualno okruženje mozete aktivirati komandom

Za Linux
```
source NAZIV_OKRUZENJA/bin/activate
```
Za Windows
```
NAZIV_OKRUZENJA\Scripts\activate
```
Da bi se ovaj primer mogao pokrenuti potrebno je postaviti putanju do python interpretera virtuelnog okruženja u PyCharm razvojnom okruženju tako što se ode na File -> Settings, pronaći prikaz Project:prodavnicesajt->Project Interpreter i otići na settings dugme i izabrati opciju Add... u prozoru koji se otvori, sa leve strane izabrati opciju Virtualenv Environment, a sa desne strane izabrati opciju Existing Environment i pronaći putanju gde je kreirano virtuelno okruženje i izabrati python interpreter.

Za Linux
```
NAZIV_OKRUZENJA/bin/python
```
Za Windows
```
NAZIV_OKRUZENJA\Scrpits\python.exe
```
Ovaj primer se može pokrenuti iz PyCharm razvojnog okruženja, ali potrebno je za manage.py modul napraviti posebnu konfiguraciju tako sto se ode na: Run -> Edit configurations. Napravi se nova Python konfiguracija i za polje Script: se izabere manage.py modul. Script parameters: se upise: runserver.
