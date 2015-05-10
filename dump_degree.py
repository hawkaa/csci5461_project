#
# Reads the degree from a co-expression network (specified in the command line)
# and prints it to the screen
#

from optparse import OptionParser
import camoco as co
import pandas as pd

parser = OptionParser()
parser.add_option("-n", "--network-name", help="Name of network", action="store",
                    type="string", dest="network_name")

def main():
    (options, args) = parser.parse_args()
    if not options.network_name: parser.error("Must specify name of network")

    network = co.COB(options.network_name)
    degree = network.degree
    
    i = 0
    for index, row in degree.iterrows():
        msg = "%s\t%s\t%s" % (i, index, row["Degree"])
        print(msg)
        i += 1

if __name__ == "__main__":
    main()
