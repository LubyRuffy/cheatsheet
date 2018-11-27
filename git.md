# 基础知识

# 任务场景
* 撤销未提交的所有修改：
```bash
git checkout .
```

* 撤销单个未提交的修改：
```bash
git checkout filepath
```

* 撤销前一次 commit: "git revert HEAD".
* error: Your local changes to the following files would be overwritten by merge错误，如果系统中有一些配置文件在服务器上做了配置修改,然后后续开发又新添加一些配置项的时候,在发布这个配置文件的时候,会发生代码冲突。直接用服务器的代码："git checkout HEAD filepath"，也可以所有文件："git reset --hard"
* 命令行记住密码：git config --global credential.helper store
* 从仓库删除但是保留本地文件：git rm --cached -r somedir
* https提示证书错误
 第一次clone的情况下：
 env GIT_SSL_NO_VERIFY=true git clone https://<host_name/git/project.git
 已经clone的情况下：git config http.sslVerify "false” 

# 常见问题