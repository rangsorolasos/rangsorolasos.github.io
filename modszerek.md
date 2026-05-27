# Miért nem mindegy, hogyan szavazunk?

Képzeljük el, hogy tizenegy ember szeretne találkozót szervezni, de három különböző időpont közül kell választaniuk. Első ránézésre ez egyszerű problémának tűnik: megszámoljuk, melyik időpontra szavaztak a legtöbben, és kész.

A valóságban azonban a „legtöbb szavazat” sokféleképpen értelmezhető. Számít, hogy mindenki csak egyetlen időpontot jelölhet-e meg, vagy többet is. Az is számít, hogy a résztvevők pusztán elfogadhatónak tartanak egy időpontot, vagy valóban azt szeretnék legjobban.

A modern szavazáselmélet egyik legérdekesebb felismerése éppen az, hogy különböző szavazási rendszerek ugyanabból a véleményhalmazból teljesen eltérő eredményt hozhatnak ki. Sőt, bizonyos helyzetekben egy intuitívan rossz eredmény nyerhet, miközben egy kompromisszumosabb lehetőség háttérbe szorul.

A választási rendszerek ráadásul nemcsak azt befolyásolják, hogy ki nyer. Hatással vannak arra is,

* mennyire arányos a politikai képviselet,
* mennyire könnyű túlhatalmat kiépíteni,
* mennyire ösztönzi a rendszer a gyűlöletkampányokat,
* és mennyire jutalmazza a korrupciós hálózatokat.

Az egy X-es szavazási rendszerek egyik problémája például, hogy a politikusokat könnyen negatív kampányra ösztönzik: elég elérni, hogy a választók jobban gyűlöljék az ellenfelet, mint amennyire szeretik a saját oldalukat. A rangsoroló rendszerek ezzel szemben gyakran együttműködésre és kompromisszumkeresésre ösztönöznek, hiszen a második-harmadik preferenciák is számíthatnak.

Az approval voting ugyan sokszor jobban működik, mint az egyszerű többségi rendszer, de erősen ösztönözheti a taktikai szavazást. Ha a választók úgy érzik, hogy csak a kedvencük megjelölése segíti valóban annak győzelmét, akkor a rendszer gyakorlatilag visszaalakul egyszerű többségi szavazássá.

A témáról további rövid összefoglalók:

* Hogyan előzzük meg a túlhatalmat? (arányos képviselet és koalíciós kényszer)
* Hogyan vethetünk véget a szimbolikus gyűlöletpolitikának? (a negatív kampány ösztönzői)
* Hogyan lehet felszámolni a korrupciót? (a választási rendszer és a korrupció kapcsolata)

Nézzünk meg egy konkrét példát.

# A három módszer

## 1. Egyszerű többségi szavazás (FPTP)

Ez a legismertebb rendszer: mindenki egyetlen opciót jelöl meg, és amelyik a legtöbb első helyes szavazatot kapja, az nyer.

Ez működik például sok parlamenti választásban, illetve sok online szavazásban is.

---

## 2. Approval voting – „minden elfogadható opciót jelölj meg”

Az olyan szolgáltatások, mint a Doodle vagy sok meeting-szervező alkalmazás, gyakran ezt a logikát használják.

Itt nem csak egyetlen időpontot lehet választani. Minden résztvevő bejelölheti az összes olyan időpontot, ami számára megfelelő.

A legtöbb jelölést kapó időpont nyer.

Ez első látásra sokkal rugalmasabbnak és igazságosabbnak tűnik, hiszen nem kényszeríti az embereket arra, hogy csak egyetlen kedvencet nevezzenek meg.

---

## 3. „Rangsoroló” módszer

Ebben a rendszerben a résztvevők sorrendbe állítják az opciókat.

A módszer lényege, hogy az időpontokat páronként hasonlítjuk össze:

* hétfő vagy kedd?
* kedd vagy csütörtök?
* hétfő vagy csütörtök?

Ha valamelyik opció minden másikat legyőz közvetlen összehasonlításban, akkor az a győztes.

Ez sokszor jobban képes felismerni a kompromisszumos, széles körben elfogadható megoldásokat.

# A példa

Tegyük fel, hogy három időpont van:

* hétfői időpont
* keddi időpont
* csütörtöki időpont

A tizenegy résztvevő preferenciái a következők:

| Résztvevők száma | Preferencia                 |
| ---------------- | --------------------------- |
| 5 fő             | hétfő > nincs találkozó > kedd > csütörtök |
| 4 fő             | kedd > csütörtök > nincs találkozó > hétfő |
| 2 fő             | csütörtök > kedd > nincs találkozó > hétfő |

Mit jelent ez?

* Öt ember kizárólag a hétfői időpontban tudna részt venni.
* Négy ember szerint a keddi időpont a legjobb, a csütörtöki még elfogadható, de a hétfő már nem.
* Két ember szerint a csütörtök a legjobb, a kedd még elfogadható, de a hétfő már nem.

Intuitívan a kedd és csütörtök időpontok egy nagyobb, kompromisszumkereső csoportot képviselnek, míg a hétfői időpont csak egy kisebbségnek igazán jó.

# Mit csinál az FPTP?

Ebben a rendszerben mindenki csak az első választását jelölheti meg.

Az eredmény:

* hétfő: 5 szavazat
* kedd: 4 szavazat
* csütörtök: 2 szavazat

Az FPTP tehát a hétfői időpontot választja győztesnek.

Pedig:

* az emberek többsége inkább keddet vagy csütörtököt szeretne,
* és a keddi időpontot a többség még a csütörtökinél is jobb kompromisszumnak tartja.

Ez az FPTP egyik klasszikus problémája:

ha két hasonló kompromisszumos opció (kedd és csütörtök) „megosztja” a szavazókat, akkor egy kisebbségi, de koncentrált támogatottságú jelölt nyerhet.

# Mit csinál az approval voting?

Most mindenki minden olyan időpontot megjelöl, amelyik számára megfelelő.

Ez pontosan olyan helyzet, mint amikor egy Doodle-felületen több időpontot is be lehet pipálni.

Tegyük fel, hogy:

* az első csoport csak a hétfői időpontot jelöli,
* a második csoport keddet és csütörtököt jelöli,
* a harmadik csoport szintén keddet és csütörtököt jelöli.

Az összesítés:

* hétfő: 5 jelölés
* kedd: 6 jelölés
* csütörtök: 6 jelölés

Az approval voting tehát azt mondja:

kedd és csütörtök egyformán jó jelöltek.

Ez teljesen érthető eredmény:

mindkét időpont ugyanannyi ember számára elfogadható.

Az approval voting tehát már sokkal jobban működik, mint az egyszerű többségi rendszer: nem a hétfői időpontot választja.

Viszont továbbra sem tud különbséget tenni a két kompromisszumos lehetőség között.

# Mit csinál a rangsoroló módszer?

Most nézzük meg a páronkénti összehasonlításokat.

## kedd kontra hétfő

* 5 ember szerint hétfő jobb
* 6 ember szerint kedd jobb

Tehát:

kedd legyőzi hétfőt.

## csütörtök kontra hétfő

* 5 ember szerint hétfő jobb
* 6 ember szerint csütörtök jobb

Tehát:

csütörtök legyőzi hétfőt.

## kedd kontra csütörtök

* az 5 fős első csoport szerint kedd jobb csütörtöknél,
* a 4 fős kedd-párti csoport szerint szintén kedd jobb,
* a 2 fős csütörtök-párti csoport szerint csütörtök jobb.

A módosított rangsoroló változatban az első 5 szavazó ebben az összehasonlításban nem számítana, mert számukra sem kedd, sem csütörtök nem elfogadható. Ekkor is kedd győzne 4–2 arányban.

Az eredmény:

* kedd: 9 szavazat
* csütörtök: 2 szavazat

Tehát:

kedd legyőzi csütörtököt.

Mivel a keddi időpont minden másik időpontot legyőz közvetlen összehasonlításban, ezért a rangsoroló módszer keddet választja győztesnek.

# Miért érdekes ez?

A példában:

* az egyszerű többségi rendszer hétfőt választja,
* az approval voting szerint kedd és csütörtök holtversenyben vannak,
* a rangsoroló módszer viszont felismeri, hogy a két kompromisszumos lehetőség közül valójában kedd a jobb közös megoldás.

Létezik egy módosított változat is, amely bizonyos helyzetekben még korrektebben kezeli az olyan eseteket, amikor valaki inkább távol maradna egy találkozótól. Valódi választásoknál vagy népszavazásoknál azonban általában nem lehet „kimaradni” a következményekből, ezért ott a klasszikus megközelítés természetesebb.

# Tanulság

A szavazási rendszerek nem pusztán technikai részletek.

Ugyanazok az emberek, ugyanazokkal a véleményekkel, egészen más eredményre juthatnak attól függően, hogyan gyűjtjük össze és értelmezzük a preferenciáikat.

Az egyszerű többségi rendszer hajlamos „büntetni” a kompromisszumos jelölteket.

Az approval voting már sokkal jobban képes megtalálni a széles körben elfogadható opciókat.

A rangsoroló módszerek pedig egy további lépéssel azt is meg tudják mutatni, hogy az elfogadható kompromisszumok közül melyiket preferálja valójában a többség.

Ezért a „ki nyert?” kérdésre sokszor nem elég csak a szavazatokat megszámolni. Az is számít, milyen szabályok szerint számolunk.
