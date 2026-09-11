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
| `description` | string | OPTIONAL\* | รายละเอียดของปัญหา (*ถ้าไม่ส่งมา ระบบจะเติมค่าเริ่มต้นให้อัตโนมัติ ไม่ error) | `"พบฝาท่อระบายน้ำชำรุด"` |
| `latitude` | number | **REQUIRED** | พิกัดละติจูด (GPS) | `13.7563` |
| `longitude` | number | **REQUIRED** | พิกัดลองจิจูด (GPS) | `100.5018` |
| `issue_category_id` | integer | OPTIONAL\*\* | 🆕 รหัสหมวดหมู่กลาง เลือกหมวดหมู่ตรงๆ | `12` |
| `org_category_id` | integer หรือ `null` | OPTIONAL\*\* | 🆕 รหัสหมวดหมู่ custom ของหน่วยงาน เลือกตรงๆ (ส่ง `null`/`"null"` ได้) | `45` |
| `category_name_th` | string | OPTIONAL\*\* | 🆕 เลือกหมวดหมู่จากชื่อภาษาไทย | `"ถนน"` |
| `topic` | string | OPTIONAL\*\* | 🆕 ชื่อประเภทปัญหา (alias ของ `topic_id`) | `"ถนน"` |
| `topic_id` / `type_id` | integer | OPTIONAL\*\* | รหัสประเภทปัญหาแบบเดิม (จาก `get-type-list`) — ยังใช้งานได้ ระบบจะ auto-convert เป็น `issue_category_id`/`org_category_id`/`category_name_th` ให้อัตโนมัติ | `12` |
| `type_name` | string | OPTIONAL\*\* | ชื่อประเภทปัญหาแบบเดิม — auto-convert เช่นกัน | `"ถนน"` |
| `photo` | array[string] | OPTIONAL\*\*\* | ลิงก์ URL ของรูปภาพปัญหา (เลือกอย่างใดอย่างหนึ่งกับ `photo_base64`) | `["https://example.com/img1.jpg"]` |
| `photo_base64` | string / array[string] | OPTIONAL\*\*\* | รูปภาพปัญหาแบบ base64 (เลือกอย่างใดอย่างหนึ่งกับ `photo`) | `"iVBORw0KGgo..."` |
| `address` | string | OPTIONAL | ที่อยู่หรือจุดสังเกต | `"ปากซอยพหลโยธิน 12"` |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานปลายทาง รองรับหลายค่าคั่นด้วยจุลภาค | `"151,1302"` |
| `reporter_name` | string | OPTIONAL | ชื่อผู้แจ้ง | `"สมชาย ใจดี"` |
| `reporter_phone` | string | OPTIONAL | เบอร์โทรผู้แจ้ง | `"0812345678"` |
| `reporter_sms` | string | OPTIONAL | เบอร์รับ SMS แจ้งเตือนความคืบหน้า | `"0812345678"` |
| `reporter_email` | string | OPTIONAL | อีเมลผู้แจ้ง สำหรับรับแจ้งเตือนความคืบหน้า | `"user@example.com"` |
| `client_user_id` | string | OPTIONAL | รหัสผู้ใช้งานในระบบของท่าน | `"U-12345"` |
| `client_ticket_id` | string | OPTIONAL | รหัสอ้างอิงเรื่องแจ้งในระบบของท่าน | `"EXT-2026-001"` |
| `client_timestamp` | string | OPTIONAL | เวลาที่แจ้งเรื่องในระบบของท่าน | `"2026-09-09T10:00:00"` |
| `token_secret_key` | string | OPTIONAL | ใช้ยืนยันตัวตนแทน Bearer token ได้ (auth ทางเลือก) | `"xxxxxxxx"` |
| `extra_detail` | object | OPTIONAL | ข้อมูลเพิ่มเติมเฉพาะของหน่วยงาน | `{"reporter_phone": "0812345678"}` |
| `line_user_id` | string | OPTIONAL | LINE User ID ของผู้แจ้ง (กรณีแจ้งผ่าน LINE) | `"U0123456789abcdef"` |
| `ai_photo_id` | string | OPTIONAL | รหัสอ้างอิงผลตรวจสอบรูปภาพด้วย AI | `"AIP-001"` |
| `gemini_id` | string | OPTIONAL | รหัสอ้างอิงผลประมวลผลด้วย Gemini | `"GEM-001"` |

\* ถ้าไม่ส่ง `description` ระบบจะเติมค่าเริ่มต้นให้เอง ไม่ error
\*\* เลือกระบุหมวดหมู่ได้ทางใดทางหนึ่ง — แนะนำให้ใช้ชุดใหม่ (`issue_category_id`/`org_category_id`/`category_name_th`/`topic`) แต่ชุดเดิม (`topic_id`/`type_id`/`type_name`) ยังใช้งานได้ตามปกติเพราะระบบ auto-convert ให้
\*\*\* เลือกส่งรูปภาพได้ทางใดทางหนึ่งระหว่าง `photo` กับ `photo_base64`

#### Example Request
```json
{
  "description": "พบฝาท่อระบายน้ำชำรุด อาจเกิดอันตราย",
  "latitude": 13.756331,
  "longitude": 100.501765,
  "issue_category_id": 12,
  "category_name_th": "ถนน",
  "address": "ใกล้ป้ายรถเมล์ BTS อารีย์",
  "photo": [
    "https://example.com/uploads/issue_1.jpg"
  ],
  "client_ticket_id": "TICKET-EXT-9988"
}
```

### Output Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `status` | string | สถานะผลลัพธ์ |
| `message` | string | ข้อความอธิบายผล |
| `exec_time` | number | เวลาที่ใช้ประมวลผล (วินาที) |
| `credit_balance` | number / null | เครดิตคงเหลือของ API key (`null` = ไม่จำกัด) |
| `api_log_session` | string | รหัส log การเรียกใช้งาน ⚠️ **สะกดไม่มี `_id`** ต่างจาก API อื่นทั้งหมด |
| `org_id` | array | รหัสหน่วยงานปลายทางของเรื่องแจ้งนี้ |
| `results.ticket_id` | string | รหัสเรื่องแจ้งที่ระบบสร้างขึ้น |
| `results.password` | string | รหัสผ่านสำหรับติดตามเรื่องแจ้ง |
| `results.smsStatus` | string | สถานะการส่ง SMS (มีเมื่อระบบส่ง SMS แจ้งเตือน) |
| `results.emailStatus` | string | สถานะการส่งอีเมล (มีเมื่อระบบส่งอีเมลแจ้งเตือน) |
| `results.client_ticket_id` | string | รหัสอ้างอิงที่ท่านส่งมา (มีเมื่อส่ง `client_ticket_id` มาในคำขอ) |
| `api_log_session_id_new-issue` | string | รหัส log จากระบบปลายทาง (มีเมื่อ downstream ส่งค่ากลับมา) |

---

## 2. API `update-issue` (อัปเดตสถานะเรื่องแจ้ง)

ใช้สำหรับปรับปรุงสถานะการดำเนินงาน (เช่น รับเรื่อง, กำลังทำ, เสร็จสิ้น) พร้อมแนบภาพการแก้ไข และควบคุมการแจ้งเตือนผู้แจ้ง/เจ้าหน้าที่

### Endpoint URL
```http
PATCH https://publicapi.traffy.in.th/exchange-api/update-issue/v1
Authorization: Bearer <token>
Content-Type: application/json
```

⚠️ ต้องเรียกด้วย HTTP Method **`PATCH`** เท่านั้น (ไม่ใช่ `POST`)

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `ticket_id` | string | REQUIRED\* | รหัสเรื่องแจ้งของ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | REQUIRED\* | หรือรหัสอ้างอิงของหน่วยงาน | `"TICKET-EXT-9988"` |
| `message_id` | integer | REQUIRED\* | หรือรหัสข้อความอ้างอิง (*เลือกระบุอย่างใดอย่างหนึ่งจากสามตัวนี้) | `30314900` |
| `org_id` | string | OPTIONAL | รหัสหน่วยงาน | `"151"` |
| `issue_status_id` | integer | REQUIRED\*\* | 🆕 รหัสสถานะกลาง เลือกสถานะตรงๆ | `3` |
| `org_status_id` | integer หรือ `null` | REQUIRED\*\* | 🆕 รหัสสถานะ custom ของหน่วยงาน เลือกตรงๆ (ส่ง `null`/`""`/`"null"` ได้) | `12` |
| `state_name` | string | REQUIRED\*\* | 🆕 ชื่อสถานะ จับคู่ได้ทั้งชื่อ custom ของหน่วยงานและชื่อสถานะกลาง | `"เสร็จสิ้น"` |
| `status_id` | integer | REQUIRED\*\* | รหัสสถานะแบบเดิม — ยังใช้งานได้ ระบบ auto-convert เป็น `issue_status_id`/`org_status_id` ให้ | `3` |
| `state_id` / `org_state_id` | integer | REQUIRED\*\* | alias ของ `status_id` แบบเดิม — auto-convert เช่นกัน | `3` |
| `note` | string | **REQUIRED** | บันทึกข้อความการดำเนินงาน | `"เจ้าหน้าที่เข้าซ่อมแซมฝาท่อเรียบร้อยแล้ว"` |
| `extra_detail` | object | OPTIONAL | ข้อมูลเพิ่มเติมเฉพาะของหน่วยงาน | `{"note_internal": "ตรวจสอบซ้ำแล้ว"}` |
| `photo` | array[string] | OPTIONAL\*\*\* | รูปภาพหลังการแก้ไข เป็นลิงก์ URL | `["https://example.com/fixed.jpg"]` |
| `photo_base64` | string / array[string] | OPTIONAL\*\*\* | รูปภาพหลังการแก้ไขแบบ base64 | `"iVBORw0KGgo..."` |
| `photos` | array[object] | OPTIONAL\*\*\* | 🆕 รูปภาพหลังการแก้ไข พร้อมระบุ note แยกรายรูป รูปแบบ `{uri หรือ url, note}` | `[{"url": "https://example.com/fixed.jpg", "note": "ซ่อมเสร็จแล้ว"}]` |
| `noti` | boolean | OPTIONAL | 🆕 shorthand ตั้งค่าให้ทั้ง `noti_reporter` และ `noti_staff` พร้อมกัน | `true` |
| `noti_reporter` | boolean | OPTIONAL (default `true`) | 🆕 แจ้งเตือนผู้แจ้งเรื่องหรือไม่ | `true` |
| `noti_staff` | boolean | OPTIONAL (default `true`) | 🆕 แจ้งเตือนเจ้าหน้าที่หรือไม่ | `true` |
| `skip_timeline` | boolean | OPTIONAL (default `false`) | 🆕 ข้ามการบันทึกรายการนี้ลง timeline หรือไม่ | `false` |
| `token_secret_key` | string | OPTIONAL | ใช้ยืนยันตัวตนแทน Bearer token ได้ (auth ทางเลือก) | `"xxxxxxxx"` |

\* เลือกระบุอย่างใดอย่างหนึ่งจาก `ticket_id`/`client_ticket_id`/`message_id`
\*\* ต้องระบุ**อย่างน้อย 1 ค่า**จากกลุ่มนี้เพื่อเปลี่ยนสถานะ ไม่มี field ชื่อ `state` เป็น string ธรรมดา — แนะนำให้ใช้ชุดใหม่ (`issue_status_id`/`org_status_id`/`state_name`) แต่ชุดเดิม (`status_id`/`state_id`/`org_state_id`) ยังใช้งานได้เพราะระบบ auto-convert ให้
\*\*\* เลือกส่งรูปภาพได้ทางใดทางหนึ่งจาก `photo`/`photo_base64`/`photos`

#### Example Request
```json
{
  "ticket_id": "2023-ABCDEF",
  "issue_status_id": 3,
  "note": "เจ้าหน้าที่ดำเนินการซ่อมแซมและเทคอนกรีตเรียบร้อยแล้ว",
  "photos": [
    { "url": "https://example.com/fixed_photo_1.jpg", "note": "หลังซ่อมแซมเสร็จสิ้น" }
  ],
  "noti_reporter": true
}
```

### Output Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `status` | string | สถานะผลลัพธ์ |
| `message` | string | ข้อความอธิบายผล |
| `exec_time` | number | เวลาที่ใช้ประมวลผล (วินาที) |
| `credit_balance` | number / null | เครดิตคงเหลือของ API key |
| `org_id` | string / array | รหัสหน่วยงาน |
| `source` | string | แหล่งที่มาของข้อมูล |
| `api_log_session_id` | string | รหัส log การเรียกใช้งาน |
| `api_log_session_id_update_message` | string | รหัส log จากระบบปลายทาง (มีเมื่อ downstream ส่งค่ากลับมา) |
| `results.smsStatus` | string | สถานะการส่ง SMS แจ้งเตือน (มีเมื่อแจ้งเตือนสำเร็จ) |
| `results.emailStatus` | string | สถานะการส่งอีเมลแจ้งเตือน (มีเมื่อแจ้งเตือนสำเร็จ) |

⚠️ ผลลัพธ์จริงของ API นี้**ไม่มี** `status_id`/`status`/`status_type` ส่งกลับมา หากต้องการตรวจสอบสถานะล่าสุดของเรื่องแจ้งหลังอัปเดต ให้เรียก [`get-issue`](./query-apis.md) เพิ่มเติม

---

## 3. API `star` (ประเมินความพึงพอใจ)

ให้คะแนนดาวความพึงพอใจหลังจากเรื่องแจ้งเสร็จสิ้น

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/star/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `star` | integer | **REQUIRED** | คะแนนดาว 1-5 (โค้ดไม่ปฏิเสธค่า `0` แต่ควรส่งค่า 1-5) | `5` |
| `ticket_id` | string | REQUIRED\* | รหัสเรื่องแจ้งของ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | REQUIRED\* | หรือรหัสอ้างอิงของหน่วยงาน (*เลือกระบุอย่างใดอย่างหนึ่ง) | `"TICKET-EXT-9988"` |

#### Example Request
```json
{
  "ticket_id": "2023-ABCDEF",
  "star": 5
}
```

### Output Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `status` | string | สถานะผลลัพธ์ |
| `message` | string | ข้อความอธิบายผล |
| `exec_time` | number | เวลาที่ใช้ประมวลผล (วินาที) |
| `credit_balance` | number / null | เครดิตคงเหลือของ API key |
| `api_log_session_id` | string | รหัส log การเรียกใช้งาน |
| `api_log_session_id_star` | string | รหัส log จากระบบปลายทาง (มีเมื่อ downstream ส่งค่ากลับมา) |

---

## 4. API `comment` (สนทนา/ให้ความเห็นเพิ่มเติม)

ส่งข้อความความคิดเห็นหลังการประเมิน หรือส่งข้อความ Chat ไปยังผู้แจ้งผ่านทาง SMS

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/comment/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `comment` | string | **REQUIRED** | ข้อความความคิดเห็น/แชท | `"ขอบคุณสำหรับการแจ้งเรื่อง"` |
| `ticket_id` | string | REQUIRED\* | รหัสเรื่องแจ้งของ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | REQUIRED\* | หรือรหัสอ้างอิงของหน่วยงาน (*เลือกระบุอย่างใดอย่างหนึ่ง) | `"TICKET-EXT-9988"` |
| `comment_type` | string | OPTIONAL | ประเภทข้อความ: `chat` / `chat_staff_only` / `comment` (ค่าเริ่มต้น `chat`) | `"chat"` |
| `base64comment` | string | OPTIONAL | ข้อความความคิดเห็นแบบ base64 (ทางเลือกแทน `comment`) | `"4Kew4Kiw4KeI4Ki..."` |
| `noti_reporter` | boolean | OPTIONAL | แจ้งเตือนผู้แจ้งเรื่องหรือไม่ | `true` |
| `noti_staff` | boolean | OPTIONAL | แจ้งเตือนเจ้าหน้าที่หรือไม่ | `true` |

#### Example Request
```json
{
  "ticket_id": "2023-ABCDEF",
  "comment": "เจ้าหน้าที่รับทราบและดำเนินการต่อให้ครับ",
  "comment_type": "chat",
  "noti_reporter": true
}
```

### Output Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `status` | string | สถานะผลลัพธ์ |
| `message` | string | ข้อความอธิบายผล |
| `exec_time` | number | เวลาที่ใช้ประมวลผล (วินาที) |
| `credit_balance` | number / null | เครดิตคงเหลือของ API key |
| `api_log_session_id` | string | รหัส log การเรียกใช้งาน |
| `api_log_session_id_messagecomment` | string | รหัส log จากระบบปลายทาง (มีเมื่อ downstream ส่งค่ากลับมา) |

---

## 5. API `join-forward` (เชิญร่วม & ส่งต่อเรื่องแจ้ง)

เชิญหน่วยงานอื่นร่วมรับผิดชอบ หรือส่งต่อเคสไปยังหน่วยงานปลายทาง

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/join-forward/v1
Authorization: Bearer <token>
Content-Type: application/json
```

### Input Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `ticket_id` | string | REQUIRED\* | รหัสเรื่องแจ้งของ Fondue | `"2023-ABCDEF"` |
| `client_ticket_id` | string | REQUIRED\* | หรือรหัสอ้างอิงของหน่วยงาน | `"TICKET-EXT-9988"` |
| `message_id` | integer | REQUIRED\* | หรือรหัสข้อความอ้างอิง (*เลือกระบุอย่างใดอย่างหนึ่งจากสามตัวนี้) | `30314900` |
| `origin_group` | integer | **REQUIRED** | รหัสหน่วยงานต้นทาง | `151` |
| `destination_group` | array[integer] | OPTIONAL | รหัสหน่วยงานปลายทาง | `[1302]` |
| `scenario` | integer | **REQUIRED** | รูปแบบการดำเนินการ: `1` = เชิญร่วม, `2` = ส่งต่อ | `2` |
| `noti` | boolean | OPTIONAL | 🆕 shorthand ตั้งค่าให้ทั้ง `noti_reporter` และ `noti_staff` พร้อมกัน | `true` |
| `noti_staff` | boolean | OPTIONAL (default `true`) | 🆕 แจ้งเตือนเจ้าหน้าที่หรือไม่ | `true` |
| `noti_reporter` | boolean | OPTIONAL (default `true`) | 🆕 แจ้งเตือนผู้แจ้งเรื่องหรือไม่ | `true` |
| `skip_timeline` | boolean | OPTIONAL (default `false`) | 🆕 ข้ามการบันทึกรายการนี้ลง timeline หรือไม่ | `false` |
| `note` | string | OPTIONAL | บันทึกข้อความประกอบการเชิญร่วม/ส่งต่อ | `"ส่งต่อหน่วยงานที่รับผิดชอบโดยตรง"` |
| `photo` | array[string] | OPTIONAL\*\* | 🆕 รูปภาพประกอบ เป็นลิงก์ URL | `["https://example.com/photo.jpg"]` |
| `photo_base64` | string / array[string] | OPTIONAL\*\* | 🆕 รูปภาพประกอบแบบ base64 | `"iVBORw0KGgo..."` |
| `recursive_counter` | integer | OPTIONAL | 🆕 ตัวนับการส่งต่อซ้ำ (ใช้ภายในระบบเพื่อป้องกันการวนลูป) | `0` |
| `timestamp` | string | OPTIONAL | 🆕 เวลาที่ทำรายการ | `"2026-09-09T10:00:00"` |
| `use_admin` | boolean | OPTIONAL | 🆕 ใช้สิทธิ์ admin ในการดำเนินการ | `true` |

\* เลือกระบุอย่างใดอย่างหนึ่งจาก `ticket_id`/`client_ticket_id`/`message_id`
\*\* เลือกส่งรูปภาพได้ทางใดทางหนึ่งจาก `photo`/`photo_base64`

#### Example Request
```json
{
  "message_id": 30314900,
  "origin_group": 151,
  "destination_group": [1302],
  "scenario": 2,
  "note": "ส่งต่อหน่วยงานที่รับผิดชอบโดยตรง",
  "noti_staff": true,
  "noti_reporter": true
}
```

### Output Parameters

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `status` | string | สถานะผลลัพธ์ |
| `message` | string | ข้อความอธิบายผล |
| `exec_time` | number | เวลาที่ใช้ประมวลผล (วินาที) |
| `credit_balance` | number / null | เครดิตคงเหลือของ API key |
| `api_log_session_id` | string | รหัส log การเรียกใช้งาน |
| `api_log_session_id_join_forward` | string | รหัส log จากระบบปลายทาง (มีเมื่อ downstream ส่งค่ากลับมา) |
| `results` | object | ⚠️ อาจไม่มี key นี้ในผลลัพธ์เลยหาก downstream ไม่ส่งข้อมูลกลับมา (ไม่ใช่แค่ array ว่าง) |
