from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # အပေါ်ဆုံးမှာ Import လုပ်ပါ
from my_parser import execute_mc 

app = FastAPI()

# ဤနေရာတွင် ထည့်ပါ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# Data structure အတွက် Class တစ်ခုဆောက်မယ်
class CodeRequest(BaseModel):
    code: str

@app.post("/run-code")
def run_code(request: CodeRequest):
    try:
        result = execute_mc(request.code)
        return {"status": "success", "output": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}