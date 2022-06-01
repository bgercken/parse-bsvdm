"""
    You can use this script to parse the AIS base station files and make them look like they came from a boat.

    All this needs to do is take the original line, strip off the time stamp, change the sentence
    prefix and then calculate the new checksum.
"""

import os
import sys

NMEA_EOLN_DELIMITER = "\r\n"


def parse_ais_file(file_name):
    """ Parse the log file looking for BSVDM or BSVDO and replacing it with AIVDM or AIVDO"""

    out_file_name = file_name + ".out"

    with open(out_file_name, 'w') as file_out:
        with open(file_name) as file_in:
            try:
                for line in file_in:
                    data = line.split("!")

                    if len(data) > 1:
                        sentence = str(data[1])
                        print('!{}'.format(sentence), end='')
                        if sentence.startswith('BS'):
                            s = sentence.replace("BS", "AI")
                            # Remove the line terminator.
                            s = s.rstrip('\r\n')
                            # Remove existing '*' character and check sum.
                            s = s[0:-3]
                            # Calculate the checksum.
                            checksum = 0
                            for j in range(0, len(s)):
                                checksum ^= ord(s[j])
                            # Use format to force the value to 2 characters.
                            h = "{:02X}".format(checksum)
                            # Finalize the format of the sentence.
                            s = "!{}*{}{}".format(s, h, NMEA_EOLN_DELIMITER)
                            print("{}".format(s), end='')

                            try:
                                file_out.write(s)
                            except IOError as error:
                                raise SystemExit("ERROR while writing file = {}".format(error))
                        """ Otherwise it is not what we want"""
            except IOError as error:
                raise SystemExit('ERROR while reading file = {}'.format(error))


def main(file_name):
    """ Run as a program. """
    if os.path.exists(file_name):
        parse_ais_file(file_name)
    else:
        raise SystemExit(
            'Unable to read from file: {}'.format(file_name)
        )


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "/path/to/ais-log-file")
        print("Does: Takes a file with a timestamp followed by a base station nmea sentence and ")
        print("      replaces the base station indicator (BS) with (AI).")
        sys.exit(1)
    main(sys.argv[1])
