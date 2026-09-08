# storefront-api

API behind the Acme web storefront: browsing, basket and the Place Order step (`POST /orders`).
Owned by the Storefront team. Monitored in Dynatrace as `SERVICE-acme-storefront`.
Releases: `v<year>.<month>.<day>-<n>`, recorded as GitHub deployments to `production`.

Dependencies: httpx 0.28, structlog 25.1.

## v2026.9.8-1
- payment_capture_mode is now required from configuration (no legacy default).
- Order confirmation shows the estimated delivery window.
- Dependency bumps.
