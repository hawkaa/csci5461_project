from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--network-kls-degree", help="Filename for network KLS degree",
                    action="store", type="string", dest="l")
parser.add_option("-s", "--network-kss-degree", help="Filename for network KSS degree",
                    action="store", type="string", dest="s")
parser.add_option("-p", "--pcc-values", help="Filename for PCC values",
                    action="store", type="string", dest="pcc")
parser.add_option("-d", "--degree-cutoff", help="Degree cutoff, will keep genes above this value, inclusive",
                    action="store", type="int", dest="degree_cutoff")
parser.add_option("-c", "--pcc-cutoff", help="PCC cutoff, will keep genes with pcc below this cutoff.",
                    action="store", type="float", dest="pcc_cutoff")

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


def merge_and_discard_degree(degree_a, degree_b, cutoff):
    merged = {}
    
    # merge phase
    for gene in set(degree_a.keys()).union(degree_b.keys()):
        # get gene degree
        a_degree = degree_a[gene] if gene in degree_a else 0
        b_degree = degree_b[gene] if gene in degree_b else 0
        # save as tuple
        merged[gene] = (a_degree, b_degree)

    #discard phase
    degree = {}
    for gene in merged:
        # keep only if one of them is above cutoff
        if merged[gene][0] >= cutoff or merged[gene][1] >= cutoff:
            degree[gene] = merged[gene]
    return degree

def pcc_discard(pcc, cutoff):
    discarded = {} 
    for gene in pcc:
        if pcc[gene] <= cutoff:
            discarded[gene] = pcc[gene]
    
    return discarded

def merge_pcc_degree(pcc, degree):
    merged = {}
    for gene in set(pcc.keys()).intersection(degree.keys()):
        merged[gene] = (pcc[gene], degree[gene][0], degree[gene][1])
    return merged

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
    if not options.degree_cutoff: parser.error("Must specify degree cutoff")
    if not options.pcc_cutoff: parser.error("Must specify pcc cutoff")

    degree_l = read_degree(options.l)
    degree_s = read_degree(options.s)
    degree = merge_and_discard_degree(degree_l, degree_s, options.degree_cutoff)
    pcc_full = read_pcc(options.pcc)
    pcc_discarded = pcc_discard(pcc_full, options.pcc_cutoff)

    merged = merge_pcc_degree(pcc_discarded, degree)
    print_merged(merged)




if __name__ == "__main__":
    main()
