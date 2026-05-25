from huggingface_hub import snapshot_download
from paddleocr import PaddleOCR

snapshot_download(
    repo_id="Qwen/Qwen2.5-7B-Instruct-GGUF",
    local_dir=".",
    allow_patterns="*Q4_K_M*.gguf"
)

ocr = PaddleOCR(lang='en')