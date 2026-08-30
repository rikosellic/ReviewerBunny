# ReviewerBunny — 心理学/临床心理/医学审稿专家 Skill

## 已完成（初版）

以 SCI 期刊同行评审人身份，对心理学、临床心理学、医学领域的论文稿件进行结构化审稿，输出审稿意见报告。

### 文件结构

```
ReviewerBunny/
├── SKILL.md                                    # 核心：角色定位、6 步审稿流程、审稿报告模板、推荐意见判定标准
└── references/
    ├── reporting-guidelines.md                 # 各类研究报告规范索引（CONSORT/STROBE/PRISMA/STARD/TRIPOD/COREQ/CARE/SPIRIT/JARS 等）
    └── statistics-checklist.md                 # 统计学方法学检查清单（11 类 + 审稿红旗）
```

### 设计要点

1. **渐进式披露**：SKILL.md 承载核心工作流（< 5k 词），领域知识下沉到 references 按需加载。
2. **研究类型 → 报告规范映射**：审稿的本质是「对照标准」，映射表是 skill 的灵魂。
3. **不编造铁律**：所有意见以原文为依据，缺什么标什么。
4. **意见分级**：Major（影响结论可信度）vs Minor（表述/格式），每条意见 = 问题 + 为何重要 + 建议 + 定位。
5. **推荐意见判定标准**：Accept / Minor Revision / Major Revision / Reject，给出可执行阈值。

### 后续可扩展方向

- `references/domain-psychometrics.md`：心理测量专项（量表信效度、临界值、文化适应）。
- `references/reviewer-ethics.md`：审稿伦理与 COPE 规范。
- `assets/review-report.docx`：Word 版审稿报告模板。
- `scripts/`：PDF 稿件解析辅助脚本（如需要）。
