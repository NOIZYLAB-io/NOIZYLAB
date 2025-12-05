import onnxruntime as ort

def inference(model_path):
    inference = ort.InferenceSession(model_path, providers=["QNNExecutionProvider"])
    return inference