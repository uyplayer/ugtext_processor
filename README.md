## OpenUyTTS
**Build a minimal Uyghur TTS pipeline**

> 注意：仓库中的 `conf/coqui_vits_train.yaml` 配置仅为简化示例，并非 Coqui TTS 官方完整配置。

### 配置说明

最小必需字段包括：

- `model`
- `output_path`
- `run_name`
- `batch_size`
- `eval_batch_size`
- `learning_rate`
- `epochs`
- `datasets`（`formatter`、`meta_file_train`、`meta_file_val`、`path`）
- `audio`（`sample_rate`、`fft_size`、`hop_length`、`win_length`、`mel_channels`）

完整配置参考请查看 [Coqui TTS 官方文档](https://tts.readthedocs.io/en/latest/configuration.html) 或本仓库的 `conf` 目录。

如需使用高级功能（如自定义优化器、调度器等），可在配置中新增相应字段，例如：

```yaml
optimizer:
  type: adam
  params:
    betas: [0.9, 0.98]

lr_scheduler:
  type: exponential
  params:
    gamma: 0.995
```

