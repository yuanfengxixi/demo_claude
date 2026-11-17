---
name: transcribe-local-media
description: Transcribe a local video or audio file into text and SRT subtitles with xhs-video-transcribe. Use when the user asks for subtitles or a transcript. This skill does not download media or access logged-in websites.
---

# Transcribe local media

Use the `xhs-video-transcribe` CLI to transcribe a local file. The CLI writes a plain-text transcript and an SRT subtitle file.

## Input boundary

- The user must provide a local video or audio file path.
- If the user provides only a webpage URL, explain that this plugin does not download media or use browser login sessions. Ask them to provide a local file they are allowed to process.
- Never upload the media or transcript to another service. Transcription runs with the user's local faster-whisper installation.
- Do not install tools or download a model without the user's approval. faster-whisper may download model weights on first use; when cache status is unknown, explain this and ask before invoking the CLI.

## Steps

1. Confirm the input is a local file. Quote the path when running shell commands.
2. Check that `xhs-video-transcribe` is available with `command -v xhs-video-transcribe` (PowerShell: `Get-Command xhs-video-transcribe`).
3. If the user specified a language, model, or output directory, pass the matching `--language`, `--model`, or `--out-dir` option. Otherwise use the CLI defaults.
4. Run `xhs-video-transcribe "<local-file>"` and wait for completion.
5. Report the exact `.txt` and `.srt` paths printed by the CLI. If asked for a summary, read the transcript and make clear that speech recognition can be inaccurate.

## Prerequisites

- Python 3.11 or newer
- The `xhs-video-transcribe` package from [the public repository](https://github.com/yuanfengxixi/xhs-video-transcribe)
- `ffmpeg` for video and non-WAV audio files
- A faster-whisper model download on first use
