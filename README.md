# Touarangi Core Engine

Touarangi Core is the external engine for real-time match tracking and betting prediction. It interfaces live with match data, odds feeds, and alerting systems, providing actionable betting intelligence to the Touarangi system.

## Features
- Fetches live NRL data from Fox Sports API
- Interfaces with Bet365 API for real-time odds
- Sends alerts to Discord using webhooks
- Modular and extensible for future integrations

## Installation
1. Clone this repository to your local system:
   ```bash
   git clone https://github.com/samdam3000/Touarangi-Core.git
   cd Touarangi-Core
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Discord webhook and Bet365 API endpoint in `touarangi_core.py`.

## Running
To run the core engine, execute the following:
```bash
python touarangi_core.py
```

## Deployment
1. Set up an appropriate cloud hosting service (e.g., Render).
2. Configure webhook endpoints and external APIs (Fox Sports, Bet365).
