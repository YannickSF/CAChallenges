
if __name__ == '__main__':

    def check_number(value):
        ch = [int(u) for u in value]

        for t in ch:
            if ch.count(t) > 1:
                return False
        return True

    def check_multiples(value1):
        for y in resolve:
            ch1 = [int(v) for v in value1]
            ch2 = [int(w) for w in y]

            ch1.sort()
            ch2.sort()

            if ch1 == ch2:
                return False
        return True

    resolve = []

    for a in range(1000):
        val = '{0:03d}'.format(a)
        if check_number(val):
            if len(resolve) > 0:
                if check_multiples(val):
                    resolve.append(val)
            else:
                resolve.append(val)

    print(resolve)
