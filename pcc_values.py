import camoco as co
import numpy as np
import scipy.stats as st
import sys


def main():
    
    # Load both the co-expression networks into memory
    KLS = co.COB("KLS")
    KSS = co.COB("KSS")

    # Get the genes from each co-expression network and create an intersection
    common_genes = np.intersect1d(KLS._expr.index.values, KSS._expr.index.values)

    # Calculate the length of the genes they have in common
    length = len(common_genes)

    # allocate array for pearson correlation coefficients
    pcc = np.zeros(length)

    # iterate over every gene
    for i in range(length):
        
        # reset scores for kls and kss
        kls_score = np.zeros(length)
        kss_score = np.zeros(length)

        # fill these arrays with score values by querying the co-expression network database
        for j in range(length):
            # skip same index
            if i == j: continue

            # get co-expression scores from the networks
            kls_score[j] = KLS.coexpression_base(common_genes[i], common_genes[j])["score"]
            kss_score[j] = KSS.coexpression_base(common_genes[i], common_genes[j])["score"]

        # calculate the pearson correlation coefficient
        (pcc[i], p_value) = st.pearsonr(kls_score, kss_score)
        
        # print the values in a tab separated manner
        msg = "%s\t%s\t%s" % (i, common_genes[i], pcc[i])
        print(msg)
        print(msg, file=sys.stderr)


if __name__ == "__main__":
    main()
