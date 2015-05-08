import camoco as co

# read refgen
ZMFGS = co.RefGen("Zm5bFGS")

# create KLS network
ZmTissueNetwork = co.COB.from_table(
       'data/splits/KSS.txt',
       'KSS_T', # Dataset Name
       'Co-expression network for all KLS annotated samples', # Short Description
       ZMFGS, #A RefGen instance
       rawtype='RNASEQ', # Expression datatype, either 'RNASEQ' or 'MICROARRAY'
       max_gene_missing=0.4, # See Expr._quality_control
       min_expr=0.1,  # See Expr._quality_control
       quantile=False,  # See Expr._quality_control
       dry_run=False,  # See Expr._quality_control
       sep=',', # table is comma seperated
       max_val=300, # See Expr._normalize
)

