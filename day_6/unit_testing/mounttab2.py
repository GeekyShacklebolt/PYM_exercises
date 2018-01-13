#!/usr/bin/python3

import os

def parse_mounts():
    '''
    Funtion to parse the mount file.
    '''

    result = []
    if os.path.exists('/proc/mounts'):
        with open('/proc/mounts') as obj:
            for line in obj:
                line = line.strip()
                words = line.split()
                if len(words) > 5:
                    res = (words[0],words[1],words[2], "(%s)" % ' '.join(words[3:-2]))
                else:
                    res = (words[0],words[1],words[2])
                result.append(res)
        return result


def mount_details():
    '''
    Prints the mount details
    '''
    result = parse_mount()
    for line in result:
        if len(line) == 4:
            print("%s on %s type %s %s" % (line))
        else:
            print("%s on %s type %s" % (line))


if __name__ == '__main__':
    mount_details()
