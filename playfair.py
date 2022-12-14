DEFAULT = [chr(i) for i in range(65, 91)]


def palyfair_transform(aidx, bidx, offset):
    ay, ax, by, bx = aidx // 5, aidx % 5, bidx // 5, bidx % 5
    
    if ax == bx:
        return ax, (ay + offset) % 5, bx, (by + offset) % 5
    if ay == by:
        return (ax + offset) % 5, ay, (bx + offset) % 5, by
    
    return bx, ay, ax, by


def forward(plaintext, key):

    monke = [key[i::5] for i in range(5)]
    prepped = prepare(plaintext)
    
    new = ''
    for a, b in zip(prepped[::2], prepped[1::2]):

        aidx, bidx = key.index(a), key.index(b)
        nax, nay, nbx, nby = palyfair_transform(aidx, bidx, 1)
        new += monke[nax][nay] + monke[nbx][nby]

    return new

def prepare(plaintext):
    plaintext = ''.join((a if a.upper() != 'J' else 'I').upper() if str(a).isalpha() else '' for a in plaintext)
    plaintext += 'Z' * (len(plaintext) % 2)
    plaintext = ''.join((a + b if a != b else f'{a}X{b}X' for a, b in zip(plaintext[::2], plaintext[1::2])))
    return plaintext

def keyword_to_key(keyword):
    keyword = keyword.upper()
    alpha = set(DEFAULT).difference({'J'})
    nkw = []
    for i in keyword:
        if i in alpha:
            nkw.append(i)
            alpha.difference_update([i])

    return nkw + sorted(alpha)

def backward(ciphertext, key):

    monke = [key[i::5] for i in range(5)]
    
    new = ''
    for a, b in zip(ciphertext[::2], ciphertext[1::2]):

        aidx, bidx = key.index(a), key.index(b)
        ay, ax, by, bx = aidx // 5, aidx % 5, bidx // 5, bidx % 5
        
        if ax == bx:
            nax, nay, nbx, nby = ax, (ay - 1) % 5, bx, (by - 1) % 5
        elif ay == by:
            nax, nay, nbx, nby = (ax - 1) % 5, ay, (bx - 1) % 5, by
        else:
            nax, nay, nbx, nby = bx, ay, ax, by

        new += monke[nax][nay] + monke[nbx][nby]

    return new

def digraph(text):
    digraphs = {}
    for a, b in zip(text[::2], text[1::2]):

        ab = a + b
        v = digraphs.get(ab, 0)
        digraphs[ab] = v + 1

    return digraphs


CHALLENGE_9_B = '''LWAU ARLMS ORYDA OOBYH HULST ROSEN INAEC TIIUH EIRTS EOOTF UHEEM SRONS ESIFH NGECN TOAID ENTMV EVCOA ATEIE YHIBI ITNEH HLRKV EEYIE IMVTY HEEAN OWDRT TFURH NSISF TNNSK DSAAM UMMER IATIV ETOBA LEPTS HETSR GEPAA EGMDS MUFYE IFPLN ITCKO HSUTH RMERI CANCY GOATT RNIGD IAVST ENHRA OAEEH EEISD TAHCL ETRTA RFWTU ROEYN GAAIT RNHLE SCRER AGKEY ESABN RACIS EUNIT COYST DEOBH HOEEN TTIRM ETLTE OVNUI BECES TDIAM WIYSA TREMI MTNRH SEKIE AARHE IYIFT DFTIM IAYNC LTLOA TRVND EOPOF OREUT EWERL ITNUR MTAEO OENPR ITVBE NOIHA TOGHT WHEAA MSTHS TBTVP NOHGN ONOTC FHIEN ICEIC GRMID YNAHH CEOIT SAMWD NTRCU EORIE NDRGS HIEIF RIRFO HEFET SNEKK NIARS TRUCN AEFGR LLOYL NEODN EHNSO REDAS TNMAH PGOIN EREAK EEIEM NPHIU ATLIR CVHPO UWREK TTINL BHLAR IEERN HPOTE ETEHN SDGET IUEAK HTENL ADEVO OEEMI ACCFP HNABO DTSSA CEFAA OILMM NRNEA AHNTR NRMLA ISNSI STADR RCKFA EOTRI BANET HLCGW LRHWU HIAEE AARDT TEMSQ TAUET EAECS IHNTE YRTAY SCNEN DNYIM ETIOA RRNVT NOMIU ROEVN FETCE OAELY BMRNE UEAHG VOLHA LILAG YOHTN TLHMO EELYW VTEET OAADF HHSSE PNTOE ITPBI HSILL SOLRP CATER OIEEN DYYPH GCSTH REFTN TTMCL WKOEA EHOSW ALUEO THLRA EYGRR EHBUC DIDAE INCNR OTADO FJERI FRKRH FCEIE EECWD ONNSW INSUV LWREO ODITB TOLEE EIPCO WEERN NEVLT ILHEI DDBEE SIUHW SAHEH YEIIB CANTN WPTHU IESFC EVTYE EHETS NMHTT FNETA SRTYE HEUFS OEOVO CYEEE MDELE ADIVU NNROT OSTSH ITHEO ASWTR LTEUL ASOEE AVSLO ATTCU TLTHC ADAIG VNEEO RIRAH FRTFN AASDT RKHEE AOWLF OTTML OREOO SOETW TREAS EBUSE YHLBE GHTIT HNMHE IERYT PGNRL NLCRC UAUTE EHPED PWEEN TCHBN EEETI CMOOA TEYNN KEMCT NOHAF SVIIE CEOOF REHSC RERCS ENREO EWIAW ULESE OAGRP UCELD REHPL NHAEA SEAYO RMVIE IFDSC RDRBC EDALC TBOHW TIIHS ETRLE KLLTA OTLNI AIKSN BYHSM KUIAI LLRRL EMSTA THSST LIEIR YCTWE OSPTE LENES HAMET SDNDG GEEGI HNTAI WCIHR EHRLT PBWAW MSIED OTNLN EOUOT MIIMN IROCC SNUHA OETIO TUDOR TAHCN ETATI DCERL TSILT LAEOR RNCBI IEWUC CHIEI TNPYR EPTLR EVTOC EIUTR LLHLH EIEOW GSTSU INTTM HEEAN OOOCF NDSCU TTEUN TAVHT EEHYO EGRTL FNITT WOODR SITLE SLAII DHPNO OTRDO CPFNE ITOOI HTELN ATEEO ARNRE OTORE HPTPT NIIGW TARSN AMAVE RHERE NREML TTIHO LKEWE EEAND ODWNR OYSTA COTUT ICTUM INHOD EISAC EVTXN HPSSE OTOHA ILLSF MMUEN UTNSR AYXAE EESIE HWDAH REIOI TPLLV TYIIM AAOCT MNNES IROUP FCCET TLSVP EEECL CLHHO LUOAI TTIRW WEIHR TAEIT HITGS'''
CHALLENGE_9_B = "".join(CHALLENGE_9_B.split(" "))

if __name__ == '__main__':

    key = keyword_to_key('MONARCHY')

    tkey = keyword_to_key('SILVERBGAD')
    print(len(tkey))

    # EXAMPLE = 'instruments'
    # res = forward(EXAMPLE, key)
    # print(res)

    # assert res == 'GATLMZCLRQTX'
    # dec = backward(res, key)
    # print(dec)

    res = backward(CHALLENGE_9_B, tkey)
    print(res[:50])

