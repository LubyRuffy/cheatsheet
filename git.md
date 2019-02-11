# 基础知识

# 任务场景
* 撤销未提交的所有修改：
```bash
git checkout . #撤销未提交的所有修改
git checkout <filepath>  #撤销单个未提交的修改
```

* 撤销前一次 commit:
```bash
git revert HEAD
```

* 如何处理error: Your local changes to the following files would be overwritten by merge错误
 如果系统中有一些配置文件在服务器上做了配置修改,然后后续开发又新添加一些配置项的时候,在发布这个配置文件的时候,会发生代码冲突。
```bash
git reset --hard # 可以直接用服务器的代码
git checkout HEAD <filepath> # 也可以针对单个文件
```

* 命令行记住密码
```bash
git config --global credential.helper store
```

* 从仓库删除但是保留本地文件：
```bash
git rm --cached -r somedir
```

* https提示证书错误
 第一次clone的情况下：
```bash
env GIT_SSL_NO_VERIFY=true git clone https://host_name/git/project.git
```
 已经clone的情况下：
```bash
git config http.sslVerify "false"
```
对于可信任的自签名的证书最好采用倒入证书为可信的方式，避免引入安全问题。

* 如何导出文件不带git信息？
```bash
git archive master | gzip > latest.tgz
```

* 如何将当前的修改提交位新的分支？
有时候你在master分支进行了代码修改，但是不想提交到master，就可以这么做：
```bash
git checkout -b newbranch
git add <files>
git commit -m "<Brief description of this commit>"
```

* 如何只查看某个目录下的branch不同？
```bash
git diff <branch1> <branch2> -- ./testdir
```

# 常见问题
* clone与fetch的区别在哪？

* fetch与pull的区别在哪？
pull相当于fetch+merge。


* git怎么发音？
git读法是/‘gi·tʌb/
