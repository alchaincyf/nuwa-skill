#!/bin/bash
# 从YouTube视频下载字幕
# 用法: ./download_subtitles.sh <YouTube_URL> [输出目录]
# 优先下载人工字幕，无人工字幕则下载自动生成字幕
# 语言优先级：中文 > 英文 > 其他
# 输出 SRT 或 VTT（YouTube 通常只提供 VTT），两种格式 srt_to_transcript.py 都能处理

set -e

URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    echo "用法: ./download_subtitles.sh <YouTube_URL> [输出目录]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

# 每次尝试先下载到独立的临时目录，确保只认本次新下载的文件
WORK_DIR=$(mktemp -d)
trap 'rm -rf "$WORK_DIR"' EXIT

# 用法: try_download <yt-dlp字幕参数> <语言列表>
# 下载成功则把字幕移到输出目录并打印路径，否则返回非零
try_download() {
    rm -rf "${WORK_DIR:?}"/*
    yt-dlp "$1" --sub-langs "$2" --sub-format "srt/vtt/best" --skip-download \
        -o "$WORK_DIR/%(title)s" "$URL" >/dev/null 2>&1 || true
    local file
    file=$(find "$WORK_DIR" -type f \( -name "*.srt" -o -name "*.vtt" \) | head -1)
    [ -n "$file" ] || return 1
    mv "$file" "$OUTPUT_DIR/"
    echo "$OUTPUT_DIR/$(basename "$file")"
}

echo ">>> 检查可用字幕..."
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20 || true

echo ""
echo ">>> 尝试下载人工字幕（中文优先）..."

# 尝试1: 人工中文字幕
if FOUND=$(try_download --write-subs "zh-Hans,zh-Hant,zh,zh-CN,zh-TW"); then
    echo "✅ 下载成功: $FOUND"
    exit 0
fi

# 尝试2: 人工英文字幕
echo ">>> 无中文人工字幕，尝试英文..."
if FOUND=$(try_download --write-subs "en,en-US,en-GB"); then
    echo "✅ 下载成功: $FOUND"
    exit 0
fi

# 尝试3: 自动生成字幕（中文优先）
echo ">>> 无人工字幕，尝试自动生成字幕..."
if FOUND=$(try_download --write-auto-subs "zh-Hans,zh,en"); then
    echo "✅ 自动字幕下载成功: $FOUND"
    exit 0
fi

echo "❌ 未找到任何可用字幕"
exit 1
