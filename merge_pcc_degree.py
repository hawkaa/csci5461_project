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



def print_merged(merged):
    print("Index\tGene\tPCC\tKLS Degree\tKSS Degree")
    i = 0
    for gene in merged:
        print("%s\t%s\t%s\t%s\t%s" % (i, gene, merged[gene][0], merged[gene][1], merged[gene][2]))
        i += 1
    
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
        try:
            print("%s\t%s\t%s\t%s\t%s" % (i, gene, pcc[gene], degree_l[gene], degree_s[gene]))
            i += 1
        except:
            pass



if __name__ == "__main__":
    main()
