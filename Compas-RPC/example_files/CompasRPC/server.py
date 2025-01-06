import numpy as np

def add_arrays(array1, array2):
    try:
        # 在終端顯示Debug用訊息
        print("Received array1:", array1)
        print("Received array2:", array2)
        return np.add(array1, array2).tolist()
    except Exception as e:
        # 捕捉錯誤並列印詳細資訊
        print("Error in add_arrays:", str(e))
        raise
