# การส่งข้อมูลให้ Traffy Fondue (Action APIs)

กลุ่ม API สำหรับส่งเรื่องแจ้งใหม่ ปรับสถานะการดำเนินงาน ให้คะแนน และจัดการส่งต่อเรื่องแจ้ง

---

## 1. API `new-issue` (ส่งเรื่องแจ้งใหม่)

ใช้สำหรับส่งเรื่องแจ้งใหม่จากระบบภายนอกเข้าสู่ระบบ Traffy Fondue

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/new-issue/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `description` | string | **REQUIRED** | รายละเอียดของปัญหา | `"พบฝาท่อระบายน้ำชำรุด"` |
| `latitude` | number | **REQUIRED** | พิกัดละติจูด (GPS) | `13.7563` |
| `longitude` | number | **REQUIRED** | พิกัดลองจิจูด (GPS) | `100.5018` |
| `type_id` | integer | OPTIONAL | รหัสประเภทปัญหา (จาก `get-type-list`) | `12` |
| `type` | string | OPTIONAL | ชื่อประเภทปัญหา | `"ถนน"` |
| `address` | string | OPTIONAL | ที่อยู่หรือจุดสังเกต | `"ปากซอยพหลโยธิน 12"` |
| `photo` | array[string] | OPTIONAL | ลิงก์ URL ของรูปภาพปัญหา | `["https://example.com/img1.jpg"]` |
| `client_ticket_id` | string | OPTIONAL | รหัสอ้างอิงเรื่องแจ้งในระบบของท่าน | `"EXT-2026-001"` |
| `extra_detail` | object | OPTIONAL | ข้อมูลเพิ่มเติมเฉพาะของหน่วยงาน | `{"reporter_phone": "0812345678"}` |

#### Example Request
```json
{
  "description": "พบฝาท่อระบายน้ำชำรุด อาจเกิดอันตราย",
  "latitude": 13.756331,
  "longitude": 100.501765,
  "type_id": 12,
  "type": "ถนน",
  "address": "ใกล้ป้ายรถเมล์ BTS อารีย์",
  "photo": [
    "https://example.com/uploads/issue_1.jpg"
  ],
  "client_ticket_id": "TICKET-EXT-9988"
}
```

---

## 2. API `update-issue` (อัปเดตสถานะเรื่องแจ้ง)

ใช้สำหรับปรับปรุงสถานะการดำเนินงาน (เช่น รับเรื่อง, กำลังทำ, เสร็จสิ้น) พร้อมแนบภาพการแก้ไข หรือไฟล์เอกสารประกอบ

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/update-issue/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `ticket_id` | string | **REQUIRED\*** | รหัสเรื่องแจ้งของ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | **REQUIRED\*** | หรือรหัสอ้างอิงของหน่วยงาน (*ต้องระบุอย่างใดอย่างหนึ่ง) | `"TICKET-EXT-9988"` |
| `state` | string | **REQUIRED** | สถานะใหม่ที่ต้องการอัปเดต (`กำลังดำเนินการ`, `เสร็จสิ้น`, `รอรับเรื่อง` ฯลฯ) | `"เสร็จสิ้น"` |
| `note` | string | OPTIONAL | บันทึกข้อความการดำเนินงาน | `"เจ้าหน้าที่เข้าซ่อมแซมฝาท่อเรียบร้อยแล้ว"` |
| `photo` | array[string] | OPTIONAL | รูปภาพหลังการแก้ไข | `["https://example.com/fixed.jpg"]` |
| `files` | array[string] | OPTIONAL | ลิงก์ไฟล์เอกสารแนบ (เช่น `.pdf`, `.docx`, `.xlsx`) | `["https://example.com/report.pdf"]` |

#### Example Request
```json
{
  "ticket_id": "2023-ABCDEF",
  "state": "เสร็จสิ้น",
  "note": "เจ้าหน้าที่ดำเนินการซ่อมแซมและเทคอนกรีตเรียบร้อยแล้ว",
  "photo": [
    "https://example.com/fixed_photo_1.jpg"
  ]
}
```

---

## 3. API `star` (ประเมินความพึงพอใจ)

ให้คะแนนดาวความพึงพอใจหลังจากเรื่องแจ้งเสร็จสิ้น

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/star/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters
```json
{
  "ticket_id": "2023-ABCDEF",
  "star": 5
}
```

---

## 4. API `comment` (สนทนา/ให้ความเห็นเพิ่มเติม)

ส่งข้อความความคิดเห็นหลังการประเมิน หรือส่งข้อความ Chat ไปยังผู้แจ้งผ่านทาง SMS

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/comment/v1
Authorization: Bearer <token>
Content-Type: application/json
```

---

## 5. API `join-forward` (เชิญร่วม & ส่งต่อเรื่องแจ้ง)

เชิญหน่วยงานอื่นร่วมรับผิดชอบ หรือส่งต่อเคสไปยังหน่วยงานปลายทาง

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/join-forward/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters
```json
{
  "message_id": 30314900,
  "origin_group": 151,
  "destination_group": [1302],
  "scenario": 2,
  "note": "ส่งต่อหน่วยงานที่รับผิดชอบโดยตรง"
}
```
