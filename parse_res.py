import pprint


def parse_line(line):
    return line.split('\t')


def parser(txt):
    res = []
    for x in txt.split('\n'):
        if x != '':
            x = parse_line(x)
            if 'round' in x[0]:
                res.append({})
            elif x[0] in ('score', 'scr_acc', 'strength', 'status'):
                for (i, y) in enumerate(x[1:]):
                    res[-1][f'{x[0]}_{i}'] = int(y)

    return res


if __name__ == '__main__':
    with open('game/default.res') as f:
        pprint.pprint(parser(f.read()))
