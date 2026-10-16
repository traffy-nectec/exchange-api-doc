# Graph Report - exchange-api-doc  (2026-10-16)

## Corpus Check
- 16 files · ~23,378 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .css 1)

## Summary
- 237 nodes · 250 edges · 25 communities (20 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `75a4d686`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- TraffyExchangeClient
- TraffyExchangeClient
- Architecture Decision Records (ADR)
- get_auth.sh
- get_issues.sh
- การส่งข้อมูลให้ Traffy Fondue (Action APIs)
- การขอข้อมูลจาก Traffy Fondue (Query APIs)
- README.md
- 🔑 API `get-auth` (ขอ JWT)
- Traffy Fondue Exchange API Documentation 📘
- การส่งข้อมูลแบบ Real-time (Webhooks)
- 3. บันทึกการปรับปรุงล่าสุด (Latest Updates & Changelog)
- 1. วัตถุประสงค์และผลลัพธ์หลัก (Objectives and Key Results - OKRs)
- Traffy Fondue Exchange API - Documentation Overview
- 2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง)
- 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)
- 6. API `get-type-list` (ขอรายการประเภทปัญหา)
- 7. API `get-status-list` (ขอรายการสถานะ)
- Technical Context & Integration Architecture
- ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec
- ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object
- ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ
- ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`)
- ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม

## God Nodes (most connected - your core abstractions)
1. `Architecture Decision Records (ADR)` - 12 edges
2. `TraffyExchangeClient` - 8 edges
3. `TraffyExchangeClient` - 8 edges
4. `Traffy Fondue Exchange API Documentation 📘` - 8 edges
5. `การขอข้อมูลจาก Traffy Fondue (Query APIs)` - 8 edges
6. `3. บันทึกการปรับปรุงล่าสุด (Latest Updates & Changelog)` - 7 edges
7. `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` - 6 edges
8. `ADR-001: การกำหนดให้ `GET /get-issue/v2` เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ` - 5 edges
9. `ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object` - 5 edges
10. `ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (25 total, 5 thin omitted)

### Community 2 - "Architecture Decision Records (ADR)"
Cohesion: 0.07
Nodes (27): ADR-001: การกำหนดให้ `GET /get-issue/v2` เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ, ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional, ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract, ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ, ADR-010: การบังคับโครงสร้างหัวการ์ด API ขึ้นบรรทัดใหม่แยกระหว่าง Title และ Endpoint URL (Strict Line-Break & Cache-Busting Fallback), Architecture Decision Records (ADR), การตัดสินใจ (Decision), การตัดสินใจ (Decision) (+19 more)

### Community 6 - "การส่งข้อมูลให้ Traffy Fondue (Action APIs)"
Cohesion: 0.07
Nodes (27): 1. API `new-issue` (ส่งเรื่องแจ้งใหม่), 2. API `update-issue` (อัปเดตสถานะเรื่องแจ้ง), 3. API `star` (ประเมินความพึงพอใจ), 4. API `comment` (สนทนา/ให้ความเห็นเพิ่มเติม), 5. API `join-forward` (เชิญร่วม & ส่งต่อเรื่องแจ้ง), Endpoint URL, Endpoint URL, Endpoint URL (+19 more)

### Community 7 - "การขอข้อมูลจาก Traffy Fondue (Query APIs)"
Cohesion: 0.10
Nodes (20): 1. API `get-issues` (ขอรายการเรื่องแจ้ง), 3. API `download-issues` (ดาวน์โหลดไฟล์ CSV), 4. API `search-org` (ค้นหาหน่วยงาน), Endpoint URL, Endpoint URL, Endpoint URL, Example Request, Example Request (+12 more)

### Community 8 - "README.md"
Cohesion: 0.16
Nodes (8): cURL, Node.js, Python, การยืนยันตัวตน (Authentication), 🛠 ตัวอย่างการเรียกใช้งาน, รูปแบบ Error Response, รหัสข้อผิดพลาดและการแก้ไข (Error Codes & Troubleshooting), 📋 รายการ Error Messages ที่พบบ่อย

### Community 9 - "🔑 API `get-auth` (ขอ JWT)"
Cohesion: 0.25
Nodes (8): 🔑 API `get-auth` (ขอ JWT), Endpoint URL, Example Request Body, Example Response (Success), Request Parameters (JSON Body), Response Parameters (JSON Body), คำเตือนด้านความปลอดภัย, ฟิลด์ใน `results`:

### Community 10 - "Traffy Fondue Exchange API Documentation 📘"
Cohesion: 0.14
Nodes (14): 1. ขอรับ JWT Token, 2026-09-26, 2026-10-05, 2026-10-12, 2026-10-16, 2. ดึงรายการเรื่องแจ้งล่าสุด, Traffy Fondue Exchange API Documentation 📘, ⚖️ ข้อกำหนดการใช้งานและข้อสงวนสิทธิ์ความรับผิดชอบ (Terms of Use & Legal Disclaimer) (+6 more)

### Community 11 - "การส่งข้อมูลแบบ Real-time (Webhooks)"
Cohesion: 0.18
Nodes (10): 1. เมื่อมีเรื่องแจ้งเข้ามาใหม่ (New Issue Event), 2. เมื่อมีการอัปเดตสถานะ (Status Update Event), 3. เมื่อมีการแสดงความคิดเห็นหรือแชท (Chat/Comment Event), Example Webhook Payload (PATCH), Example Webhook Payload (POST), Example Webhook Payload (POST), Webhook Payload (`PATCH`), Webhook Payload (`POST`) (+2 more)

### Community 12 - "3. บันทึกการปรับปรุงล่าสุด (Latest Updates & Changelog)"
Cohesion: 0.18
Nodes (11): 1. ข้อมูลกรรมสิทธิ์และ Repositories (Project Ownership), 2. โครงสร้างและเนื้อหาสำคัญที่ส่งมอบ (Delivered Artifacts), 3. บันทึกการปรับปรุงล่าสุด (Latest Updates & Changelog), 4. ขั้นตอนการนำไปต่อยอดและพัฒนาต่อ (Next Steps & Recommendations), 🚀 Exchange API (v2) Release (Version: 2026-09-26), 🧪 Live API Verification & Contract Alignment Release (Version: 2026-10-05), Project Handoff Documentation, 🛠️ Response Alignment & Navigation Single Source of Truth (Version: 2026-10-12) (+3 more)

### Community 13 - "1. วัตถุประสงค์และผลลัพธ์หลัก (Objectives and Key Results - OKRs)"
Cohesion: 0.25
Nodes (8): 1. วัตถุประสงค์และผลลัพธ์หลัก (Objectives and Key Results - OKRs), 2.1 บริการ API แบ่งตามหมวดหมู่ (Service Domains), 2.2 มาตรฐานความถูกต้องของข้อมูล (Data Validation Principles), 2. กรอบความรู้เชิงระบบ (System Knowledge Framework), 🎯 Objective 1: เอกสาร API มาตรฐานสมบูรณ์แบบ 100% สำหรับหน่วยงานภายนอก (Standardized API Docs), 🎯 Objective 2: ลดระยะเวลาและภาระงานในการ Onboarding หน่วยงานใหม่ (Fast Integration), 🎯 Objective 3: การจัดการความปลอดภัยและโควต้าอย่างเป็นระบบ (Security & Quota Management), Objectives, Knowledge & Framework (OKF)

### Community 14 - "Traffy Fondue Exchange API - Documentation Overview"
Cohesion: 0.25
Nodes (8): 📤 1. ส่งข้อมูลเข้า Traffy Fondue (Data Ingestion), 📥 2. ขอข้อมูลจาก Traffy Fondue (Data Retrieval), 🔔 3. ส่งข้อมูลแบบ Real-time (Webhooks / Push), Traffy Fondue Exchange API - Documentation Overview, 🚀 ขั้นตอนการขอใช้งาน Exchange API (Onboarding), ⚖️ ข้อกำหนดการใช้งานและข้อสงวนสิทธิ์ความรับผิดชอบ (Terms of Use & Legal Disclaimer), ⚠️ ข้อกำหนดเรื่องโควต้า (Credit Balance), 🔹 รูปแบบการเชื่อมต่อ (Integration Modes)

### Community 15 - "2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง)"
Cohesion: 0.29
Nodes (7): 2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง), Endpoint URL, Example Request, Example Response (ผลจริงจากการทดสอบ), Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 16 - "5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)"
Cohesion: 0.29
Nodes (7): 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด), Endpoint URL, Example Request, Example Response (ผลจริงจากการทดสอบ org_id=151), Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 17 - "6. API `get-type-list` (ขอรายการประเภทปัญหา)"
Cohesion: 0.29
Nodes (7): 6. API `get-type-list` (ขอรายการประเภทปัญหา), Endpoint URL, Example Request, Example Response, Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 18 - "7. API `get-status-list` (ขอรายการสถานะ)"
Cohesion: 0.29
Nodes (7): 7. API `get-status-list` (ขอรายการสถานะ), Endpoint URL, Example Request, Example Response, Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 19 - "Technical Context & Integration Architecture"
Cohesion: 0.33
Nodes (6): 1. ข้อมูลระบบและสิ่งแวดล้อม (System Overview), 2.1 Issue Data Model, 2.2 Quota & Usage Model, 2. โครงสร้างข้อมูลหลัก (Core Schemas), 3. ความปลอดภัยและข้อควรระวัง (Security & Integration Principles), Technical Context & Integration Architecture

### Community 20 - "ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec"
Cohesion: 0.40
Nodes (5): ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 21 - "ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object"
Cohesion: 0.40
Nodes (5): ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 22 - "ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ"
Cohesion: 0.40
Nodes (5): ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 23 - "ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`)"
Cohesion: 0.40
Nodes (5): ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`), การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 24 - "ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม"
Cohesion: 0.40
Nodes (5): ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Architecture Decision Records (ADR)` connect `Architecture Decision Records (ADR)` to `README.md`, `ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec`, `ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object`, `ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ`, `ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`)`, `ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม`?**
  _High betweenness centrality (0.335) - this node is a cross-community bridge._
- **Should `Architecture Decision Records (ADR)` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._
- **Why does `การขอข้อมูลจาก Traffy Fondue (Query APIs)` connect `การขอข้อมูลจาก Traffy Fondue (Query APIs)` to `README.md`, `2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง)`, `5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)`, `6. API `get-type-list` (ขอรายการประเภทปัญหา)`, `7. API `get-status-list` (ขอรายการสถานะ)`?**
  _High betweenness centrality (0.310) - this node is a cross-community bridge._
- **Should `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._
- **Why does `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` connect `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` to `README.md`?**
  _High betweenness centrality (0.182) - this node is a cross-community bridge._
- **Should `การขอข้อมูลจาก Traffy Fondue (Query APIs)` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `Traffy Fondue Exchange API Documentation 📘` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._