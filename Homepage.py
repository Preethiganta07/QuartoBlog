import streamlit as st

# ── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Preethi Ganta | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background: #f9fafb !important;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
    background: #0a0f1e;
    padding: 100px 8vw 80px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 60% 70% at 70% 50%, rgba(0,112,243,0.18), transparent 65%),
        radial-gradient(ellipse 40% 40% at 10% 80%, rgba(0,180,216,0.12), transparent 60%);
    pointer-events: none;
}
.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,112,243,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,112,243,0.04) 1px, transparent 1px);
    background-size: 60px 60px;
}
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00b4d8;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 30px;
    height: 1px;
    background: #00b4d8;
}
.hero-name {
    font-size: clamp(3rem, 6vw, 5.5rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 10px;
}
.hero-name span {
    background: linear-gradient(135deg, #0070f3, #00b4d8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-role {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.45);
    margin-bottom: 20px;
    font-weight: 300;
}
.hero-desc {
    font-size: 1rem;
    color: rgba(255,255,255,0.4);
    line-height: 1.8;
    max-width: 540px;
    margin-bottom: 40px;
    font-weight: 300;
}
.hero-btns { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 60px; }
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 26px;
    background: linear-gradient(135deg, #0070f3, #00b4d8);
    color: #fff !important;
    font-size: 14px;
    font-weight: 500;
    border-radius: 8px;
    text-decoration: none !important;
    box-shadow: 0 4px 20px rgba(0,112,243,0.35);
    transition: all 0.25s;
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,112,243,0.45); }
.btn-ghost {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 26px;
    background: transparent;
    color: rgba(255,255,255,0.65) !important;
    font-size: 14px;
    font-weight: 500;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 8px;
    text-decoration: none !important;
    transition: all 0.25s;
}
.btn-ghost:hover { border-color: rgba(255,255,255,0.4); color: #fff !important; }

/* stats row */
.hero-stats {
    display: flex;
    gap: 40px;
    padding-top: 40px;
    border-top: 1px solid rgba(255,255,255,0.06);
    flex-wrap: wrap;
}
.stat-item { text-align: left; }
.stat-val {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #0070f3, #00b4d8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 4px;
}
.stat-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: rgba(255,255,255,0.3);
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ── SECTION ── */
.section { padding: 80px 8vw; max-width: 1300px; margin: 0 auto; }
.section-alt { background: #fff; padding: 80px 8vw; }
.section-alt-inner { max-width: 1300px; margin: 0 auto; }
.section-dark { background: #0a0f1e; padding: 80px 8vw; }
.section-dark-inner { max-width: 1300px; margin: 0 auto; }

.sec-tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #0070f3;
    background: rgba(0,112,243,0.07);
    border: 1px solid rgba(0,112,243,0.15);
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.sec-tag-dark {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00b4d8;
    background: rgba(0,180,216,0.08);
    border: 1px solid rgba(0,180,216,0.2);
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.sec-title {
    font-size: clamp(1.6rem, 2.5vw, 2.2rem);
    font-weight: 700;
    color: #1a2332;
    letter-spacing: -0.5px;
    margin-bottom: 40px;
}
.sec-title-dark {
    font-size: clamp(1.6rem, 2.5vw, 2.2rem);
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 40px;
}

/* ── ABOUT ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
.about-text p { font-size: 1rem; color: #5a6a7e; line-height: 1.85; margin-bottom: 18px; }
.about-text p strong { color: #1a2332; font-weight: 500; }
.highlight {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 13px 16px;
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    font-size: 13.5px;
    color: #1a2332;
    font-weight: 500;
    margin-bottom: 10px;
    transition: all 0.2s;
}
.highlight:hover { border-color: rgba(0,112,243,0.3); transform: translateX(4px); }
.hi { width: 34px; height: 34px; border-radius: 8px; background: rgba(0,112,243,0.08); display: flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0; }

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; }
.skill-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s;
}
.skill-card:hover { background: rgba(0,112,243,0.08); border-color: rgba(0,112,243,0.25); transform: translateY(-3px); }
.skill-card-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00b4d8;
    margin-bottom: 14px;
}
.skill-tags { display: flex; flex-wrap: wrap; gap: 7px; }
.stag {
    font-size: 12px;
    padding: 4px 10px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 4px;
    color: rgba(255,255,255,0.65);
}

/* ── PROJECTS ── */
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
.proj-card {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
    transition: all 0.3s;
    text-decoration: none !important;
    display: block;
}
.proj-card:hover { border-color: rgba(0,112,243,0.3); box-shadow: 0 10px 36px rgba(0,112,243,0.1); transform: translateY(-4px); }
.proj-top { height: 5px; background: linear-gradient(90deg, #0070f3, #00b4d8); }
.proj-card:nth-child(2) .proj-top { background: linear-gradient(90deg, #00b4d8, #0070f3); }
.proj-card:nth-child(3) .proj-top { background: linear-gradient(90deg, #0070f3, #005bc4); }
.proj-card:nth-child(4) .proj-top { background: linear-gradient(90deg, #00b4d8, #0070f3); }
.proj-card:nth-child(5) .proj-top { background: linear-gradient(90deg, #0070f3, #00b4d8); }
.proj-body { padding: 24px; }
.proj-icon { font-size: 28px; margin-bottom: 14px; }
.proj-title { font-size: 1.05rem; font-weight: 600; color: #1a2332; margin-bottom: 8px; }
.proj-desc { font-size: 13px; color: #5a6a7e; line-height: 1.7; margin-bottom: 16px; }
.proj-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
.ptag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    padding: 3px 8px;
    background: rgba(0,112,243,0.06);
    border: 1px solid rgba(0,112,243,0.12);
    border-radius: 4px;
    color: #0070f3;
}
.proj-link { font-size: 13px; color: #0070f3; font-weight: 500; }

/* ── CONTACT ── */
.contact-wrap { background: #0a0f1e; padding: 80px 8vw; text-align: center; }
.contact-inner { max-width: 560px; margin: 0 auto; }
.contact-title { font-size: clamp(1.6rem, 2.5vw, 2.2rem); font-weight: 700; color: #fff; letter-spacing: -0.5px; margin-bottom: 14px; }
.contact-desc { font-size: 1rem; color: rgba(255,255,255,0.4); line-height: 1.75; margin-bottom: 40px; font-weight: 300; }
.slinks { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.slink {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 20px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    color: rgba(255,255,255,0.6) !important;
    font-size: 13.5px;
    font-weight: 500;
    text-decoration: none !important;
    transition: all 0.25s;
}
.slink:hover { background: rgba(0,112,243,0.12); border-color: rgba(0,112,243,0.35); color: #fff !important; transform: translateY(-2px); }

/* ── FOOTER ── */
.footer { background: #06090f; padding: 24px 8vw; text-align: center; border-top: 1px solid rgba(255,255,255,0.04); }
.footer p { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: rgba(255,255,255,0.2); }
.footer strong { color: #00b4d8; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
st.markdown("""
<section class="hero">
  <div class="hero-grid"></div>
  <div style="position:relative;z-index:2;">
    <div class="hero-eyebrow">Available for opportunities</div>
    <div class="hero-name">Preethi<br/><span>Ganta</span></div>
    <div class="hero-role">Data Analyst · SQL · Python · Power BI</div>
    <div class="hero-desc">
      Transforming raw data into clear, actionable insights.
      I specialise in customer analytics, churn modelling,
      and building dashboards that help businesses make smarter decisions.
    </div>
    <div class="hero-btns">
      <a href="https://github.com/Preethiganta07" target="_blank" class="btn-primary">🚀 View My Projects</a>
      <a href="https://www.linkedin.com/in/preethi-g-4b414b28b" target="_blank" class="btn-ghost">💼 LinkedIn</a>
    </div>
    <div class="hero-stats">
      <div class="stat-item"><div class="stat-val">4+</div><div class="stat-lbl">Years Exp.</div></div>
      <div class="stat-item"><div class="stat-val">5+</div><div class="stat-lbl">Projects</div></div>
      <div class="stat-item"><div class="stat-val">SQL</div><div class="stat-lbl">Primary Tool</div></div>
      <div class="stat-item"><div class="stat-val">Python</div><div class="stat-lbl">Analytics</div></div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-alt">
<div class="section-alt-inner">
  <div class="sec-tag">About Me</div>
  <div class="sec-title">Turning Data into Decisions</div>
  <div class="about-grid">
    <div class="about-text">
      <p>Hi, I'm <strong>Preethi Ganta</strong> — a Data Analyst with <strong>4+ years of experience</strong> and a passion for finding the story hidden inside numbers. I enjoy working across the full analytics pipeline, from wrangling messy datasets to building clean, interactive dashboards.</p>
      <p>I'm currently seeking <strong>Data Analyst roles</strong> where I can apply my skills in SQL, Python, and data visualisation to drive real business impact. I thrive in environments where curiosity is valued and data drives decisions.</p>
      <p>When I'm not querying databases, I'm building portfolio projects, exploring new datasets, and sharing insights through my blog.</p>
    </div>
    <div>
      <div class="highlight"><div class="hi">🎯</div> Specialised in Customer & Churn Analytics</div>
      <div class="highlight"><div class="hi">📊</div> Dashboard design with Power BI & Tableau</div>
      <div class="highlight"><div class="hi">🗄️</div> Advanced SQL — window functions, CTEs, subqueries</div>
      <div class="highlight"><div class="hi">🐍</div> Python for data wrangling & visualisation</div>
      <div class="highlight"><div class="hi">📈</div> Translating analysis into business recommendations</div>
    </div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-dark">
<div class="section-dark-inner">
  <div class="sec-tag-dark">Skills & Tools</div>
  <div class="sec-title-dark">My Analytical Toolkit</div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-card-title">Languages</div>
      <div class="skill-tags">
        <span class="stag">SQL</span><span class="stag">Python</span><span class="stag">R</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-card-title">Python Libraries</div>
      <div class="skill-tags">
        <span class="stag">Pandas</span><span class="stag">NumPy</span><span class="stag">Matplotlib</span><span class="stag">Seaborn</span><span class="stag">Scikit-learn</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-card-title">Visualisation</div>
      <div class="skill-tags">
        <span class="stag">Power BI</span><span class="stag">Tableau</span><span class="stag">Plotly</span><span class="stag">Streamlit</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-card-title">Databases</div>
      <div class="skill-tags">
        <span class="stag">PostgreSQL</span><span class="stag">MySQL</span><span class="stag">SQLite</span><span class="stag">BigQuery</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-card-title">Analytics</div>
      <div class="skill-tags">
        <span class="stag">A/B Testing</span><span class="stag">Cohort Analysis</span><span class="stag">Churn Modelling</span><span class="stag">KPI Reporting</span>
      </div>
    </div>
    <div class="skill-card">
      <div class="skill-card-title">Tools</div>
      <div class="skill-tags">
        <span class="stag">Git</span><span class="stag">Jupyter</span><span class="stag">Quarto</span><span class="stag">VS Code</span><span class="stag">Excel</span>
      </div>
    </div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-alt">
<div class="section-alt-inner">
  <div class="sec-tag">Featured Projects</div>
  <div class="sec-title">Work I'm Proud Of</div>
  <div class="projects-grid">

    <a href="https://preethiganta07.github.io/QuartoBlog/posts/SQL%20Customer%20Churn%20Analysis/Churn-Analysis.html" target="_blank" class="proj-card">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">🔍</div>
        <div class="proj-title">SQL Customer Churn Analysis</div>
        <p class="proj-desc">Simulated a 2,000-customer database, ran 8 SQL queries to uncover churn patterns — 45% Basic plan churn rate identified.</p>
        <div class="proj-tags"><span class="ptag">Python</span><span class="ptag">SQLite</span><span class="ptag">Pandas</span><span class="ptag">Matplotlib</span></div>
        <div class="proj-link">Read case study →</div>
      </div>
    </a>

    <a href="https://preethiganta07.github.io/QuartoBlog/posts/E-commerce-Sales-Dashboard/Index.html" target="_blank" class="proj-card">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">🛒</div>
        <div class="proj-title">E-Commerce Sales Dashboard</div>
        <p class="proj-desc">Interactive dashboard tracking revenue trends, top products, and regional performance for data-driven decisions.</p>
        <div class="proj-tags"><span class="ptag">Power BI</span><span class="ptag">SQL</span><span class="ptag">Excel</span><span class="ptag">DAX</span></div>
        <div class="proj-link">Read case study →</div>
      </div>
    </a>

    <a href="https://preethiganta07.github.io/QuartoBlog/posts/Car%20Price%20Prediction/Prediction.html" target="_blank" class="proj-card">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">🚗</div>
        <div class="proj-title">Car Price Prediction</div>
        <p class="proj-desc">ML regression model predicting car prices based on brand, mileage, year, and fuel type with feature importance analysis.</p>
        <div class="proj-tags"><span class="ptag">Python</span><span class="ptag">Scikit-learn</span><span class="ptag">Regression</span><span class="ptag">Pandas</span></div>
        <div class="proj-link">Read case study →</div>
      </div>
    </a>

    <a href="https://preethiganta07.github.io/QuartoBlog/posts/wine%20data/wine.html" target="_blank" class="proj-card">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">🍷</div>
        <div class="proj-title">Wine Quality Analysis</div>
        <p class="proj-desc">Analysed physicochemical properties of wines to predict quality scores using classification models and EDA.</p>
        <div class="proj-tags"><span class="ptag">Python</span><span class="ptag">Seaborn</span><span class="ptag">Classification</span><span class="ptag">EDA</span></div>
        <div class="proj-link">Read case study →</div>
      </div>
    </a>

    <a href="https://preethiganta07.github.io/QuartoBlog/posts/Iris%20Data/Report.html" target="_blank" class="proj-card">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">🌸</div>
        <div class="proj-title">Iris Classification</div>
        <p class="proj-desc">Multiclass classification on the Iris dataset — decision boundaries, model comparison, and species cluster visualisation.</p>
        <div class="proj-tags"><span class="ptag">Python</span><span class="ptag">Scikit-learn</span><span class="ptag">Matplotlib</span><span class="ptag">ML</span></div>
        <div class="proj-link">Read case study →</div>
      </div>
    </a>

    <div class="proj-card" style="opacity:0.5;cursor:default;">
      <div class="proj-top"></div>
      <div class="proj-body">
        <div class="proj-icon">⚙️</div>
        <div class="proj-title">More Coming Soon</div>
        <p class="proj-desc">Working on customer segmentation, cohort analysis, and predictive analytics projects. Stay tuned!</p>
        <div class="proj-tags"><span class="ptag">Tableau</span><span class="ptag">Python</span><span class="ptag">ML</span></div>
        <div class="proj-link" style="color:#5a6a7e;">In progress...</div>
      </div>
    </div>

  </div>
</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="contact-wrap">
  <div class="contact-inner">
    <div class="sec-tag-dark" style="margin-bottom:20px;">Get In Touch</div>
    <div class="contact-title">Let's Work Together</div>
    <div class="contact-desc">I'm actively looking for Data Analyst opportunities. Whether you have a role, a project, or just want to talk data — I'd love to hear from you.</div>
    <div class="slinks">
      <a href="https://www.linkedin.com/in/preethi-g-4b414b28b" target="_blank" class="slink">💼 LinkedIn</a>
      <a href="https://github.com/Preethiganta07" target="_blank" class="slink">🐙 GitHub</a>
      <a href="mailto:preethiganta@email.com" class="slink">✉️ Email Me</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  <p>Designed & built by <strong>Preethi Ganta</strong> · Data Analyst · 2025</p>
</div>
""", unsafe_allow_html=True)