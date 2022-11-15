import sys

if __name__ == '__main__':

    def resolve_stages(car, iteration):
        stages = []
        for i in range(iteration):
            s = '{0}'.format(car)
            for j in range(i * 2):
                s += '{0}'.format(car)
            stages.append(s)

        return stages


    try:
        args = sys.argv
        args.remove(sys.argv[0])
        args[1] = int(args[1])

        max_pad = (args[1] - 1) * 2 + 1

        resolve = resolve_stages(args[0], args[1])
        for r in resolve:
            lr_fill = int((max_pad - len(r)) / 2)
            print(r.center(lr_fill, '*'))

    except ValueError as ve:
        print('Error.')

