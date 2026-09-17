# การส่งข้อมูลแบบ Real-time (Webhooks)

Traffy Fondue สามารถส่งข้อมูลแจ้งเตือนแบบ Real-time ไปยัง Server Endpoint ของหน่วยงานได้โดยอัตโนมัติ โดย **ไม่นับรวมในโควต้าการใช้งาน (Non-credit balance)**

> [!NOTE]
> กรุณาประสานงานกับทีมพัฒนา Traffy Fondue ผ่านทาง Line **[@fonduehelp](https://line.me/R/ti/p/%40155yjrwo)** เพื่อลงทะเบียน Endpoint URL สำหรับรับ Webhook

---

## 1. เมื่อมีเรื่องแจ้งเข้ามาใหม่ (New Issue Event)

เมื่อมีเรื่องแจ้งใหม่ส่งเข้ามายังหน่วยงานของท่านในระบบ Fondue ทางระบบจะยิง HTTP `POST` Request ไปยัง URL ที่ท่านลงทะเบียนไว้  
<span style="color: red;">**หมายเหตุ: ห้ามส่งเรื่องแจ้งใหม่ที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API new-issue เพื่อป้องกันการเกิด loop**</span>

### Webhook Payload (`POST`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | string | วันเวลาที่แจ้ง (UTC+7) | `"2026-08-31 10:00:00.000000"` |
| `ticket_id` | string | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2026-ABCDEF"` |
| `description` | string | ข้อความรายละเอียดปัญหา | `"พบฝาท่อระบายน้ำชำรุด"` |
| `type_id` | integer | รหัสประเภทปัญหา | `12` |
| `type` | string | ชื่อประเภทปัญหา | `"ถนน"` |
| `photo` | array[string] | ลิงก์ URL รูปภาพประกอบการแจ้ง | `["https://storage.googleapis.com/..."]` |
| `latitude` | number | ละติจูดพิกัด GPS | `13.754158` |
| `longitude` | number | ลองจิจูดพิกัด GPS | `100.5014985` |
| `address` | string | ที่อยู่สถานที่เกิดเหตุ | `"112 ถ.พหลโยธิน ต.คลองหนึ่ง อ.คลองหลวง จ.ปทุมธานี"` |
| `orgs` | array[object] | รายชื่อหน่วยงานที่รับผิดชอบ | `[{"org_id": 151, "org": "Traffy @ ITS Lab2"}]` |

#### Example Webhook Payload (POST)
```json
{
  "timestamp": "2026-08-31 10:00:00.000000",
  "ticket_id": "2026-ABCDEF",
  "description": "พบฝาท่อระบายน้ำชำรุด",
  "type_id": 12,
  "type": "ถนน",
  "photo": [
    "https://storage.googleapis.com/traffy-fondue/line_img/example.jpeg"
  ],
  "latitude": 13.754158,
  "longitude": 100.5014985,
  "address": "112 ถ.พหลโยธิน ต.คลองหนึ่ง อ.คลองหลวง จ.ปทุมธานี",
  "orgs": [
    {
      "org_id": 151,
      "org": "Traffy @ ITS Lab2"
    }
  ]
}
```

---

## 2. เมื่อมีการอัปเดตสถานะ (Status Update Event)

เมื่อเจ้าหน้าที่ในระบบ Fondue มีการปรับเปลี่ยนสถานะเคส ระบบจะยิง HTTP `PATCH` Request ไปยัง URL ปลายทางของท่าน  
<span style="color: red;">**หมายเหตุ: ห้ามส่งการอัปเดตที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API update-issue เพื่อป้องกันการเกิด loop**</span>

### Webhook Payload (`PATCH`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `timestamp` | string | วันเวลาที่มีการอัปเดต (UTC+7) | `"2026-08-31 11:30:00.000000"` |
| `ticket_id` | string | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2026-ABCDEF"` |
| `org` | string | ชื่อหน่วยงานที่ดำเนินการ | `"Traffy @ ITS Lab2"` |
| `status` | string | สถานะที่มีการอัปเดต | `"เสร็จสิ้น"` |
| `note` | string | ข้อความบันทึกการปฏิบัติงาน | `"ได้ทำการแก้ไขเรียบร้อยแล้วครับ"` |
| `photo` | array[string] | ภาพถ่ายหลังการแก้ไข | `["https://storage.googleapis.com/..."]` |

#### Example Webhook Payload (PATCH)
```json
{
  "timestamp": "2026-08-31 11:30:00.000000",
  "ticket_id": "2026-ABCDEF",
  "org": "Traffy @ ITS Lab2",
  "status": "เสร็จสิ้น",
  "note": "ได้ทำการแก้ไขเรียบร้อยแล้วครับ",
  "photo": [
    "https://storage.googleapis.com/traffy-fondue/line_img/fixed_example.jpeg"
  ]
}
```

---

## 3. เมื่อมีการแสดงความคิดเห็นหรือแชท (Chat/Comment Event)

เมื่อมีการพิมพ์แชทโต้ตอบ หรือมีการให้คะแนนความพึงพอใจในเรื่องแจ้ง ระบบจะยิง HTTP `POST` Request ไปยัง URL ปลายทางของท่าน
<span style="color: red;">**หมายเหตุ: ห้ามส่งการแสดงความคิดเห็นที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API messagecomment เพื่อป้องกันการเกิด loop**</span>

### Webhook Payload (`POST`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `event` | string | ประเภทของเหตุการณ์ (`chat`, `rating`, `comment`, `chat_staff_only`) | `"chat"` |
| `message_comment_id` | integer | รหัสความคิดเห็นในระบบ | `2115334` |
| `message_id` | integer | รหัสข้อความในระบบ | `2040189` |
| `ticket_id` | string | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2026-MRFY4M"` |
| `comment` | string | ข้อความแสดงความคิดเห็น | `"test"` |
| `timestamp` | string | วันเวลาที่มีการแสดงความคิดเห็น (UTC+7) | `"2026-09-17 15:13:57.662001"` |
| `sender_org_id` | integer | รหัสหน่วยงานผู้ส่ง (null ถ้าเป็นผู้แจ้ง) | `151` |
| `sender_org` | string | ชื่อหน่วยงานผู้ส่ง (null ถ้าเป็นผู้แจ้ง) | `"Traffy @ ITS Lab2"` |
| `sender_user_id` | integer | รหัสผู้ใช้งานผู้ส่ง | `4006` |
| `sender_username` | string | ชื่อผู้ใช้งานผู้ส่ง | `"SuperToy Noppadol"` |

#### Example Webhook Payload (POST)
```json
{
  "event": "chat",
  "message_comment_id": 2115334,
  "message_id": 2040189,
  "ticket_id": "2026-MRFY4M",
  "comment": "test",
  "timestamp": "2026-09-17 15:13:57.662001",
  "sender_org_id": 151,
  "sender_org": "Traffy @ ITS Lab2",
  "sender_user_id": 4006,
  "sender_username": "SuperToy Noppadol"
}
```
