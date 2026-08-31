# รหัสข้อผิดพลาดและการแก้ไข (Error Codes & Troubleshooting)

รายการข้อความแจ้งเตือนสถานะและข้อผิดพลาดมาตรฐานที่อาจได้รับจากการเรียกใช้ Traffy Fondue Exchange API

---

## รูปแบบ Error Response
```json
{
  "status": "fail",
  "message": "This token has expired | Token นี้หมดอายุแล้ว",
  "exec_time": "0.012s",
  "credit_balance": 820,
  "results": []
}
```

---

## 📋 รายการ Error Messages ที่พบบ่อย

| Message | สาเหตุ | แนวทางการแก้ไข |
| :--- | :--- | :--- |
| `Invalid user or pass` | Username หรือ Password ไม่ถูกต้อง | ตรวจสอบข้อมูลใน Email ที่ได้รับจากทีมงาน Fondue |
| `This token has expired` | JWT Token หมดอายุ | เรียก API `get-auth` เพื่อขอรับ Token ชุดใหม่ |
| `ERR 1 - Invalid token` | Token ไม่ถูกต้อง หรือไม่ได้แนบ Bearer header | ตรวจสอบรูปแบบ Header: `Authorization: Bearer <token>` |
| `Running out of API usage quota` | โควต้าการใช้งานประจำเดือนหมด | ติดต่อขอเพิ่มโควต้าผ่านทาง LINE: `@fonduehelp` |
| `Almost running out of API usage quota` *(Warning)* | โควต้าคงเหลือใกล้หมด | เตรียมประสานงานขอขยายโควต้า |
| `Invalid input JSON format` | Body ไม่ได้อยู่ในรูปแบบ JSON ที่ถูกต้อง | ตรวจสอบ Syntax ของ JSON Payload |
| `[Parameter] is not specified` | ขาดพารามิเตอร์ที่จำเป็น (Required field) | ตรวจสอบว่าได้ส่งฟิลด์ดังกล่าวมาครบถ้วน |
