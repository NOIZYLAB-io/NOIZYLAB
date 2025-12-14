# Optimized ONNX Runtime Inference Session Initialization

This function initializes an ONNX Runtime inference session with the specified model path, optimized for reuse and clarity.

## Improvements
- Renamed the variable `inference` to `session` to avoid confusion with the function name.
- Added optional parameter to specify providers, defaulting to `["QNNExecutionProvider"]`.
- Added basic error handling to catch initialization issues.
- Added docstring for clarity.

## Code

```python
import onnxruntime as ort

def create_inference_session(model_path, providers=None):
    """
    Create an ONNX Runtime inference session.

    Args:
        model_path (str): Path to the ONNX model file.
        providers (list, optional): List of execution providers to use. Defaults to ["QNNExecutionProvider"].

    Returns:
        ort.InferenceSession: Initialized inference session.

    Raises:
        RuntimeError: If the session initialization fails.
    """
    if providers is None:
        providers = ["QNNExecutionProvider"]
    try:
        session = ort.InferenceSession(model_path, providers=providers)
    except Exception as e:
        raise RuntimeError(f"Failed to create inference session: {e}")
    return session