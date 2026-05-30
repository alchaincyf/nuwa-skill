# 工具辅助与信息获取指南

Phase 1 调研过程中可用的工具和已安装 Skill。

---

## 辅助脚本

### 书籍获取
- Z-Library/LibGen 搜索下载 → 存入 `sources/books/`

### 视频字幕获取

已提供脚本，直接调用：

**Step 1 下载字幕**：
```bash
bash [skill目录]/scripts/download_subtitles.sh <YouTube_URL> [输出目录]
```
- 依赖 `yt-dlp`（安装：`brew install yt-dlp` 或 `pip install yt-dlp`）
- 自动优先人工字幕 → 中文 → 英文 → 自动生成字幕
- 输出 SRT/VTT 文件到指定目录

**Step 2 清洗为纯文本**：
```bash
python3 [skill目录]/scripts/srt_to_transcript.py <input.srt> [output.txt]
```
- 去时间戳、序号、HTML标签、连续重复行
- 输出干净的可阅读 transcript → 存入 `sources/transcripts/`
- 需要 Python 3.6+

**用户提供本地视频文件（无字幕）**：用 gemini-video skill 转写

### 播客
- 搜索 transcript 网站（podcastnotes.org 等）

### 调研摘要生成（Phase 1.5 用）
```bash
python3 [skill目录]/scripts/merge_research.py <skill目录>
```
- 自动扫描 `references/research/01-06.md`，统计来源数、一手/二手占比、关键发现
- 输出 Phase 1.5 检查点的 markdown 表格，无需手动统计

### 质量自检（Phase 4 用）
```bash
python3 [skill目录]/scripts/quality_check.py <SKILL.md路径>
```
- 自动检查6项通过标准：心智模型数量、局限性、表达DNA、诚实边界、内在张力、一手来源占比
- 输出逐项 PASS/FAIL 和总结

---

## 利用已安装的信息获取 Skill

Phase 1 启动前，**主动扫描 `.claude/skills/` 目录**，检查是否有可用于信息获取的 skill。如果有，在调研中优先调用，比 WebSearch 更稳定高效：

| 已安装Skill | 用途 | 调用场景 |
|------------|------|---------|
| `gemini-video` | 分析本地视频文件，提取transcript | 用户提供了视频文件但没有字幕 |
| `web-article-reader` | 精确读取网页文章全文 | 找到重要文章URL时，精确提取而非依赖搜索摘要 |
| `agent-reach` | 多渠道信息获取（17个平台） | 需要从X/Reddit/YouTube等平台获取信息 |
| `huashu-research` | 结构化深度调研 | 需要对某个维度做深度调研而非广撒网 |
| `pdf` | 读取PDF书籍/论文 | 用户提供了PDF格式的一手素材 |

**执行方式**：在 spawn subagent 时，把可用 skill 的名称和用途告知 agent，让 agent 在调研中按需调用。这比让 agent 自己用 WebSearch 摸索效率高得多。
