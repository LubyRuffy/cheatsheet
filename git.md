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

* 如何将当前的代码提交位新的项目？
```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin git@<gitserver>:<project_url>.git
git push -u origin --all
git push -u origin --tags
```

* 如何只查看某个目录下的branch不同？
```bash
git diff <branch1> <branch2> -- ./testdir
```

* 如何查看某个文件修改历史纪录，并且找到某行代码对应的历史行数
用于分析漏洞：
```bash
file=dubbo-rpc/dubbo-rpc-http/src/main/java/org/apache/dubbo/rpc/protocol/http/HttpProtocol.java; \
content='RpcContext.getContext'; \
    git log $file | grep commit | awk '{print $2}' | \
    xargs -n 1 -I{} sh -c "git show {}:$file | grep $content -n"
```

* 如何clone到指定目录？
```bash
mkdir -p /project/path/
git clone https://host_name/git/project.git /project/path/
```
一个典型的场景比如go项目，我们希望从github下载到go/src对应的目录下面，咱们可以这样：
```bash
echo https://github.com/macronut/phantomsocks | awk -F'//' '{print $2}' | xargs -I{} git clone https://{} `go env GOPATH`/src/{}
```

* 删除本地和云端的tag？
```bash
git tag -d v0.0.1
git push --delete origin v0.0.1
```

* windows下msys2的git用LF而不是CR+LF
```bash
git config --global core.autocrlf false
git config --global core.eol lf
```
对于已经git clone到本地的仓库，可以这么操作：
```
git ls-files -z | xargs -0 rm
git checkout .
```
这种方式最常见的场景是：windows下clone的代码，在linux下执行./bootstrap会报错提示```-bash: ./bootstrap: /bin/sh^M: bad interpreter: No such file or directory```

* `git clone --recurse-submodules`失败后如何把子模块重新下载？
`fatal: clone of 'https://github.com/xxx/xxx' into submodule path 'xxx/xxx' failed`
```shell
git submodule update
```

* 合并分支到主分支
```shell
# 先切换到主分支
git checkout main
# 合并分子
git merge branch1
git push
```

# 常见问题
* clone与fetch的区别在哪？

* fetch与pull的区别在哪？
pull相当于fetch+merge。

* git怎么发音？
git读法是/‘gi·tʌb/

* warning: refname 'develop' is ambiguous.
```bash
git fetch --prune
git pull origin develop
```
