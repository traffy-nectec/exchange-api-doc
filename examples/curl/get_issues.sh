#!/usr/bin/env bash
TOKEN="YOUR_JWT_TOKEN"
curl --location "https://publicapi.traffy.in.th/exchange-api/get-issues/v1" \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "state": ["รอรับเรื่อง", "กำลังดำเนินการ"],
    "offset": 0,
    "limit": 50
  }'
