
import sys

if __name__ == '__main__':
    path_name = sys.argv[0].split('/')
    print(path_name[len(path_name) - 1])
