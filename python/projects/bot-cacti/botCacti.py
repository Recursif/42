from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
lnom = [["Richard","Quinn"],["Mason","St-Jacques"],["Jules","Duranseau"],["Arno","Beaujolie"],["Gregoire","Lessard"],["Lundy","Sauve"],["Richard","Deserres"],["Marie","Goulet"],["Arianne","Gauthier"],["Fayme","Poulin"],["Suzette","Laforest"],["Alexis","Migneault"],["Matthieu","Gagne"],["Lance","Berie"],["Millard","Beauchamps"],["Soren","Frappier"],["Veronique","Bisson"],["Maurelle","Laliberte"],["Remy","Lesperance"],["Pascaline","Gabriaux"],["Neville","Charlesbois"],["Xavier","Senneville"],["Pierre","Laisne"],["Aubrey","Gaulin"],["Frederic","Mothe"],["Natalie","Chretien"],["Alain","Letourneau"],["Alexis","Gosselin"],["Robinette","Langlois"],["Royden","Blanchard"],["Maryse","Aubin"],["Joseph","Dumont"],["Favor","Roy"],["Tempeste","Moise"],["Ambra","Angelil"],["Ansel","Bonenfant"],["Campbell","Doiron"],["Roger","Norbert"],["Lorraine","Henrichon"],["Aubine","Cliche"],["Flordelis","Letourneau"],["Manville","Sevier"],["Davet","Lachance"],["Peverell","Lamothe"],["Josette","Bondy"],["Avenall","Benoit"],["Zerbino","Laprise"],["Lothair","Mothe"],["Dominique","Brodeur"],["Corette","Authier"],["Esmeraude","Lussier"],["Constance","Barjavel"],["Nicolette","Poissonnier"],["Iven","Bler"],["Bernadette","Chalifour"],["Gregoire","Sorel"],["Christine","Fortier"],["Kerman","Tougas"],["Aubrey","Blondlot"],["Stephanie","Lacharite"],["Viollette","Desnoyers"],["Robert","Bouvier"],["Bellamy","Cuillerier"],["Babette","L'Angelier"],["Leverett","Forest"],["Christabel","Meunier"],["Fusberta","Fortin"],["Iven","Barrientos"],["Marmion","Viens"],["Alexis","Courtois"],["Melusina","Lagueux"],["etienne","Lizotte"],["Ernest","Frechette"],["Orva","Bourget"],["Laverne","Routhier"],["Moore","Mailhot"],["Amelie","Laprise"],["Benoît","Barteaux"],["Faye","Casgrain"],["Robert","Bler"],["Aloin","Hughes"],["Marlon","Lebel"],["etienne","Courtemanche"],["Tabor","Fontaine"],["Normand","Landry"],["Legget","Jardine"],["Natalie","Demers"],["Marie","Chaussee"],["Harbin","Laramee"],["Alexis","Brian"],["Millicent","Echeverri"],["Calandre","Deblois"],["Rene","Trudeau"],["Lotye","Denis"],["Burrell","Charlebois"],["Prewitt","Lejeune"],["Robinette","Rocher"],["elise","Charlebois"],["Dorene","Chartier"],["Madeleine","Berger"],["Turner","Tessier"],["Brice","Guay"],["Dexter","De","La","Ronde"],["Blanche","Lachapelle"],["Eglantine","Vernadeau"],["Frontino","Cotuand"],["Roux","Lereau"],["Sibyla","Rocher"],["Lotye","Gamelin"],["Honore","Fremont"],["Malagigi","Audet"],["Mariette","Houle"],["Iva","Pinneau"],["Neville","Brault"],["Verney","Lachapelle"],["Curtis","Simard"],["Vallis","Brasseur"],["Ferragus","Perreault"],["Clarimunda","Laprise"],["Jerôme","Boucher"],["Blondelle","Dufresne"],["Archard","Chabot"],["Caresse","Desnoyer"],["Marsilius","Routhier"],["Oliver","Louineaux"],["Orva","Leroux"],["Merlin","Lamy"],["Jeoffroi","Quenneville"],["Brigliador","Parizeau"],["Ila","Beaupre"],["Philippine","Busque"],["Phillipa","Duhamel"],["Jewel","Lesage"],["Mireille","Labonte"],["Philippe","Fouquet"],["Audric","Ruais"],["Christien","Gaillard"],["Christine","Lefebvre"],["Trinette","Bonsaint"],["Fayette","Jacques"],["Gradasso","Royer"],["Odo","Lavallee"],["Annette","Thibault"],["Brie","Côte"],["Malagigi","Lagueux"],["Antoinette","Benoit"],["Carine","Bourget"],["Eulalie","Bazin"],["Roger","Chicoine"],["Gaetan","Labbe"],["Fauna","Laforest"],["Claire","Monty"],["Pierrette","Bordeaux"],["Minette","David"],["Claude","Salmons"],["Louis","Laurent"],["Allyriane","Belair"],["Patricia","Beaujolie"],["Vachel","Denis"],["Leone","Sanschagrin"],["Royce","Foucault"],["Clovis","Morneau"],["Saber","Despins"],["Jerôme","Mailhot"],["Lucas","Pellerin"],["Daisi","Riel"],["Huette","Gauthier"],["Vernon","Migneault"],["Penelope","Pelletier"],["Harbin","Lizotte"],["Geoffrey","Gagne"],["Lothair","Tisserand"],["Coralie","Lafontaine"],["Agathe","Desilets"],["Fanchon","Berie"],["D'Arcy","Chabot"],["Berangaria","Thibodeau"],["Joy","Bler"],["Leon","Beaupre"],["Victoire","Plaisance"],["Isaac","Lemelin"],["Alfred","Duperre"],["Oriel","Perillard"],["Aceline","Desilets"],["Noemi","Allaire"],["Ignace","Joly"],["Robert","Coupart"],["Chapin","Leclerc"],["Marcel","edouard"],["Fauna","Casgrain"],["Rule","Gaulin"],["Amarante","Ricard"],["Marthe","Lamontagne"],["elisabeth","Marseau"],["Yves","Marcoux"],["Cerise","Ratte"],["Turner","Bourgouin"],["Noel","Laframboise"],["Leone","Charrette"],["Anne","Bellemare"],["eric","CinqMars"],["Bruce","Pouchard"],["Paien","Cormier"],["Dalmace","Paulet"],["Melusina","Brunault"],["Royce","Beausoleil"],["Maurelle","Metivier"],["Charlot","Bois"],["Garland","Duranseau"],["Nadine","Camus"],["Roch","Côte"],["Leone","Landry"],["Porter","Boisclair"],["Carole","Tachel"],["Arber","Barrientos"],["Eugenia","Dagenais"],["Villette","Barrientos"],["Chapin","Saurel"],["Astrid","Chaussee"],["Garland","Echeverri"],["Arlette","Rodrigue"],["Audric","Dubois"],["Ray","Marcoux"],["Nicholas","Cuillerier"],["Amabella","Cadieux"],["Ormazd","Simon"],["Auriville","Hebert"],["Aime","Longpre"],["Clarimunda","Tachel"],["Brigliador","L'Heureux"],["Esperanza","Devoe"],["Germaine","Ayot"],["Arno","Despins"],["Anais","Chouinard"],["Florus","Duplessis"],["Fleurette","Lebel"],["Lucas","Jette"],["Benjamin","Laboissonniere"],["Marcel","Josseaume"],["Catherine","Dostie"],["Jeoffroi","Chauvin"],["Ancelina","Bosse"],["Rabican","Laforge"],["Aymon","Quirion"],["Adorlee","Aupry"],["Emmeline","St-Pierre"],["Guerin","Sylvain"],["Guillaume","Labrosse"],["Moore","Laprise"],["Langley","Devost"],["Burrell","Chouinard"],["Franck","Charbonneau"],["Beltane","Therrien"],["Eustache","Quenneville"],["Margaux","Labbe"],["Adele","Mercure"],["Archard","Paquette"],["Vachel","Baril"],["Loyal","Leroux"],["Therese","Audet"],["Eulalie","Lavallee"],["Tearlach","Loiseau"],["Apolline","Rouleau"],["Aurelie","Crete"],["Eulalie","Ayot"],["Ancelote","Simon"],["Marine","Trudeau"],["Belle","Hetu"],["Brigliador","Therrien"],["Xavier","Bosse"],["Nicole","Mazuret"],["Catherine","Rheaume"],["edith","Roy"],["Stephanie","Vallee"],["Alaine","Gabriaux"],["Marthe","Charest"],["Ferragus","Leveille"],["Daisi","Gadbois"],["Laurette","Quiron"],["Fabien","Allard"],["Arienne","Mercier"],["emile","Sansouci"],["Coralie","Charbonneau"],["David","Cousteau"],["Galatee","Beaudry"],["Valiant","Tachel"],["Gaetane","Allain"],["Musette","Foucault"],["Albracca","Racine"],["Hugues","Barjavel"],["Annette","Devoe"],["Esmeraude","Ruest"],["Adorlee","Lemaître"],["Travers","Guerette"],["Cosette","LaGrande"],["Fletcher","Veilleux"],["Frontino","Bizier"],["France","Pelletier"],["Aurore","Genereux"],["Orville","Desjardins"],["Sidney","Rouleau"],["Auguste","Bedard"],["Zurie","Breton"],["Raina","Lagace"],["Rive","Blanc"],["Fusberta","Morel"],["Charmaine","Daoust"],["Ormazd","Ratte"],["Verrill","Bolduc"],["Hedvige","Lafond"],["Raoul","Faure"],["edouard","Bellefeuille"],["Jeoffroi","Marier"],["Travers","Giroux"],["Dominic","Beauchesne"],["Medoro","Jacques"],["Frederic","DuLin"],["Roger","Noel"],["Suzette","Poulin"],["Chandler","L'Anglais"],["Maureen","Chabot"],["Agathe","Boulanger"],["Claire","Sevier"],["Sibyla","Lafontaine"],["Heloise","Lacombe"],["Oliver","Franchet"],["Flordelis","Foucault"],["Felicien","Brisette"],["Grosvenor","Barriere"],["Isabelle","Tachel"],["Sabine","Parizeau"],["Tearlach","Belair"],["Jay","Lanctot"],["Jeannine","Gamache"],["Serge","Raymond"],["Thibaut","Lebel"],["Joseph","Bouchard"],["Telford","Gingras"],["Felicien","Brisebois"],["Fortun","Boivin"],["Ansel","Gamelin"],["Felicienne","Beaudoin"],["Pauline","Marleau"],["Isaac","Therriault"],["Brigitte","Devoe"],["Coralie","Martin"],["Roux","Senneville"],["Parnella","Chenard"],["Quincy","Bisson"],["Allyriane","Lamy"],["Gerard","Lagueux"],["Cinderella","Bernier"],["Marguerite","Lampron"],["etienne","Bernard"],["Musette","Guimond"],["Talon","Guimond"],["Laurent","Brunelle"],["Mireille","D'Avis"],["Vaden","Charlebois"],["Alphonsine","Senneville"],["Etoile","Cressac"],["Amber","Pariseau"],["Tearlach","Barrientos"],["Dominique","CinqMars"],["Arthur","Provencher"],["Xavierre","Senneville"],["Pomeroy","Lachapelle"],["Agate","etoile"],["Burrell","Daviau"],["Amedee","Lapresse"],["Nouel","Courtois"],["Ermengardi","Paiement"],["Carine","Berube"],["Henri","Monjeau"],["Favor","Auberjonois"],["Cendrillon","Lamour"],["Geoffrey","Fournier"],["Jewel","Thivierge"],["Armina","Letourneau"],["Andree","Trudeau"],["Lucille","Veronneau"],["Beltane","Leduc"],["Dixie","Marleau"],["Philip","Hetu"],["Senior","Bisaillon"],["Amedee","CinqMars"],["Blanchefle","Bordeaux"],["Bayard","Guedry"],["Falerina","Savard"],["Nicolas","Blondlot"],["Gerard","Cressac"],["Jules","Forest"],["Halette","Dubeau"],["Hedvige","Simard"],["Latimer","Ruel"],["Viollette","Lanteigne"],["Ernest","Labrie"],["Sydney","Desrosiers"],["Sargent","D'Aubigne"],["Raison","Brunault"],["Latimer","Lambert"],["Barry","Lazure"],["Merci","Lafontaine"],["Alphonse","Nadeau"],["Peverell","Voisine"],["Pierrette","Desilets"],["Clovis","D'Aubigne"],["Marie","Doyon"],["Agrican","Beauchemin"],["Jeannine","Briard"],["Dreux","Desilets"],["Pomeroy","Cyr"],["Valiant","Sciverit"],["Antoine","Bonami"],["Ferrau","Grenier"],["Babette","Sarrazin"],["Archard","D'Aubigne"],["Medoro","Hebert"],["Tearlach","Lambert"],["Halette","Lapointe"],["Leverett","Boutot"],["Lirienne","Mercier"],["Elita","Bureau"],["Millard","Lagueux"],["Albertine","Pinette"],["Fusberta","Chauvet"],["Philip","Labbe"],["Warrane","Croteau"],["Jeanne","Rouleau"],["Mayhew","Bisson"],["Philippine","Allain"],["Sophie","Artois"],["Rosamonde","Bordeleau"]]

n = 4
browser = webdriver.Chrome()
i = 0
while (i < 600):
    pers = lnom[i]
    print(pers)


    browser.get('http://www.challenges-citoyens-cgi.com/votes_2018/votes_2018.html?nav=inscrit')
    print('landing ok')

    time.sleep(n)
    #browser.implicitly_wait(10)
    nom = browser.find_element_by_id("vo_nom")

    nom.send_keys(pers[0])

    pre = browser.find_element_by_id("vo_prenom")

    pre.send_keys(pers[1])

    email = browser.find_element_by_id("vo_email")


    e = pers[0].lower()+ "." + pers[1].lower() + "@gmail.com"

    print(e)

    email.send_keys(e+ '\n')


    time.sleep(n)

    r = random.sample(range(4,12,1), 2)

    vote = browser.find_elements_by_class_name('video-vote')

    name = browser.find_elements_by_class_name('projet')

    z = 2
    k = 0
    for a in name:
        if (a.text == 'Cacti'):
            z = k
            print (a.text)
        k += 1
    cacti = vote[z]

    l1 = vote[r[0]].get_property("href")

    l2 = vote[r[1]].get_property("href")

    lcacti = cacti.get_property("href")

    print(l1, l2, lcacti)
    browser.get(lcacti)

    time.sleep(n)
    form1 = browser.find_element_by_id('form1')
    form1.submit()
    print ("cacti ok")

    browser.get(l1)

    time.sleep(n)
    form1 = browser.find_element_by_id('form1')
    form1.submit()
    print ("p1 ok")

    browser.get(l2)

    time.sleep(n)
    form1 = browser.find_element_by_id('form1')
    form1.submit()
    print ("p2 ok")

    time.sleep(10)

    input = browser.find_elements_by_tag_name('input')

    for a in input:
        if (a.get_property("value") == "Je valide mon vote"):
            a.click()
            print("vote ok")

    print("\n")
    time.sleep(2)
    i+= 1



#cacti.click()
#"Background-color:#e31937;color:#FFFFFF;font-weight:bold; border-width: 0px 0px 0px 0px;")
