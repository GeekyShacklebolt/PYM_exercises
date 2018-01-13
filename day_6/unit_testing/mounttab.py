#!/usr/bin/python3

import os

def mount_details():
    '''
    Prints the mount details
    '''
    if os.path.exists("/proc/mounts"):
        with open("/proc/mounts") as obj:
            for line in obj:
                line = line.strip()
                words = line.split()
                print("%s on %s type %s" % (words[0], words[1], words[2]), end=' ')
                if len(words) > 5:
                    print("(%s)" % ' '.join(words[3:-2]))
                else:
                    print('')


if __name__ == '__main__':
    mount_details()
