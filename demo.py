import requests
# 用于存储API返回的上下文
class gpt:
    def send_request(self,messages):
        # 设置代理服务器的地址和端口
        proxies = {
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
        }
        # ChatGPT API的URL
        url = "https://api.openai.com/v1/chat/completions"
        # ChatGPT API的访问密钥
        api_key = "【在这输入 ChatGPT API的访问密钥】"
        # 请求参数
        parameters = {
                      "model": "gpt-3.5-turbo-0301", #gpt-3.5-turbo-0301
                      "messages":messages# [{"role": "user", "content": context}]
                    }
        # 请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        # 发送请求
        response = requests.post(url, headers=headers, json=parameters, proxies=proxies)

        # 解析响应
        if response.status_code == 200:
            data = response.json()
            text = data["choices"][0]["message"]

            return text
        else:
            print(response)
            return "Sorry, something went wrong."

    def start_conversation(self,messages):
        print("Welcome to ChatGPT! How can I help you today?")

        # 进入对话循环
        while True:
            # 获取用户输入
            user_input = input("> ")
            user_message={"role": "user", "content": user_input}
            messages.append(user_message)
            # 发送API请求
            response = self.send_request(messages)
            # 输出API返回内容
            print("助手：",response["content"])
            messages.append(response)
            # 如果API返回的内容包含"goodbye"，则结束对话循环
            if "goodbye" in user_input:
                print("Goodbye!")
                break
if __name__ == '__main__':
    messages=[{"role": "system", "content": "你是一个助手"}] #初始化prompt
    gpt().start_conversation(messages)