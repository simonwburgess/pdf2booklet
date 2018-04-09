from PyPDF2 import pdf


def copy_page(page_number, source_pdf, destination_pdf):
    if page_number >= source_pdf.getNumPages():
        destination_pdf.addPage(pdf.PageObject.createBlankPage(source_pdf))
    else:
        destination_pdf.addPage(source_pdf.getPage(page_number))
    print(".", end="")


def get_page_order(source_pdf):
    pages_required = source_pdf.getNumPages() + (4 - source_pdf.getNumPages()) % 4
    blocks = int(pages_required / 4)
    evens = range(2, pages_required, 2)
    odds = range(1, pages_required, 2)
    pages = []
    middle_page = 0

    for block in range(blocks):
        pages.append(pages_required - odds[block])
        pages.append(middle_page)
        middle_page += 1
        pages.append(middle_page)
        middle_page += 1
        pages.append(pages_required - evens[block])

    return pages
