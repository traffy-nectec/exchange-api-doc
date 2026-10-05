# การยืนยันตัวตน (Authentication)

การใช้งาน API ของ Traffy Fondue Exchange API เกือบทุกเส้นทาง (ยกเว้น `get-auth` และ Real-time Webhook ขาเข้า) จำเป็นต้องยืนยันตัวตนด้วย **JSON Web Token (JWT)** โดยส่งผ่าน Header:

```http
Authorization: Bearer <your_jwt_token>
```

---

## 🔑 API `get-auth` (ขอ JWT)

ใช้สำหรับนำ `user` และ `pass` ที่ได้รับอนุมัติจากทีมงาน Traffy Fondue มาแลกรับ JWT Token เพื่อนำไปใช้กับ API อื่นๆ

### Endpoint URL
```http
POST https://publicapi.traffy.in.th/exchange-api/get-auth/v1
Content-Type: application/json
```

### คำเตือนด้านความปลอดภัย
> [!CAUTION]
> **ห้ามเปิดเผย `user` และ `pass` สู่สาธารณะเด็ดขาด** (เช่น ห้าม Hardcode ไว้ใน Mobile App หรือ Frontend Website ที่ผู้ใช้สามารถ Inspect ดูได้) การขอ Token จะต้องกระทำผ่านฝั่ง Server-side เท่านั้น

---

### Request Parameters (JSON Body)

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| `user` | string | **REQUIRED** | ชื่อผู้ใช้งานของ Account ที่ได้รับแจ้งทาง Email | `"YOUR_USERNAME"` |
| `pass` | string | **REQUIRED** | รหัสผ่านของ Account ที่ได้รับแจ้งทาง Email | `"YOUR_PASSWORD"` |

#### Example Request Body
```json
{
  "user": "YOUR_USERNAME",
  "pass": "YOUR_PASSWORD"
}
```

---

### Response Parameters (JSON Body)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `status` | string | สถานะการทำงาน (`success`, `fail`, `warning`) | `"success"` |
| `message` | string | ข้อความอธิบายสถานะหรือข้อผิดพลาด | `""` |
| `exec_time` | string | เวลาที่ใช้ในการประมวลผล | `"0.041s"` |
| `credit_balance` | integer \| null | จำนวนครั้งการใช้งาน API ที่เหลืออยู่ในเดือนนี้ (เป็น `null` หาก Account ไม่ได้กำหนดโควต้าไว้ / ใช้งานไม่จำกัด) | `820` |
| `quota_limit` | integer | โควต้าการใช้งานทั้งหมดต่อเดือน | `1000` |
| `permissions` | array[string] | สิทธิ์การเข้าถึงของ Account (`["read", "write"]`) | `["read", "write"]` |
| `results` | object | ข้อมูล Token ที่ได้ | *ดูตารางด้านล่าง* |
| `api_log_session_id` | integer | หมายเลข API log session สำหรับใช้ debug การทำงานของ API ร่วมกับทีม Traffy | `2122913957` |

#### ฟิลด์ใน `results`:
| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `token` | string | JWT Token สำหรับนำไปใส่ใน Header `Authorization: Bearer <token>` | `"eyJhbGciOiJIUzI1Ni..."` |
| `expire_timestamp` | string | วันเวลาที่ Token หมดอายุ (เวลาประเทศไทย UTC+7) | `"2026-10-12 19:06:12"` |

#### Example Response (Success)
```json
{
  "status": "success",
  "message": "",
  "exec_time": "1.056s",
  "credit_balance": 995,
  "quota_limit": 1000,
  "permissions": [
    "read",
    "write"
  ],
  "results": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expire_timestamp": "2026-10-12 19:06:12"
  },
  "api_log_session_id": 922348568
}
```

---

## 🛠 ตัวอย่างการเรียกใช้งาน

### cURL
```bash
curl --location 'https://publicapi.traffy.in.th/exchange-api/get-auth/v1' \
--header 'Content-Type: application/json' \
--data '{
    "user": "YOUR_USERNAME",
    "pass": "YOUR_PASSWORD"
}'
```

### Python
```python
import requests

url = "https://publicapi.traffy.in.th/exchange-api/get-auth/v1"
payload = {
    "user": "YOUR_USERNAME",
    "pass": "YOUR_PASSWORD"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

if data.get("status") == "success" and "results" in data:
    token = data["results"]["token"]
    print(f"Token: {token}")
    print(f"Expires at: {data['results']['expire_timestamp']}")
```

### Node.js
```javascript
const response = await fetch('https://publicapi.traffy.in.th/exchange-api/get-auth/v1', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    user: 'YOUR_USERNAME',
    pass: 'YOUR_PASSWORD'
  })
});

const data = await response.json();
if (data.status === 'success' && data.results) {
  const token = data.results.token;
  console.log('Token:', token);
}
```
