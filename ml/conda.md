# 基础知识
conda 主要解决的是python环境的问题。在不同的python代码依赖项可能发生冲突，这时候用conda可以最小化的解决冲突问题。

# 任务

## 添加镜像源
```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```

## 查看镜像源
```shell
conda config --get channels
```

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

## 升级软件
```shell
conda update numpy
```

- 使用conda-forge的升级包
```shell
conda update -c conda-forge numpy
```

或者
```shell
conda update --all
```

## 清空未使用的包和缓存
```shell
conda clean -a
```

## 清空环境的所有包并且删除环境
```shell
conda remove --all
```
对于删除base会报错：
```shell
conda remove -n base --all
CondaEnvironmentError: cannot remove root environment, add -n NAME or -p PREFIX option
```

## 让一个环境回归初始状态
```shell
conda install --revision 0
```

## 查看一个安装包的版本
```shell
conda list -f tensorflow
```

# 常见问题

## [ ] 老是提示新版本存在？
```shell
$ conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 23.7.4
  latest version: 23.11.0

Please update conda by running

    $ conda update -n base -c defaults conda

Or to minimize the number of packages updated during conda update use

     conda install conda=23.11.0


# All requested packages already installed.
```
诡异的问题，暂时没有解决。
conda在mac上的问题还挺多。