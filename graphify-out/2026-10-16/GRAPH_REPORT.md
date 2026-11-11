# Graph Report - exchange-api-doc  (2026-10-16)

## Corpus Check
- 16 files · ~23,074 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 5 file(s) not represented in the graph (top: (none) 4, .css 1)

## Summary
- 232 nodes · 245 edges · 23 communities (18 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2e11dd93`
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
- 3. API `download-issues` (ดาวน์โหลดไฟล์ CSV)
- 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)
- 6. API `get-type-list` (ขอรายการประเภทปัญหา)
- 4. API `search-org` (ค้นหาหน่วยงาน)
- ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional
- ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec
- ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract
- ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ

## God Nodes (most connected - your core abstractions)
1. `Architecture Decision Records (ADR)` - 11 edges
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

## Communities (23 total, 5 thin omitted)

### Community 2 - "Architecture Decision Records (ADR)"
Cohesion: 0.07
Nodes (27): ADR-001: การกำหนดให้ `GET /get-issue/v2` เป็นมาตรฐานหลักในการดึงข้อมูลรายละเอียดเรื่องแจ้งรายใบ, ADR-002: การปรับปรุง Contract ของ `POST /get-auth/v1` ให้ `results` เป็น JSON Object, ADR-003: การระบุคำแนะนำเชิงป้องกันสำหรับ `GET /get-org-list/v1` ให้ส่ง Parameter `org_id` เสมอ, ADR-005: การรองรับบริบทการใช้งาน 2 รูปแบบใน `POST /comment/v1` (`comment` vs `chat`), ADR-007: มาตรการป้องกัน Infinite Webhook Feedback Loop ระหว่างระบบภายนอกและแพลตฟอร์ม, Architecture Decision Records (ADR), การตัดสินใจ (Decision), การตัดสินใจ (Decision) (+19 more)

### Community 6 - "การส่งข้อมูลให้ Traffy Fondue (Action APIs)"
Cohesion: 0.07
Nodes (27): 1. API `new-issue` (ส่งเรื่องแจ้งใหม่), 2. API `update-issue` (อัปเดตสถานะเรื่องแจ้ง), 3. API `star` (ประเมินความพึงพอใจ), 4. API `comment` (สนทนา/ให้ความเห็นเพิ่มเติม), 5. API `join-forward` (เชิญร่วม & ส่งต่อเรื่องแจ้ง), Endpoint URL, Endpoint URL, Endpoint URL (+19 more)

### Community 7 - "การขอข้อมูลจาก Traffy Fondue (Query APIs)"
Cohesion: 0.09
Nodes (22): 1. API `get-issues` (ขอรายการเรื่องแจ้ง), 2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง), 7. API `get-status-list` (ขอรายการสถานะ), Endpoint URL, Endpoint URL, Endpoint URL, Example Request, Example Request (+14 more)

### Community 8 - "README.md"
Cohesion: 0.15
Nodes (9): 1. ข้อมูลระบบและสิ่งแวดล้อม (System Overview), 2.1 Issue Data Model, 2.2 Quota & Usage Model, 2. โครงสร้างข้อมูลหลัก (Core Schemas), 3. ความปลอดภัยและข้อควรระวัง (Security & Integration Principles), Technical Context & Integration Architecture, รูปแบบ Error Response, รหัสข้อผิดพลาดและการแก้ไข (Error Codes & Troubleshooting) (+1 more)

### Community 9 - "🔑 API `get-auth` (ขอ JWT)"
Cohesion: 0.15
Nodes (13): 🔑 API `get-auth` (ขอ JWT), cURL, Endpoint URL, Example Request Body, Example Response (Success), Node.js, Python, Request Parameters (JSON Body) (+5 more)

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
Cohesion: 0.22
Nodes (8): 1. วัตถุประสงค์และผลลัพธ์หลัก (Objectives and Key Results - OKRs), 2.1 บริการ API แบ่งตามหมวดหมู่ (Service Domains), 2.2 มาตรฐานความถูกต้องของข้อมูล (Data Validation Principles), 2. กรอบความรู้เชิงระบบ (System Knowledge Framework), 🎯 Objective 1: เอกสาร API มาตรฐานสมบูรณ์แบบ 100% สำหรับหน่วยงานภายนอก (Standardized API Docs), 🎯 Objective 2: ลดระยะเวลาและภาระงานในการ Onboarding หน่วยงานใหม่ (Fast Integration), 🎯 Objective 3: การจัดการความปลอดภัยและโควต้าอย่างเป็นระบบ (Security & Quota Management), Objectives, Knowledge & Framework (OKF)

### Community 14 - "Traffy Fondue Exchange API - Documentation Overview"
Cohesion: 0.25
Nodes (8): 📤 1. ส่งข้อมูลเข้า Traffy Fondue (Data Ingestion), 📥 2. ขอข้อมูลจาก Traffy Fondue (Data Retrieval), 🔔 3. ส่งข้อมูลแบบ Real-time (Webhooks / Push), Traffy Fondue Exchange API - Documentation Overview, 🚀 ขั้นตอนการขอใช้งาน Exchange API (Onboarding), ⚖️ ข้อกำหนดการใช้งานและข้อสงวนสิทธิ์ความรับผิดชอบ (Terms of Use & Legal Disclaimer), ⚠️ ข้อกำหนดเรื่องโควต้า (Credit Balance), 🔹 รูปแบบการเชื่อมต่อ (Integration Modes)

### Community 15 - "3. API `download-issues` (ดาวน์โหลดไฟล์ CSV)"
Cohesion: 0.33
Nodes (6): 3. API `download-issues` (ดาวน์โหลดไฟล์ CSV), Endpoint URL, Example Request, Example Response (ผลจริงจากการทดสอบ org_id=151&duration=today — header + 1 แถวแรกจากไฟล์ CSV จริง), Input Parameters (Query String), Output Parameters

### Community 16 - "5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)"
Cohesion: 0.29
Nodes (7): 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด), Endpoint URL, Example Request, Example Response (ผลจริงจากการทดสอบ org_id=151), Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 17 - "6. API `get-type-list` (ขอรายการประเภทปัญหา)"
Cohesion: 0.29
Nodes (7): 6. API `get-type-list` (ขอรายการประเภทปัญหา), Endpoint URL, Example Request, Example Response, Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 18 - "4. API `search-org` (ค้นหาหน่วยงาน)"
Cohesion: 0.33
Nodes (6): 4. API `search-org` (ค้นหาหน่วยงาน), Endpoint URL, Example Request, Input Parameters (Query String), Output Parameters (JSON Response), ฟิลด์ใน `results`:

### Community 19 - "ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional"
Cohesion: 0.40
Nodes (5): ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 20 - "ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec"
Cohesion: 0.40
Nodes (5): ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 21 - "ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract"
Cohesion: 0.40
Nodes (5): ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

### Community 22 - "ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ"
Cohesion: 0.40
Nodes (5): ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ, การตัดสินใจ (Decision), บริบท (Context), ผลสืบเนื่อง (Consequences), สถานะ (Status)

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `การขอข้อมูลจาก Traffy Fondue (Query APIs)` connect `การขอข้อมูลจาก Traffy Fondue (Query APIs)` to `README.md`, `3. API `download-issues` (ดาวน์โหลดไฟล์ CSV)`, `5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)`, `6. API `get-type-list` (ขอรายการประเภทปัญหา)`, `4. API `search-org` (ค้นหาหน่วยงาน)`?**
  _High betweenness centrality (0.315) - this node is a cross-community bridge._
- **Should `Architecture Decision Records (ADR)` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._
- **Why does `Architecture Decision Records (ADR)` connect `Architecture Decision Records (ADR)` to `README.md`, `ADR-004: การปรับ Parameter `origin_group` ใน `POST /join-forward/v1` เป็นแบบ Optional`, `ADR-006: การคงความเข้ากันได้ย้อนหลัง (Backward Compatibility) และการประกาศ Dual-Version ใน OpenAPI Spec`, `ADR-008: การรวม Single Source of Truth สำหรับ Versioning ใน UI และการปรับปรุงความถูกต้องของ Parameter & Response Contract`, `ADR-009: การปรับปรุงโครงสร้างหัวการ์ด API เป็น 2 บรรทัด (Two-Row Hierarchy) และการประกาศข้อกำหนดความรับผิดชอบต่อเนื้อหาและข้อมูลดิบ`?**
  _High betweenness centrality (0.311) - this node is a cross-community bridge._
- **Should `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` be split into smaller, more focused modules?**
  _Cohesion score 0.07407407407407407 - nodes in this community are weakly interconnected._
- **Why does `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` connect `การส่งข้อมูลให้ Traffy Fondue (Action APIs)` to `README.md`?**
  _High betweenness centrality (0.185) - this node is a cross-community bridge._
- **Should `การขอข้อมูลจาก Traffy Fondue (Query APIs)` be split into smaller, more focused modules?**
  _Cohesion score 0.09090909090909091 - nodes in this community are weakly interconnected._
- **Should `Traffy Fondue Exchange API Documentation 📘` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._