# -*- coding: utf-8 -*-
import os

d = r'C:\Users\66419\Desktop\审稿skill\ReviewerBunny'
for f in os.listdir(d):
    b = f.encode('utf-8')
    print(len(f), 'chars |', b.hex())
    print('   repr:', repr(f))
