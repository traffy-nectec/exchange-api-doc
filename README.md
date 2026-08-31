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
* [บริบททางเทคนิคและสถาปัตยกรรม (CONTEXT.md)](CONTEXT.md)
* [เอกสารส่งมอบงานและการต่อยอด (HANDOFF.md)](HANDOFF.md)

---

## ⚡ ตารางสรุป Endpoint ทั้งหมด (Quick API Reference)

**Base URL:** `https://publicapi.traffy.in.th/exchange-api`

| Endpoint | Method | Authentication | คำอธิบาย |
| :--- | :---: | :---: | :--- |
| [`/get-auth/v1`](docs/authentication.md) | `POST` | User/Pass | ขอรับ JWT Bearer Token |
| [`/get-issues/v1`](docs/query-apis.md#1-api-get-issues-ขอรายการเรื่องแจ้ง) | `POST` | Bearer Token | ดึงรายการเรื่องแจ้งของหน่วยงาน พร้อมตัวกรอง |
| [`/get-issue/v1`](docs/query-apis.md#2-api-get-issue-ขอรายละเอียดเชิงลึกของเรื่องแจ้ง) | `POST` | Bearer Token | ดึงรายละเอียดเชิงลึกของเรื่องแจ้งราย `ticket_id` |
| [`/download-issues/v1`](docs/query-apis.md#3-api-download-issues-ดาวน์โหลดไฟล์-csv) | `POST` | Bearer Token | ส่งออกข้อมูลเรื่องแจ้งเป็นไฟล์ CSV |
| [`/search-org/v1`](docs/query-apis.md#4-api-search-org-ค้นหาหน่วยงาน) | `POST` | Bearer Token | ค้นหารหัสหน่วยงาน (`org_id`) จากชื่อ |
| [`/get-org-list/v1`](docs/query-apis.md#5-api-get-org-list-ขอโครงสร้างหน่วยงานในสังกัด) | `POST` | Bearer Token | ดึงผังรายชื่อหน่วยงานในสังกัด |
| [`/get-type-list/v1`](docs/query-apis.md#6-api-get-type-list-ขอรายการประเภทปัญหา) | `POST` | Bearer Token | ดึงประเภทปัญหาที่เปิดรับเรื่อง |
| [`/get-status-list/v1`](docs/query-apis.md#7-api-get-status-list-ขอรายการสถานะ) | `POST` | Bearer Token | ดึงรายการสถานะของเรื่องแจ้ง |
| [`/new-issue/v1`](docs/action-apis.md#1-api-new-issue-ส่งเรื่องแจ้งใหม่) | `POST` | Bearer Token | ส่งเรื่องแจ้งใหม่เข้าสู่ระบบ Fondue |
| [`/update-issue/v1`](docs/action-apis.md#2-api-update-issue-อัปเดตสถานะเรื่องแจ้ง) | `POST` | Bearer Token | ปรับปรุงสถานะเรื่องแจ้ง พร้อมรูปภาพ/ไฟล์แนบ |
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
curl --location 'https://publicapi.traffy.in.th/exchange-api/get-issues/v1' \
--header 'Authorization: Bearer YOUR_JWT_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "offset": 0,
    "limit": 10
}'
```

---

## 📁 โครงสร้างโปรเจกต์ (Repository Structure)

```text
.
├── README.md               # เอกสารหน้าแรกและสรุป Endpoint
├── OKF.md                  # Objectives, Key Results & System Knowledge Framework
├── CONTEXT.md              # Technical Context & Integration Architecture
├── HANDOFF.md              # Handoff Documentation & Next Steps
├── openapi.yaml            # OpenAPI 3.0.3 Specification
├── docs/                   # เอกสารรายละเอียดแยกตามหมวดหมู่
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

## 📞 ติดต่อและขอรับการสนับสนุน

* **สมัครใช้งาน Exchange API:** [แบบฟอร์มขอใช้งาน](https://forms.gle/bvFEhjPHSmU1x7wP7)
* **ขอเพิ่มโควต้า / ปรึกษาเชิงเทคนิค:** LINE Official: **[@fonduehelp](https://line.me/R/ti/p/%40155yjrwo)**
* **เว็บไซต์หลัก:** [https://www.traffy.in.th](https://www.traffy.in.th)
