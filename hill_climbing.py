from playfair import keyword_to_key, backward
from random import randrange
from idxoc import index_of_conicidence

TEST = '''DN CN UBQM IGOGMN QMFQ B URPA GLWM NS RRVNK QMK IVPININB DTGEZUEBYNDQOT YYBRPDNA XEBPG DN QBN YGVUGI MZSIGEGAF XNMPVP PQQP TKDNKQ YBNDQOQ KLWK UKULNNKI RS ZNQ NQT GXIK QDBZNEUF YTI UH UBYVP OKUMI NQ HFMG QNKGB LCVBLOEGENUNT B ELWH UBRSZNMQ P IGLNDO QO QMG NINBLNDQO TL QMG NFR LNEUNMB DTRH PTI B URPA LQTN DN TGQDOAF ERUGO NKG QPNZIG TL QMK IQONMONT QD ZQBZ MSRZENUN D UBYVP VNK NVB GREKGTN PGUGY REIKGD ON GSICLFN DN DRBDVPFQRNQ URPA RG IKNODRDNMM ZQ NKG IXBRY WPQM ZQ NGQNK EU NVB DTGEZUEBYNDQOT CNILBZTNUQ ZGQ UBYVA RK IQBGOMI UBQM IMNCEOEUM OKG UNX QCXNMT ZV GNIAYIK DN QMGIN EX YTNRPA Y TKYAR GCNH CZN D NEBSE QOAF Y QHFYVR GCNM SQBS ZQMK ITRH URPA RM ICNRSUGIGI CF KX KDPBLB LTI KGB DVRPGLHPN INBGYLQ XH UGIK ILBGPKNN CO QVI BKNRIK TL RS UGIOF HK NDPQ MKP HFMG QMK IQOUNDSRNQ IMNUHNU IXALNIGI PQM ZKG IXALGI BROE QMNU QMKP EDHKQ DH PRAM NQ TKUG KQV NVC OCXNMH ZVGMGM ZT LVGKNQFYVF OQBN D QBUG LBBLOEMI LTD LEUYA YBIKXYT NQ NKG WLVPS ZNQ YARVX VT NV GKNMN DN QMFQ QKNVFR IGGTUG PQP KURIMSIG ND ZKG QPNZIG TL QMK NCXNME GUGU ED ZKGC XXNINDS QMH UYF EU AQRDE BQ MYQ IHNU XNMI QMGIH URPA RN UN GURIMSIM NN LGVUG DN B UNVFR IH PGXYX KQOIKIOMI DP C EUNX ZAQGIM NT LEUI RTREN DRLDLB PQB MGI RSYVPGLHPN QBCVCL IWQ ZG PQTS ZODYBG SD ZKGH ZKGO NKGC XNQYUINI DLBCLEUK RGPALGQUNN CN DN YQTNCRAM NQBS ZQMKP QBUG LTYVRVUHM TM NV RPQORKP YAQMNVHK B ELWH IKUNU UGCL BYIGPZF OT GQODNVG KF NUURGVTENUQ FTI EU PQC KYQM NKG NKIXBRSF NMFH FQ QMG KHPBTWPDOGIQ XRPA RH UFQBKEUM LVG ODYBMGCO PQM ZBLRPQ YSUQP TKDNG BGEPBOT RSTDVGQFRAH PTI QYPM PQR TSIN E QBUG RSEFPGNMM ZKG GQXNGMKUNIEUH LS ZQMH IPQE C UBYVR GMNVIQ EGI NQ IXALNIGI D NEBSE B ELWG EPQLHMI NQ DELIKNT QQ EGI PQR TQ EGI RSYVPGLHPN AFSUT PBLSE QMG ICNSX TL EUNMDLGIEUM LVIQMGI R DQONCIMIGC TGQUBOE QMGE KF DRY BLBI RO NKG GQIN TL RSOUEUDROE QMGE RQQM QMFQ QMCN ABQ Y OVUGIOEGON NLGIFQRNQ IZN B UNVFR LIMPGI OQS ZNQ IGUGYA KF TLPDDRYA RINUNDSF QMGIG IGEPBOT L BCNM SQBZ TF YDSRUDNENQ XNVFR IH EGONRNUNI CF SKGT ZS VQNKGC OKIVIDNF YHGSIENQ YQ CPQMGCO QMKP LBN EO IGHVPLB RSONYBQ ZDNM QKG PMIMBLR GKNGIUG PQM ZQBN QGOPQCNFQRNT EREMQ BYCVCL NVS DKGKSN CD TP SFHN ET YAYKVHGI ZY UINBGYLN CN DQ CMNNMD OV RHPUG KT TKDNQ BTI KT LDPQE XOTVIG ND TP CIMONDNA XQBNMUGD OKGA CGPENUG D NEBSE B ELWG EPQLHMI NQ RSOUEUIK QMGE TL QMK NGIRNXNUNXYT QD ZKGRB NCNZFQRNO TEUIKIGAF LSVIQ YCBBQFH VQTREWYVYV'''
TEST = TEST.replace(' ', '')

def try_keys(try_key, score, initkey, max_iterations=1_000_000):
    key = initkey.copy()
    d = score(try_key(key))
    for i in range(max_iterations):
        nkey: list = key.copy()

        for _ in range(randrange(1, (i // 500) + 2)):
            sw1 = randrange(0, 25)
            sw2 = randrange(0, 25)

            v = nkey.pop(sw1)
            nkey.insert(sw2, v)

        ns = score(try_key(nkey))
        if not i % 500:
            print(f'{i:>5}: Trying key {"".join(nkey)}, Score: {ns:>4} {d}')

        if ns > d:
            d = ns
            key = nkey

def score_by_ic(text):
    return abs(index_of_conicidence(text))


if __name__ == '__main__':

    try_keys(lambda x: backward(TEST, x), score_by_ic, keyword_to_key(''))

