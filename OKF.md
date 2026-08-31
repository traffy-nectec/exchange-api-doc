# Objectives, Knowledge & Framework (OKF)

เอกสารวัตถุประสงค์ ผลลัพธ์หลัก และกรอบความรู้เชิงระบบ (Objectives, Key Results & Knowledge Framework) สำหรับ **Traffy Fondue Exchange API Documentation**

---

## 1. วัตถุประสงค์และผลลัพธ์หลัก (Objectives and Key Results - OKRs)

### 🎯 Objective 1: เอกสาร API มาตรฐานสมบูรณ์แบบ 100% สำหรับหน่วยงานภายนอก (Standardized API Docs)
- **KR 1.1:** จัดทำและรวบรวม Endpoint ทั้งหมดของ Exchange API ครอบคลุมทั้ง Inbound (ส่งข้อมูลเข้า), Outbound (ดึงข้อมูลออก), และ Real-time Push (Webhooks)
- **KR 1.2:** แปลงสเปกจาก Google Docs และ Notion มาเป็นเอกสาร Markdown ที่มีโครงสร้างชัดเจน พร้อม Schema, Parameters, Error Codes, และ Example Requests/Responses
- **KR 1.3:** จัดทำ OpenAPI 3.0.3 Specification (`openapi.yaml`) ที่ผ่านการ Validate สามารถนำไป Import เข้า Swagger UI, Postman หรือใช้สร้าง Client SDK ได้ทันที

### 🎯 Objective 2: ลดระยะเวลาและภาระงานในการ Onboarding หน่วยงานใหม่ (Fast Integration)
- **KR 2.1:** มี Onboarding Flow ที่ชัดเจน 4 ขั้นตอน ตั้งแต่การกรอกแบบฟอร์มขอใช้งาน การรับสิทธิ์ การแลก Token และการเริ่มยิง API
- **KR 2.2:** มีตัวอย่าง Code Wrapper พร้อมใช้ใน 3 ภาษา/เครื่องมือหลัก ได้แก่ cURL Shell Scripts, Python SDK Client, และ Node.js/JavaScript Client
- **KR 2.3:** มีตาราง Error Codes & Troubleshooting Guide ที่ครอบคลุมปัญหาหลัก เช่น Token หมดอายุ, โควต้าเต็ม, รูปแบบ JSON ไม่ถูกต้อง เพื่อให้ผู้พัฒนาแก้ปัญหาได้เองทันที

### 🎯 Objective 3: การจัดการความปลอดภัยและโควต้าอย่างเป็นระบบ (Security & Quota Management)
- **KR 3.1:** กำหนดมาตรฐานการยืนยันตัวตนด้วย JWT Bearer Token และห้ามเปิดเผย Credential (`user`/`pass`) สู่ Client-side
- **KR 3.2:** ระบบติดตามโควต้าการใช้งานประจำเดือน (`credit_balance` / `quota_limit`) พร้อมช่องทางประสานงานขอขยายโควต้าผ่าน LINE Official: `@fonduehelp`

---

## 2. กรอบความรู้เชิงระบบ (System Knowledge Framework)

### 2.1 บริการ API แบ่งตามหมวดหมู่ (Service Domains)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Traffy Fondue Exchange Platform                       │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│   🔐 Authentication      │   📥 Data Retrieval      │   📤 Data Submission  │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ • POST /get-auth/v1      │ • POST /get-issues/v1    │ • POST /new-issue/v1  │
│   (JWT Token Generation) │ • POST /get-issue/v1     │ • POST /update-issue/v1│
│                          │ • POST /download-issues/v1│ • POST /star/v1      │
│                          │ • POST /search-org/v1    │ • POST /comment/v1    │
│                          │ • POST /get-org-list/v1  │ • POST /join-forward/v1│
│                          │ • POST /get-type-list/v1 │                       │
│                          │ • POST /get-status-list/v1│                       │
├──────────────────────────┴──────────────────────────┴───────────────────────┤
│                        🔔 Real-time Push (Webhooks)                         │
│ • POST -> Client Webhook (เมื่อมีเรื่องแจ้งใหม่)                              │
│ • PATCH -> Client Webhook (เมื่อมีการอัปเดตสถานะ)                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 มาตรฐานความถูกต้องของข้อมูล (Data Validation Principles)
1. **HTTP Method:** Endpoint ทั้งหมดของ Exchange API ใช้ `POST` Method พร้อมส่ง Payload ในรูปแบบ JSON Body (`Content-Type: application/json`)
2. **Timezone:** ข้อมูลวันเวลาในระบบใช้เวลามาตรฐานประเทศไทย (UTC+7 / `Asia/Bangkok`) รูปแบบ `YYYY-MM-DD HH:MM:SS` หรือ ISO 8601
3. **Geo-coordinates:** พิกัดตำแหน่งใช้ระบบพิกัด WGS84 (Latitude, Longitude เป็นเลขทศนิยม)
4. **Token Expiry:** JWT Token มีอายุการใช้งานจำกัด และจะระบุ `expire_timestamp` มาพร้อมกับ Response ของ `get-auth`
