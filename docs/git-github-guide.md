# دليل Git وGitHub للفريق

## 1. التثبيت والإعداد الأولي

ثبّت Git ثم افتح Terminal أو PowerShell داخل مجلد المشروع. نفّذ:

```bash
git --version
git config --global user.name "اسمك الحقيقي"
git config --global user.email "بريدك المرتبط بـ GitHub"
```

## 2. إنشاء المستودع المحلي

```bash
cd ProductStudio
git init
git add .
git commit -m "chore: initialize ProductStudio project"
git branch -M main
```

## 3. إنشاء مستودع GitHub

من GitHub اختر **New repository**، واكتب اسمًا مثل:

```text
se-lab-team-01-productstudio
```

اختر Private أو Public حسب تعليمات المدرس، ولا تنشئ README إضافيًا إذا كان موجودًا في الحزمة.

## 4. ربط المشروع ورفعه

استبدل الرابط التالي برابط مستودعكم:

```bash
git remote add origin https://github.com/USERNAME/se-lab-team-01-productstudio.git
git push -u origin main
```

إذا طلب GitHub تسجيل الدخول، استخدم GitHub Desktop أو Personal Access Token بدل كلمة المرور العادية.

## 5. إضافة أعضاء الفريق

من صفحة المستودع افتح **Settings → Collaborators → Add people**، ثم أضف حسابي العضوين الآخرين. بعد ذلك أنشئوا GitHub Project Board بالأعمدة:

```text
Backlog | Ready | In Progress | In Review | Done
```

## 6. دورة تنفيذ كل مهمة

ابدأ من Issue موجود في `docs/kanban.md`، ثم أنشئ فرعًا مستقلًا:

```bash
git checkout main
git pull origin main
git checkout -b feature/image-transform
```

نفّذ التغيير، ثم راجع الملفات واختبرها:

```bash
git status
git diff
git add frontend backend docs
git commit -m "feat: add image transform operations"
git push -u origin feature/image-transform
```

افتح Pull Request من GitHub، واربطه بالـ Issue، واطلب من عضو آخر مراجعته. بعد الموافقة والاختبار اضغط **Merge pull request**، ثم أغلق الـ Issue.

## 7. تحديث الفرع بعد الدمج

```bash
git checkout main
git pull origin main
git branch -d feature/image-transform
```

## 8. أنواع الفروع والرسائل

| الاستخدام | اسم الفرع المقترح | رسالة Commit |
|---|---|---|
| خاصية جديدة | `feature/...` | `feat: ...` |
| إصلاح خطأ | `bugfix/...` | `fix: ...` |
| توثيق | `docs/...` | `docs: ...` |
| اختبار | `test/...` | `test: ...` |
| تحسين داخلي | `refactor/...` | `refactor: ...` |

## 9. أخطاء شائعة

لا تعملوا جميعًا على `main` مباشرة، ولا ترفعوا مجلد `.venv` أو `node_modules` أو الصور الكبيرة أو مفاتيح API. إذا تعارضت التغييرات، نفّذ `git pull`، عالج العلامات التي تظهر في الملفات، ثم نفّذ `git add` و`git commit` و`git push` من جديد.

## 10. التسليم للمدرس

أرسل رابط المستودع، وتأكد أن README يشرح التشغيل، وأن `docs/SRS.md` و`AI_Log.md` موجودان، وأن لوحة Project تحتوي مهامًا موزعة على أكثر من عمود، وأن Pull Requests وIssues مرتبطة بالمتطلبات.
