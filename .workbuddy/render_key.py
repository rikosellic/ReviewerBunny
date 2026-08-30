# -*- coding: utf-8 -*-
import pymupdf
import os

PDF = r'C:\Users\66419\Desktop\调试统计\【教材】高级心理统计 刘红云.pdf'
OUT = r'C:\Users\66419\Desktop\审稿skill\ReviewerBunny\.workbuddy\pages'
os.makedirs(OUT, exist_ok=True)
doc = pymupdf.open(PDF)

# 印刷页 X -> PDF页 = X+14. 渲染关键节段(前言 + 各章"值得注意的问题" + 重要方法节)
pages_to_render = [
    # 前言(印刷3-10)
    5,6,7,8,9,10,
    # Ch1 §1 目的(印刷1), §2 极端(印刷1-4), §3 缺失(印刷5-10), §4 假设(印刷11-16)
    15,16,17,18,
    19,20,21,22,23,24,
    25,26,27,28,29,30,
    # Ch3 §7-8 回归注意与局限(印刷71-75)
    85,86,87,88,89,
    # Ch4 §4 Logistic注意(印刷91)
    105,
    # Ch6 §5 聚类注意(印刷120)
    134,
    # Ch7 §6 因素分析注意(印刷146-148)
    160,161,162,
    # Ch8 §4 数据搜集/参数估计(印刷180-182), §5 模型评价/修正(印刷183-186)
    194,195,196,197,198,199,200,
    # Ch8 §8 等价性检验(印刷200-209)
    214,215,216,217,218,219,220,
    # Ch9 §7 路径注意(印刷232)
    246,
    # Ch10 §5-6 SEM注意与局限(印刷250-256)
    264,265,266,267,268,269,270,
    # Ch11 §5 中介注意(印刷284-289)
    298,299,300,301,302,303,
    # Ch12 各小节首段
    317,318,319,320,321,322,  # §3 显变量调节
    331,332,333,334,335,336,  # §4 潜变量调节
    350,351,352,353,354,355,  # §5 有调节的中介
    359,360,361,362,363,364,  # §6 有中介的调节
    # Ch13 §4 多层线性注意(印刷364-365)
    378,379,
    # Ch14 §3 追踪研究注意(印刷388)
    402,
]

# 去重保持顺序
seen = set()
ordered = []
for p in pages_to_render:
    if p not in seen:
        seen.add(p)
        ordered.append(p)

for p in ordered:
    if p-1 >= doc.page_count: continue
    page = doc[p-1]
    pix = page.get_pixmap(dpi=160)
    fp = os.path.join(OUT, f'page_{p:03d}.png')
    pix.save(fp)
print('rendered', len(ordered), 'pages')
