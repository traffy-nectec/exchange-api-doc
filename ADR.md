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
* [ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract](#adr-008-การรวม-single-source-of-truth-สำหรับ-versioning-ใน-ui-และการปรับปรุงความถูกต้องของ-parameter--response-contract)
* [ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ](#adr-009-การปรับปรุงโครงสร้างหัวการ์ด-api-เป็น-2-บรรทัด-two-row-hierarchy-และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ)
* [ADR-010: การบังคับโครงสร้างหัวการ์ด API ขึ้นบรรทัดใหม่แยกระหว่าง Title และ Endpoint URL (Strict Line-Break & Cache-Busting Fallback)](#adr-010-การบังคับโครงสร้างหัวการ์ด-api-ขึ้นบรรทัดใหม่แยกระหว่าง-title-และ-endpoint-url-strict-line-break--cache-busting-fallback)
* [ADR-011: การเพิ่มข้อมูลผู้แจ้ง (Reporter Details) และประวัติแชท (Chat Logs) ใน Response ของ `GET /get-issue/v2` พร้อมข้อกำหนดคุ้มครองข้อมูลส่วนบุคคล (PDPA)](#adr-011-การเพิ่มข้อมูลผู้แจ้ง-reporter-details-และประวัติแชท-chat-logs-ใน-response-ของ-get-get-issuev2-พร้อมข้อกำหนดคุ้มครองข้อมูลส่วนบุคคล-pdpa)
* [ADR-012: มาตรฐานการทำเอกสาร Webhook Payload และ Response Contract ให้ครบถ้วน](#adr-012-มาตรฐานการทำเอกสาร-webhook-payload-และ-response-contract-ให้ครบถ้วน)
* [ADR-013: การจำกัด Public Contract ของ `POST /join-forward/v1` ให้เหลือเฉพาะพารามิเตอร์ที่เปิดเผย](#adr-013-การจำกัด-public-contract-ของ-post-join-forwardv1-ให้เหลือเฉพาะพารามิเตอร์ที่เปิดเผย)
* [ADR-014: การขยายฟิลด์บริบทเรื่องแจ้งใน Query APIs (`type_reporter`, `user_id`, `is_follow`, `is_forward`, `status_latest`) และการรองรับ Wildcard ใน `GET /search-org/v1`](#adr-014-การขยายฟิลด์บริบทเรื่องแจ้งใน-query-apis-type_reporter-user_id-is_follow-is_forward-status_latest-และการรองรับ-wildcard-ใน-get-search-orgv1)
* [ADR-015: การปรับปรุง Webhook Event Contract ให้ครอบคลุม `client_ticket_id` และข้อมูลผู้ส่ง (`sender_user_id`, `sender_user_name`) พร้อมการจัดระเบียบตาราง Output Parameters](#adr-015-การปรับปรุง-webhook-event-contract-ให้ครอบคลุม-client_ticket_id-และข้อมูลผู้ส่ง-sender_user_id-sender_user_name-พร้อมการจัดระเบียบตาราง-output-parameters)
* [ADR-016: การปรับปรุงความถูกต้องของโครงสร้าง Timeline (`user_id`, `user_name`), ข้อมูลแชท (`comment_type`), คอลัมน์ CSV (`user_id`), และข้อความเตือน Loop ป้องกันข้อผิดพลาด](#adr-016-การปรับปรุงความถูกต้องของโครงสร้าง-timeline-user_id-user_name-ข้อมูลแชท-comment_type-คอลัมน์-csv-user_id-และข้อความเตือน-loop-ป้องกันข้อผิดพลาด)
* [ADR-017: การปรับปรุงข้อกำหนดการป้องกัน Webhook Loop ให้ครอบคลุม Outbound Event Suppression และ Echo Loop Prevention](#adr-017-การปรับปรุงข้อกำหนดการป้องกัน-webhook-loop-ให้ครอบคลุม-outbound-event-suppression-และ-echo-loop-prevention)

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

---

## ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-12)

### บริบท (Context)
เดิมแถบนำทางด้านซ้าย (Sidebar Navigation: `.docs-sidebar-nav`) และเมนูเลือก Endpoint บนหน้าเอกสาร `docs.html` มีการระบุเลขเวอร์ชันกำกับไว้ในชื่อเมนู เช่น `/get-issues/v2`, `/update-issue/v1` 
การมีเลขเวอร์ชันกระจายอยู่หลายแห่งก่อให้เกิดปัญหา:
1. **Redundant Maintenance Overhead:** เมื่อมีการปรับปรุง Endpoint เป็นเวอร์ชันใหม่ ผู้ดูแลเอกสารต้องตามแก้ไขเวอร์ชันในหลายจุด (ทั้ง Sidebar, Dropdown Menu, หัวการ์ด API, cURL Example, และ Response Block) ซึ่งมักเกิดข้อผิดพลาดหรือแก้ไม่ครบ
2. **Contract Discrepancy & Parameter Drift:** คำอธิบาย Input Parameters และตัวอย่าง JSON Response ในเอกสารบางจุดไม่สอดคล้องกับพฤติกรรมจริงของ Live Backend Server เช่น ใน `GET /get-issue/v2` คำอธิบายเคยระบุว่ารองรับ `client_ticket_id` ทั้งที่โค้ดจริงรับเฉพาะ `ticket_id` เท่านั้น

### การตัดสินใจ (Decision)
1. **Single Source of Truth สำหรับ Versioning:** นำ `/v1` และ `/v2` ออกจากชื่อรายการใน Sidebar Navigation (`.docs-sidebar-nav`) ให้คงเหลือเฉพาะชื่อ Resource หลัก (เช่น `/get-issues`, `/get-issue`, `/new-issue`) และกำหนดให้ **การ์ดรายละเอียดของแต่ละ API** เป็นจุดเดียว (Single Source of Truth) ที่ระบุและควบคุมเวอร์ชันของ Endpoint นั้นๆ
2. **Response Contract Alignment:** อัปเดตตัวอย่างผลลัพธ์ JSON ใน `docs.html` (ทั้งสำหรับ Action APIs และ Webhooks) ให้ตรงกับ Live Production Server Response ในปัจจุบัน
3. **Parameter Precision:** ตรวจสอบและแก้ไขคำอธิบาย Input Parameters ราย Endpoint อ้างอิงตามโค้ด Backend ใน `exchange-api-php` เป็นหลัก ยืนยันว่า `GET /get-issue/v2` ไม่รองรับ `client_ticket_id` เพื่อไม่ให้ผู้ใช้งานสับสน

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** เมนูนำทางเรียบง่าย สะอาดตา และเมื่อมีการอัปเกรดเวอร์ชันของ API ใดๆ ในอนาคต มีจุดที่ต้องแก้ไขเวอร์ชันเพียงจุดเดียวที่การ์ด API นั้นๆ ป้องกันการแก้ไม่ครบ
- **ความแม่นยำ:** ผู้พัฒนาระบบภายนอกได้รับสเปก Parameter และตัวอย่าง Response ที่ถูกต้องตรงกับเซิร์ฟเวอร์จริง 100%

---

## ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-16)

### บริบท (Context)
1. **API Card Header Clarity:** รูปแบบเดิมของหัวการ์ด API ใน `docs.html` รวมเอา Method Badge, Endpoint Path ย่อ, ชื่อคำอธิบายภาษาไทย, และ Authentication Badge ไว้ในแถวเดียวกันแบบแนวนอน (Flex-wrap) ทำให้ผู้ใช้งานสับสนระหว่างชื่อฟังก์ชันการทำงานกับ URL จริง และผู้พัฒนาไม่สามารถมองเห็น Full Production URL ของ Endpoint ได้ทันทีในจุดเดียว
2. **Platform & Content Liability Governance:** แพลตฟอร์ม Traffy Fondue ทำหน้าที่เป็นตัวกลางทางเทคโนโลยี และข้อมูลที่ส่งผ่าน Exchange API เป็นข้อมูลเรื่องแจ้งดิบที่ยังไม่ผ่านการคัดกรองหรือเซนเซอร์ (Uncensored) จึงจำเป็นต้องมีข้อตกลงและประกาศข้อสงวนสิทธิ์ทางกฎหมาย (Legal Disclaimer) ที่ชัดเจน เพื่อป้องกันข้อพิพาทและให้ผู้ใช้ API ปฏิบัติตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA) อย่างเคร่งครัด

### การตัดสินใจ (Decision)
1. **Two-Row API Header Structure:**
   - ปรับหัวการ์ด API ทุกการ์ด (13 Core Endpoints และ 3 Webhooks) ให้มีโครงสร้างลำดับชั้น 2 บรรทัด:
     - **บรรทัดที่ 1 (Title Row):** ระบุลำดับ, ชื่อ endpoint ในรูปแบบ code pill, และคำอธิบายภาษาไทย เช่น `1. <code>/get-auth</code> ขอ JWT Bearer Token`
     - **บรรทัดที่ 2 (Meta Row):** ระบุ Method Badge, Full Production URL (เช่น `https://publicapi.traffy.in.th/exchange-api/get-auth/v1`), และ Authentication Badge (เช่น `🔑 Auth: User / Pass` หรือ `🛡️ Header: Bearer Token`)
   - เพิ่มคลาส `.api-card-header-top`, `.api-card-title`, และ `.api-card-header-bottom` ใน `css/style.css` พร้อมรองรับ Responsive Display
2. **Legal Disclaimer & Raw Data Warning Banner:**
   - เพิ่มแบนเนอร์และข้อกำหนดความรับผิดชอบทางกฎหมาย (Platform Service Provider Disclaimer) ใน `docs.html` (`#sec-disclaimer`), `index.html` (`#disclaimer`), `README.md`, `docs/overview.md`, `docs/query-apis.md`, และ `openapi.yaml`
   - ระบุชัดเจนว่าความรับผิดชอบต่อเนื้อหาตกอยู่แก่ (1) เจ้าของเรื่องแจ้ง (2) เจ้าหน้าที่/หน่วยงานผู้รับผิดชอบ และ (3) ผู้นำข้อมูลไปใช้ต่อ โดยตรง และ สวทช./NECTEC ขอปฏิเสธความรับผิดในกรณีเกิดข้อพิพาท
   - เพิ่มคำเตือนและข้อปฏิบัติเรื่องข้อมูลดิบ (Raw Uncensored Data) กำชับให้ผู้ใช้งานระวังการเผยแพร่ต่อสาธารณะ และต้องทำ Data Masking / Redaction ข้อมูลส่วนบุคคลตาม PDPA ก่อนเสมอ

### ผลสืบเนื่อง (Consequences)
- **Developer Experience (DX):** ผู้พัฒนาเห็นชื่อฟังก์ชันภาษาไทยและ Full Production URL ของแต่ละ Endpoint ได้ในพริบตา สามารถคัดลอกหรือนำ URL ไปใช้งานต่อได้สะดวกขึ้น
- **Legal Protection & Risk Mitigation:** ปกป้องแพลตฟอร์มจากความเสี่ยงทางกฎหมายและข้อพิพาทเกี่ยวกับเนื้อหา และสร้างความตระหนักรู้ด้านความเป็นส่วนตัวของข้อมูลแก่ผู้ใช้งาน API ภายนอก

---

## ADR-010: การบังคับโครงสร้างหัวการ์ด API ขึ้นบรรทัดใหม่แยกระหว่าง Title และ Endpoint URL (Strict Line-Break & Cache-Busting Fallback)

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-16)

### บริบท (Context)
แม้จะมีการแบ่งโครงสร้าง DOM ใน `docs.html` เป็น 2 บรรทัด (`.api-card-header-top` และ `.api-card-header-bottom`) ใน ADR-009 แต่จากการทดสอบการแสดงผลบนเว็บบราวเซอร์จริงของผู้ใช้ พบปัญหา:
1. เว็บบราวเซอร์จำแคชของไฟล์ `css/style.css` เก่า ซึ่งมีสไตล์ `display: flex; justify-content: space-between;` ทำให้ Title (`.api-card-header-top`) และ URL/Badge (`.api-card-header-bottom`) แสดงผลเคียงข้างกันในแนวนอนบนบรรทัดเดียวกัน
2. เพื่อให้มั่นใจ 100% ว่า URL จะตกลงมาอยู่อีกบรรทัดหนึ่งอย่างแน่นอน จำเป็นต้องมีกลไกป้องกันทั้งในระดับ CSS และ Inline HTML รวมถึงกลไก Cache-Busting

### การตัดสินใจ (Decision)
1. **Strict Flex Column & Display Block ใน CSS:**
   - กำหนดให้ `.api-card-header` ใน `css/style.css` มี `display: flex !important; flex-direction: column !important; align-items: flex-start !important; justify-content: flex-start !important;`
   - กำหนดให้ `.api-card-header-top` มี `display: block; width: 100%;` เพื่อครอบครองความกว้างเต็มแถวเสมอ
2. **Inline Style Defensive Fallback ใน HTML:**
   - เพิ่ม `style="flex-direction: column; align-items: flex-start;"` ใน Element `.api-card-header` ของการ์ด API ทั้ง 16 จุดใน `docs.html` ป้องกันกรณี CSS ไม่ทำงาน
3. **Cache-Busting Query Parameter:**
   - ปรับการเชื่อมโยงสไตล์ชีทใน `docs.html` เป็น `<link rel="stylesheet" href="css/style.css?v=2">` เพื่อบังคับให้บราวเซอร์ดึง CSS ไฟล์ล่าสุดทันที

### ผลสืบเนื่อง (Consequences)
- **Visual Stability:** รับประกัน 100% ว่า Full URL และ Method/Auth Badges จะแสดงผลอยู่ใต้คำอธิบาย Endpoint ในบรรทัดใหม่อย่างสวยงามบนทุกอุปกรณ์
- **Zero Cache Latency:** ผู้ใช้งานจะเห็นการจัดวางรูปแบบใหม่ทันทีโดยไม่ต้องสั่ง Hard Refresh

---

## ADR-011: การเพิ่มข้อมูลผู้แจ้ง (Reporter Details) และประวัติแชท (Chat Logs) ใน Response ของ `GET /get-issue/v2` พร้อมข้อกำหนดคุ้มครองข้อมูลส่วนบุคคล (PDPA)

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-10-20)

### บริบท (Context)
ในการบริหารจัดการเรื่องร้องเรียนของเจ้าหน้าที่หน่วยงาน จำเป็นต้องมีข้อมูลสำหรับติดต่อกลับประชาชนผู้แจ้งเหตุเพื่อขอข้อมูลเพิ่มเติม รวมถึงติดตามประวัติการสื่อสารโต้ตอบระหว่างเจ้าหน้าที่และประชาชนในเรื่องแจ้งนั้นๆ ฝั่ง Backend API จึงได้ปรับปรุง Response Contract ของ `GET /exchange-api/get-issue/v2` โดยเพิ่มข้อมูลผู้แจ้ง (`user_id`, `reporter_phone`) และประวัติการสนทนา (`chat[]`)

อย่างไรก็ตาม เนื่องจากข้อมูลเบอร์โทรศัพท์และข้อความแชทอาจมีข้อมูลระบุตัวบุคคล (Personally Identifiable Information: PII) จึงจำเป็นต้องมีข้อตกลงและคำเตือนกำกับชัดเจนในเอกสาร API และ Schema เพื่อป้องกันการนำข้อมูลนี้ไปเปิดเผยสู่สาธารณะ

### การตัดสินใจ (Decision)
1. **Response Contract Enhancement:**
   - เพิ่มฟิลด์ `user_id` (Id ของผู้แจ้ง) และ `reporter_phone` (เบอร์โทรศัพท์ของผู้แจ้ง) ไว้ใน `results` Object
   - เพิ่มฟิลด์ `chat` (Array ของข้อความแชท) ไว้ใน `results` โดยแต่ละข้อความประกอบด้วย:
     - `org_id`: รหัสหน่วยงาน (เป็น `null` หากข้อความส่งโดยผู้แจ้ง)
     - `comment`: ข้อความการสนทนา
     - `user_id`: รหัสประจำตัวของผู้ส่งข้อความ
     - `timestamp`: เวลาที่ส่งข้อความ (ISO 8601)
2. **PDPA & Privacy Protection Directive:**
   - กำหนดข้อห้ามในเอกสาร (`docs.html`, `docs/query-apis.md`, `openapi.yaml`): **ห้ามเผยแพร่ข้อมูลในส่วนของ `chat` และ `reporter_phone` สู่สาธารณะโดยเด็ดขาด**
   - การเข้าถึงข้อมูลนี้มีวัตถุประสงค์เพื่อให้เจ้าหน้าที่หน่วยงานใช้ติดต่อประสานงานกับผู้แจ้งเท่านั้น
3. **Synchronized Documentation & Schema:**
   - ปรับปรุงตัวอย่าง JSON Response และตาราง Parameter Output ใน `docs.html` และ `docs/query-apis.md`
   - เพิ่ม schema `IssueChatItem` และฟิลด์ `user_id`, `reporter_phone`, `chat` ใน `GetIssueResponse` ของ `openapi.yaml`

### ผลสืบเนื่อง (Consequences)
- **Complete Communication Context:** หน่วยงานที่เชื่อมต่อ API สามารถดึงข้อมูลผู้แจ้งและประวัติการสนทนาไปทำงานร่วมกับระบบ CRM หรือ Helpdesk ภายในของตนเองได้อย่างสมบูรณ์
- **PDPA Compliance Awareness:** ผู้พัฒนาระบบภายนอกตระหนักถึงความอ่อนไหวของข้อมูล และมีแนวปฏิบัติที่ชัดเจนในการปกป้องข้อมูลส่วนบุคคลของประชาชนผู้แจ้ง

---

## ADR-012: มาตรฐานการทำเอกสาร Webhook Payload และ Response Contract ให้ครบถ้วน

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-06)

### บริบท (Context)
ตาราง Incoming Payload ของ Webhook ใน `docs.html` เดิมแสดงเพียงบางฟิลด์ ไม่ครบตาม JSON Sample จริงที่ระบบส่งออกไป ทำให้ผู้เชื่อมต่ออาจพลาดฟิลด์สำคัญ เช่น `status_en`, `is_follow`, `is_forward`, `status_type` และฟิลด์ระดับหน่วยงาน นอกจากนี้ยังไม่มีตัวอย่าง Response ที่ชัดเจนว่าปลายทางควรตอบกลับอย่างไร

### การตัดสินใจ (Decision)
1. **Payload Completeness:** สำหรับ Webhook ทั้ง 3 ตัว (`new-issue`, `update-issue`, `chat/comment`) ตาราง Incoming Payload ต้องแสดงฟิลด์ครบทุกฟิลด์ที่ปรากฏใน JSON Sample พร้อมระบุ Type ตามข้อมูลจริง
2. **Response Contract:** กำหนด Response Example มาตรฐานที่ปลายทางควรตอบกลับเป็น `{ "status": "success", "message": "" }`
3. **Synchronized Documentation:** ใช้ `docs.html` เป็นเอกสารอ้างอิงหลัก และซิงค์ตาราง/ตัวอย่าง JSON พร้อม Response Example ลง `docs/webhooks.md` ให้ตรงกัน พร้อมถือมาตรฐานนี้เมื่อปรับปรุงเอกสาร Webhook ในอนาคต

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** ผู้เชื่อมต่อเห็น Contract ครบถ้วนตั้งแต่ต้น ลดปัญหาฟิลด์ตกหล่นและลดการสอบถามทีม Traffy
- **ข้อควรระวัง:** เมื่อ Backend เพิ่มหรือเปลี่ยนฟิลด์ของ Webhook ต้องอัปเดตตารางและ Sample ใน `docs.html` ให้ตรงกันทุกครั้ง

---

## ADR-013: การจำกัด Public Contract ของ `POST /join-forward/v1` ให้เหลือเฉพาะพารามิเตอร์ที่เปิดเผย

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-06)

### บริบท (Context)
เอกสาร `join-forward` เดิมแสดงพารามิเตอร์ภายในและพารามิเตอร์เดิมที่ไม่ใช่ส่วนหนึ่งของ Public Contract เช่น `noti`, `noti_staff`, `noti_reporter`, `skip_timeline`, `recursive_counter`, `timestamp`, `use_admin` รวมถึงฟิลด์ `results` ที่ส่งผ่านมาจาก internal API `join_forward` ทำให้ผู้ใช้งานเข้าใจผิดว่าต้องส่งหรือจะได้รับฟิลด์เหล่านี้เสมอ

### การตัดสินใจ (Decision)
1. **Request Body:** แสดงเฉพาะพารามิเตอร์สาธารณะ ได้แก่ `ticket_id` / `client_ticket_id` / `message_id`, `origin_group`, `destination_group`, `scenario`, `note`, `photo` / `photo_base64` ทั้งใน `docs.html` และ `docs/action-apis.md`
2. **Output:** แสดงเฉพาะฟิลด์ผลลัพธ์สาธารณะ ได้แก่ `status`, `message`, `exec_time`, `credit_balance`, `api_log_session_id`, `api_log_session_id_join_forward` โดยนำ `results` ออก
3. **ไม่เปลี่ยนแปลงพฤติกรรมเซิร์ฟเวอร์:** เป็นการปรับเอกสารให้สะท้อน Public Contract เท่านั้น พารามิเตอร์ภายในยังคงทำงานเหมือนเดิม

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** Contract ชัดเจนขึ้น ผู้ใช้งานไม่ต้องเดาว่าฟิลด์ใดต้องส่งหรือฟิลด์ใดเป็นข้อมูลภายใน
- **ข้อควรระวัง:** หากในอนาคตต้องการเปิดพารามิเตอร์เพิ่มเติม ต้องผ่านการทบทวนและบันทึกเป็น Public Contract อย่างชัดเจนก่อน

---

## ADR-014: การขยายฟิลด์บริบทเรื่องแจ้งใน Query APIs (`type_reporter`, `user_id`, `is_follow`, `is_forward`, `status_latest`) และการรองรับ Wildcard ใน `GET /search-org/v1`

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-07)

### บริบท (Context)
ผู้ใช้งาน API ที่ดึงรายการเรื่องแจ้งผ่าน `get-issues` (JSON) และ `download-issues` (CSV) ต้องการข้อมูลบริบทเรื่องแจ้งที่ละเอียดขึ้น เพื่อนำไปใช้คัดกรองและประมวลผลต่อในระบบ Helpdesk ภายใน ได้แก่:
1. ความแตกต่างระหว่างประเภทปัญหาที่ผู้แจ้งระบุ (`type_reporter`) กับประเภทปัญหาที่หน่วยงานเห็นหรือปรับแก้ (`type`)
2. รหัสประจำตัวของผู้แจ้ง (`user_id`) สำหรับการติดตามและเชื่อมโยงข้อมูล
3. ตัวบ่งชี้สถานะติดตามเรื่อง (`is_follow`) และสถานะส่งต่อเรื่อง (`is_forward`)
4. สถานะล่าสุดในระบบ (`status_latest`) คู่ขนานกับสถานะปัจจุบัน (`status`)
นอกจากนี้ ใน API `GET /search-org/v1` ระบบ Backend รองรับการสืบค้นชื่อหน่วยงานด้วย Wildcard (`*` แทนหลายตัวอักษร และ `?` แทนหนึ่งตัวอักษร) แต่ยังไม่เคยระบุคุณสมบัตินี้ในเอกสารอย่างเป็นทางการ

### การตัดสินใจ (Decision)
1. **Query Results Fields:** เพิ่มฟิลด์ `type_reporter`, `user_id`, `is_follow`, `is_forward`, `status_latest` ใน Response Object ของ `get-issues` และใน Header/คอลัมน์ของไฟล์ CSV `download-issues`
2. **Timeline & Chat Details:** เพิ่ม `sender_user_id` ใน `timeline[]` และ `user_name` ใน `chat[]` ของ `get-issue/v2`
3. **Wildcard Search Documentation:** ระบุคำอธิบายพารามิเตอร์ `text` ใน `search-org` ว่ารองรับ wildcard `*` และ `?` (เช่น `บางเขน`, `Traffy*`, `เขตจตุจัก?`)
4. **Synchronized Documentation:** ซิงค์ข้อมูลทั้งหมดให้ตรงกันระหว่าง `docs.html`, `docs/query-apis.md`, และ `openapi.yaml`

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** ผู้ใช้งานสามารถแยกแยะหมวดหมู่ปัญหาและสถานะได้อย่างแม่นยำตั้งแต่ระดับรายการ โดยไม่ต้องเรียก API รายใบซ้ำซ้อน
- **ข้อดี:** การค้นหาหน่วยงานมีความยืดหยุ่นสูงขึ้น ค้นหาได้ง่ายขึ้นแม้จำชื่อเต็มไม่ได้

---

## ADR-015: การปรับปรุง Webhook Event Contract ให้ครอบคลุม `client_ticket_id` และข้อมูลผู้ส่ง (`sender_user_id`, `sender_user_name`) พร้อมการจัดระเบียบตาราง Output Parameters

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-07)

### บริบท (Context)
1. ในระบบ Real-time Webhooks ข้อมูลที่ระบบส่งออกไปยัง Webhook URL ของหน่วยงานมีการแนบหมายเลขเรื่องแจ้งของหน่วยงานปลายทาง (`client_ticket_id`) รวมถึงข้อมูลระบุตัวตนของผู้กระทำเหตุการณ์ (`sender_user_id` และ `sender_user_name`) ทั้งในเหตุการณ์รับเคสใหม่ (`new-issue`), การอัปเดตสถานะ (`update-issue`), และข้อความสนทนา (`chat/comment`) การไม่มีฟิลด์เหล่านี้ในเอกสารทำให้ผู้เชื่อมต่อไม่สามารถใช้งานข้อมูลอ้างอิงได้อย่างเต็มประสิทธิภาพ
2. ในส่วนของตาราง Output Parameters ของ API ต่างๆ ในเอกสารสาธารณะ เดิมมีการแสดง session log และ debug fields ภายใน (`api_log_session_id`, `api_log_session_id_*`, `exec_time`, `source`) ปะปน ทำให้เกิดความสับสนต่อผู้พัฒนาระบบภายนอกว่าจำเป็นต้องประมวลผลฟิลด์เหล่านี้หรือไม่

### การตัดสินใจ (Decision)
1. **Webhook Payloads:** บรรจุฟิลด์ `client_ticket_id`, `sender_user_id`, `sender_user_name` ลงในตาราง Incoming Payload และ JSON Example ของ Webhook ทั้ง 3 ตัว
2. **Webhook Warning Standardization:** ปรับข้อความเตือนการป้องกัน Echo Loop ให้เป็นมาตรฐานเดียวกัน: `"หมายเหตุ: ห้ามส่งข้อมูลที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API [endpoint] เพื่อป้องกันการเกิด loop"`
3. **Public Output Table Hygiene:** จัดระเบียบตาราง Output Parameters ในเอกสารสาธารณะ โดยถอดฟิลด์ internal logging (`api_log_session_id*`) ออกจากตารางคำอธิบายหลัก แต่ยังคงแสดงไว้ในตัวอย่าง Response JSON Payload สำหรับการอ้างอิงและ debug
4. **Synchronized Documentation:** ซิงค์ตารางและข้อกำหนดให้ตรงกันระหว่าง `docs.html`, `docs/webhooks.md`, `docs/action-apis.md`, `docs/query-apis.md`, `docs/authentication.md`, และ `openapi.yaml`

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** Webhook Contract มีความครบถ้วนสมบูรณ์ รองรับการจับคู่เคสข้ามระบบผ่าน `client_ticket_id` และทราบผู้ปฏิบัติงานทันที
- **ข้อดี:** ตาราง Output Parameters ในเอกสารเข้าใจง่าย ชัดเจนใน Business Payload หลัก

---

## ADR-016: การปรับปรุงความถูกต้องของโครงสร้าง Timeline (`user_id`, `user_name`), ข้อมูลแชท (`comment_type`), คอลัมน์ CSV (`user_id`), และข้อความเตือน Loop ป้องกันข้อผิดพลาด

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-08)

### บริบท (Context)
จากการตรวจสอบความถูกต้องของเอกสารเทียบกับ Payload จริงของ API บน Live Server พบประเด็นที่ต้องปรับปรุงรายละเอียดให้ตรงกัน:
1. ใน `timeline[]` ของ `GET /get-issue/v2` คีย์ที่แท้จริงที่ระบบส่งกลับมาคือ `user_id` และ `user_name` (เดิมระบุเป็น `sender_user_id`)
2. ใน `chat[]` ของ `GET /get-issue/v2` มีฟิลด์ `comment_type` ระบุประเภทของข้อความ (`chat`, `chat_staff_only`, `rating`, `comment`)
3. ในไฟล์ CSV จาก `GET /download-issues/v2` มีคอลัมน์ `user_id` ต่อท้ายในแถวข้อมูลจริง
4. ใน Webhook Chat/Comment คำเตือนเรื่องการป้องกัน Echo Loop เดิมอ้างอิงถึงชื่อ API ภายใน `messagecomment` ควรปรับเป็นชื่อ Public Endpoint `comment`
5. การจัดรูปแบบชื่อเจ้าหน้าที่ตัวอย่างให้มีเว้นวรรคมาตรฐาน (`"จนท. Traffy Fondue"`)

### การตัดสินใจ (Decision)
1. ปรับปรุงตารางและ JSON Example ของ `timeline[]` ใน `docs.html`, `docs/query-apis.md`, และ `openapi.yaml` ให้ใช้คีย์ `user_id` และ `user_name`
2. เพิ่มฟิลด์ `comment_type` ในตารางและโครงสร้างของ `chat[]` ใน `docs.html`, `docs/query-apis.md`, และ `openapi.yaml`
3. เพิ่มคอลัมน์ `user_id` ในตัวอย่าง header และแถวข้อมูลของไฟล์ CSV ใน `docs.html` และ `docs/query-apis.md`
4. ปรับข้อความเตือน Loop ใน `docs/webhooks.md` ให้ตรงกับ `docs.html` โดยระบุ `API comment`
5. ซิงค์ชื่อแสดงตัวอย่าง `"จนท. Traffy Fondue"` ให้ตรงกันทุกไฟล์

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** ตัวอย่างโค้ดและ Response Structure ตรงกับผลลัพธ์จริงจาก Live Server 100% ลดความสับสนของนักพัฒนาเมื่อเข้าถึงคีย์ข้อมูลใน Timeline และ Chat

---

## ADR-017: การปรับปรุงข้อกำหนดการป้องกัน Webhook Loop ให้ครอบคลุม Outbound Event Suppression และ Echo Loop Prevention

### สถานะ (Status)
**Accepted** (มีผลบังคับใช้ตั้งแต่วันที่ 2026-11-11)

### บริบท (Context)
ในการเชื่อมต่อระบบผ่าน Webhook มีโอกาสเกิด Infinite Loop จาก 2 กรณี:
1. การที่ระบบ Traffy Fondue ส่ง event ซ้ำกลับไปยังผู้ที่เพิ่งยิง Action API (`/new-issue`, `/update-issue`, `/comment`) ทำให้เกิด duplicate notification
2. การที่ระบบของหน่วยงานภายนอกรับข้อมูลจาก Webhook แล้วนำข้อมูลชุดเดิมวนกลับมายิง Action API เข้าสู่ Traffy Fondue ซ้ำ

เดิมในเอกสารมีการระบุข้อความเตือนเฉพาะกรณีที่ 2 ว่า "ห้ามส่งข้อมูลที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API เพื่อป้องกันการเกิด loop" ทำให้ผู้พัฒนาระบบมีความกังวลหรือสงสัยว่าระบบจะส่ง event ซ้ำกลับมาจากการยิง API ฝั่งตนเองหรือไม่

### การตัดสินใจ (Decision)
1. ปรับปรุงข้อความเตือนและเงื่อนไขการป้องกัน loop ใน Webhook ทั้ง 3 เหตุการณ์ (`new-issue`, `update-issue`, `chat/comment`) ให้ระบุอย่างชัดเจน 2 ข้อ:
   - ระบบจะไม่ส่ง event ที่เกิดขึ้นจากการเรียก API ต้นทาง (`/new-issue`, `/update-issue`, `/comment`) วนกลับมา
   - ห้ามส่งข้อมูลที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API (`/new-issue`, `/update-issue`, `/comment`) เพื่อป้องกันการเกิด loop
2. ซิงค์ข้อความเตือนให้สอดคล้องกันทุกส่วนใน `docs.html` และ `docs/webhooks.md`

### ผลสืบเนื่อง (Consequences)
- **ข้อดี:** ชี้แจงพฤติกรรมของระบบ Traffy Fondue ในการกรอง event ฝั่งตนเอง (Outbound Event Suppression) ให้ชัดเจน ลดความสับสนของผู้พัฒนา และตอกย้ำข้อควรระวังในการป้องกัน Echo Loop ฝั่งผู้รับอย่างมีประสิทธิภาพ






