

if __name__ == '__main__':
    resolve = []

    for i in range(100):
        for j in range(100):
            if j > i:
                resolve.append('{0:02d} {1:02d}'.format(i, j))

    print(resolve)
