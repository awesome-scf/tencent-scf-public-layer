# tencent-scf-public-layer

此项目用于提供可以在腾讯云 SCF 云函数中使用的公共依赖库，并以层的形式进行包装。

通过选择部署所需的层，可以快速使用到难以自行下载、打包的依赖库。

依赖库的封装使用 serverless framework 的 layer component，可以在依赖库目录下使用 sls deploy 快速将依赖库安装到账号的层下。