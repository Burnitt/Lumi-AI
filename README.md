# Lumi-AI

> AI-powered marketing automation tool for small/medium sized businesses.

Lumi handles the time-consuming stuff, ad campaigns, emails, and content, so owners can focus on running their business.

## Phase Roadmap

| Phase | Features |
|-------|----------|
| I | Campaign plan generation, email drafting, user dashboard, Stripe payments |
| II | AI video generation, image editing, scheduling, social posting |

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

API runs at `http://localhost:8000`  
Docs at `http://localhost:8000/docs`


### Frontend

```bash
cd frontend
npm install
npm run dev
```

UI runs at `http://localhost:5173`



## Tech Stack

| Layer | Choice | Why? |
|-------|--------|-----|
| Backend | FastAPI (Python) | Async, fast, great for AI apps |
| AI | OpenAI GPT-4o | Best instruction-following for marketing copy |
| Frontend | React + Vite + Tailwind | Fast dev, easy to hire for |
| DB / Auth | Supabase | Postgres + auth out of the box |
| Storage | AWS S3 | Industry standard for media |
| Email | SendGrid | Reliable delivery, good free tier |
| Payments | Stripe | Standard choice |
