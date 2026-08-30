# -*- coding: utf-8 -*-
import pymupdf
import os

PDF = r'C:\Users\66419\Desktop\调试统计\【教材】高级心理统计 刘红云.pdf'
OUT = r'C:\Users\66419\Desktop\审稿skill\ReviewerBunny\.workbuddy\pages'
os.makedirs(OUT, exist_ok=True)

doc = pymupdf.open(PDF)
# render preface + TOC region (pages 5..14, 0-indexed 4..13) and last metadata page
pages = list(range(4, 14))
for p in pages:
    page = doc[p]
    pix = page.get_pixmap(dpi=150)
    fp = os.path.join(OUT, f'page_{p+1:03d}.png')
    pix.save(fp)
    print('saved', fp, pix.width, 'x', pix.height)
