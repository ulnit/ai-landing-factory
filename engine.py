#!/usr/bin/env python3
"""AI Landing Page Factory - Generate beautiful product landing pages from config."""
import json, os, sys
from datetime import datetime
from pathlib import Path

CSS = """/* AI Landing Factory - Auto-generated */
:root{--bg:#0a0a1a;--card:#12122a;--accent:#6C5CE7;--accent2:#A29BFE;--text:#e0e0f0;--muted:#8888aa;--radius:12px}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.container{max-width:1100px;margin:0 auto;padding:0 24px}
/* Hero */
.hero{padding:100px 0 60px;text-align:center;background:linear-gradient(135deg,var(--bg) 0%,#1a1a3a 100%)}
.hero h1{font-size:3rem;margin-bottom:16px;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero .subtitle{font-size:1.25rem;color:var(--muted);max-width:700px;margin:0 auto 32px}
.hero .price{font-size:2.5rem;font-weight:800;color:var(--accent2)}
.hero .price span{font-size:1rem;color:var(--muted);font-weight:400}
.btn{display:inline-block;padding:14px 36px;border-radius:var(--radius);font-weight:600;text-decoration:none;margin:8px;transition:all .2s}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent2);transform:translateY(-2px)}
.btn-outline{border:2px solid var(--accent);color:var(--accent)}
.btn-outline:hover{background:var(--accent);color:#fff}
/* Features */
.features{padding:80px 0}
.features h2{text-align:center;font-size:2rem;margin-bottom:48px}
.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.feature-card{background:var(--card);padding:32px;border-radius:var(--radius);border:1px solid rgba(108,92,231,.15);transition:transform .3s}
.feature-card:hover{transform:translateY(-4px);border-color:var(--accent)}
.feature-icon{font-size:2.5rem;margin-bottom:16px}
.feature-card h3{font-size:1.15rem;margin-bottom:8px}
.feature-card p{color:var(--muted);font-size:.95rem}
/* Pricing */
.pricing{padding:80px 0;text-align:center}
.pricing h2{font-size:2rem;margin-bottom:48px}
.price-card{background:var(--card);padding:48px 32px;border-radius:var(--radius);border:1px solid rgba(108,92,231,.15);max-width:400px;margin:0 auto}
.price-card.featured{border-color:var(--accent);background:linear-gradient(135deg,var(--card),#1a1a40)}
.price-amount{font-size:3rem;font-weight:800;color:var(--accent2)}
.price-period{color:var(--muted)}
.price-features{list-style:none;margin:24px 0}
.price-features li{padding:8px 0;color:var(--muted)}
.price-features li::before{content:'✓ ';color:var(--accent);font-weight:bold}
/* CTA */
.cta{padding:80px 0;text-align:center}
.cta h2{font-size:2rem;margin-bottom:16px}
.cta p{color:var(--muted);margin-bottom:32px;max-width:500px;margin-left:auto;margin-right:auto}
/* Email form */
.cta-form{display:flex;gap:12px;max-width:500px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.cta-form input{flex:1;min-width:250px;padding:14px 20px;border-radius:var(--radius);border:1px solid rgba(108,92,231,.3);background:var(--card);color:var(--text);font-size:1rem}
.cta-form button{background:var(--accent);color:#fff;border:none;padding:14px 36px;border-radius:var(--radius);font-weight:600;cursor:pointer;font-size:1rem}
/* Social proof */
.social-proof{padding:40px 0;text-align:center}
.social-stats{display:flex;justify-content:center;gap:48px;flex-wrap:wrap}
.stat{text-align:center}
.stat-number{font-size:2rem;font-weight:800;color:var(--accent2)}
.stat-label{color:var(--muted);font-size:.9rem}
/* Footer */
footer{padding:40px 0;text-align:center;color:var(--muted);font-size:.85rem;border-top:1px solid rgba(108,92,231,.1)}
footer a{color:var(--accent2);text-decoration:none}
.related-products{padding:40px 0}
.related-products h3{text-align:center;margin-bottom:24px;color:var(--muted)}
.related-grid{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}
.related-tag{display:inline-block;padding:8px 18px;background:var(--card);border-radius:99px;color:var(--accent2);text-decoration:none;font-size:.9rem;border:1px solid rgba(108,92,231,.2)}
.related-tag:hover{background:var(--accent);color:#fff}
@media(max-width:768px){.hero h1{font-size:2rem}.hero{padding:60px 0 40px}}
"""

PRODUCTS_RELATED = [
    ("AI Video Factory", "https://github.com/ulnit/ai-video-factory"),
    ("AI API Gateway", "https://github.com/ulnit/ai-api-gateway"),
    ("AI Trading Signals", "https://github.com/ulnit/ai-trading-signals"),
    ("AI Resume Optimizer", "https://github.com/ulnit/ai-resume-optimizer"),
    ("AI Agent Toolkit", "https://github.com/ulnit/ai-agent-toolkit"),
    ("AI Text Pro", "https://github.com/ulnit/ai-chrome-extension"),
    ("Agent Templates", "https://github.com/ulnit/agent-templates"),
    ("Bug Bounty Kit", "https://github.com/ulnit/bb-automation-kit"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="{meta_desc}">
<meta property="og:title" content="{name} — {tagline}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="https://ulnit.github.io/{slug}/og.png">
<meta name="twitter:card" content="summary_large_image">
<title>{name} — {tagline}</title>
<style>{css}</style>
</head>
<body>

<section class="hero">
  <div class="container">
    <h1>✨ {name}</h1>
    <p class="subtitle">{tagline}</p>
    <div class="price">${price} <span>{price_unit}</span></div>
    <br>
    <a href="https://paypal.me/ulnit" class="btn btn-primary">🚀 立即购买</a>
    <a href="https://github.com/ulnit/{slug}" class="btn btn-outline">查看源码</a>
  </div>
</section>

<section class="social-proof">
  <div class="container">
    <div class="social-stats">
      <div class="stat"><div class="stat-number">🤖</div><div class="stat-label">100% 自动化</div></div>
      <div class="stat"><div class="stat-number">🕐</div><div class="stat-label">24/7 运行</div></div>
      <div class="stat"><div class="stat-number">💻</div><div class="stat-label">$35 Pi 驱动</div></div>
      <div class="stat"><div class="stat-number">⭐</div><div class="stat-label">开源可审计</div></div>
    </div>
  </div>
</section>

<section class="features">
  <div class="container">
    <h2>核心功能</h2>
    <div class="feature-grid">
      {features_html}
    </div>
  </div>
</section>

<section class="pricing">
  <div class="container">
    <h2>简单定价</h2>
    <div class="price-card featured">
      <div class="price-amount">${price}</div>
      <div class="price-period">{price_unit}</div>
      <ul class="price-features">
        <li>永久访问，一次性付费</li>
        <li>完整源码 + 部署指南</li>
        <li>30天免费更新</li>
        <li>24/7 自动运行</li>
        <li>社区支持</li>
      </ul>
      <a href="https://paypal.me/ulnit" class="btn btn-primary">立即购买 — ${price}</a>
    </div>
  </div>
</section>

<section class="cta">
  <div class="container">
    <h2>准备好自动化了吗？</h2>
    <p>获取最新更新、产品发布通知和AI自动化技巧</p>
    <form class="cta-form" action="https://formspree.io/f/your-form-id" method="POST">
      <input type="email" name="email" placeholder="输入你的邮箱..." required>
      <button type="submit">订阅更新</button>
    </form>
  </div>
</section>

<section class="related-products">
  <div class="container">
    <h3>🔗 相关产品</h3>
    <div class="related-grid">
      {related_html}
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <p>© 2026 <a href="https://ulnit.github.io/agent-store">AI Agent Store</a> · Built on $35 Raspberry Pi · <a href="https://github.com/ulnit">GitHub</a> · <a href="https://paypal.me/ulnit">PayPal</a></p>
  </div>
</footer>

</body>
</html>"""

def generate(config):
    """config = {name, slug, tagline, meta_desc, price, price_unit, features: [{icon, title, desc}]}"""
    slug = config.get("slug", config["name"].lower().replace(" ", "-"))

    # Features HTML
    features_html = ""
    for f in config.get("features", []):
        features_html += f'<div class="feature-card"><div class="feature-icon">{f["icon"]}</div><h3>{f["title"]}</h3><p>{f["desc"]}</p></div>\n'

    # Related products HTML
    related_html = ""
    related = config.get("related", PRODUCTS_RELATED)
    for name, url in related[:8]:
        if name != config["name"]:
            related_html += f'<a href="{url}" class="related-tag">{name}</a>\n'

    page = TEMPLATE.format(
        css=CSS,
        name=config["name"],
        slug=slug,
        tagline=config["tagline"],
        meta_desc=config["meta_desc"],
        price=config["price"],
        price_unit=config.get("price_unit", "一次性"),
        features_html=features_html,
        related_html=related_html,
    )

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    path = out_dir / f"{slug}.html"
    path.write_text(page)
    return str(path)

# ── Product configs ────────────────────────
PRODUCTS = [
    {
        "name": "AI Video Factory",
        "slug": "ai-video-factory",
        "tagline": "零人工，纯AI驱动的YouTube视频工厂",
        "meta_desc": "AI自动写脚本、生成幻灯片、合成视频。1080p输出，$35树莓派24/7运行。YouTube创作者必备。",
        "price": 9,
        "price_unit": "/月",
        "features": [
            {"icon": "🎬", "title": "全自动视频生成", "desc": "AI从选题到成品，零人工干预。每天自动产出1-3个视频。"},
            {"icon": "🎨", "title": "精美幻灯片", "desc": "Pillow渲染1080p幻灯片，支持渐变背景、自定义字体、图标。"},
            {"icon": "📝", "title": "AI脚本编写", "desc": "自动研究热门话题，生成专业级视频脚本。"},
            {"icon": "🎵", "title": "背景音乐", "desc": "FFmpeg自动合成背景音乐，专业级视听体验。"},
            {"icon": "🔄", "title": "定时发布", "desc": "Cron定时任务，每天7:00自动生成。设好就忘。"},
            {"icon": "📊", "title": "多平台格式", "desc": "YouTube 16:9 + TikTok 9:16 + Instagram 1:1，一套素材全平台。"},
        ],
    },
    {
        "name": "AI API Gateway",
        "slug": "ai-api-gateway",
        "tagline": "白标AI API转售，30-50%利润",
        "meta_desc": "兼容OpenAI格式的API Gateway。转售GPT-4o、Claude等模型，30-50%加价。一键部署，被动收入。",
        "price": 9,
        "price_unit": "/月",
        "features": [
            {"icon": "🔌", "title": "OpenAI兼容", "desc": "完全兼容OpenAI SDK，用户无需学习新API。即插即用。"},
            {"icon": "💰", "title": "30-50%加价", "desc": "你的定价 - 你的成本 = 你的利润。每笔调用自动赚钱。"},
            {"icon": "📊", "title": "用量统计", "desc": "实时Token统计，按用户/模型/日期查看。"},
            {"icon": "🔑", "title": "API Key管理", "desc": "为每个客户生成独立Key，设置限额。"},
            {"icon": "⚡", "title": "0依赖", "desc": "Python stdlib only，$35树莓派即可运行。"},
            {"icon": "🛡️", "title": "速率限制", "desc": "内置rate limiting，防止滥用。"},
        ],
    },
    {
        "name": "AI Trading Signals",
        "slug": "ai-trading-signals",
        "tagline": "A股AI交易信号，每日自动推送",
        "meta_desc": "基于新浪财经实时数据的A股AI交易信号。每日16:00自动生成报告。$35 Pi 24/7运行。",
        "price": 29,
        "price_unit": "/月",
        "features": [
            {"icon": "📈", "title": "A股全覆盖", "desc": "新浪财经实时数据，覆盖沪深全部股票。"},
            {"icon": "🧠", "title": "AI趋势分析", "desc": "多维度技术指标 + AI趋势预判。"},
            {"icon": "📊", "title": "每日报告", "desc": "工作日16:00自动生成，含买卖信号+置信度。"},
            {"icon": "🔔", "title": "信号推送", "desc": "交易信号自动推送到你的消息平台。"},
            {"icon": "📉", "title": "风险评分", "desc": "每支股票AI风险评分，帮助仓位管理。"},
            {"icon": "🏆", "title": "热门榜单", "desc": "AI选出的当日最值得关注的Top 10。"},
        ],
    },
    {
        "name": "AI Agent Toolkit",
        "slug": "ai-agent-toolkit",
        "tagline": "AI Agent开发者必备工具集",
        "meta_desc": "零依赖Python CLI工具集。网页爬取、API调用、文件处理、数据分析——AI Agent基础设施。",
        "price": 9,
        "price_unit": "一次性",
        "features": [
            {"icon": "🛠️", "title": "零依赖", "desc": "Python stdlib only，无pip install，开箱即用。"},
            {"icon": "🌐", "title": "Web工具", "desc": "HTTP请求、HTML解析、JSON处理一站式。"},
            {"icon": "📁", "title": "文件处理", "desc": "批量重命名、格式转换、文本搜索替换。"},
            {"icon": "📊", "title": "数据分析", "desc": "CSV/JSON分析，统计报告自动生成。"},
            {"icon": "🤖", "title": "Agent就绪", "desc": "为AI Agent优化的CLI接口，结构化输出。"},
            {"icon": "📦", "title": "20+ 工具", "desc": "爬虫、API、数据、文件、监控全覆盖。"},
        ],
    },
    {
        "name": "AI Thumbnail Pro",
        "slug": "ai-thumbnail-pro",
        "tagline": "AI驱动的社交媒体缩略图生成器",
        "meta_desc": "Python+Pillow自动生成YouTube封面、博客配图、社交媒体卡片。8种预设，8组配色，零人工。",
        "price": 5,
        "price_unit": "一次性",
        "features": [
            {"icon": "🎨", "title": "8种预设", "desc": "YouTube/博客/Twitter/LinkedIn/Instagram/Story/Product。"},
            {"icon": "🌈", "title": "8组配色", "desc": "紫/绿/蓝/橙/粉/暗/黄/热粉，自动渐变。"},
            {"icon": "⚡", "title": "批量生成", "desc": "一个命令，所有格式一键生成。"},
            {"icon": "📝", "title": "文字排版", "desc": "自动换行、居中、多级标题，无需手动调整。"},
            {"icon": "🔄", "title": "API模式", "desc": "支持API调用，可集成到自动化工作流。"},
            {"icon": "🎯", "title": "品牌定制", "desc": "自定义品牌色、logo水印。"},
        ],
    },
]

# ── CLI ────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AI Landing Page Factory")
    parser.add_argument("--all", action="store_true", help="Generate all product pages")
    parser.add_argument("--product", type=str, help="Generate specific product page")
    parser.add_argument("--config", type=str, help="JSON config file path")
    args = parser.parse_args()

    if args.config:
        config = json.loads(Path(args.config).read_text())
        path = generate(config)
        print(f"✅ {path}")

    elif args.all:
        for p in PRODUCTS:
            path = generate(p)
            print(f"✅ {path}")

    elif args.product:
        for p in PRODUCTS:
            if p["slug"] == args.product:
                path = generate(p)
                print(f"✅ {path}")
                break
        else:
            print(f"产品 '{args.product}' 未找到")

    else:
        print("用法: python engine.py --all | --product <slug> | --config <file>")
        print("可用产品: ", ", ".join(p["slug"] for p in PRODUCTS))