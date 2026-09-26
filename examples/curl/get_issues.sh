#!/usr/bin/env bash
TOKEN="YOUR_JWT_TOKEN"
curl --location --request GET \
  "https://publicapi.traffy.in.th/exchange-api/get-issues/v2?org_id=151&duration=today" \
  --header "Authorization: Bearer $TOKEN"
