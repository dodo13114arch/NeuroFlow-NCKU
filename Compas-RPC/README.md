# Compas RPC Example

## Overview

在Grasshopper環境透過CompasRPC調用外部環境Python。

## Step 1 - Environment Setup

1. Miniconda中創建環境

    ```bash
    conda create -n gh_rpc_env python=3.9
    conda activate gh_rpc_env
    ``` 

2. 下載必要模組

    ```bash
    pip install compas numpy
    ```

或直接參考 ` Environment.yml ` 配置


## Step 2 - Python Setup

1. 創建專案資料夾，範例建立在桌面
    ```
    C:\Users\<USERNAME>\Desktop\CompasRPC
    ```

2. 在專案資料夾中建立python ( 範例為 ` server.py ` )
3. 撰寫Python運算內容 
    ```python
    import numpy as np

    def add_arrays(array1, array2):
    array1 = np.array(array1)
    array2 = np.array(array2)
    return (array1 + array2).tolist()
    ```

## Step 3 - RPCServer Setup

1. 終端中導向專案資料夾
    ```bash
    cd C:\Users\<USERNAME>\Desktop\CompasRPC
    ```

2. 終端輸入 
    ```
    python -m compas.rpc.services.default --port 1753
    ```
    此時終端應顯示
    ```
    Starting default RPC service on port 1753...
    Listening with autoreload of modules enabled...
    Press CTRL+C to abort
    ```


## Step 4 - Grasshopper Setup

1. 開啟Grasshopper，使用GHPython Component
2. 撰寫Code
    ```
    from compas.rpc import Proxy
    
    p = Proxy('server') # server對應server.py名稱

    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    result = p.add_arrays(array1, array2)

    a = result
    ```
3. 點擊ghpython內的test 應顯示
    ```
    Debug 訊息 .......
    ```

    
若沒遇到問題，
