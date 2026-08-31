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
| `user` | string | **REQUIRED** | ชื่อผู้ใช้งานของ Account ที่ได้รับแจ้งทาง Email | `"traffy"` |
| `pass` | string | **REQUIRED** | รหัสผ่านของ Account ที่ได้รับแจ้งทาง Email | `"1234"` |

#### Example Request Body
```json
{
  "user": "traffy",
  "pass": "1234"
}
```

---

### Response Parameters (JSON Body)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `status` | string | สถานะการทำงาน (`success`, `fail`, `warning`) | `"success"` |
| `message` | string | ข้อความอธิบายสถานะหรือข้อผิดพลาด | `""` |
| `exec_time` | string | เวลาที่ใช้ในการประมวลผล | `"0.041s"` |
| `credit_balance` | integer | จำนวนครั้งการใช้งาน API ที่เหลืออยู่ในเดือนนี้ (-1 = Unlimited) | `820` |
| `quota_limit` | integer | โควต้าการใช้งานทั้งหมดต่อเดือน | `1000` |
| `permissions` | array[string] | สิทธิ์การเข้าถึงของ Account (`["read", "write"]`) | `["read", "write"]` |
| `results` | array[object] | ข้อมูล Token ที่ได้ | *ดูตารางด้านล่าง* |

#### ฟิลด์ใน `results`:
| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `token` | string | JWT Token สำหรับนำไปใส่ใน Header `Authorization: Bearer <token>` | `"eyJhbGciOiJIUzI1Ni..."` |
| `expire_timestamp` | string | วันเวลาที่ Token หมดอายุ (เวลาประเทศไทย UTC+7) | `"2026-08-31 23:59:59"` |

#### Example Response (Success)
```json
{
  "status": "success",
  "message": "",
  "exec_time": "0.041s",
  "credit_balance": 820,
  "quota_limit": 1000,
  "permissions": [
    "read",
    "write"
  ],
  "results": [
    {
      "token": "abcdefghijklmnopqrstuvwxyz1234567890",
      "expire_timestamp": "2026-08-31 23:59:59"
    }
  ]
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

if data.get("status") == "success":
    token = data["results"][0]["token"]
    print(f"Token: {token}")
    print(f"Expires at: {data['results'][0]['expire_timestamp']}")
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
console.log(data);
```
