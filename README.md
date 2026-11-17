# demo_claude

A small Claude Code plugin that connects the `/local-media-transcribe:transcribe` skill to the public [`xhs-video-transcribe`](https://github.com/yuanfengxixi/xhs-video-transcribe) CLI.

## Install prerequisites

- Install Claude Code and sign in.
- Install the public CLI and its Python dependencies: `python -m pip install "git+https://github.com/yuanfengxixi/xhs-video-transcribe.git@v0.1.0"`.
- Install `ffmpeg` for video and non-WAV audio inputs.
- faster-whisper downloads the selected model on first use if it is not already cached. The skill asks before running when this download may be needed.

This plugin does not download Xiaohongshu content, access browser sessions, or upload media. It operates only on a local file path that the user provides.

## Try the plugin

From this repository's root, load the plugin for one Claude Code session:

```sh
claude --plugin-dir .
```

Then invoke the skill with a local file path:

```text
/local-media-transcribe:transcribe ./video.mp4
```

The skill asks the CLI for a transcript and SRT file, then reports the paths printed by the CLI. It does not automatically summarize or publish the result.

To validate the manifest and skill metadata with Claude Code itself, run `claude plugin validate .`.

The plugin directory and skill layout follow the [official plugin](https://code.claude.com/docs/en/plugins/create) and [skill](https://code.claude.com/docs/en/skills) documentation.

## Validate the package

```sh
python scripts/validate_plugin.py
python -m compileall -q scripts
```

The CI checks the plugin manifest, skill frontmatter, public CLI reference, and absence of the private downloader path. It does not require Claude authentication or download a transcription model.

## License

MIT. See [LICENSE](LICENSE).
