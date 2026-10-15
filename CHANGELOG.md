# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]
- Planned: CI workflow, production Shopify/Stripe integrations, container image (GHCR), auth/multi-tenant.

## [0.1.0] - 2026-10-15
### Added
- Initial demo release with simulated transaction stream.
- Streamlit dashboard with interactive KPIs and Plotly visualizations.
- Prophet-based forecasting (configurable 7/14/30 day horizons).
- Webhook alerting support (Slack/Discord/Twilio) hooks (simulated).
- Basic README, demo GIF, and architecture diagram.
- requirements.txt and example app entry (app.py).

### Fixed
- README mermaid diagram syntax and copy improvements.

### Notes
- This release uses simulated data by default. Production connectors (Shopify/Stripe) are configurable via environment variables in `.env`.