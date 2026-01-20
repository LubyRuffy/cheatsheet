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

* 冲突情况下取消合并
```shell
git merge --abort
```

* 如何列出仓库里面的超大文件
有时候不小心提交了很多二进制文件，导致pull很慢，需要列出来并且从仓库中删除
```shell
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print$1}')"

# top 10 的文件会被列出来
91cef7829d4e7f9db95858c9eaed419fecfd374d rawgrab11
431df760285244c658ef3bfbef9f106b14ae50f1 rawgrab.exe
f38200586392bc019917f9069995df76b55b7143 rawgrab0516
0385244e5fb05bbb6c657fc8f149e15f9cda254b cmd/cli/cli
9141c4bc20bab72e5c1f48530e73f130b390a901 rawgrab
2595bd3f7c5b5b6fe4cd43c3ef622dd657ca8eb8 rawgrab
b13145c32fbfc695182b4c970f556eaa1d17342e rawgrab
0f870eeaf25458a24b793527a333b595b2bf7587 rawgrab.exe
8f0fc17bb7f49034476af0c84bee1e42d9783860 grab
3599d57534e2bdba0de9697933abc5055a6c17b1 cmd/grab.exe
```

* 如何查看一个大文件是谁在哪个版本导入进来的？
```shell
git log --diff-filter=A -- rawgrab.exe
```

* 如何删除一个历史版本中的文件？
```shell
git filter-repo --path rawgrab.exe --invert-paths
```
如果报错（Aborting: Refusing to destructively overwrite repo history since this does not look like a fresh clone.），可以先对齐版本再操作：
```shell
git reflog expire --expire=now --all
git gc --prune=now
git filter-repo --path rawgrab.exe --invert-paths
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
