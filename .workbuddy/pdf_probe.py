# -*- coding: utf-8 -*-
import pymupdf
import os

PDF = r'C:\Users\66419\Desktop\调试统计\【教材】高级心理统计 刘红云.pdf'
print('exists:', os.path.exists(PDF), '| size:', os.path.getsize(PDF) if os.path.exists(PDF) else 0)
doc = pymupdf.open(PDF)
print('Total pages:', doc.page_count)

# Check text vs image on sample pages
for p in [0, 4, 11, 15, 30, 100, 200, 300, 400, 433]:
    page = doc[p]
    txt = page.get_text().strip()
    imgs = page.get_images()
    print(f'page {p+1}: text_len={len(txt)}, images={len(imgs)}')
    if txt:
        print('   preview:', txt[:120].replace('\n', ' '))
