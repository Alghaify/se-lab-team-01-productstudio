# ProductStudio

محرر صور ويب إبداعي لمعالجة صور المنتجات.

## فكرة المشروع
يسمح التطبيق برفع الصور وتحريرها بالقص وتغيير الحجم والدوران والقلب والفلاتر وعمليات البكسل والرسم والطبقات، ثم إزالة الخلفية أو استبدالها بخلفية من مكتبة داخلية وتصدير النتيجة.

## أعضاء الفريق
- عبدالله الجحافي — الواجهة وتجربة المستخدم
- واثق المريسي — معالجة الصور وواجهات API
- ايمن الوهبي — الاختبارات والتوثيق والتكامل

## التقنيات
- Frontend: React / Vite أو HTML-CSS-JavaScript في النسخة التعليمية الأولى.
- Backend: Python + FastAPI.
- Image Processing: Pillow وOpenCV.
- Collaboration: Git وGitHub Issues وGitHub Projects وPull Requests.

## الوثائق
- [وثيقة المتطلبات](docs/SRS.md)
- [قصص المستخدم](docs/user-stories.md)
- [معمارية النظام](docs/architecture.md)
- [حالات الاختبار](docs/test-cases.md)
- [خطة Kanban](docs/kanban.md)
- [خطة التنفيذ](docs/implementation-plan.md)
- [سجل استخدام الذكاء الاصطناعي](AI_Log.md)

## التشغيل السريع

### تشغيل الخلفية
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### تشغيل الواجهة

إذا استُخدم قالب React/Vite:
```bash
cd frontend
npm install
npm run dev
```

النسخة الحالية تحتوي على هيكل بداية وتعليقات TODO؛ يجب إكمال وظائف Canvas، الطبقات، وحفظ الحالة وفق خطة التنفيذ.

## طريقة العمل
ينشئ الفريق Issue، ثم فرعًا مستقلًا، ثم ينفذ التغيير ويرفع Pull Request للمراجعة. لا تُنقل المهمة إلى Done إلا بعد تحقق معايير القبول والاختبار والتوثيق.
