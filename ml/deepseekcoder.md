# deepseek coder

## 基础知识
deepseek coder在验证过几轮后，发现最对我们胃口，对于逻辑和代码的微调效果比起他模型更好。
美中不足的是只有7b和33b，没有13b这样的大小。
导致在apple电脑上用llama-factory来微调，只能微调7b的，33b直接爆OOM。

## 任务场景

## 常见问题

## 实验
### mlx微调33b
用llama-factory来微调33b直接爆OOM，因为没有量化，只能fp32，导致内存爆满，即便把批次大小改成1，还是如此。

思路：
- 下载33b的模型：目前只有`mlx-community/deepseek-coder-33b-instruct-hf-4bit-mlx`可用，其他的都提示`No safetensors found`，参考[mlx](mlx.ipynb)
- 准备数据：生成
```json
{"text":"<｜begin▁of▁sentence｜>你是华顺信安公司开发的助理机器人，名叫FOFABot。你要帮助用户解答所有关于fofa的任何问题。\n### Instruction:\n回答如下关于fofa的问题。```fofa网址是？```\n### Response:\nfofa网址是：https:\/\/fofa.info\n<|EOT|>"}
```
- mlx微调
```shell
# cp *.jsonl ~/PycharmProjects/cheatsheet/ml/data
python -m mlx_lm.lora --model mlx-community/deepseek-coder-33b-instruct-hf-4bit-mlx --train --data ./data --adapter-file fofabot_deepseek_33b.npz --learning-rate 5e-5
```
- mlx生成验证
```shell
python -m mlx_lm.lora --model mlx-community/deepseek-coder-33b-instruct-hf-4bit-mlx --adapter-file fofabot_deepseek_33b.npz --prompt "<｜begin▁of▁sentence｜>你是华顺信安公司开发的助理机器人，名叫FOFABot。你要帮助用户解答所有关于fofa的任何问题。
### Instruction:
回答如下关于fofa的问题。
fofa网址是？
### Response:
"
```
