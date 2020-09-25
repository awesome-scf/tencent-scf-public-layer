# tencent scf pycryptodome layer

此项目提供在腾讯云 SCF 中创建 pycryptodome 层

## 使用方式

1. 升级最新的 serverless framework 命令行工具
2. 在项目根目录下使用 `sls deploy` 命令，部署层。所需的层的名称可以在 serverless.yml 中根据需要修改
3. 在函数中绑定层，并按 `import Crypto` 引用库的方式引用并使用

### 测试

可以在测试目录下使用 `sls deploy` 命令部署测试函数，并通过调用测试函数验证依赖库的有效性。

如果部署层时修改了层的名称，需要对等修改测试目录下的 serverless.yml 文件，layer 配置指向正确的名称和版本。

## 项目说明

* src 目录保存 3.9.8 版本的 pycryptodome
* test 目录保存测试用函数，可以在测试目录
