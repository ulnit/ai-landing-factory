# 🏗️ AI Landing Page Factory — Auto Product Pages

**Generate beautiful, SEO-optimized landing pages from JSON config. Dark theme, responsive, email capture included.**

## What Is This?

A Python engine that takes a product definition (name, tagline, features, pricing) and outputs a complete, production-ready HTML landing page. Dark theme, mobile-responsive, with email capture forms, social proof stats, and cross-product links.

## Quick Start

```bash
# Generate all product pages at once
python3 engine.py --all

# Generate one specific product
python3 engine.py --product ai-video-factory

# Generate from custom JSON config
python3 engine.py --config my-product.json
```

## Pages Generated

Each page includes:
- 🎯 SEO meta tags (OG, Twitter Card)
- 🎨 Gradient hero with pricing
- ⭐ Social proof stats
- 📋 Feature cards grid
- 💰 Pricing card
- 📧 Email capture form (Formspree)
- 🔗 Cross-product related links
- 📱 Mobile responsive
- 🌙 Dark theme

## Built-in Products

1. AI Video Factory
2. AI API Gateway
3. AI Trading Signals
4. AI Agent Toolkit
5. AI Thumbnail Pro

## Custom Landing Page Config

```json
{
  "name": "My Product",
  "slug": "my-product",
  "tagline": "One-liner value prop",
  "meta_desc": "SEO description (150 chars)",
  "price": 9,
  "price_unit": "/月",
  "features": [
    {"icon": "🚀", "title": "Feature 1", "desc": "Description"}
  ]
}
```

## Pricing: $9 (one-time)

Includes source code, 5 built-in templates, and 30 days of updates.

[💰 Buy Now](https://paypal.me/ulnit) · [📦 GitHub](https://github.com/ulnit/ai-landing-factory)

## Related Products

- [AI Thumbnail Pro](https://github.com/ulnit/ai-thumbnail-pro) — Auto graphics
- [AI Social Media Kit](https://github.com/ulnit/ai-social-kit) — Auto posts
- [AI Video Factory](https://github.com/ulnit/ai-video-factory) — Auto videos
- [AI Agent Toolkit](https://github.com/ulnit/ai-agent-toolkit) — CLI tools
- [Full Store](https://ulnit.github.io/agent-store) — All 20+ AI products

## Tech Stack

- Python 3 stdlib
- Static HTML/CSS output
- GitHub Pages hosting
- Zero server costs

---

*Part of the [AI Agent Store](https://ulnit.github.io/agent-store) — 20+ AI products running on a $35 Raspberry Pi.*