# Použití

Do editačního menu se lze dostat pomocí dodatku do url, kdy se za jazyk dosadí `/?edit`. Následuje přihlášení superusera. Django CMS obsahuje dva módy (Draft a Published), ten první je na upravování věcí a není vidět veřejností. Jakmile jsou změny dokončeny, pomocí publikace se změny projeví veřejnosti.

Stránka se skládá z pluginů. Struktura těchto pluginů je vidět po stisknutí tlačítka vpravo nahoře. V tomto menu lze pluginy přidávat, editovat a mazat.

# MERKIT

#### Link

Plugin `Merkit Navbar Plugin` obsahuje styl navbaru, aby mohly být odkazy viditelné, je potřeba mu udělat dítě `Merkit Link Plugin`. Následě u každých dalších pluginů je potřeba zaškrtnout `Show link` a vyplnit `Link Title` (tento text se objeví v navbaru jako odkaz) a `Link href` (ID sekce na kterou se bude odkaz odkazovat). Pro objevení stránky je nutné v stromu stránek zaškrtnout `Menu`, stejně jako u klasických Django CMS navigačních stromů.

#### Služby

Jelikož stránka podporuje vytvoření více služeb než je povoleno zobrazit (3), je vše zahrnuto v pluginu `Merkit Service List Plugin`. Na tento plugin se lze odkazovat v navbaru. Do tohoto pluginu lze jako děti přidat jednotlivé služby pomocí pluginu `Merkit Service Plugin`. Tento plugin obsahuje pole `Name`, podle kterého lze pak vybrat, zda se zobrazí nebo ne. Po vytvoření pluginu je potřeba jej ještě zvolit v menu pod titulkem `Merkit Service List Plugin`, které se objeví pouze v Draft módu. Každá služba může mít jako dítě ještě detail služby (produkt). Tento plugin se nazývá `Merkit Service Detail Plugin`. Pokud je služba zvolena k zobrazení, zobrazí se i příslušný detail.

#### Kontakt

Kontaktní formulář zasílá email na vybranou emailovou adresu. Tato adresa se nastaví v správy, v záložce `Global preferences`. Pokud adresa není nastavena, email se pošle sám sobě, tedy bude na emailové adrese, která posílá email. 

# Deploy

Pro deploynutí jsou připraveny 2 scripty (`config.sh` a `simple_deploy.sh`). `simple_deploy.sh` by měl být zapnut ve virtuálnim prostředí. Jediné, co je potřeba vyplnit je `config.sh`, jeho pole jsou:
- GIT_REPO - odkaz k git repozitáři
- DIR - složka do které chceš clonovat/pullnout git
- REPO_DIR - upřesnění v git repozitáři, kde se nachází Django projekt
- REQUIREMENTS - v jakém filu se nachází requirements, většinou `requirements.txt`
- CONFIG - do jakého filu se má uložit nastavení, klasicky `.env`

- IP - jaké IP adresy jsou povoleny, musí obsahovat IP adresu na kterém web běží a zároveň jeho DNS, např. `IP = "['127.0.0.1','mujweb.cz','www.mujweb.cz']"`

- DATABASE_ENGINE - engine databáze, např. `django.db.backends.postgresql_psycopg2`
- DATABASE_NAME - jméno databáze
- DATABASE_USER - uživatel databáze
- DATABASE_PASSWORD - heslo databáze
- DATABASE_HOST - host databáze

- RECAPTCHA_PUBLIC_KEY - veřejný klíč recaptchy
- RECAPTCHA_PRIVATE_KEY - soukromý klíč recaptchy

- EMAIL_HOST_USER - email, ze kterého contact form posílá emaily
- EMAIL_HOST_PASSWORD - jeho aplikační heslo

- PYTHON_VERSION - verze python, klasicky `3`

Script updatuje git, vyplní příslušné nastavení stránky, nastaví databázi, recaptchu, email a zajistí správu Djanga, jako je migrace, překlad a posbírání static filů. Během spuštění lze vytvořit superusera. Aby se změny projevily na stránce, je potřeba ještě restartovat service. Toto script neřeší.

Pro změnu `.env` souboru scriptem je potřeba celý adresář vymazat a spustim script načisto.
