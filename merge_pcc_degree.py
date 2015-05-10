#
# Merge PCC and degree values
#
# Will print a tab-separated list with gene values and the corresponding KLS
# and KSS degree. Used to find the most "extreme" value.
#

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--network-kls-degree", help="Filename for network KLS degree",
                    action="store", type="string", dest="l")
parser.add_option("-s", "--network-kss-degree", help="Filename for network KSS degree",
                    action="store", type="string", dest="s")
parser.add_option("-p", "--pcc-values", help="Filename for PCC values",
                    action="store", type="string", dest="pcc")

# reads the degrees from a file
def read_degree(filename):
    f = open(filename, "r")
    degree = {}
    for line in f:
        # split by tab
        (i, gene, deg) = tuple(line.split("\t"))
        # save only gene and degree
        degree[gene] = int(deg.strip())
    f.close()
    return degree

# reads the pcc values from a file
def read_pcc(filename):
    f = open(filename, "r")
    pcc = {}
    for line in f:
        # split by tab
        (i, gene, pcc_value) = tuple(line.split("\t"))
        # save only gene and degree
        pcc[gene] = float(pcc_value.strip())
    f.close()
    return pcc
    
def main():
    (options, args) = parser.parse_args()
    if not options.l: parser.error("Must specify filename for network KLS degree")
    if not options.s: parser.error("Must specify filename for network KSS degree")
    if not options.pcc: parser.error("Must specify filename for PCC values")

    degree_l = read_degree(options.l)
    degree_s = read_degree(options.s)
    pcc = read_pcc(options.pcc)

    print("Index\tGene\tPCC\tKLS Degree\tKSS Degree")
    i = 0
    for gene in pcc:
        l = degree_l[gene] if gene in degree_l else 0
        s = degree_s[gene] if gene in degree_s else 0
        print("%s\t%s\t%s\t%s\t%s" % (i, gene, pcc[gene], l, s))
        i += 1

if __name__ == "__main__":
    main()
