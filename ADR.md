# Architecture Decision Records (ADR)

เอกสารบันทึกการตัดสินใจเชิงสถาปัตยกรรมและการกำหนดข้อตกลงในการเชื่อมต่อระบบ (Architecture Decision Records) สำหรับ **Traffy Fondue Exchange API**

---

## สารบัญรายการตัดสินใจ (Table of ADRs)

* [ADR-001: การกำหนดให้ `GET /get-issue/v2` เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ](#adr-001-การกำหนดให้-get-get-issuev2-เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ)
* [ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object](#adr-002-การปรับปรุง-contract-ของ-post-get-authv1-ให้-results-เป็น-json-object)
* [ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ](#adr-003-การระบุคำแนะนำเชิงป้องกันสำหรับ-get-get-org-listv1-ให้ส่ง-parameter-org_id-เสมอ)
* [ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional](#adr-004-การปรับ-parameter-origin_group-ใน-post-join-forwardv1-เป็นแบบ-optional)
* [ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`)](#adr-005-การรองรับบริบทการใช้งาน-2-รูปแบบใน-post-commentv1-comment-vs-chat)
* [ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec](#adr-006-การคงความเข้ากันได้ย้อนหลัง-backward-compatibility-และการประกาศ-dual-version-ใน-openapi-spec)
* [ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม](#adr-007-มาตรการป้องกัน-infinite-webhook-feedback-loop-ระหว่างระบบภายนอกและแพลตฟอร์ม)

---

## ADR-001: การกำหนดให้ `GET /get-issue/v2` เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
เดิมเอกสารและตัวอย่างโค้ดแนะนำการเรียก `GET /exchange-api/get-issue/v1?ticket_id=...` แต่จากการทดสอบการเชื่อมต่อจริงกับ Public API พบว่าเซิร์ฟเวอร์เปิดให้บริการ Endpoint `GET /exchange-api/get-issue/v2` ควบคู่กัน โดยในเวอร์ชัน `v2` มีฟิลด์ข้อมูลที่ทันสมัยและครอบคลุมมากกว่า เช่น:
- ฟิลด์ `status_th_latest` ใน Root Object
- ฟิลด์ชื่อหน่วยงานใน `orgs[]` ใช้คีย์ `name` (แทนคีย์ `org`)
- มีข้อมูลสถานะและหมวดหมู่เชิงลึกระดับหน่วยงาน: `issue_category_id`, `issue_status_id`, `status_en`, `is_follow`, และ `is_forward`

### การตัดสินใจ (Decision)
1. ปรับเอกสารหลัก (`docs.html`, `docs/query-apis.md`, `README.md`, `OKF.md`) ให้แนะนำ `GET /exchange-api/get-issue/v2` เป็น Endpoint หลัก
2. ปรับปรุง OpenAPI Specification (`openapi.yaml`) ให้มีทั้ง `/get-issue/v2` (Primary) และคง `/get-issue/v1` (Deprecated) ไว้เพื่อความเข้ากันได้ย้อนหลัง
3. ปรับปรุง Client SDK (`examples/python/client.py`, `examples/nodejs/client.js`) ให้เรียกใช้ `/get-issue/v2`

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** นักพัฒนาและหน่วยงานภายนอกได้รับโครงสร้างข้อมูลที่สมบูรณ์และตรงกับพฤติกรรมปัจจุบันของระบบ Traffy Fondue มากขึ้น
- **ข้อควรระวัง:** โค้ดเดิมที่อ่าน `orgs[].org` ควรเปลี่ยนมารองรับ `orgs[].name` (หรือเขียน Fallback ตรวจสอบทั้งสองคีย์)

---

## ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
ในเอกสารเวอร์ชันเดิม ระบุ JSON Schema ของ Response จาก `POST /get-auth/v1` ว่า `results` เป็น `array[object]` ซึ่งทำให้ตัวอย่างโค้ดใน SDK เข้าถึง Token ด้วย `data.results[0].token` หรือ `data["results"][0]["token"]`
แต่จากการทดสอบจริงด้วย cURL และ Live Server พบว่า Payload จริงที่ส่งกลับมาคือ:
```json
{
  "status": 200,
  "message": "OK",
  "results": {
    "token": "eyJhbGciOi...",
    "expire_timestamp": "2026-10-06 00:00:00"
  }
}
```
การระบุเป็น Array ในเอกสารเดิมส่งผลให้โค้ดของนักพัฒนาเกิด Uncaught TypeError / IndexError เมื่อพยายามเข้าถึง index `[0]`

### การตัดสินใจ (Decision)
1. แก้ไข Schema ใน `docs/authentication.md`, `docs.html`, และ `openapi.yaml` ให้ `results` เป็นประเภท `object` (ไม่ใช่ `array`)
2. แก้ไข Client SDK ทั้งภาษา Python (`examples/python/client.py`) และ Node.js (`examples/nodejs/client.js`) ให้เข้าถึง Token แบบปลอดภัย โดยตรวจสอบทั้ง `isinstance(results, dict)` และ Fallback กรณีเป็น List

### ผลสืบเนื่อง (Consequences)
- โค้ดตัวอย่างใน SDK ทำงานได้จริง 100% โดยไม่เกิด Runtime Crash
- Schema ใน OpenAPI ถูกต้องตามมาตรฐาน JSON Schema

---

## ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
จากการทดสอบเรียก `GET /exchange-api/get-org-list/v1` โดยไม่ส่ง Query Parameter `?org_id={org_id}` พบว่า Backend API (PHP) ส่ง PHP Warning ล้นออกมาข้างหน้า JSON Payload:
```text
<br />
<b>Warning</b>:  Undefined array key "org_id" in <b>/var/www/html/.../get_org_list.php</b> on line <b>208</b><br />
{"status":200,"message":"OK","results":[...]}
```
สิ่งนี้ทำให้ HTTP Client ทั่วไปที่ทำการ Parse JSON ล้มเหลวทันที (`SyntaxError: Unexpected token < in JSON at position 0`) แต่เมื่อส่ง `?org_id=43152` เซิร์ฟเวอร์จะคืนค่า JSON ที่สะอาดและถูกต้องโดยไม่มี Warning

### การตัดสินใจ (Decision)
1. เพิ่มคำเตือนและคำแนะนำ (Best Practice Note) ใน `docs.html`, `docs/query-apis.md`, และ `openapi.yaml` ให้นักพัฒนาระบุ `?org_id={org_id}` เสมอ
2. ปรับตัวอย่าง cURL และ SDK ให้ส่ง Parameter `org_id`

### ผลสืบเนื่อง (Consequences)
- ป้องกันความผิดพลาดของ Client Applications ในการ Deserialize JSON Response
- ลด Ticket สอบถามปัญหาเข้ามายังทีม Support

---

## ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
ในเอกสารเดิมระบุว่า `origin_group` (รหัสหน่วยงานต้นทาง) เป็น Required Field แต่ในการทดสอบจริง พบว่าหากผู้เรียก API ไม่ได้ระบุ `origin_group` เข้ามา เซิร์ฟเวอร์จะกำหนดหน่วยงานต้นทางให้อัตโนมัติโดยอิงจากบัญชีผู้ใช้ที่เป็นเจ้าของ Bearer Token

นอกจากนี้ Response ที่เซิร์ฟเวอร์ตอบกลับมาคือ:
```json
{
  "status": 200,
  "message": "OK",
  "results": []
}
```
(เดิมเอกสารระบุ Schema ผลลัพธ์ซับซ้อนเกินจริง)

### การตัดสินใจ (Decision)
1. ปรับสถานะของ Parameter `origin_group` ในเอกสารทุกฉบับให้เป็น `Optional` (มีค่า Default เป็นหน่วยงานของ Token)
2. ปรับตัวอย่างและ Schema ของ Response ให้สะท้อนผลลัพธ์จริง (`results: []`)

### ผลสืบเนื่อง (Consequences)
- ผู้พัฒนาระบบภายนอกลดความยุ่งยากในการ Hardcode หรือส่งต่อ `origin_group` ซ้ำซ้อน
- ป้องกันความสับสนเรื่อง Output Schema ของ API นี้

---

## ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`)

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
API `POST /exchange-api/comment/v1` มีพารามิเตอร์ `comment_type` ซึ่งในระบบจริงรองรับ 2 บริบทที่แตกต่างกัน:
1. `comment_type: "comment"` ใช้สำหรับการส่งข้อเสนอแนะ/ความเห็นหลังจากประเมินความพึงพอใจ (Rating Feedback)
2. `comment_type: "chat"` ใช้สำหรับการสนทนา/สื่อสารระหว่างเจ้าหน้าที่หรือหน่วยงาน และส่งข้อความ SMS ไปยังประชาชนผู้แจ้งเรื่อง

### การตัดสินใจ (Decision)
1. ระบุความหมายและค่า Enums ของ `comment_type` ในเอกสารให้ชัดเจน
2. อัปเดต OpenAPI Specification ให้รองรับ Enum `["comment", "chat"]`

### ผลสืบเนื่อง (Consequences)
- นักพัฒนาเข้าใจวัตถุประสงค์ในการเลือกใช้ `comment_type` อย่างถูกต้องตาม Flow งานจริง

---

## ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-05)

### บริบท (Context)
เนื่องจากยังมีหน่วยงานภายนอกจำนวนมากที่ยังเชื่อมต่อระบบผ่าน Endpoint เวอร์ชัน 1 เช่น `/get-issue/v1` หากนำเวอร์ชันเดิมออกจาก OpenAPI Spec อาจทำให้ระบบที่ผูกไว้กับ Spec เดิมได้รับผลกระทบ

### การตัดสินใจ (Decision)
1. ใน `openapi.yaml` ให้ประกาศทั้ง `/get-issue/v2` (แนะนำเป็นหลัก) และ `/get-issue/v1` (ติดแท็ก `deprecated: true`)
2. ในเอกสาร Markdown และ HTML ให้แนะนำการอัปเกรดเป็น `v2` พร้อมทั้งใส่หมายเหตุระบุว่า `v1` ยังสามารถใช้งานได้

### ผลสืบเนื่อง (Consequences)
- ระบบ Legacy เดิมไม่หยุดชะงัก
- ระบบใหม่ที่เข้ามารวมระบบจะเลือกใช้เวอร์ชัน `v2` ที่ทันสมัยที่สุดทันที

---

## ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-09-26 และย้ำเตือน 2026-10-05)

### บริบท (Context)
การผสานรวมระบบสองทิศทาง (Bi-directional Sync) ระหว่าง Traffy Fondue และระบบบริหารจัดการของหน่วยงาน (เช่น Service Desk หรือ CRM) หากไม่มีการกรอง Event ที่ถูกต้อง อาจเกิดเหตุการณ์:
1. Traffy Fondue ยิง Webhook แจ้งเรื่องใหม่ไปยังระบบหน่วยงาน
2. ระบบหน่วยงานรับเรื่อง แล้วยิง API `new-issue` กลับมายัง Traffy Fondue อีกครั้ง
3. เกิดการสร้าง Ticket ซ้ำซ้อนวนลูปแบบไม่สิ้นสุด (Data Storm / Infinite Loop)

### การตัดสินใจ (Decision)
1. กำหนดกฎเกณฑ์เคร่งครัดในระดับ Architecture ใน `OKF.md`, `CONTEXT.md`, `docs/webhooks.md`, และ `docs.html`
2. ระบบของหน่วยงานต้องแยกแยะ Source Identifier และห้ามนำ Payload จาก Webhook ส่งย้อนกลับเข้ามาที่ Inbound API

### ผลสืบเนื่อง (Consequences)
- ป้องกันความเสียหายต่อทรัพยากรเซิร์ฟเวอร์ และรักษาความถูกต้องของข้อมูลในระบบ
