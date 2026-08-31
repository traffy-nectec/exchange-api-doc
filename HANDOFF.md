# Project Handoff Documentation

เอกสารส่งมอบงาน (Handoff Documentation) สำหรับวิศวกรซอฟต์แวร์, Technical Writer, และผู้ดูแลระบบที่จะเข้ามารับช่วงต่อในการพัฒนา บำรุงรักษา และเผยแพร่เอกสาร **Traffy Fondue Exchange API**

---

## 1. ข้อมูลกรรมสิทธิ์และ Repositories (Project Ownership)

- **GitHub Repository:** [https://github.com/traffy-nectec/exchange-api-doc](https://github.com/traffy-nectec/exchange-api-doc)
- **Organization:** `traffy-nectec`
- **Default Branch:** `main`
- **Visibility:** Private (สำหรับองค์กรและผู้พัฒนาที่ได้รับสิทธิ์)
- **หน่วยงานเจ้าของโครงการ:** ศูนย์เทคโนโลยีอิเล็กทรอนิกส์และคอมพิวเตอร์แห่งชาติ (NECTEC) / สำนักงานพัฒนาวิทยาศาสตร์และเทคโนโลยีแห่งชาติ (สวทช.)

---

## 2. โครงสร้างและเนื้อหาสำคัญที่ส่งมอบ (Delivered Artifacts)

| ไฟล์ / ไดเรกทอรี | รายละเอียด |
| :--- | :--- |
| **`README.md`** | หน้าแรกของ Repository สรุป Quick API Reference, Quickstart, และโครงสร้างโปรเจกต์ |
| **`OKF.md`** | Objectives, Key Results และ System Knowledge Framework |
| **`CONTEXT.md`** | สถาปัตยกรรมการเชื่อมต่อ, Data Schemas, และ Security Principles |
| **`HANDOFF.md`** | เอกสารส่งมอบงานและแนวทางการต่อยอด |
| **`openapi.yaml`** | สเปกมาตรฐาน OpenAPI 3.0.3 สำหรับนำเข้า Swagger / Postman หรือใช้สร้าง SDK |
| **`docs/overview.md`** | สรุปภาพรวมและ Onboarding Flow 4 ขั้นตอน (Synchronized จาก Notion) |
| **`docs/authentication.md`**| รายละเอียดการเรียก `get-auth`, JWT Header, และการจัดการโควต้า |
| **`docs/query-apis.md`** | เอกสาร API ดึงข้อมูล (`get-issues`, `get-issue`, `download-issues`, `search-org`, ฯลฯ) |
| **`docs/action-apis.md`** | เอกสาร API ส่งข้อมูลและอัปเดต (`new-issue`, `update-issue`, `star`, `comment`, `join-forward`) |
| **`docs/webhooks.md`** | เอกสาร Real-time Webhook Specification (New Issue POST & Status Update PATCH) |
| **`docs/error-codes.md`** | รหัสข้อผิดพลาดและการแก้ปัญหา (Troubleshooting) |
| **`examples/`** | ตัวอย่างโค้ดพร้อมรันสำหรับ cURL, Python Client SDK, และ Node.js Client SDK |

---

## 3. ขั้นตอนการนำไปต่อยอดและพัฒนาต่อ (Next Steps & Recommendations)

1. **Deploy Swagger UI / Redoc Documentation Site:**
   * สามารถใช้ `openapi.yaml` ในการสร้าง Static Docs Site (เช่น ผ่าน GitHub Pages, Redocly, หรือ Docusaurus)
2. **Postman Collection Export:**
   * นำ `openapi.yaml` ไป Import เข้า Postman เพื่อสร้าง Official Postman Collection และแจกจ่ายให้กับ Partner
3. **Automated SDK Generation:**
   * ใช้ OpenAPI Generator เพื่อคอมไพล์ Client SDK ในภาษาต่างๆ (เช่น Go, Java, C#, PHP) อัตโนมัติใน CI/CD
4. **การประสานงานการขอสิทธิ์และการแก้ไข:**
   * สำหรับการเพิ่มฟีเจอร์หรือแก้ไข Endpoint ให้ปรับปรุงทั้งใน Markdown และ `openapi.yaml` ควบคู่กันเสมอ
