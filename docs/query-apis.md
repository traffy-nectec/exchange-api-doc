# การขอข้อมูลจาก Traffy Fondue (Query APIs)

กลุ่ม API สำหรับดึงข้อมูลเรื่องแจ้ง โครงสร้างหน่วยงาน ประเภทปัญหา และสถานะต่างๆ จากระบบ Traffy Fondue มาประมวลผลหรือแสดงผลบนระบบของหน่วยงาน

ทั้ง 7 API ในกลุ่มนี้เป็น **GET** ทั้งหมด รับพารามิเตอร์ผ่าน **Query String** (ไม่ใช่ JSON Body) และต้องแนบ `Authorization: Bearer <token>` ที่ได้จาก `get-auth` เสมอ

---

## 1. API `get-issues` (ขอรายการเรื่องแจ้ง)

ใช้สำหรับดึงรายการเรื่องแจ้งที่หน่วยงานได้รับ กรองตามหน่วยงาน (`org_id`) และช่วงเวลา (`duration`) เท่านั้น — **ไม่รองรับ** การกรองตามวันที่แบบกำหนดเอง สถานะ ประเภทปัญหา คำค้นหา หรือการแบ่งหน้า (Pagination)

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/get-issues/v1?org_id={org_id}&duration={duration}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล คั่นด้วยคอมมาได้หลายรหัส | `151` หรือ `151,1302` (Default: หน่วยงานของ account) |
| `duration` | string | OPTIONAL | ช่วงเวลาของข้อมูล — `today` หรือ `all` | `"today"` (Default) |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/get-issues/v1?org_id=151&duration=today
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล (cache หรือ live) |
| `credit_balance` | integer / null | โควต้าคงเหลือ (null = unlimited) |
| `org_id` | array | รายการรหัสหน่วยงานที่ใช้ค้นหา |
| `count` | integer | จำนวนรายการที่พบ |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |
| `results` | array[object] | รายการเรื่องแจ้ง (ดูฟิลด์ด้านล่าง) |

#### ฟิลด์ใน `results`:
* `ticket_id`: หมายเลขเรื่องแจ้งในระบบ Fondue (เช่น `"2023-ABCDEF"`)
* `type`: ชื่อประเภทปัญหา
* `organization`: ชื่อหน่วยงาน
* `description`: รายละเอียดของปัญหา
* `photo`: ลิงก์รูปภาพเริ่มต้น
* `latitude` / `longitude`: พิกัด GPS
* `address`: ที่อยู่สถานที่เกิดเหตุ
* `subdistrict` / `district` / `province`: ตำบล / อำเภอ / จังหวัด
* `timestamp`: วันเวลาที่แจ้ง (UTC+7)
* `photo_after`: รูปภาพหลังดำเนินการ
* `timestamp_inprogress`: วันเวลาที่เริ่มดำเนินการ
* `timestamp_finished`: วันเวลาที่เสร็จสิ้น
* `org_finished`: หน่วยงานที่ดำเนินการเสร็จสิ้น
* `status`: สถานะปัจจุบัน
* `confirmed`: ยืนยันปิดเรื่องแล้วหรือไม่
* `star`: คะแนนดาวที่ได้รับ
* `count_reopen`: จำนวนครั้งที่ถูกเปิดใหม่
* `last_activity`: วันเวลากิจกรรมล่าสุด

#### Example Response (ผลจริงจากการทดสอบ org_id=151&duration=all — count จริง 4367 รายการ, exec_time สูงเพราะ duration=all ดึงข้อมูลทั้งหมด ปกติแนะนำใช้ duration=today จะเร็วกว่ามาก)
```json
{
    "status": "success",
    "message": "",
    "exec_time": "14.128s",
    "source": "h db, db",
    "credit_balance": null,
    "org_id": [151],
    "count": 4367,
    "results": [
        {
            "ticket_id": "2026-B9WGC7",
            "type": "ทางเท้า",
            "organization": "Traffy @ ITS Lab2, Accom Park",
            "description": "(***) ทดสอบแจ้ง",
            "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2026-08/6eb2ed20729af8d57572c6ee3515ab72.jpeg",
            "latitude": 14.060383,
            "longitude": 100.596114,
            "address": "ตำบลคลองหนึ่ง อำเภอคลองหลวง จังหวัดปทุมธานี",
            "subdistrict": "คลองหนึ่ง",
            "district": "คลองหลวง",
            "province": "ปทุมธานี",
            "timestamp": "2026-08-20 22:25:37.433959",
            "photo_after": "https://storage.googleapis.com/traffy_public_bucket/",
            "timestamp_inprogress": null,
            "timestamp_finished": null,
            "org_finished": "Accom Park",
            "status": "ส่งต่อ(ใหม่)",
            "confirmed": false,
            "star": 0,
            "count_reopen": 0,
            "last_activity": "2026-09-09 14:38:19.663501"
        },
        { "...": "ตัดรายการที่เหลืออีก 4366 รายการ" }
    ],
    "api_log_session_id": 2030246239
}
```

---

## 2. API `get-issue` (ขอรายละเอียดเชิงลึกของเรื่องแจ้ง)

ใช้สำหรับดึงข้อมูลรายละเอียดอย่างสมบูรณ์ของเรื่องแจ้งราย `ticket_id` รวมถึงประวัติการดำเนินการ (Timeline) และรายละเอียดของทุกหน่วยงานที่เกี่ยวข้อง

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/get-issue/v1?ticket_id={ticket_id}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `ticket_id` | string | **REQUIRED** | หมายเลขเรื่องแจ้งในระบบ Fondue (**ไม่รองรับ** `client_ticket_id`) | `"2023-ABCDEF"` |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/get-issue/v1?ticket_id=2023-ABCDEF
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล (cache หรือ live) |
| `credit_balance` | integer / null | โควต้าคงเหลือ (null = unlimited) |
| `ticket_id` | string | หมายเลขเรื่องแจ้งที่ค้นหา |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |
| `results` | object | รายละเอียดเรื่องแจ้ง (ดูฟิลด์ด้านล่าง) |

#### ฟิลด์ใน `results`:
* `ticket_id`, `type`, `organization`, `description`, `photo`, `latitude`, `longitude`, `address`, `subdistrict`, `district`, `province`, `timestamp` — เช่นเดียวกับ `get-issues`
* `status_type`: ประเภทของสถานะ
* `confirmed`: ยืนยันปิดเรื่องแล้วหรือไม่
* `star`: คะแนนดาวที่ได้รับ
* `count_reopen`: จำนวนครั้งที่ถูกเปิดใหม่
* `last_activity`: วันเวลากิจกรรมล่าสุด
* `orgs[]`: รายการหน่วยงานที่เกี่ยวข้องกับเรื่องแจ้งนี้ แต่ละรายการมี:
  * `timestamp`: วันเวลาที่ส่งต่อ/รับเรื่อง
  * `org_id` / `org`: รหัสและชื่อหน่วยงาน
  * `type_id` / `type` / `type_en`: รหัสและชื่อประเภทปัญหา (ไทย/อังกฤษ)
  * `status_id` / `status` / `status_type`: รหัส ชื่อ และประเภทของสถานะ
  * `org_category_id`: รหัสหมวดหมู่แบบ custom ของหน่วยงาน (null = ใช้หมวดหมู่กลาง)
  * `org_status_id`: รหัสสถานะแบบ custom ของหน่วยงาน (null = ใช้สถานะกลาง)
* `timeline[]`: ประวัติการดำเนินการ แต่ละรายการมี `timestamp`, `status_id`, `status`, `org_id`, `org`, `note`, `photo`

#### Example Response (ผลจริงจากการทดสอบ ticket_id=2026-GYDHMT, org 151)
```json
{
    "status": "success",
    "message": "",
    "exec_time": "1.193s",
    "source": "h cache 2026-09-09 16:42:17 (expire 600s), db",
    "credit_balance": null,
    "ticket_id": "2026-GYDHMT",
    "results": {
        "ticket_id": "2026-GYDHMT",
        "type": "อื่นๆ",
        "organization": "Traffy @ ITS Lab2, ทดสอบ toy (2)",
        "description": "ทดสอบแจ้ง ด้วย ssl ใหม่",
        "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2026-08/2d85cd26729c8bff06e30718d2629e5f.jpeg",
        "latitude": 14.077774,
        "longitude": 100.60131,
        "address": "ตำบลคลองหนึ่ง อำเภอคลองหลวง จังหวัดปทุมธานี",
        "subdistrict": "คลองหนึ่ง",
        "district": "คลองหลวง",
        "province": "ปทุมธานี",
        "timestamp": "2026-08-27 22:15:33.416627",
        "status_type": "inprogress",
        "confirmed": false,
        "star": null,
        "count_reopen": 0,
        "last_activity": "2026-09-01 16:14:49.465362",
        "orgs": [
            {
                "timestamp": "2026-08-27 22:15:33.416627",
                "org_id": 151,
                "org": "Traffy @ ITS Lab2",
                "type_id": 620543,
                "type": "อื่นๆ",
                "type_en": "Other",
                "status_id": 105125,
                "status": "กำลังดำเนินการ",
                "status_type": "inprogress",
                "org_category_id": null,
                "org_status_id": 1219411
            },
            {
                "timestamp": "2026-08-27 22:15:33.416627",
                "org_id": 26683,
                "org": "ทดสอบ toy (2)",
                "type_id": 620543,
                "type": "อื่นๆ",
                "type_en": "Other",
                "status_id": 105125,
                "status": "กำลังดำเนินการ",
                "status_type": "inprogress",
                "org_category_id": null,
                "org_status_id": null
            }
        ],
        "timeline": [
            {
                "timestamp": "2026-08-27 22:15:33.416627",
                "status_id": null,
                "status": "รอรับเรื่อง",
                "org_id": null,
                "org": null,
                "note": "ทดสอบแจ้ง ด้วย ssl ใหม่",
                "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2026-08/2d85cd26729c8bff06e30718d2629e5f.jpeg"
            },
            {
                "timestamp": "2026-08-27 22:18:06.282372",
                "status_id": 106369,
                "status": "จัดทำนโยบาย",
                "org_id": 151,
                "org": "Traffy @ ITS Lab2",
                "note": "ทดสอบ",
                "photo": null
            },
            { "...": "ตัดรายการที่เหลือ" }
        ]
    },
    "api_log_session_id": 2077283457
}
```
*(หมายเหตุ: `org_status_id: 1219411` คือสถานะ custom "จัดทำนโยบาย" ที่ org 151 ตั้งไว้เอง — org 26683 ยังไม่ได้ตั้ง custom status เลยได้ `null`)*

---

## 3. API `download-issues` (ดาวน์โหลดไฟล์ CSV)

ใช้สำหรับ Export ข้อมูลเรื่องแจ้งเป็นไฟล์ CSV กรองตามหน่วยงาน (`org_id`) และช่วงเวลา (`duration`) เหมือนกับ `get-issues`

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/download-issues/v1?org_id={org_id}&duration={duration}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล คั่นด้วยคอมมาได้หลายรหัส | `151` (Default: หน่วยงานของ account) |
| `duration` | string | OPTIONAL | ช่วงเวลาของข้อมูล — `today` หรือ `all` | `"today"` (Default) |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/download-issues/v1?org_id=151&duration=all
Authorization: Bearer <token>
```

---

### Output Parameters

กรณีสำเร็จ: คืนค่าเป็นไฟล์ **CSV** โดยตรง มีคอลัมน์ตรงกับฟิลด์ใน `results` ของ `get-issues` (ไม่รวม `org_id`)

#### Example Response (ผลจริงจากการทดสอบ org_id=151&duration=today — header + 1 แถวแรกจากไฟล์ CSV จริง)
```csv
ticket_id,type,organization,description,photo,latitude,longitude,address,subdistrict,district,province,timestamp,photo_after,timestamp_inprogress,timestamp_finished,org_finished,status,confirmed,star,count_reopen,last_activity
2026-B9WGC7,ทางเท้า,"Traffy @ ITS Lab2, Accom Park","(***) ทดสอบแจ้ง",https://storage.googleapis.com/traffy_public_bucket/attachment/2026-08/6eb2ed20729af8d57572c6ee3515ab72.jpeg,14.060383,100.596114,"ตำบลคลองหนึ่ง อำเภอคลองหลวง จังหวัดปทุมธานี",คลองหนึ่ง,คลองหลวง,ปทุมธานี,"2026-08-20 22:25:37.433959",https://storage.googleapis.com/traffy_public_bucket/,,,"Accom Park",ส่งต่อ(ใหม่),,0,0,"2026-09-09 14:38:19.663501"
```
*(หมายเหตุ: ไฟล์จริงมีขึ้นต้นด้วย UTF-8 BOM (`\xEF\xBB\xBF`) ก่อนบรรทัด header — ปกติของ CSV export ที่เปิดกับ Excel ได้ถูกต้อง)*

กรณีผิดพลาด: คืนค่าเป็น JSON ตามรูปแบบ error wrapper

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `fail` หรือ `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล |
| `credit_balance` | integer / null | โควต้าคงเหลือ |
| `org_id` | array | รายการรหัสหน่วยงานที่ใช้ค้นหา |
| `count` | integer | จำนวนรายการ |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |
| `results` | array | ว่างเปล่าในกรณี error |

---

## 4. API `search-org` (ค้นหาหน่วยงาน)

ค้นหารหัสหน่วยงาน (`org_id`) และชื่อหน่วยงานจากคำค้นหา เพื่อนำไปใช้กับ API อื่นๆ

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/search-org/v1?text={text}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `text` | string | **REQUIRED** | คำค้นหาชื่อหน่วยงาน ต้องมีความยาวอย่างน้อย 3 byte | `"บางเขน"` |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/search-org/v1?text=บางเขน
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล |
| `credit_balance` | integer / null | โควต้าคงเหลือ |
| `text` | string | คำค้นหาที่ใช้ |
| `count` | integer | จำนวนหน่วยงานที่พบ |
| `results` | array[object] | รายการหน่วยงาน (ดูฟิลด์ด้านล่าง) |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |
| `api_log_session_id_show_joinforward_from_hierarchy` | string | รหัส session ของ downstream (มีเฉพาะเมื่อ downstream ส่งมา) |

#### ฟิลด์ใน `results`:
* `org_id`: รหัสหน่วยงาน
* `name`: ชื่อหน่วยงาน
* `photo`: รูปโลโก้/รูปหน่วยงาน
* `latitude` / `longitude`: พิกัด GPS
* `address`: ที่อยู่หน่วยงาน
* `province`: จังหวัด
* `is_official`: หน่วยงานที่ได้รับการยืนยันอย่างเป็นทางการหรือไม่

---

## 5. API `get-org-list` (ขอโครงสร้างหน่วยงานในสังกัด)

ดึงรายชื่อหน่วยงานที่อยู่ภายใต้การกำกับดูแลของ Account นี้

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/get-org-list/v1?org_id={org_id}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล คั่นด้วยคอมมาได้หลายรหัส | `151,1302` (Default: หน่วยงานของ account) |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/get-org-list/v1?org_id=151
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล |
| `credit_balance` | integer / null | โควต้าคงเหลือ |
| `org_id` | string | หมายเลขหน่วยงาน (ถ้าระบุหลายรหัสมา จะได้แค่รหัสแรกกลับมา — **ไม่ใช่ array**) |
| `count` | integer | จำนวนหน่วยงานที่พบ |
| `results` | array[object] | รายการหน่วยงาน (ดูฟิลด์ด้านล่าง) |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |

#### ฟิลด์ใน `results`:
* `org_id`: รหัสหน่วยงาน
* `name` / `name_en`: ชื่อหน่วยงาน (ไทย/อังกฤษ)
* `photo`: รูปโลโก้/รูปหน่วยงาน
* `latitude` / `longitude`: พิกัด GPS
* `address`: ที่อยู่หน่วยงาน
* `province`: จังหวัด
* `is_official`: หน่วยงานที่ได้รับการยืนยันอย่างเป็นทางการหรือไม่

#### Example Response (ผลจริงจากการทดสอบ org_id=151)
```json
{
    "status": "success",
    "message": "",
    "exec_time": "0.943s",
    "source": "db",
    "credit_balance": null,
    "org_id": "151",
    "count": 1,
    "results": [
        {
            "org_id": 151,
            "name": "Traffy @ ITS Lab2",
            "name_en": "Traffy @ ITS Lab2",
            "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2022-01/998ce45a17d6fd64b0e35f7fb65c778a63397777.jpg",
            "latitude": 14.077786,
            "longitude": 100.601313,
            "address": "112 อุทยานวิทยาศาสตร์ ถนนพหลโยธิน ตำบล คลองหนึ่ง อำเภอคลองหลวง ปทุมธานี 12120 ประเทศไทย ตำบล คลองหนึ่ง ประเทศไทย",
            "province": "ปทุมธานี",
            "is_official": true
        }
    ],
    "api_log_session_id": 1800786405
}
```

---

## 6. API `get-type-list` (ขอรายการประเภทปัญหา)

ดึง Master Data รายการประเภทปัญหาที่หน่วยงานรับผิดชอบ พร้อมรายการหมวดหมู่กลางและหมวดหมู่แบบ custom ของหน่วยงาน (`org_category`)

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/get-type-list/v1?org_id={org_id}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล คั่นด้วยคอมมาได้หลายรหัส | `151,1302` (Default: หน่วยงานของ account) |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/get-type-list/v1?org_id=151
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล |
| `credit_balance` | integer / null | โควต้าคงเหลือ |
| `org_id` | array | รายการรหัสหน่วยงานที่ใช้ค้นหา |
| `count` | integer | จำนวนรายการประเภทปัญหาที่พบ |
| `results` | array[object] | รายการประเภทปัญหา (ดูฟิลด์ด้านล่าง) |
| `org_category` | array[object] | รายการหมวดหมู่กลาง + หมวดหมู่ custom ของหน่วยงาน (ดูฟิลด์ด้านล่าง) |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |

#### ฟิลด์ใน `results`:
* `org_id`: รหัสหน่วยงาน
* `topic_id` / `type_id`: รหัสหมวดหมู่ / ประเภทปัญหา
* `type` / `type_en`: ชื่อประเภทปัญหา (ไทย/อังกฤษ)
* `photo`: รูปไอคอนประเภทปัญหา
* `index`: ลำดับการแสดงผล

#### ฟิลด์ใน `org_category` (ใหม่):
* `org_id`: รหัสหน่วยงาน (`null` = หมวดหมู่กลาง)
* `issue_category_id`: รหัสหมวดหมู่กลาง
* `org_category_id`: รหัสหมวดหมู่ custom ของหน่วยงาน (`null` = ใช้หมวดหมู่กลาง)
* `name_th` / `name_en`: ชื่อหมวดหมู่ (ไทย/อังกฤษ)
* `sort_order`: ลำดับการแสดงผล
* `icon_url`: ลิงก์ไอคอน
* `category_group`: กลุ่มของหมวดหมู่

#### Example Response (ผลจริงจากการทดสอบ org_id=151, ตัดให้เหลือ 2 รายการต่อ array จาก count จริง 34 / org_category 37 รายการ)
```json
{
    "status": "success",
    "message": "",
    "exec_time": "1.179s",
    "source": "h cache 2026-09-09 16:42:17 (expire 600s), db",
    "credit_balance": null,
    "org_id": [151],
    "count": 34,
    "results": [
        {
            "org_id": 151,
            "topic_id": 78,
            "type_id": 196886,
            "type": "น้ำท่วม",
            "type_en": "Flood",
            "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2021-09/s-1630552986.779968.png",
            "index": 4
        },
        {
            "org_id": 151,
            "topic_id": 5,
            "type_id": 24181,
            "type": "ความสะอาด",
            "type_en": "Cleanliness",
            "photo": "https://storage.googleapis.com/traffy_public_bucket/attachment/2018-03/s-1520325639.52.png",
            "index": 6
        },
        { "...": "ตัดรายการที่เหลือ" }
    ],
    "org_category": [
        {
            "org_id": 151,
            "issue_category_id": 6,
            "org_category_id": 166551,
            "name_th": "ฟิวเพิ่มประเภท",
            "name_en": "Fewjatest",
            "sort_order": 10,
            "icon_url": "attachment/2018-03/s-1520325589.18.png",
            "category_group": null
        },
        {
            "org_id": 151,
            "issue_category_id": 12,
            "org_category_id": 133481,
            "name_th": "ความปลอดภัย",
            "name_en": "Safety",
            "sort_order": 999,
            "icon_url": "attachment/2018-04/s-1524623011.7.png",
            "category_group": null
        },
        { "...": "ตัดรายการที่เหลือ" }
    ],
    "api_log_session_id": 424355237
}
```
*(หมายเหตุ: `"ฟิวเพิ่มประเภท"/"Fewjatest"` เป็นชื่อหมวดหมู่ custom จริงที่หน่วยงาน org 151 ตั้งไว้เองตอนทดสอบระบบ — เป็นผลจริงจาก production ไม่ใช่ตัวอย่างที่แต่งขึ้น)*

---

## 7. API `get-status-list` (ขอรายการสถานะ)

ดึงรายการสถานะกลางที่สามารถใช้งานได้ในการปรับปรุงเรื่องแจ้ง พร้อมรายการสถานะแบบ custom ของหน่วยงาน (`org_status`)

### Endpoint URL
```http
GET https://publicapi.traffy.in.th/exchange-api/get-status-list/v1?org_id={org_id}
Authorization: Bearer <token>
```

### Input Parameters (Query String)

| Parameter | Type | Required | Description | Example / Default |
| :--- | :--- | :---: | :--- | :--- |
| `org_id` | string | OPTIONAL | รหัสหน่วยงานที่ต้องการดึงข้อมูล | `151` (Default: หน่วยงานของ account) |

#### Example Request
```http
GET https://publicapi.traffy.in.th/exchange-api/get-status-list/v1?org_id=151
Authorization: Bearer <token>
```

---

### Output Parameters (JSON Response)

| Field | Type | Description |
| :--- | :--- | :--- |
| `status` | string | `success`, `fail`, `warning` |
| `message` | string | รายละเอียดข้อผิดพลาด |
| `exec_time` | string | เวลาประมวลผล |
| `source` | string | แหล่งข้อมูล |
| `credit_balance` | integer / null | โควต้าคงเหลือ |
| `org_id` | array | รายการรหัสหน่วยงานที่ใช้ค้นหา |
| `count` | integer | จำนวนสถานะที่พบ |
| `results` | array[object] | รายการสถานะกลาง (ดูฟิลด์ด้านล่าง) |
| `org_status` | array[object] | รายการสถานะกลาง + สถานะ custom ของหน่วยงาน (ดูฟิลด์ด้านล่าง) |
| `api_log_session_id` | string | รหัส session สำหรับอ้างอิง log |

#### ฟิลด์ใน `results`:
* `org_id`: รหัสหน่วยงาน
* `status_id`: รหัสสถานะ
* `status`: ชื่อสถานะ
* `status_type`: ประเภทของสถานะ
* `index`: ลำดับการแสดงผล

#### ฟิลด์ใน `org_status` (ใหม่):
* `org_id`: รหัสหน่วยงาน (`null` = สถานะกลาง)
* `issue_status_id`: รหัสสถานะกลาง
* `org_statuses_id`: รหัสสถานะ custom ของหน่วยงาน (`null` = ใช้สถานะกลาง)
* `group_name_th` / `group_name_en`: ชื่อกลุ่มสถานะ (ไทย/อังกฤษ)
* `sort_order`: ลำดับการแสดงผล
* `bg_color` / `text_color` / `border_color`: สีพื้นหลัง/ตัวอักษร/ขอบ สำหรับแสดงผล
* `is_active`: เปิดใช้งานอยู่หรือไม่ (string `"t"`/`"f"`)

#### Example Response (ผลจริงจากการทดสอบ org_id=151, ตัดให้เหลือ 2 รายการต่อ array จาก count จริง 20 / org_status 17 รายการ)
```json
{
    "status": "success",
    "message": "",
    "exec_time": "1.121s",
    "source": "h cache 2026-09-09 16:42:17 (expire 600s), db",
    "credit_balance": null,
    "org_id": [151],
    "count": 20,
    "results": [
        {
            "org_id": 151,
            "status_id": 81,
            "status": "รอรับเรื่อง",
            "status_type": "start",
            "index": 1
        },
        {
            "org_id": 151,
            "status_id": 192003,
            "status": "รับเรื่อง",
            "status_type": "inprogress",
            "index": 2
        },
        { "...": "ตัดรายการที่เหลือ" }
    ],
    "org_status": [
        {
            "org_id": null,
            "issue_status_id": 1,
            "org_statuses_id": null,
            "group_name_th": "รอรับเรื่อง",
            "group_name_en": "Open",
            "sort_order": 1,
            "bg_color": "#f98a89",
            "text_color": "#000",
            "border_color": "#ef5d4a",
            "is_active": "t"
        },
        {
            "org_id": null,
            "issue_status_id": 2,
            "org_statuses_id": null,
            "group_name_th": "กำลังดำเนินการ",
            "group_name_en": "In Progress",
            "sort_order": 2,
            "bg_color": "#ffeca0",
            "text_color": "#92400E",
            "border_color": "#f4bf00",
            "is_active": "t"
        },
        { "...": "ตัดรายการที่เหลือ" }
    ],
    "api_log_session_id": 1841962945
}
```
