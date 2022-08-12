# DDL 摸大鱼-智能创作平台
体验账户为：
``` json
username: user1
password: user1
```

## 部署步骤
> 以下假设服务器拥有 GPU 设备
- 根据 Pytorch 支持的 CUDA 版本、显卡类型和系统来安装 GPU 驱动。
- 安装 docker 和 nvidia-docker。
- `docker-compose up && docker-compose build`，即可一键建立前后端（用户需要根据自己的平台在 `Dockerfile` 文件中修改拉取的镜像地址）。

## 模型文件

模型文件应文件放在 `modayu/deploy/saved_models` 中。
