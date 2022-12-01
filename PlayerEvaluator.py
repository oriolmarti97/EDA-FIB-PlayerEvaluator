import argparse
import parse_res
import random
import os
import csv
import sys
from pathlib import Path

directori_partides='partides'
directori_resultats='resultats'

def crea_dirs():
    for x in (directori_partides, directori_resultats):
        p = Path(x)
        p.mkdir(exist_ok=True)


def main():
    crea_dirs()
    parser = argparse.ArgumentParser(prog = 'PlayerEvaluator', description = "Avalua jugadors del joc d'EDA. Executa N partides del joc amb seeds consecutives i els jugadors que s'hagin definit, i mostra un resum de les principals mètriques resultants",epilog = '')
    parser.add_argument('jugadors', metavar='jugador', type=str, nargs=4, default=['Dummy','Dummy','Dummy','Dummy'], help="Noms dels 4 jugadors que s'executaran. Cal que estiguin definits al joc")
    parser.add_argument('-c','--cnf', default='default.cnf', help="Arxiu de configuració que volem que utilitzi el joc. Cal que pengi del directori game")
    parser.add_argument('-d','--desa-partides', action=argparse.BooleanOptionalAction, help='Conserva la partida sencera (arxiu .res)')
    parser.add_argument('-s','--seed-min',default=None, type=int, help="Seed mínima. Si no s'indica, serà aleatòria")
    parser.add_argument('-n','--num-proves',default=100, type=int, help="Nombre d'iteracions a executar")
    args = parser.parse_args()
    #print(args)

    if args.seed_min==None:
        args.seed_min=random.randint(1,1000000)

    resum={'min':{}, 'max':{},'acumulat':{}}
    n=0
    guanyades=[0,0,0,0]

    for i in range(args.seed_min, args.seed_min+args.num_proves):
        cmd = f'game/Game -s {i} {args.jugadors[0]} {args.jugadors[1]} {args.jugadors[2]} {args.jugadors[3]} <./game/{args.cnf} 2>/dev/null'
        with os.popen(cmd) as f:
            txt = f.read()
            resultat = parse_res.parser(txt)
        if args.desa_partides:
            nom_partida=f'{directori_partides}/{i}.res'
            with open(nom_partida,'w') as f:
                f.write(txt)
                print(f'Partida desada a {nom_partida}',file=sys.stderr)
        nom_resultat=f'{directori_resultats}/{i}.csv'
        with open(nom_resultat,'w') as f:
            writer = csv.DictWriter(f,fieldnames=resultat[0].keys())
            writer.writeheader()
            writer.writerows(resultat)
            print(f'Resultat de la partida desat a {nom_resultat}',file=sys.stderr)
        for (clau, valor) in resultat[-1].items():
            if clau not in resum['min']:
                resum['min'][clau]=valor
            else:
                resum['min'][clau]=min(valor, resum['min'][clau])
            if clau not in resum['max']:
                resum['max'][clau]=valor
            else:
                resum['max'][clau]=max(valor, resum['max'][clau])
            if clau not in resum['acumulat']:
                resum['acumulat'][clau]=valor
            else:
                resum['acumulat'][clau]+=valor
        guanyador = max((resultat[-1][f'score_{x}'],x) for x in range(4))[1]
        guanyades[guanyador]+=1
        n+=1

    print('Partides guanyades:')
    for (i,nom) in enumerate(args.jugadors):
        print(f'\t{nom}: {guanyades[i]}/{n}')
    print('Mínims:')
    for (clau, valor) in resum['min'].items():
        print(f'\t{clau}: {valor}')
    print('Màxims:')
    for (clau, valor) in resum['max'].items():
        print(f'\t{clau}: {valor}')
    print('Mitjans:')
    for (clau, valor) in resum['min'].items():
        print(f'\t{clau}: {valor/n}')


if __name__=='__main__':
    main()
