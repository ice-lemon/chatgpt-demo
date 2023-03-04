# 使用 Python Requests 库调用 ChatGPT API 的多轮对话脚本

这是一个 Python 脚本，使用 [requests](https://docs.python-requests.org/en/latest/) 库调用 [ChatGPT](https://github.com/microsoft/DialoGPT) API 进行多轮对话，并且可以添加自定义代理服务器。该脚本可以用于不同场景下的自动化对话，例如客服自动回复、人机对话测试等。

## 如何使用

### 前置条件

在使用该脚本前，你需要拥有一个 ChatGPT API 的访问口令（Token）。可以参考 [ChatGPT API 的文档](https://github.com/microsoft/DialoGPT#access-control) 获取该访问口令。

### 安装依赖

在使用该脚本前，你需要安装 `requests` 库。可以使用以下命令安装：

```sh
pip install requests
```

### 运行脚本

在运行脚本之前，你需要编辑 `chat.py` 文件，配置 ChatGPT API 的访问口令和代理服务器地址（如果需要）。

然后，你可以使用以下命令运行脚本：

```sh
python chat.py
```

该脚本会启动一个命令行界面，你可以在命令行内输入对话内容与 API 进行交互。

### 配置代理服务器

如果你需要使用代理服务器来访问 ChatGPT API，可以在 `config.py` 中进行配置。只需要将 `USE_PROXY` 设置为 True，并在 `PROXY_URL` 中填写代理服务器地址即可。

## 注意事项

1. 在使用 ChatGPT API 进行多轮对话时，需要注意 API 的并发调用限制以及接口响应时间等因素。
2. 在使用自定义代理服务器时，需要注意代理服务器的访问速度和稳定性。
3. 该脚本仅供学习和研究使用，使用时请遵守相关法律法规。
