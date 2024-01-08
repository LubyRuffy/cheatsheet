# 基础知识
机器学习需要了解Python以及transformers、pytorch、tensorflow等等大量基于python的生态，为了学习和记录方便，我们都会使用ipynb的格式的文档，这种文档对应的工具就是jupyter。

jupyter可以记录code和markdown文本知识，最方便的是可以在编辑过程中运行代码，并且实时把返回内容保存到文件中，这样方便学习者了解完整的过程。

## 安装
```shell
pip install jupyterlab
```

## 启动
```shell
jupyter lab
```
如果运行失败，提示`Running as root is not recommended. Use --allow-root to bypass.`，说明是在root环境下启动，需要加上参数运行：
```shell
jupyter lab --allow-root
```

## 快捷键
分为两种模式，一种是在一个单元格Cell内这种叫编辑模式，一种是聚焦不在单元格内这种叫命令模式。通过ESC的方式从编辑模式跳到命令模式。

### 通用快捷键
| 快捷键      | 说明           |
|----------|--------------|
| SHIFT+回车 | 执行当前当前单元格的内容 |


### 命令模式快捷键
| 快捷键           | 说明                       |
|---------------|--------------------------|
| CTRL+SHIFT+H  | 调出快捷键帮助页面                |
| 上下            | 切换Cell选中                 |
| D+D           | 删除                       |
| A             | 上面插入Cell                 |
| B             | 下面插入Cell                 |
| C             | 复制Cell                   |
| X             | 剪切Cell                   |
| 回车            | 切换到编辑模式                  |
| CTRL+SHIFT+上下 | 把当前的单元格往上下挪动             |
| M/Y           | M切为markdown格式，Y切换为code格式 |
| SHIFT+上下      | 多选单元格                    |
| SHIFT+M       | 合并单元格                    |

## [输出技巧](jupyter.ipynb)


# 任务

# 常见问题

## 报错：Jupyter command `jupyter-notebook` not found.
```shell
conda install notebook

或者
pip install notebook
```