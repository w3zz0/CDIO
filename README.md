# Gruppe 21 - CDIO (62410) 2023 - Lego Mindstorm EV3

Vi har valgt at gå med en server/client arkitektur, hvor robotten fungere som serveren og pc'en som klienten, de bliver forbundet
over et fælles netværk de begge er på igennem ssh 

Vi har valgt at gå med en server/client arkitektur i vores projekt. I projektet fungerer Lego Mindstorm EV3-robotten som serveren,
og en PC som klienten. Forbindelsen mellem serveren og klienten etableres via et fælles netværk, som begge enheder er forbundet til.

Vi har brugt SSH (Secure Shell) protokollen til at kommunikere og styre robotten fra klienten.

"ssh robot@xxx.xx.xx.x"
password: maker

Efter at have udarbejdet server mappen, konverter vi denne til en .zip fil som vi så overfører til robotten vha. SCP (Secure Copy Protocol), efter at have overført .zip filen kan vi unzip denne.

Overførelse af .zip filen
"scp /Users/user/Desktop/CDIO/Server.zip robot@xxx.xx.xx.x:"
password: maker

Unzippe og tilgå Server mappen
"unzip Server.zip"
"cd Server"

Påbegyndelse for serveren
"python3 MainServer.py"

Påbegyndelse for klienten
"python3 MainClient.py"


I mappen '1. ORIGINAL-CODE' ligger vores tidligere kode, dette var oprindeligt koden vi ville have brugt, desværre fik et gruppe medlem ikke lavet sin del af koden i tids nok, og droppede desværre helt af fra projektet 1 uge inden konkurrencedagen. Vi i gruppen prøvede at samarbejde om at færdiggør personens del, dog uden held, vi blev derfor enige om at lave projektet om, så vi i det mindste havde en fungerende robot der kunne kører og samle bolde op, vi måtte derfor ditche ideen om brug af kamera til genkendelse og i stedet falde tilbage på sensorer, projektet blev ikke hvad vi havde håbet på, vi er dog glad for vi i det mindste kunne vise en server/client arkitektur og en fungerende robot der virkede ift. inputtet den fik.





