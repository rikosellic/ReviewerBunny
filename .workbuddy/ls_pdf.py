# -*- coding: utf-8 -*-
import os
import unicodedata

d = r'C:\Users\66419\Desktop\审稿skill\ReviewerBunny'
for f in os.listdir(d):
    if f.lower().endswith('.pdf'):
        print('RAW repr:', repr(f))
        print('NFC repr:', repr(unicodedata.normalize('NFC', f)))
        print('NFD repr:', repr(unicodedata.normalize('NFD', f)))
        print('exists NFC path:', os.path.exists(os.path.join(d, unicodedata.normalize('NFC', f))))
        print('exists raw path:', os.path.exists(os.path.join(d, f)))
