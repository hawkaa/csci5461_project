from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--network-a-degree", help="Filename for network A degree",
                    action="store", type="string", dest="a")
parser.add_option("-b", "--network-b-degree", help="Filename for network B degree",
                    action="store", type="string", dest="b")
parser.add_option("-p", "--pcc-values", help="Filename for PCC values",
                    action="store", type="string", dest="pcc")
parser.add_option("-d", "--degree-cutoff", help="Degree cutoff, will keep genes above this value, inclusive",
                    action="store", type="int", dest="degree_cutoff")
parser.add_option("-c", "--pcc-cutoff", help="PCC cutoff, will keep genes with pcc below this cutoff.",
                    action="store", type="float", dest="pcc_cutoff")

def main():
    (options, args) = parser.parse_args()
    if not options.a: parser.error("Must specify filename for network A degree")
    if not options.b: parser.error("Must specify filename for network B degree")
    if not options.pcc: parser.error("Must specify filename for PCC values")
    if not options.degree_cutoff: parser.error("Must specify degree cutoff")
    if not options.pcc_cutoff: parser.error("Must specify pcc cutoff")


if __name__ == "__main__":
    main()
