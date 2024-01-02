# 基础知识
conda 主要解决的是python环境的问题。在不同的python代码依赖项可能发生冲突，这时候用conda可以最小化的解决冲突问题。

# 任务

## 列出所有环境
```shell
conda env list
```

## 创建环境
```shell
 conda create -n llama2
```

## 删除环境
```shell
conda remove -n llama2 --all
```

## 安装软件
```shell
conda install numpy
```

# 常见问题