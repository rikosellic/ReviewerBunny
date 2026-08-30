# -*- coding: utf-8 -*-
import os
d = r'C:\Users\66419\Desktop\审稿skill\ReviewerBunny'
print('dir exists:', os.path.exists(d))
for f in os.listdir(d):
    print(repr(f))
