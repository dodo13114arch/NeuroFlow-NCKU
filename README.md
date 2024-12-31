# NeuroFlow -NCKU

## Todo List
on personal github

- Not-project-specific workflow

Project Structure
 - overview
 - methods
    - Not-project-specific workflow -> [knowledge base](https://kb.rccn.dev)
    - project workflow
 - Result

## Abstract Table

## Overview

## How to use NeuroFlow 

# Core technique on Knowledge base

## Compas-Eve !!! 

How to use compas eve in brief.

## Compas RPC ???

## Ollama in Grasshopper 

How to intergrate llm into grasshopper through ollama, gh python.

### 參考資料 Reference 

[chatGPTinGrasshopper by SerjoschDuering](https://github.com/SerjoschDuering/chatGPTinGrasshopper)

[Note](https://www.notion.so/Note-1027-14c57755feb98111bd7be8d9cb0b03bf?pvs=4#14c57755feb981a2803bd5256e9315ce)

### 

### 操作方式

1. 在Grasshopper Convas中創建一個GHPython Component
2. 開啟編輯器並輸入以下程式碼 
    ```
    """GHPython Component
    输入：
        prompt: 要傳給给 Ollama API 的用户提示
        model_name: 要使用的 Ollama 模型（例如，'llama2'）
        max_tokens: 響應的最大 tokens 數（默認為 800）
    输出：
        response: API 返回的文字
    """

    import json
    import rhinoscriptsyntax as rs
    import scriptcontext as sc
    import Grasshopper as gh
    import Rhino.Geometry as rg
    import System
    import time

    from System.Net import WebRequest, WebException
    from System.Text import Encoding
    from System.IO import StreamReader

    def call_ollama(prompt, model_name="llama3.1", max_tokens=800, retries=3, retry_delay=5):
        """调用 Ollama API 并返回响应内容。"""

        url = "http://localhost:11434/api/generate"

        payload = {
            "model": model_name,
            "prompt": prompt,
            "stream": False,  
            "options": {
                "max_tokens": max_tokens
            }
        }

        json_data = json.dumps(payload)
        bytes_data = Encoding.UTF8.GetBytes(json_data)

        for attempt in range(retries):
            try:
                # 设置 HTTP 请求
                request = WebRequest.Create(url)
                request.Method = "POST"
                request.ContentType = "application/json"

                # 写入数据到请求流
                with request.GetRequestStream() as stream:
                    stream.Write(bytes_data, 0, bytes_data.Length)

                # 获取 API 响应
                response = request.GetResponse()
                response_stream = response.GetResponseStream()

                # 读取响应
                with StreamReader(response_stream) as reader:
                    response_text = reader.ReadToEnd()

                # 打印响应文本以进行调试
                print("Response Text:", response_text)

                # 解析响应
                response_json = json.loads(response_text)
                return response_json['response']

            except WebException as e:
                # 错误处理部分保持不变
                if e.Response and hasattr(e.Response, 'StatusCode') and e.Response.StatusCode == 429:
                    print("429 请求过多。{} 秒后重试...".format(retry_delay))
                    time.sleep(retry_delay)
                else:
                    if e.Response:
                        with StreamReader(e.Response.GetResponseStream()) as reader:
                            error_message = reader.ReadToEnd()
                        print("API 错误: {}".format(error_message))
                    else:
                        print("网络错误: {}".format(e))
                    return None

        print("所有重试均已失败。请稍后再试。")
        return None

    # 调用示例
    response = call_ollama(prompt, model_name, max_tokens)
    a = response  # 将结果传递给输出变量

    ```

