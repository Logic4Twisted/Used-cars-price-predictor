from django import forms

FUEL_TYPE = (
	('---', '---'),
	('andere', 'andere'),
	('benzin', 'benzin'),
	('cng', 'cng'),
	('diesel', 'diesel'),
	('elektro', 'elektro'),
	('hybrid', 'hybrid'),
)

GEAR_BOX = (
	('---', '---'),
	('manuell', 'manuell'),
	('automatik', 'automatik'),
)

VEHICLE_TYPE = (
	('---', '---'),
	('andere', 'andere'),
	('bus', 'bus'),
	('cabrio', 'cabrio'),
	('coupe', 'coupe'),
	('kleinwagen', 'kleinwagen'),
	('kombi', 'kombi'),
	('limousine', 'limousine'),
	('suv', 'suv'),
)

BRAND = (
	('---', '---'),
	(' alfa_romeo ',' alfa_romeo '),
	(' audi ',' audi '),
	(' bmw ',' bmw '),
	(' chevrolet ',' chevrolet '),
	(' chrysler ',' chrysler '),
	(' citroen ',' citroen '),
	(' dacia ',' dacia '),
	(' daewoo ',' daewoo '),
	(' daihatsu ',' daihatsu '),
	(' fiat ',' fiat '),
	(' ford ',' ford '),
	(' honda ',' honda '),
	(' hyundai ',' hyundai '),
	(' jaguar ',' jaguar '),
	(' jeep ',' jeep '),
	(' kia ',' kia '),
	(' lada ',' lada '),
	(' lancia ',' lancia '),
	(' land_rover ',' land_rover '),
	(' mazda ',' mazda '),
	(' mercedes_benz ',' mercedes_benz '),
	(' mini ',' mini '),
	(' mitsubishi ',' mitsubishi '),
	(' nissan ',' nissan '),
	(' opel ',' opel '),
	(' peugeot ',' peugeot '),
	(' porsche ',' porsche '),
	(' renault ',' renault '),
	(' rover ',' rover '),
	(' saab ',' saab '),
	(' seat ',' seat '),
	(' skoda ',' skoda '),
	(' smart ',' smart '),
	(' subaru ',' subaru '),
	(' suzuki ',' suzuki '),
	(' toyota ',' toyota '),
	(' trabant ',' trabant '),
	(' volkswagen ',' volkswagen '),
	(' volvo ',' volvo '),
)

MODEL = (
	('---', '---'),
	(' 100 ',' 100 '),
(' 145 ',' 145 '),
(' 147 ',' 147 '),
(' 156 ',' 156 '),
(' 159 ',' 159 '),
(' 1_reihe ',' 1_reihe '),
(' 1er ',' 1er '),
(' 200 ',' 200 '),
(' 2_reihe ',' 2_reihe '),
(' 300c ',' 300c '),
(' 3_reihe ',' 3_reihe '),
(' 3er ',' 3er '),
(' 4_reihe ',' 4_reihe '),
(' 500 ',' 500 '),
(' 5_reihe ',' 5_reihe '),
(' 5er ',' 5er '),
(' 601 ',' 601 '),
(' 6_reihe ',' 6_reihe '),
(' 6er ',' 6er '),
(' 7er ',' 7er '),
(' 80 ',' 80 '),
(' 850 ',' 850 '),
(' 90 ',' 90 '),
(' 900 ',' 900 '),
(' 9000 ',' 9000 '),
(' 911 ',' 911 '),
(' a1 ',' a1 '),
(' a2 ',' a2 '),
(' a3 ',' a3 '),
(' a4 ',' a4 '),
(' a5 ',' a5 '),
(' a6 ',' a6 '),
(' a8 ',' a8 '),
(' a_klasse ',' a_klasse '),
(' accord ',' accord '),
(' agila ',' agila '),
(' alhambra ',' alhambra '),
(' almera ',' almera '),
(' altea ',' altea '),
(' amarok ',' amarok '),
(' andere ',' andere '),
(' antara ',' antara '),
(' arosa ',' arosa '),
(' astra ',' astra '),
(' auris ',' auris '),
(' avensis ',' avensis '),
(' aveo ',' aveo '),
(' aygo ',' aygo '),
(' b_klasse ',' b_klasse '),
(' b_max ',' b_max '),
(' beetle ',' beetle '),
(' berlingo ',' berlingo '),
(' bora ',' bora '),
(' boxster ',' boxster '),
(' bravo ',' bravo '),
(' c1 ',' c1 '),
(' c2 ',' c2 '),
(' c3 ',' c3 '),
(' c4 ',' c4 '),
(' c5 ',' c5 '),
(' c_klasse ',' c_klasse '),
(' c_max ',' c_max '),
(' c_reihe ',' c_reihe '),
(' caddy ',' caddy '),
(' calibra ',' calibra '),
(' captiva ',' captiva '),
(' carisma ',' carisma '),
(' carnival ',' carnival '),
(' cayenne ',' cayenne '),
(' cc ',' cc '),
(' ceed ',' ceed '),
(' charade ',' charade '),
(' cherokee ',' cherokee '),
(' citigo ',' citigo '),
(' civic ',' civic '),
(' cl ',' cl '),
(' clio ',' clio '),
(' clk ',' clk '),
(' clubman ',' clubman '),
(' colt ',' colt '),
(' combo ',' combo '),
(' cooper ',' cooper '),
(' cordoba ',' cordoba '),
(' corolla ',' corolla '),
(' corsa ',' corsa '),
(' cr_reihe ',' cr_reihe '),
(' croma ',' croma '),
(' crossfire ',' crossfire '),
(' cuore ',' cuore '),
(' cx_reihe ',' cx_reihe '),
(' defender ',' defender '),
(' delta ',' delta '),
(' discovery ',' discovery '),
(' discovery_sport ',' discovery_sport '),
(' doblo ',' doblo '),
(' ducato ',' ducato '),
(' duster ',' duster '),
(' e_klasse ',' e_klasse '),
(' elefantino ',' elefantino '),
(' eos ',' eos '),
(' escort ',' escort '),
(' espace ',' espace '),
(' exeo ',' exeo '),
(' fabia ',' fabia '),
(' fiesta ',' fiesta '),
(' focus ',' focus '),
(' forester ',' forester '),
(' forfour ',' forfour '),
(' fortwo ',' fortwo '),
(' fox ',' fox '),
(' freelander ',' freelander '),
(' fusion ',' fusion '),
(' g_klasse ',' g_klasse '),
(' galant ',' galant '),
(' galaxy ',' galaxy '),
(' getz ',' getz '),
(' gl ',' gl '),
(' glk ',' glk '),
(' golf ',' golf '),
(' grand ',' grand '),
(' i3 ',' i3 '),
(' i_reihe ',' i_reihe '),
(' ibiza ',' ibiza '),
(' impreza ',' impreza '),
(' insignia ',' insignia '),
(' jazz ',' jazz '),
(' jetta ',' jetta '),
(' jimny ',' jimny '),
(' juke ',' juke '),
(' justy ',' justy '),
(' ka ',' ka '),
(' kadett ',' kadett '),
(' kaefer ',' kaefer '),
(' kalina ',' kalina '),
(' kalos ',' kalos '),
(' kangoo ',' kangoo '),
(' kappa ',' kappa '),
(' kuga ',' kuga '),
(' laguna ',' laguna '),
(' lancer ',' lancer '),
(' lanos ',' lanos '),
(' legacy ',' legacy '),
(' leon ',' leon '),
(' lodgy ',' lodgy '),
(' logan ',' logan '),
(' lupo ',' lupo '),
(' lybra ',' lybra '),
(' m_klasse ',' m_klasse '),
(' m_reihe ',' m_reihe '),
(' materia ',' materia '),
(' matiz ',' matiz '),
(' megane ',' megane '),
(' meriva ',' meriva '),
(' micra ',' micra '),
(' mii ',' mii '),
(' modus ',' modus '),
(' mondeo ',' mondeo '),
(' move ',' move '),
(' musa ',' musa '),
(' mustang ',' mustang '),
(' mx_reihe ',' mx_reihe '),
(' navara ',' navara '),
(' niva ',' niva '),
(' note ',' note '),
(' nubira ',' nubira '),
(' octavia ',' octavia '),
(' omega ',' omega '),
(' one ',' one '),
(' outlander ',' outlander '),
(' pajero ',' pajero '),
(' panda ',' panda '),
(' passat ',' passat '),
(' phaeton ',' phaeton '),
(' picanto ',' picanto '),
(' polo ',' polo '),
(' primera ',' primera '),
(' ptcruiser ',' ptcruiser '),
(' punto ',' punto '),
(' q3 ',' q3 '),
(' q5 ',' q5 '),
(' q7 ',' q7 '),
(' qashqai ',' qashqai '),
(' r19 ',' r19 '),
(' range_rover ',' range_rover '),
(' range_rover_evoque ',' range_rover_evoque '),
(' range_rover_sport ',' range_rover_sport '),
(' rangerover ',' rangerover '),
(' rav ',' rav '),
(' rio ',' rio '),
(' roadster ',' roadster '),
(' roomster ',' roomster '),
(' rx_reihe ',' rx_reihe '),
(' s60 ',' s60 '),
(' s_klasse ',' s_klasse '),
(' s_max ',' s_max '),
(' s_type ',' s_type '),
(' samara ',' samara '),
(' sandero ',' sandero '),
(' santa ',' santa '),
(' scenic ',' scenic '),
(' scirocco ',' scirocco '),
(' seicento ',' seicento '),
(' serie_2 ',' serie_2 '),
(' serie_3 ',' serie_3 '),
(' sharan ',' sharan '),
(' signum ',' signum '),
(' sirion ',' sirion '),
(' sl ',' sl '),
(' slk ',' slk '),
(' sorento ',' sorento '),
(' spark ',' spark '),
(' spider ',' spider '),
(' sportage ',' sportage '),
(' sprinter ',' sprinter '),
(' stilo ',' stilo '),
(' superb ',' superb '),
(' swift ',' swift '),
(' terios ',' terios '),
(' tigra ',' tigra '),
(' tiguan ',' tiguan '),
(' toledo ',' toledo '),
(' touareg ',' touareg '),
(' touran ',' touran '),
(' transit ',' transit '),
(' transporter ',' transporter '),
(' tt ',' tt '),
(' tucson ',' tucson '),
(' twingo ',' twingo '),
(' up ',' up '),
(' v40 ',' v40 '),
(' v50 ',' v50 '),
(' v60 ',' v60 '),
(' v70 ',' v70 '),
(' v_klasse ',' v_klasse '),
(' vectra ',' vectra '),
(' verso ',' verso '),
(' viano ',' viano '),
(' vito ',' vito '),
(' vivaro ',' vivaro '),
(' voyager ',' voyager '),
(' wrangler ',' wrangler '),
(' x_reihe ',' x_reihe '),
(' x_trail ',' x_trail '),
(' x_type ',' x_type '),
(' xc_reihe ',' xc_reihe '),
(' yaris ',' yaris '),
(' yeti ',' yeti '),
(' ypsilon ',' ypsilon '),
(' z_reihe ',' z_reihe '),
(' zafira ',' zafira '),
)

DAMAGE = (
	('Unknown', 'Unknown'),
	('No', 'No'),
	('Yes', 'Yes'),
)

class NameForm(forms.Form):
	fuel_type = forms.ChoiceField(choices=FUEL_TYPE, required=True)
	gear_box = forms.ChoiceField(choices=GEAR_BOX, required=True)
	vehicle_type = forms.ChoiceField(choices=VEHICLE_TYPE, required=True)
	brand = forms.ChoiceField(choices=BRAND, required=True)
	model = forms.ChoiceField(choices=MODEL, required=True)
	damage = forms.ChoiceField(choices=DAMAGE, required=True)
	year_of_registration = forms.IntegerField(min_value = 1950, max_value=2016)
	power_ps = forms.IntegerField(min_value=10, max_value = 500)
	kilometers = forms.IntegerField(required=False)
