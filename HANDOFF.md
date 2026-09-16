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
| **`index.html`** | หน้าแรก Landing Page / Developer Portal แนะนำภาพรวมและ Onboarding Flow |
| **`docs.html`** | Interactive API Documentation แบบละเอียด ครอบคลุม 13 Endpoints + 2 Webhooks พร้อม Search & Filter, Collapsible Schemas, และ Code Copy |
| **`css/style.css`** | Modern Responsive Design System (Clean UI, Glassmorphism, Theme Variables) |
| **`js/app.js`** | ฟังก์ชัน Interactive (Live Search, ScrollSpy Navigation, Copy-to-Clipboard) |
| **`README.md`** | หน้าแรกของ Repository สรุป Quick API Reference, Quickstart, และโครงสร้างโปรเจกต์ |
| **`OKF.md`** | Objectives, Key Results และ System Knowledge Framework |
| **`CONTEXT.md`** | สถาปัตยกรรมการเชื่อมต่อ, Data Schemas, และ Security Principles |
| **`HANDOFF.md`** | เอกสารส่งมอบงาน บันทึกการปรับปรุง และแนวทางการต่อยอด |
| **`openapi.yaml`** | สเปกมาตรฐาน OpenAPI 3.0.3 สำหรับนำเข้า Swagger / Postman หรือใช้สร้าง SDK |
| **`docs/overview.md`** | สรุปภาพรวมและ Onboarding Flow 4 ขั้นตอน (Synchronized จาก Notion) |
| **`docs/authentication.md`**| รายละเอียดการเรียก `get-auth`, JWT Header, และการจัดการโควต้า |
| **`docs/query-apis.md`** | เอกสาร API ดึงข้อมูล (`get-issues`, `get-issue`, `download-issues`, `search-org`, ฯลฯ) |
| **`docs/action-apis.md`** | เอกสาร API ส่งข้อมูลและอัปเดต (`new-issue`, `update-issue`, `star`, `comment`, `join-forward`) |
| **`docs/webhooks.md`** | เอกสาร Real-time Webhook Specification (New Issue POST & Status Update PATCH) |
| **`docs/error-codes.md`** | รหัสข้อผิดพลาดและการแก้ปัญหา (Troubleshooting) |
| **`examples/`** | ตัวอย่างโค้ดพร้อมรันสำหรับ cURL, Python Client SDK, และ Node.js Client SDK |

---

## 3. บันทึกการปรับปรุงล่าสุด (Latest Updates & Changelog)

### ⚠️ Webhook Loop Prevention Warning (`docs/webhooks.md`, `docs.html`)
- **Loop Prevention Notes:** เพิ่มข้อความเน้นตัวหนาสีแดงเตือนห้ามส่งข้อมูลจาก Webhook วนกลับเข้ามาที่ API `new-issue` และ `update-issue` เพื่อป้องกัน Infinite Data Loop
- **System Framework & Architecture:** บันทึกข้อกำหนด Webhook Loop Prevention ลงใน `OKF.md` และ `CONTEXT.md`

### 🎨 UI/UX Refactoring ของหน้า Interactive Documentation (`docs.html`)
- **Request Body & Query Parameters:** ปรับเป็น Toggle ที่ **เปิดแสดงไว้เป็นค่าเริ่มต้น (Open by default)** เพื่อให้นักพัฒนาเห็นฟิลด์ที่ต้องส่งได้ทันทีโดยไม่ต้องคลิกเปิด
- **cURL Example:** เปิดแสดงเป็นค่าเริ่มต้นพร้อมปุ่ม **Copy** เพื่อความสะดวกในการคัดลอกไปทดสอบคำสั่งทันที
- **Response Example (200 OK):** สลับลำดับมาอยู่ **ก่อนหน้า** JSON Output Parameters และซ่อนไว้ใน Toggle **(Closed by default)** พร้อมปุ่ม **Copy** ในส่วน Header เพื่อให้หน้าเว็บดูสะอาด ไม่รก แต่ยังสามารถเปิดดูและคัดลอก Response ตัวอย่างได้ง่าย
- **JSON Output Parameters:** จัดวางต่อจาก Response Example ในแบบ Toggle **(Closed by default)**
- **Webhooks:** ปรับ Incoming Payload ให้เปิดเป็นค่าเริ่มต้น และเพิ่มปุ่ม **Copy** ให้กับ Incoming Payload Sample ทุกตัว พร้อมระบุคำเตือน Loop Prevention
- **Sidebar Group Navigation (หมวด 1-5):** ปรับหัวข้อตัวเลขหมวดหมู่ 1, 2, 3, 4, 5 ที่แถบเมนูด้านซ้ายและเมนูมือถือ ให้เป็นลิงก์ Anchor (`<a href="#sec-...">`) พร้อมเอฟเฟกต์ Hover และกำหนด `scroll-margin-top` เพื่อให้คลิกแล้ว Scroll ไปยังหัวข้อหมวดหมู่นั้นๆ ได้อย่างราบรื่นและแม่นยำ ไม่ถูก Header ทับ
- **Fluid Full-Width Layout:** ขยาย Container ให้เป็น 100% Full-Width รองรับหน้าจอทุกขนาด (ตั้งแต่โน้ตบุ๊ก, Full HD ไปจนถึงจอ 2K/4K) ตารางพารามิเตอร์มีพื้นที่กว้างขวาง อ่านง่าย ไม่ถูกบีบ
- **Mobile Sticky Nav Clearance & Table Scroll:** ปรับ `scroll-margin-top` บน Mobile/Tablet ให้คำนวณเผื่อทั้ง Fixed Header และ Sticky Dropdown Bar (ข้ามไปแล้วไม่โดนเมนูบังหัวข้อการ์ด) พร้อมเพิ่ม `min-width` ให้ตารางเลื่อนแนวนอนได้ ไม่บีบตัวอักษรแตกแถว

---

## 4. ขั้นตอนการนำไปต่อยอดและพัฒนาต่อ (Next Steps & Recommendations)

1. **Deploy Swagger UI / Redoc Documentation Site:**
   * สามารถใช้ `openapi.yaml` ในการสร้าง Static Docs Site (เช่น ผ่าน GitHub Pages, Redocly, หรือ Docusaurus)
2. **Postman Collection Export:**
   * นำ `openapi.yaml` ไป Import เข้า Postman เพื่อสร้าง Official Postman Collection และแจกจ่ายให้กับ Partner
3. **Automated SDK Generation:**
   * ใช้ OpenAPI Generator เพื่อคอมไพล์ Client SDK ในภาษาต่างๆ (เช่น Go, Java, C#, PHP) อัตโนมัติใน CI/CD
4. **การประสานงานการขอสิทธิ์และการแก้ไข:**
   * สำหรับการเพิ่มฟีเจอร์หรือแก้ไข Endpoint ให้ปรับปรุงทั้งใน `docs.html`, Markdown และ `openapi.yaml` ควบคู่กันเสมอ
