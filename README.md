# IRSystem

安装solr
cd到目录下
solr.cmd start 启动
solr.cmd create -c test1创建核心!
我把文件都上传在test1，test2用来查看增删效果
使用example文件夹里面的post.jar工具将指定目录文件post上去
java -jar -Dc=test1 -Dauto example\exampledocs\post.jar example\P1docs
P1docs里面就是上次爬的json
打开localhost 8393就能看到solr的界面
在左边下拉框可以切换core
左边栏里query可以查， documents可以增加文件（修改文件只要上传一个id相同的文件就行）

安装django
运行
