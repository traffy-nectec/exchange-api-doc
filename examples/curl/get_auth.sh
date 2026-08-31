#!/usr/bin/env bash
curl --location "https://publicapi.traffy.in.th/exchange-api/get-auth/v1" \
  --header "Content-Type: application/json" \
  --data '{
    "user": "YOUR_USERNAME",
    "pass": "YOUR_PASSWORD"
  }'
