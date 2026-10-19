# Traffy Fondue Exchange API Documentation 📘

[![GitHub Pages](https://img.shields.io/badge/Live_Docs-GitHub_Pages-553924?style=for-the-badge&logo=github)](https://traffy-nectec.github.io/exchange-api-doc/)

🌐 **Live Documentation Website:** [https://traffy-nectec.github.io/exchange-api-doc/](https://traffy-nectec.github.io/exchange-api-doc/)

เอกสารและคู่มือการเชื่อมต่อระบบ **Traffy Fondue Exchange API** สำหรับหน่วยงานภายนอกและนักพัฒนาระบบ (Developers & Integrators) ในการส่งข้อมูลเรื่องแจ้งเหตุ ปัญหาเมือง และติดตามสถานะการแก้ไขปัญหากับแพลตฟอร์ม Traffy Fondue

---

## 📑 สารบัญ (Table of Contents)

* [ภาพรวมระบบและขั้นตอนการขอใช้งาน (Overview & Onboarding)](docs/overview.md)
* [การยืนยันตัวตนและการจัดการ Token (Authentication)](docs/authentication.md)
* [API ขอข้อมูลจาก Traffy Fondue (Query APIs)](docs/query-apis.md)
* [API ส่งข้อมูลเข้า Traffy Fondue (Action APIs)](docs/action-apis.md)
* [การส่งข้อมูลแบบ Real-time (Webhooks)](docs/webhooks.md)
* [รหัสข้อผิดพลาดและการแก้ไข (Error Codes & Troubleshooting)](docs/error-codes.md)
* [OpenAPI 3.0 Specification (`openapi.yaml`)](openapi.yaml)
* [ตัวอย่างโค้ดการเชื่อมต่อ (Code Examples)](examples/)
* [กรอบความรู้เชิงระบบและเป้าหมาย (OKF.md)](OKF.md)
* [บันทึกการตัดสินใจเชิงสถาปัตยกรรม (ADR.md)](ADR.md)
* [บริบททางเทคนิคและสถาปัตยกรรม (CONTEXT.md)](CONTEXT.md)
* [เอกสารส่งมอบงานและการต่อยอด (HANDOFF.md)](HANDOFF.md)

---

## ⚡ ตารางสรุป Endpoint ทั้งหมด (Quick API Reference)

**Base URL:** `https://publicapi.traffy.in.th/exchange-api`

| Endpoint | Method | Authentication | คำอธิบาย |
| :--- | :---: | :---: | :--- |
| [`/get-auth/v1`](docs/authentication.md) | `POST` | User/Pass | ขอรับ JWT Bearer Token |
| [`/get-issues/v2`](docs/query-apis.md#1-api-get-issues-ขอรายการเรื่องแจ้ง) | `GET` | Bearer Token | ดึงรายการเรื่องแจ้งของหน่วยงาน (org_id, duration, filters) |
| [`/get-issue/v2`](docs/query-apis.md#2-api-get-issue-ขอรายละเอียดเชิงลึกของเรื่องแจ้ง) | `GET` | Bearer Token | ดึงรายละเอียดเชิงลึกของเรื่องแจ้งราย `ticket_id` |
| [`/download-issues/v2`](docs/query-apis.md#3-api-download-issues-ดาวน์โหลดไฟล์-csv) | `GET` | Bearer Token | ส่งออกข้อมูลเรื่องแจ้งเป็นไฟล์ CSV |
| [`/search-org/v1`](docs/query-apis.md#4-api-search-org-ค้นหาหน่วยงาน) | `GET` | Bearer Token | ค้นหารหัสหน่วยงาน (`org_id`) จากชื่อ |
| [`/get-org-list/v1`](docs/query-apis.md#5-api-get-org-list-ขอโครงสร้างหน่วยงานในสังกัด) | `GET` | Bearer Token | ดึงผังรายชื่อหน่วยงานในสังกัด |
| [`/get-type-list/v2`](docs/query-apis.md#6-api-get-type-list-ขอรายการประเภทปัญหา) | `GET` | Bearer Token | ดึงประเภทปัญหาที่เปิดรับเรื่อง (รวม custom category ต่อหน่วยงาน) |
| [`/get-status-list/v2`](docs/query-apis.md#7-api-get-status-list-ขอรายการสถานะ) | `GET` | Bearer Token | ดึงรายการสถานะของเรื่องแจ้ง (รวม custom status ต่อหน่วยงาน) |
| [`/new-issue/v1`](docs/action-apis.md#1-api-new-issue-ส่งเรื่องแจ้งใหม่) | `POST` | Bearer Token | ส่งเรื่องแจ้งใหม่เข้าสู่ระบบ Fondue |
| [`/update-issue/v1`](docs/action-apis.md#2-api-update-issue-อัปเดตสถานะเรื่องแจ้ง) | `PATCH` | Bearer Token | ปรับปรุงสถานะเรื่องแจ้ง พร้อมรูปภาพ/ไฟล์แนบ |
| [`/star/v1`](docs/action-apis.md#3-api-star-ประเมินความพึงพอใจ) | `POST` | Bearer Token | ประเมินคะแนนความพึงพอใจ (1-5 ดาว) |
| [`/comment/v1`](docs/action-apis.md#4-api-comment-สนทนาให้ความเห็นเพิ่มเติม) | `POST` | Bearer Token | ส่งข้อความสนทนาไปยังผู้แจ้งผ่าน SMS |
| [`/join-forward/v1`](docs/action-apis.md#5-api-join-forward-เชิญร่วม--ส่งต่อเรื่องแจ้ง) | `POST` | Bearer Token | เชิญหน่วยงานร่วม หรือส่งต่อเรื่องแจ้ง |

---

## 🚀 เริ่มต้นใช้งานอย่างรวดเร็ว (Quickstart)

### 1. ขอรับ JWT Token
```bash
curl --location 'https://publicapi.traffy.in.th/exchange-api/get-auth/v1' \
--header 'Content-Type: application/json' \
--data '{
    "user": "YOUR_USERNAME",
    "pass": "YOUR_PASSWORD"
}'
```

### 2. ดึงรายการเรื่องแจ้งล่าสุด
```bash
curl --location 'https://publicapi.traffy.in.th/exchange-api/get-issues/v2?org_id=YOUR_ORG_ID&duration=today' \
--header 'Authorization: Bearer YOUR_JWT_TOKEN'
```

---

## 📁 โครงสร้างโปรเจกต์ (Repository Structure)

```text
.
├── index.html              # หน้าแรก Landing Page / Developer Portal
├── docs.html               # Interactive API Documentation & Reference
├── css/                    # Custom CSS Stylesheet (Theme & Layout)
│   └── style.css
├── js/                     # Client Script (Search, ScrollSpy, Copy)
│   └── app.js
├── README.md               # เอกสารหน้าแรกและสรุป Endpoint
├── OKF.md                  # Objectives, Key Results & System Knowledge Framework
├── ADR.md                  # Architecture Decision Records
├── CONTEXT.md              # Technical Context & Integration Architecture
├── HANDOFF.md              # Handoff Documentation & Next Steps
├── openapi.yaml            # OpenAPI 3.0.3 Specification
├── docs/                   # เอกสารรายละเอียดแยกตามหมวดหมู่ (Markdown)
│   ├── overview.md         # สรุปภาพรวมและขั้นตอนการสมัคร
│   ├── authentication.md   # การยืนยันตัวตนและการขอ Token
│   ├── query-apis.md       # API ดึงข้อมูล
│   ├── action-apis.md      # API ส่งข้อมูลเข้าและอัปเดต
│   ├── webhooks.md         # การรับส่งข้อมูล Real-time Webhook
│   └── error-codes.md      # Error Codes และการแก้ไข
└── examples/               # ตัวอย่างโค้ด
    ├── curl/               # สคริปต์ cURL
    ├── python/             # ตัวอย่าง Python Client
    └── nodejs/             # ตัวอย่าง Node.js Client
```

---

## 📝 ประวัติการเปลี่ยนแปลง (Change Log)

### 2026-10-20
- **อัปเดตฟิลด์ผลลัพธ์ของ `GET /get-issue/v2` (Reporter & Chat Log Data):** เพิ่มฟิลด์ `user_id` (Id ผู้แจ้ง), `reporter_phone` (เบอร์โทรศัพท์ผู้แจ้ง) และ `chat` (Array ข้อความแชทระหว่างเจ้าหน้าที่กับผู้แจ้ง ประกอบด้วย `org_id`, `comment`, `user_id`, `timestamp`) ใน `results` ของ API `get-issue` บน `docs.html`, `docs/query-apis.md` และ `openapi.yaml` พร้อมเพิ่มคำเตือนมาตรการคุ้มครองข้อมูลส่วนบุคคล (PDPA) ห้ามเผยแพร่ข้อมูลแชทสู่สาธารณะ

### 2026-10-16
- **โครงสร้างหัวการ์ด API 2 บรรทัดและการบังคับขึ้นบรรทัดใหม่ (Two-Row Hierarchy & Strict Line Break):** ปรับแก้หัวข้อของการ์ด API ทุกตัวใน `docs.html` (13 Core APIs และ 3 Webhooks) ให้เอาลำดับและคำอธิบายภาษาไทยขึ้นก่อนในบรรทัดแรก และขึ้นบรรทัดใหม่ด้วย Method Badge, Full Production URL (เช่น `https://publicapi.traffy.in.th/exchange-api/get-auth/v1`), และวิธีการ Authentication พร้อมทั้งบังคับการขึ้นบรรทัดใหม่ด้วย `!important` ใน CSS, Inline Style Fallback และ Cache-Busting เพื่อความชัดเจนและป้องกันบราวเซอร์แคชแสดงผลผิดพลาด
- **ข้อกำหนดความรับผิดชอบและการคุ้มครองข้อมูล (Disclaimer & Data Privacy):** เพิ่มแบนเนอร์และข้อกำหนดระบุสถานะ Traffy Fondue ในฐานะแพลตฟอร์มผู้ให้บริการระบบตัวกลาง (Platform Service Provider) ความรับผิดชอบต่อเนื้อหาตกอยู่แก่ผู้แจ้งเหตุ เจ้าหน้าที่ และผู้นำข้อมูลไปใช้ต่อ พร้อมทั้งกำชับคำเตือนเรื่องข้อมูลดิบที่ไม่ผ่านการเซนเซอร์ (Raw Uncensored Data) ให้ปฏิบัติตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) อย่างเคร่งครัด
- บันทึกการตัดสินใจเชิงสถาปัตยกรรม [ADR-009](ADR.md#adr-009-การปรับปรุงโครงสร้างหัวการ์ด-api-เป็น-2-บรรทัด-two-row-hierarchy-และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ) และ [ADR-010](ADR.md#adr-010-การบังคับโครงสร้างหัวการ์ด-api-ขึ้นบรรทัดใหม่แยกระหว่าง-title-และ-endpoint-url-strict-line-break--cache-busting-fallback)

### 2026-10-12
- ปรับปรุงการนำทางในเอกสาร (`docs.html`): ถอด `/v1` และ `/v2` ออกจากเมนูด้านซ้าย (`docs-sidebar-nav`) โดยแสดงเฉพาะชื่อ Resource หลัก และกำหนดให้ส่วนรายละเอียดในการ์ด API แต่ละตัวเป็นจุดเดียวในการระบุเวอร์ชัน (Single Source of Truth) เพื่อป้องกันการแก้ไขเวอร์ชันไม่ครบหลายจุด
- อัปเดตตัวอย่างผลลัพธ์ JSON (Response Examples) ของ API ต่างๆ และ Webhooks ให้ตรงกับเวอร์ชันและผลลัพธ์จริงจากเซิร์ฟเวอร์
- ตรวจสอบความถูกต้องของ Input Parameters อ้างอิงตามโค้ด Backend จริง (เช่น ยืนยันว่า `get-issue` ไม่รองรับ `client_ticket_id` และระบุคำอธิบายให้ถูกต้อง)
- บันทึกการตัดสินใจเชิงสถาปัตยกรรม [ADR-008](ADR.md#adr-008-การรวม-single-source-of-truth-สำหรับ-versioning-ใน-ui-และการปรับปรุงความถูกต้องของ-parameter--response-contract)

### 2026-10-05
- ทดสอบการเชื่อมต่อ API ครบทั้ง 14 Endpoints บน Live Server ด้วยชุดทดสอบอัตโนมัติ (ผลลัพธ์ผ่าน 100%)
- กำหนดให้ใช้ `/get-issue/v2` เป็น Primary Endpoint และปรับปรุงโครงสร้างข้อมูลให้ตรงกับ Server Response ปัจจุบัน (`status_th_latest`, `name` ใน `orgs[]`, `issue_category_id`, ฯลฯ)
- แก้ไข JSON Schema และ Code Examples ของ `/get-auth/v1` ให้ `results` เป็น Object
- เพิ่ม Best Practice แนะนำการส่ง `?org_id={org_id}` ใน `/get-org-list/v1`
- ปรับปรุงข้อกำหนดพารามิเตอร์ `origin_group` ใน `/join-forward/v1` เป็น Optional
- เพิ่มเอกสาร [`ADR.md`](ADR.md) บันทึกการตัดสินใจเชิงสถาปัตยกรรม (ADR-001 ถึง ADR-007)
- ปรับปรุง Client SDK (Python & Node.js) ให้รองรับการแกะ Bearer Token อย่างถูกต้อง

### 2026-09-26
- เปลี่ยนไปใช้ API `get-type-list/v2` และ `get-status-list/v2`
- ปรับปรุง API `get-issues` และ `download-issues` ให้รองรับ parameter `type_name_th` (และ alias), `issue_category_id`, `org_category_id`, `is_follow`, `is_forward` และ เพิ่มตัวเลือก `3days` สำหรับ parameter `duration`

---

## ⚖️ ข้อกำหนดการใช้งานและข้อสงวนสิทธิ์ความรับผิดชอบ (Terms of Use & Legal Disclaimer)

1. **บทบาทของแพลตฟอร์ม (Platform Service Provider):**
   * Traffy Fondue และทีมงานผู้พัฒนาระบบ (NECTEC/สวทช.) ทำหน้าที่เป็นเพียง **ผู้ให้บริการระบบเทคโนโลยีสารสนเทศตัวกลางในการรับส่งและประสานงานข้อมูลเท่านั้น** มิได้เป็นผู้ผลิต สร้างสรรค์ ควบคุม ตรวจสอบ หรือรับรองความถูกต้องของเนื้อหา ข้อมูล ข้อความ รูปภาพ หรือพิกัดใดๆ ในระบบ
2. **ขอบเขตความรับผิดชอบต่อเนื้อหาทางกฎหมาย (Content Liability):**
   * ความรับผิดชอบตามกฎหมายทั้งหมดเกี่ยวกับเนื้อหาตกอยู่แก่บุคคลและหน่วยงานดังต่อไปนี้โดยตรง:
     * **เจ้าของเรื่องแจ้ง (ผู้แจ้งเหตุ/ประชาชน):** รับผิดชอบต่อข้อเท็จจริง ข้อความ และภาพถ่ายที่นำเข้าสู่ระบบ
     * **เจ้าหน้าที่และหน่วยงานผู้รับผิดชอบ:** รับผิดชอบต่อการบันทึก การชี้แจง ภาพผลงาน และการอัปเดตสถานะการดำเนินงาน
     * **ผู้นำข้อมูลไปใช้ต่อ (API Consumer / Integrator):** รับผิดชอบต่อการประมวลผล การจัดเก็บ และการนำข้อมูลไปใช้งานหรือเผยแพร่ต่อ
   * หากเกิดข้อพิพาท การละเมิดสิทธิ หรือการฟ้องร้องดำเนินคดีใดๆ ผู้พัฒนาและผู้ให้บริการแพลตฟอร์ม Traffy Fondue **ขอปฏิเสธความรับผิด (Disclaimer of Liability) ในทุกกรณี**
3. **คำเตือนสำคัญสำหรับผู้ใช้งาน Exchange API (Raw & Uncensored Data):**
   * ข้อมูลที่ได้รับผ่าน Exchange API เป็น **"ข้อมูลดิบ (Raw Data)"** ที่ส่งตรงจากระบบ **โดยยังไม่ผ่านการคัดกรองหรือเซนเซอร์ใดๆ ทั้งสิ้น (Uncensored)**
   * **ให้ระวังการเผยแพร่ข้อมูลออกสู่สาธารณะให้มากที่สุด**
   * ผู้ใช้งาน API มีหน้าที่ต้องปฏิบัติตามกฎหมายที่เกี่ยวข้องอย่างเคร่งครัด เช่น **พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA)** และ **พ.ร.บ. คอมพิวเตอร์** โดยต้องทำการเบลอภาพ เซนเซอร์ หรือตัดทอนข้อมูลส่วนบุคคล (เช่น ใบหน้าบุคคล, ป้ายทะเบียนรถ, เบอร์โทรศัพท์, ที่อยู่) ก่อนการเผยแพร่ออกสู่สาธารณะโดยเด็ดขาด

---

## 📞 ติดต่อและขอรับการสนับสนุน

* **สมัครใช้งาน Exchange API:** [แบบฟอร์มขอใช้งาน](https://forms.gle/bvFEhjPHSmU1x7wP7)
* **ขอเพิ่มโควต้า / ปรึกษาเชิงเทคนิค:** LINE Official: **[@fonduehelp](https://line.me/R/ti/p/%40155yjrwo)**
* **เว็บไซต์หลัก:** [https://www.traffy.in.th](https://www.traffy.in.th)

