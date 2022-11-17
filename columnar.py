CHALLENGE_6_A = '''NNFYR LKWAN SARTO AOFLA XEERB OUATD EDIHS TPEAP RACEO NFARC OELHA GUEEL EMAHD SGOOA DETEM TPAOL OTOTO RRWIK BUTDS EASKE EHHEW TRDGQ UNEOI ONTWS REIES HEINH SSADO EFTSH ESAII GHRTL WASTN IUCHM BTITW TAUNO UEGSO RATIH OURES SPICS IUTHE NPOIC ELHOS ETDUA ARRBI PSANR DENTS EATNG TOHLE ACBHE KEEOP TGHTI SSRSA EWEBU TYTAT DIADH STOTP NDRIS VUGPA NSIHE ITNTS TIEGV IONTS AETHT EIADW OARTR ASIST ANHDG LLLEI WNDTA HTARS CEEED TMOEV EVAEH EDORF EHEHT IFWAY HAGEN TDEND THEER TERAV WAPEA BIEBA LNBHA TTWKL DHUAO SLOEW VITRD IETDO HWGHE DTRNE RSVHI LDHUA OHADE PVNTY EOLIM ETTFT OPSOO EAPLO RIFTT HUWER YEENS COICS WEUWO LFILN IUTTO ODRRO OWMTH EFRIA SAWNE HINTG YONGR WWHTH TEIAK ERSBT ITUSB MSTEO EUCHM OOCOI ANFDE NICCH ATTTE CAREM HSEDS TISAN EDHAV IENLS SEENG ALLIY TTRAO CNONI STKAY IWNST HEOWT ERITT ASODL IATFE NEDIK ELALC CIADN TTHNA ETHII TTEVE HRTEE PDEYS POTTS THENS ORELO IHENS EUNNG IITRU LDOBW IDDHE EROMF VNWTH EEIRW AASCA NDTIS ONTGH NEACB HEAIN RIDWI TGHNO ARHDA CRIFM OCENS EEVES NTIAT OGRIW ARSMS GARNO IDITN TUREW EAHOA MNBSA NCLEU RSIOG NFABO ONBUT YPDIC ELDOE RSVWI EPRRE ERINA GPSEA ORTWH EHNCL EFETW YBEAI MTOOM OAIMI TSPCB UITTO NTDTI NKTIH HWILY LENDA INFHI NTGYG UEYSM STHIA SNNAA HTBEE SNADN AIPKD ITEWP LDNUT OTHEE FBSTT RIITH AETMD HAAPH NEDET PBANA KOFIC FIOTH OLUAI TWHAG SUAUL SPRIY OLOTH TEREA KRIBI THWTN VICET HFORM CITOH DAEOV EDRNU LTACV ESIDN OCHAX NEFOR ETGIR FERHD OMEIE ULDON CUITQ ETEWH EYSME OONSO ULWDE KIDEN BPEDP AAERT THFRI MCEET IAUMB PINOG HATTH HTTTA ACEDM EESHG EMAIS TEXHP GINIA TLWAS TUIRT HOONX FOORD ICHHR WDILA LEALB GUEMA NIATD TOEGG THETL EPLIM GAERS TTHUT APTOC EOANR LLSAT CHEMT OOLEN IUBER SBOML LTAHF ENISO EANKB ORICI FAFTO GSELE RWHIT THEHP TPLEO IEYNN LFNNK SAORI CEFCF LTRLA ASDOE NCIVE GYTAS MUUOA SAHNC TERNC ITCAP NETSI UGBLS IANNL LIEGT CEHNA ELWAA YSEEN BASGP AIRBF BOOST ORKWA SJUSD TNOWI NNKHO IWSGL LIANC HOAWN GHENW TDYCA ELHDC AENLL LYEOT LOTAT USISI DHBLY UTOEI FUYRC ANUCO SSROE RRENE CFALL CSETH EOBTA VIHOE OFARS UPECS TUJOD OISET USPEI DEVOA AKETO SONBT OUTHE HBTKA NNDAE VBHAT AGAQI HREAB KNGAL NLIER UHLTA NDSWE ATASN EAITW EDORS FODTH IENMO HATPG NWEEQ PCKLI YUOTT PESPA TATDN LYRNE ADOHN NALLC EEHOR WARTH RGENI METSE OMARP FRENA TPRAN YDLLO CMAOO NSIAT EVEDR NIMET LYNIM NMYIA TDEEL EFYTL OEVHE WHEWS ARALK TISTO AGNNE ADHED ORAFQ DETSI PUTOT TAOTH EECKL ITLWA NTPSO AIBLS ESLIS OTTIN BNUEE DIWDT NAGAE MGETO TTGEO ELHAT ICOOA TADFN MTHOE RTWOE RNNDW AEKAB LEERC ROOST EFERR SCEIN TETHA ITWTT HXAEA DBHET SENNT ESTBU EJRET OHFHI RTDET HOFSO ALLCS EILEH WWOUL CDELI STTNT OTNHE ALLCS ETHOI UWWAR ARTTA TNEAI SNTOX UTOAM TICAT LAENC YRLTE DPBYH ESTYY EMSTO SELAH MTIGH LTPSW ERREB LEATE EADRI ONDCA OTDSE LEUAT THHTE NDSEE ADAHD RDALE ADROF EEYRY PCTNN THOEI ELFST MTGAA VHHET TEESU FMFAI ENCTI USEAT COGIL TOANO SFACI AILFT ERNCI TANPD ENDIA THERI VFODI EOSJL CUALC IONTS AERIR GAITU TSHAV ISGEE RENCE HERPW IHPET RIDFI OVIUT WBEEN THOAD TIMEE VCRAO CTTNO IWKWE HSAAA NOETV RLEEA HOFOT LDWIN ONLYO RWKEK NOEWW UCAON YITFO ODSAN UDROK FOOLA RDWTR EEISN OOURY DGRYP CTE'''
CHALLENGE_6_A = ''.join(CHALLENGE_6_A.split(' '))

if __name__ == '__main__':

    key = [2, 3, 4, 1, 5, 0]
    #      N  N  F  Y  R  L
    new = ['\0'] * len(CHALLENGE_6_A)
    for idx, letter in enumerate(CHALLENGE_6_A):

        offset = key[idx % len(key)]
        pos = idx // len(key) * len(key)
        new[pos + offset] = letter

    print(''.join(new))
