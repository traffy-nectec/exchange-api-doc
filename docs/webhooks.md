# การส่งข้อมูลแบบ Real-time (Webhooks)

Traffy Fondue สามารถส่งข้อมูลแบบ Real-time ไปยัง Server Endpoint ของหน่วยงานได้โดยอัตโนมัติ โดย **ไม่นับรวมในโควต้าการใช้งาน (Non-credit balance)**

> [!NOTE]
> กรุณาประสานงานกับทีมพัฒนา Traffy Fondue ผ่านทาง Line **[@fonduehelp](https://line.me/R/ti/p/%40155yjrwo)** เพื่อลงทะเบียน Endpoint URL สำหรับรับ Webhook

---

## 1. เมื่อมีเรื่องแจ้งเข้ามาใหม่ (New Issue Event)

เมื่อมีเรื่องแจ้งใหม่ส่งเข้ามายังหน่วยงานของท่านในระบบ Fondue ทางระบบจะยิง HTTP `POST` Request ไปยัง URL ที่ท่านลงทะเบียนไว้  
<span style="color: red;">**หมายเหตุ: ห้ามส่งเรื่องแจ้งใหม่ที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API new-issue เพื่อป้องกันการเกิด loop**</span>

### Webhook Payload (`POST`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `event` | string | ประเภทของเหตุการณ์ (`new-issue`) | `"new-issue"` |
| `timestamp` | string | วันเวลาที่แจ้ง (UTC+7) | `"2026-10-10 19:19:37.389642"` |
| `ticket_id` | string | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2026-ABCDEF"` |
| `description` | string | ข้อความรายละเอียดปัญหา | `"ทดสอบแจ้งเข้าหน่วยงาน 2026-10-10"` |
| `type` | string | ประเภทปัญหา (ภาษาไทย) | `"อื่นๆ"` |
| `type_en` | string | ประเภทปัญหา (ภาษาอังกฤษ) | `"Other"` |
| `issue_category_id` | integer | รหัสหมวดหมู่ปัญหา | `12` |
| `org_category_id` | integer / null | รหัสหมวดหมู่หน่วยงาน (null เมื่อไม่มี) | `null` |
| `status` | string | สถานะ (ภาษาไทย) | `"รอรับเรื่อง"` |
| `status_en` | string | สถานะ (ภาษาอังกฤษ) | `"Open"` |
| `is_follow` | boolean | สถานะการติดตามเรื่อง | `false` |
| `is_forward` | boolean | สถานะการส่งต่อเรื่อง | `false` |
| `issue_status_id` | integer | รหัสสถานะของเรื่องแจ้ง | `1` |
| `org_status_id` | integer / null | รหัสสถานะของหน่วยงาน (null เมื่อไม่มี) | `null` |
| `status_type` | string | ประเภทของสถานะ | `"start"` |
| `photo` | string | ลิงก์ภาพประกอบการแจ้ง | `"https://storage.googleapis.com/..."` |
| `latitude` | string | ละติจูดพิกัด GPS (WGS84) | `"14.077771879738362"` |
| `longitude` | string | ลองจิจูดพิกัด GPS (WGS84) | `"100.60131479546563"` |
| `address` | string | ที่อยู่สถานที่เกิดเหตุ | `"112 ถนนพหลโยธิน ตำบลคลองหนึ่ง อำเภอคลองหลวง ปทุมธานี 12120"` |
| `orgs` | array[object] | รายชื่อหน่วยงานที่รับผิดชอบ | `[{"org": "Traffy @ ITS Lab2", "org_id": 151}]` |
| `orgs[].org` | string | ชื่อหน่วยงาน | `"Traffy @ ITS Lab2"` |
| `orgs[].org_id` | integer | รหัสหน่วยงาน | `151` |

#### Example Webhook Payload (POST)
```json
{
  "event": "new-issue",
  "timestamp": "2026-10-10 19:19:37.389642",
  "ticket_id": "2026-ABCDEF",
  "description": "ทดสอบแจ้งเข้าหน่วยงาน 2026-10-10",
  "type": "อื่นๆ",
  "type_en": "Other",
  "issue_category_id": 12,
  "org_category_id": null,
  "status": "รอรับเรื่อง",
  "status_en": "Open",
  "is_follow": false,
  "is_forward": false,
  "issue_status_id": 1,
  "org_status_id": null,
  "status_type": "start",
  "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2026-10/7f3358882698a7d4f1d23d93be009ab2.jpeg",
  "latitude": "14.077771879738362",
  "longitude": "100.60131479546563",
  "address": "112 ถนนพหลโ ยธิน ตำบล คลองหนึ่ง อำเภอคลองหลวง ปทุมธานี 12120",
  "orgs": [
    {
      "org": "Traffy @ ITS Lab2",
      "org_id": 151
    }
  ]
}
```

#### Response Example
```json
{
  "status": "success",
  "message": ""
}
```

---

## 2. เมื่อมีการอัปเดตสถานะ (Status Update Event)

เมื่อเจ้าหน้าที่ในระบบ Fondue มีการปรับเปลี่ยนสถานะเคส ระบบจะยิง HTTP `PATCH` Request ไปยัง URL ปลายทางของท่าน  
<span style="color: red;">**หมายเหตุ: ห้ามส่งการอัปเดตที่ได้รับมาจาก Traffy Fondue webhook วนกลับมาที่ API update-issue เพื่อป้องกันการเกิด loop**</span>

### Webhook Payload (`PATCH`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `event` | string | ประเภทของเหตุการณ์ (`update-issue`) | `"update-issue"` |
| `timestamp` | string | วันเวลาที่อัปเดต (UTC+7) | `"2026-10-10 18:00:05.753977+0700"` |
| `ticket_id` | string | หมายเลขเรื่องแจ้งในระบบ Fondue | `"2026-ABCDEF"` |
| `client_ticket_id` | string / null | หมายเลขเรื่องแจ้งฝั่งผู้เรียก (ถ้ามี) | `null` |
| `status` | string | สถานะที่อัปเดต (ภาษาไทย) | `"กำลังดำเนินการ"` |
| `status_en` | string | สถานะที่อัปเดต (ภาษาอังกฤษ) | `"In Progress"` |
| `status_type` | string | ประเภทของสถานะ | `"inprogress"` |
| `is_follow` | boolean | สถานะการติดตามเรื่อง | `false` |
| `is_forward` | boolean | สถานะการส่งต่อเรื่อง | `false` |
| `issue_status_id` | integer | รหัสสถานะของเรื่องแจ้ง | `2` |
| `org_status_id` | integer / null | รหัสสถานะของหน่วยงาน (null เมื่อไม่มี) | `null` |
| `tl_org_id` | integer | รหัสหน่วยงานผู้ดำเนินการ | `151` |
| `tl_org` | string | ชื่อหน่วยงานผู้ดำเนินการ | `"Traffy @ ITS Lab2"` |
| `tl_status` | string | สถานะที่บันทึกใน timeline (รวมถึง "ติดตามเรื่อง" และ "ส่งต่อ") | `"กำลังดำเนินการ"` |
| `note` | string | หมายเหตุประกอบการอัปเดต | `"ทดสอบปรับสถานะ"` |
| `photo` | array[string] / null | ภาพถ่ายหลังการแก้ไข (null เมื่อไม่มี) | `["https://storage.googleapis.com/..."]` |

#### Example Webhook Payload (PATCH)
```json
{
  "event": "update-issue",
  "timestamp": "2026-10-10 18:00:05.753977+0700",
  "ticket_id": "2026-ABCDEF",
  "client_ticket_id": null,
  "status": "กำลังดำเนินการ",
  "status_en": "In Progress",
  "status_type": "inprogress",
  "is_follow": false,
  "is_forward": false,
  "issue_status_id": 2,
  "org_status_id": null,
  "tl_org_id": 151,
  "tl_org": "Traffy @ ITS Lab2",
  "tl_status": "กำลังดำเนินการ",
  "note": "ทดสอบปรับสถานะ",
  "photo": [
    "https://storage.googleapis.com/traffy_public_bucket/attachment/2026-10/5b2aeca91541bff9d5515e6bb194f40a.jpg"
  ]
}
```

#### Response Example
```json
{
  "status": "success",
  "message": ""
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
| `sender_org_id` | integer / null | รหัสหน่วยงานผู้ส่ง (null ถ้าเป็นผู้แจ้ง) | `151` |
| `sender_org` | string / null | ชื่อหน่วยงานผู้ส่ง (null ถ้าเป็นผู้แจ้ง) | `"Traffy @ ITS Lab2"` |
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

#### Response Example
```json
{
  "status": "success",
  "message": ""
}
```
