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
| **`ADR.md`** | Architecture Decision Records บันทึกการตัดสินใจเชิงสถาปัตยกรรมและข้อตกลง API |
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

### 🏷️ Two-Row API Header & Legal Disclaimer Release (Version: 2026-10-16)
- **Two-Row API Header Structure:**
  - ปรับโครงสร้างหัวการ์ด API ทุกรายการ (13 Core Endpoints และ 3 Webhooks) ใน `docs.html` เป็นแบบลำดับชั้น 2 บรรทัด (Two-Row Hierarchy)
  - บรรทัดที่ 1 (Title): แสดงลำดับ, ชื่อ endpoint ในรูปแบบ badge code, และคำอธิบายภาษาไทย (เช่น `1. /get-auth ขอ JWT Bearer Token`)
  - บรรทัดที่ 2 (Meta): แสดง Method Badge, Full Production URL (เช่น `https://publicapi.traffy.in.th/exchange-api/get-auth/v1`), และ Auth Method Badge อย่างเป็นสัดส่วน
  - เพิ่ม CSS Classes `.api-card-header-top`, `.api-card-title`, `.api-card-header-bottom` ใน `css/style.css` รองรับ Responsive เต็มรูปแบบ
- **Platform Service Provider & Content Liability Disclaimer:**
  - เพิ่มแบนเนอร์ข้อกำหนดการใช้งานและข้อสงวนสิทธิ์ความรับผิดชอบใน `docs.html` (`#sec-disclaimer`), `index.html` (`#disclaimer`), `docs/overview.md`, `README.md`, และ `openapi.yaml`
  - ชี้แจงบทบาทของ Traffy Fondue และ สวทช. ในฐานะผู้ให้บริการระบบเทคโนโลยีสารสนเทศตัวกลาง โดยความรับผิดชอบต่อเนื้อหาตกอยู่แก่ผู้แจ้งเหตุ เจ้าหน้าที่ผู้ดำเนินการ และผู้นำข้อมูลไปใช้ต่อโดยตรง
- **Raw Uncensored Data Caution & PDPA Compliance:**
  - เพิ่มคำเตือนระบุว่าข้อมูลที่ได้รับผ่าน Exchange API เป็นข้อมูลดิบที่ไม่ผ่านการเซนเซอร์ (Uncensored)
  - กำชับให้ผู้ใช้งานระมัดระวังการเผยแพร่ออกสู่สาธารณะ และต้องทำ Data Masking / Redaction ข้อมูลส่วนบุคคลตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA)
- **Architecture Decision Record (ADR-009):**
  - บันทึกการตัดสินใจเชิงสถาปัตยกรรมเรื่อง Two-Row API Header และ Legal Disclaimer ลงใน [`ADR.md`](ADR.md)

### 🛠️ Response Alignment & Navigation Single Source of Truth (Version: 2026-10-12)
- **Single Source of Truth for API Versioning:**
  - ถอดเลขเวอร์ชัน (`/v1`, `/v2`) ออกจากลิงก์เมนูนำทางด้านซ้าย (`.docs-sidebar-nav`) ใน `docs.html` คงเหลือเฉพาะชื่อ Resource หลัก (เช่น `/get-issues`, `/get-issue`, `/new-issue`)
  - กำหนดให้การ์ดรายละเอียดของแต่ละ API เป็นจุดระบุเวอร์ชันและควบคุมเวอร์ชันเพียงจุดเดียว (Single Source of Truth) เพื่อลดความซ้ำซ้อนและป้องกันการแก้ไขเวอร์ชันตกหล่นในอนาคต
- **Live Response & Webhook Schema Alignment:**
  - อัปเดตตัวอย่าง Response JSON ใน `docs.html` (ทั้งสำหรับ Action APIs และ Webhook Events เช่น `new-issue`, `update-issue`, `star`, `comment`, `join-forward`) ให้ตรงกับข้อมูลจริงที่เซิร์ฟเวอร์ตอบกลับมา
- **Parameter Validation & Documentation Accuracy:**
  - ตรวจสอบ Input Parameters ของทุก Endpoint เทียบกับซอร์สโค้ดจริงใน `exchange-api-php` ยืนยันว่า `GET /get-issue/v2` รับเฉพาะ `ticket_id` และไม่รองรับ `client_ticket_id` พร้อมปรับคำอธิบายให้ถูกต้องตรงกัน
- **Architecture Decision Record (ADR-008):**
  - บันทึกการตัดสินใจเชิงสถาปัตยกรรมเรื่อง Single Source of Truth สำหรับ Versioning ใน UI ลงใน [`ADR.md`](ADR.md)

### 🧪 Live API Verification & Contract Alignment Release (Version: 2026-10-05)
- **End-to-End Live Testing:** ทำการทดสอบยิง API จริงครบทุก Endpoint (14 APIs: Authentication, Query, Action) ผ่านระบบอัตโนมัติ ผลลัพธ์ผ่านทั้งหมด 100% (HTTP 200 OK)
- **`POST /exchange-api/get-auth/v1` Contract Alignment:**
  - ปรับปรุง JSON Schema ของ `results` ให้เป็น `object` (จากเดิมระบุเป็น `array[object]`) ให้ตรงกับพฤติกรรมจริงของ API
  - อัปเดต Client SDK ใน `examples/python/client.py` และ `examples/nodejs/client.js` ให้ดึง Token จาก Object อย่างถูกต้องและปลอดภัย
- **`GET /exchange-api/get-issue/v2` Official Adoption:**
  - กำหนดให้ `/get-issue/v2` เป็น Primary Endpoint สำหรับการดึงข้อมูลเรื่องแจ้งรายใบ
  - อัปเดตโครงสร้างฟิลด์ใหม่: `status_th_latest`, คีย์ชื่อหน่วยงาน `name` ใน `orgs[]`, `issue_category_id`, `issue_status_id`, `status_en`, `is_follow`, และ `is_forward`
  - คง `/get-issue/v1` ไว้ใน `openapi.yaml` พร้อมระบุ `deprecated: true` เพื่อความเข้ากันได้ย้อนหลัง (Backward Compatibility)
- **`GET /exchange-api/get-org-list/v1` Best Practice Guidance:**
  - ระบุคำแนะนำให้นักพัฒนาส่ง `?org_id={org_id}` เสมอ เพื่อป้องกันปัญหา PHP Warning รั่วไหลออกมาก่อน JSON Payload เมื่อไม่ระบุ Parameter
- **`POST /exchange-api/join-forward/v1` Schema Refinement:**
  - ปรับสถานะพารามิเตอร์ `origin_group` เป็น Optional (เซิร์ฟเวอร์จะอ้างอิงจากหน่วยงานของ Token เจ้าของบัญชีให้อัตโนมัติ)
  - ปรับปรุง Response Example และ Schema ให้ตรงกับผลลัพธ์จริง (`results: []`)
- **`POST /exchange-api/comment/v1` Context Clarification:**
  - เพิ่มคำอธิบายความแตกต่างของ `comment_type`: `"comment"` สำหรับความเห็นประเมินความพึงพอใจ และ `"chat"` สำหรับการสนทนากับประชาชนผ่าน SMS
- **Architecture Decision Records (ADR):**
  - เพิ่มเอกสาร [`ADR.md`](ADR.md) บันทึกเหตุผลการตัดสินใจทางสถาปัตยกรรม (ADR-001 ถึง ADR-007)
- **Code & Specs Synchronization:**
  - ตรวจทานและอัปเดต `docs.html`, `openapi.yaml`, `README.md`, `OKF.md`, `CONTEXT.md`, และ `docs/*.md` ให้สอดคล้องกันทุกส่วน

### 🚀 Exchange API (v2) Release (Version: 2026-09-26)
- **`GET /exchange-api/get-issues/v2` & `GET /exchange-api/download-issues/v2`:**
  - **ปรับปรุง Parameter `duration`:** `today` *(Default - ย้อนหลัง 1 วัน)*, `3days` / `3day` *(ย้อนหลัง 3 วัน)*, `all` *(ดึงทั้งหมด สูงสุด 5,000 รายการ)*
  - **เพิ่ม Parameter Filter หมวดหมู่/ประเภทเรื่อง:** `type_name_th` (รองรับ alias: `type_name`, `category_name_th`, `category_name`), `issue_category_id`, `org_category_id` *(โดย `type_name_th` มีความสำคัญสูงสุดและไม่สนใจ category ID อื่นหากระบุ)*
  - **เพิ่ม Parameter Filter ติดตาม/ส่งต่อ:** `is_follow` (Boolean - ติดตามเรื่อง), `is_forward` (Boolean - ส่งต่อเรื่อง)
- **`GET /exchange-api/get-type-list/v2`:**
  - `org_id` parameter รับเป็น Integer เดี่ยวเท่านั้น (ไม่รองรับ Comma-separated)
  - นำฟิลด์ `org_id` ออกจากแต่ละ Object ใน `results`, รวมหมวดหมู่กลางและเฉพาะหน่วยงานไว้ใน `results[]` (6 ฟิลด์: `type`, `type_en`, `issue_category_id`, `org_category_id`, `photo`, `index`), กรองเฉพาะ `is_active = true`
- **`GET /exchange-api/get-status-list/v2`:**
  - `org_id` parameter รับเป็น Integer เดี่ยวเท่านั้น
  - เปลี่ยนชื่อฟิลด์เป็น `status` และ `status_en`, เพิ่มฟิลด์ `status_type`, ปรับ `is_active` เป็น Boolean (`true`/`false`), นำฟิลด์ `org_id` ออกจากแต่ละ Object ใน `results`, กรองเฉพาะ `is_active = true`
- **Synchronized Documentation & Code Examples:**
  - อัปเดต OpenAPI 3.0.3 spec (`openapi.yaml`)
  - อัปเดต Interactive Web Portal (`docs.html`)
  - อัปเดต Markdown Documentation (`docs/query-apis.md`, `README.md`, `OKF.md`, `docs/overview.md`)
  - อัปเดต Script และ Client Examples (`examples/curl/get_issues.sh`, `examples/nodejs/client.js`, `examples/python/client.py`)

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
