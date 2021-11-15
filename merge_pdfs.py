from PyPDF2 import PdfFileMerger

pdfs = ['pdf_files/gross_income_vs_staking.pdf', 'pdf_files/transactions_vs_fees.pdf', 'pdf_files/avg_cost_per_transaction.pdf']

pdf_merger = PdfFileMerger()

for pdf in pdfs:
    pdf_merger.append(pdf)

pdf_merger.write('merged_dashboard.pdf')
pdf_merger.close()
