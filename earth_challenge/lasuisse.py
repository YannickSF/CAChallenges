
import sys

if __name__ == '__main__':
    usr = [sys.argv[1], sys.argv[2], sys.argv[3]]
    usr.sort()

    if usr[0] == usr[1] == usr[2]:
        print('erreur.')
    else:
        print(usr[1])
