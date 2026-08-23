from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

app = FastAPI(title="ProductStudio API", version="0.1.0")
ALLOWED = {"image/png", "image/jpeg", "image/webp"}
MAX_BYTES = 10 * 1024 * 1024

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "ProductStudio"}

@app.post("/api/images/upload")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED:
        raise HTTPException(400, "صيغة الصورة غير مدعومة")
    data = await file.read()
    if len(data) > MAX_BYTES:
        raise HTTPException(413, "حجم الصورة أكبر من الحد المسموح")
    try:
        image = Image.open(BytesIO(data))
        image.verify()
    except Exception as exc:
        raise HTTPException(400, "الملف ليس صورة سليمة") from exc
    return {"filename": file.filename, "content_type": file.content_type, "width": image.width, "height": image.height}

@app.post("/api/images/adjust")
async def adjust_image(file: UploadFile = File(...), brightness: float = 1.0, contrast: float = 1.0, saturation: float = 1.0):
    data = await file.read()
    try:
        image = Image.open(BytesIO(data)).convert("RGBA")
    except Exception as exc:
        raise HTTPException(400, "تعذر قراءة الصورة") from exc
    image = ImageEnhance.Brightness(image).enhance(max(0, brightness))
    image = ImageEnhance.Contrast(image).enhance(max(0, contrast))
    image = ImageEnhance.Color(image).enhance(max(0, saturation))
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return StreamingResponse(output, media_type="image/png")

@app.post("/api/images/transform")
async def transform_image(file: UploadFile = File(...), rotate: int = 0, flip_horizontal: bool = False, flip_vertical: bool = False):
    data = await file.read()
    try:
        image = Image.open(BytesIO(data)).convert("RGBA")
    except Exception as exc:
        raise HTTPException(400, "تعذر قراءة الصورة") from exc
    if rotate % 360:
        image = image.rotate(-rotate, expand=True)
    if flip_horizontal:
        image = ImageOps.mirror(image)
    if flip_vertical:
        image = ImageOps.flip(image)
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)
    return StreamingResponse(output, media_type="image/png")
