# Ollama調用，包含對話歷史(另存於csv中)

``` python
import json
import csv
import os  # 用來檢查檔案是否存在
import time  # 用來延遲重試
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Grasshopper as gh
import Rhino.Geometry as rg

from System.Net import WebRequest, WebException
from System.Text import Encoding
from System.IO import StreamReader

def load_conversation_history(csv_file):
    """從指定的 CSV 檔案讀取對話歷史，如果檔案不存在則回傳空列表。"""
    if not os.path.exists(csv_file):
        print("[DEBUG] 沒有找到對話歷史檔案，將建立新的檔案。")
        return []  # 如果檔案不存在，回傳空對話歷史

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        history = [{"role": row[0], "content": row[1]} for row in reader]
        print("[DEBUG] 讀取到 {} 筆對話歷史。".format(len(history)))
        return history

def save_conversation_history(history, csv_file):
    """將對話歷史儲存到指定的 CSV 檔案中。"""
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        for message in history:
            writer.writerow([message["role"], message["content"]])
    print("[DEBUG] 已儲存 {} 筆對話歷史。".format(len(history)))

def format_conversation_history(history):
    """將對話歷史格式化為字串，供 API 使用。"""
    formatted = "\n".join(["{}: {}".format(msg["role"], msg["content"]) for msg in history])
    print("[DEBUG] 格式化的對話歷史:\n{}".format(formatted))
    return formatted

def call_ollama(prompt, csv_file, model_name, max_tokens, retries=3, retry_delay=5):
    """呼叫 Ollama API 並回傳回應內容。"""

    url = "http://localhost:11434/api/generate"

    # 讀取之前的對話歷史
    conversation_history = load_conversation_history(csv_file)

    # 添加新的使用者輸入到對話歷史
    conversation_history.append({"role": "user", "content": prompt})
    print("[DEBUG] 已新增使用者輸入: {}".format(prompt))

    # 將對話歷史格式化為字串
    formatted_prompt = format_conversation_history(conversation_history)

    payload = {
        "model": model_name,
        "prompt": formatted_prompt,
        "stream": False,
        "max_tokens": max_tokens
    }

    json_data = json.dumps(payload)
    bytes_data = Encoding.UTF8.GetBytes(json_data)

    for attempt in range(retries):
        try:
            # 設定 HTTP 請求
            print("[DEBUG] 發送 API 請求...")
            request = WebRequest.Create(url)
            request.Method = "POST"
            request.ContentType = "application/json"

            # 寫入資料到請求流
            with request.GetRequestStream() as stream:
                stream.Write(bytes_data, 0, bytes_data.Length)

            # 獲取 API 回應
            response = request.GetResponse()
            response_stream = response.GetResponseStream()

            # 讀取回應
            with StreamReader(response_stream) as reader:
                response_text = reader.ReadToEnd()

            # 解析回應
            response_json = json.loads(response_text)
            assistant_response = response_json['response']
            print("[DEBUG] 接收到助理回應: {}".format(assistant_response))

            # 將助理的回應加入對話歷史
            conversation_history.append({"role": "assistant", "content": assistant_response})

            # 將更新後的對話歷史儲存到 CSV 檔案
            save_conversation_history(conversation_history, csv_file)

            return assistant_response

        except WebException as e:
            # 錯誤處理保持不變
            if e.Response and hasattr(e.Response, 'StatusCode') and e.Response.StatusCode == 429:
                print("[DEBUG] 429 請求過多。{} 秒後重試...".format(retry_delay))
                time.sleep(retry_delay)
            else:
                if e.Response:
                    with StreamReader(e.Response.GetResponseStream()) as reader:
                        error_message = reader.ReadToEnd()
                    print("[DEBUG] API 錯誤: {}".format(error_message))
                else:
                    print("[DEBUG] 網路錯誤: {}".format(e))
                return None

    print("[DEBUG] 所有重試均已失敗。請稍後再試。")
    return None

# 使用 Toggle 判斷是否執行 API 呼叫
if start:  # 當 Toggle 為 True 時觸發 API 呼叫
    print("[DEBUG] 開始 API 呼叫...")
    Response = call_ollama(prompt, csv_file, model_name, max_tokens=max_output_length)
else:
    Response = "等待 Toggle 觸發..."  # 當 Toggle 為 False 時的輸出
    print("[DEBUG] Toggle 未啟動。")
```