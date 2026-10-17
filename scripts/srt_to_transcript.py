#!/usr/bin/env python3
"""
将SRT/VTT字幕文件清洗为干净的纯文本transcript。
去除时间戳、序号、重复行、HTML标签，输出可直接阅读的文本。

用法:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]

如果不指定输出文件，默认输出到 input_transcript.txt
"""

import sys
import re
from pathlib import Path


# Windows consoles commonly default stdout to a legacy code page (GBK/CP936 on
# zh-CN systems). This script prints emoji and CJK text, which raises
# UnicodeEncodeError there and aborts the run before any result is shown.
# Force UTF-8 output; degrade gracefully if the stream cannot be reconfigured.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


def clean_srt(content: str) -> str:
    """清洗SRT格式字幕"""
    lines = content.strip().split('\n')
    texts = []

    for line in lines:
        line = line.strip()
        # 跳过序号行（纯数字）
        if re.match(r'^\d+$', line):
            continue
        # 跳过时间戳行
        if re.match(r'\d{2}:\d{2}:\d{2}', line):
            continue
        # 跳过空行
        if not line:
            continue
        # 去除HTML标签
        line = re.sub(r'<[^>]+>', '', line)
        # 去除VTT的position标记
        line = re.sub(r'align:.*$|position:.*$', '', line).strip()
        if line:
            texts.append(line)

    # 去重（自动字幕常有连续重复行）
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    # 合并成段落：连续的短句合并，遇到句末标点或长停顿换行
    result = []
    current = []

    for text in deduped:
        current.append(text)
        # 如果当前累积文本够长或遇到句末标点，形成一个段落
        joined = ' '.join(current)
        if len(joined) > 200 or re.search(r'[。！？.!?]$', text):
            result.append(joined)
            current = []

    if current:
        result.append(' '.join(current))

    return '\n\n'.join(result)


def clean_vtt(content: str) -> str:
    """清洗VTT格式字幕（先去掉VTT头部，然后按SRT逻辑处理）"""
    # 去掉WEBVTT头部
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    # 去掉NOTE块
    content = re.sub(r'NOTE.*?\n\n', '', content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    if len(sys.argv) < 2:
        print("用法: python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"❌ 文件不存在: {input_path}")
        sys.exit(1)

    # 默认输出文件名
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    # 读取并检测格式
    content = input_path.read_text(encoding='utf-8')

    if input_path.suffix.lower() == '.vtt' or content.startswith('WEBVTT'):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding='utf-8')

    # 统计
    word_count = len(transcript)
    line_count = transcript.count('\n') + 1
    print(f"✅ 转换完成: {output_path}")
    print(f"   字数: {word_count}  段落数: {line_count}")


if __name__ == '__main__':
    main()
