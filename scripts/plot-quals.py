import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

quals = [record.qual for record in VariantFile(snakemake.input[0]) if record.qual is not None]
plt.hist(quals)
plt.xlabel("Quality score")
plt.ylabel("Variant count")
plt.title("Variant Quality Distribution")

plt.savefig(snakemake.output[0])
