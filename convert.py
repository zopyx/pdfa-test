import os

variants= ["PDF", "PDFA1A", "PDFA1B", "PDFA2A", "PDFA2B", "PDFA2U", "PDFA3A", "PDFA3B", "PDFA3U", "PDFX1A_2001", "PDFX1A_2003", "PDFX3_2002", "PDFX3_2003", "PDFX4"]

for variant in variants:
    print variant
    cmd = '/opt/PDFreactor8/bin/pdfreactor.py --conformance {} -i html/index.html -o out_{}.pdf'.format(variant, variant)
    os.system(cmd)
