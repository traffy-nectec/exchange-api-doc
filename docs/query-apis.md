# การขอข้อมูลจาก Traffy Fondue (Query APIs)

กลุ่ม API สำหรับดึงข้อมูลเรื่องแจ้ง โครงสร้างหน่วยงาน ประเภทปัญหา และสถานะต่างๆ จากระบบ Traffy Fondue มาประมวลผลหรือแสดงผลบนระบบของหน่วยงาน

---

## 1. API `get-issues` (ขอรายการเรื่องแจ้ง)

ใช้สำหรับดึงรายการเรื่องแจ้งที่หน่วยงานได้รับ พร้อมตัวกรอง (Filter) ต่างๆ เช่น วันที่, สถานะ, ประเภทปัญหา, คำค้นหา และการแบ่งหน้า (Pagination)

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-issues/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `start_date` | string | OPTIONAL | วันที่เริ่มต้น (YYYY-MM-DD) | `"2023-01-01"` (Default: 3 วันย้อนหลัง) |
| `end_date` | string | OPTIONAL | วันที่สิ้นสุด (YYYY-MM-DD) | `"2023-01-31"` (Default: วันปัจจุบัน) |
| `state` | string / array | OPTIONAL | กรองสถานะเรื่องแจ้ง เช่น `"รอรับเรื่อง"`, `"กำลังดำเนินการ"`, `"เสร็จสิ้น"` | `["รอรับเรื่อง", "กำลังดำเนินการ"]` |
| `type` | string / array | OPTIONAL | กรองประเภทปัญหา เช่น `"ถนน"`, `"ทางเท้า"`, `"ความสะอาด"` | `["ถนน", "ทางเท้า"]` |
| `org_id` | integer / array | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล (เฉพาะหน่วยงานในสังกัด) | `151` หรือ `[151, 1302]` |
| `client_ticket_id` | string | OPTIONAL | รหัสเรื่องแจ้งอ้างอิงของหน่วยงานภายนอก | `"MY-TICKET-001"` |
| `keyword` | string | OPTIONAL | คำค้นหาในรายละเอียดหรือที่อยู่ | `"ท่อระบายน้ำ"` |
| `sort` | string | OPTIONAL | รูปแบบการเรียงลำดับ (`timestamp_asc`, `timestamp_desc`, `update_asc`, `update_desc`) | `"timestamp_desc"` |
| `offset` | integer | OPTIONAL | ลำดับเริ่มต้นของรายการ (เริ่มที่ 0) | `0` |
| `limit` | integer | OPTIONAL | จำนวนรายการสูงสุดต่อรอบ (สูงสุดไม่เกิน 1,000) | `100` |

#### Example Request
```json
{
  "start_date": "2023-01-01",
  "end_date": "2023-01-31",
  "state": ["รอรับเรื่อง", "กำลังดำเนินการ"],
  "sort": "timestamp_desc",
  "offset": 0,
  "limit": 50
}
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `credit_balance` | integer | โควต้าคงเหลือ |
| `total` | integer | จำนวนรายการทั้งหมดที่ตรงตามเงื่อนไข |
| `results` | array[object] | รายการเรื่องแจ้ง (ดูฟิลด์ด้านล่าง) |

#### ฟิลด์ใน `results`:
* `ticket_id`: หมายเลขเรื่องแจ้งในระบบ Fondue (เช่น `"2023-ABCDEF"`)
* `client_ticket_id`: หมายเลขเรื่องแจ้งของหน่วยงานภายนอก (ถ้ามี)
* `description`: รายละเอียดของปัญหา
* `type_id` / `type`: รหัสและชื่อประเภทปัญหา
* `timestamp`: วันเวลาที่แจ้ง (UTC+7)
* `last_update`: วันเวลาที่มีการอัปเดตล่าสุด
* `state`: สถานะปัจจุบัน (`รอรับเรื่อง`, `กำลังดำเนินการ`, `เสร็จสิ้น`, `ส่งต่อ` ฯลฯ)
* `latitude` / `longitude`: พิกัด GPS
* `address`: ที่อยู่สถานที่เกิดเหตุ
* `photo_url`: ลิงก์รูปภาพเริ่มต้น
* `orgs`: รายชื่อหน่วยงานที่รับผิดชอบ

---

## 2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง)

ใช้สำหรับดึงข้อมูลรายละเอียดอย่างสมบูรณ์ของเรื่องแจ้งราย `ticket_id` รวมถึงประวัติการดำเนินการ (Action Logs) และภาพประกอบทุกขั้นตอน

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-issue/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `ticket_id` | string | **REQUIRED\*** | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | **REQUIRED\*** | หรือใช้รหัสอ้างอิงของหน่วยงานภายนอก (*ต้องระบุอย่างใดอย่างหนึ่ง) | `"MY-APP-0099"` |

#### Example Request
```json
{
  "ticket_id": "2023-ABCDEF"
}
```

---

## 3. API `download-issues` (ดาวน์โหลดไฟล์ CSV)

ใช้สำหรับ Export ข้อมูลเรื่องแจ้งเป็นไฟล์ CSV ตามช่วงเวลาและตัวกรองที่กำหนด

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/download-issues/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Output Parameters
คืนค่าเป็น URL สำหรับดาวน์โหลดไฟล์ CSV หรือส่งข้อมูลไฟล์โดยตรง

---

## 4. API `search-org` (ค้นหาหน่วยงาน)

ค้นหารหัสหน่วยงาน (`org_id`) และชื่อหน่วยงานจากคำค้นหา เพื่อนำไปใช้กับ API อื่นๆ

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/search-org/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters
```json
{
  "keyword": "บางเขน"
}
```

---

## 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)

ดึงรายชื่อหน่วยงานที่อยู่ภายใต้การกำกับดูแลของ Account นี้

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-org-list/v1
Authorization: Bearer <token>
Content-Type: application/json
```

---

## 6. API `get-type-list` (ขอรายการประเภทปัญหา)

ดึง Master Data รายการประเภทปัญหาและหมวดหมู่ที่หน่วยงานรับผิดชอบ

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-type-list/v1
Authorization: Bearer <token>
Content-Type: application/json
```

---

## 7. API `get-status-list` (ขอรายการสถานะ)

ดึงรายการสถานะที่สามารถใช้งานได้ในการปรับปรุงเรื่องแจ้ง

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-status-list/v1
Authorization: Bearer <token>
Content-Type: application/json
```
