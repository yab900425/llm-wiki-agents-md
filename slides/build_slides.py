"""slides.json → index.html（單一檔案、無外部資源）。先跑 check_slides.py 通過再建置。"""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/yab900425/llm-wiki-agents-md/blob/main/"
data = json.loads((ROOT / "slides" / "slides.json").read_text(encoding="utf-8"))
e = html.escape

def lis(items):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"

def basis(refs):
    links = "".join(f'<a href="{REPO}{r}" target="_blank" rel="noopener">{e(r.split("/")[-1])}</a>' for r in refs)
    return f'<div class="basis"><span>依據的 wiki 頁面</span>{links}</div>'

def render(i, s):
    L = s["layout"]
    k = f'<p class="kicker">{e(s.get("kicker",""))}</p>' if s.get("kicker") else ""
    if L == "title":
        body = f'<p class="kicker">{e(s["kicker"])}</p><h1>{e(s["title"])}</h1><p class="sub">{e(s["sub"])}</p>'
        return f'<section class="slide title" id="s{i}">{body}</section>'
    h = f'{k}<h2>{e(s["title"])}</h2>'
    if L == "list":
        c = lis(s["items"])
    elif L == "table":
        head = "".join(f"<th>{e(x)}</th>" for x in s["head"])
        rows = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in s["rows"])
        c = f'<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
    elif L == "cols":
        n = len(s["cols"])
        cols = "".join(f'<div class="col"><h3>{e(c["head"])}</h3>{lis(c["items"])}</div>' for c in s["cols"])
        c = f'<div class="cols n{n}">{cols}</div>'
    elif L == "code":
        c = f'<pre>{e(s["code"])}</pre>' + lis(s["items"])
    elif L == "sources":
        c = "<ol class='src'>" + "".join(
            f'<li><b>{e(a)}</b> {e(b)}<br><a href="{e(u)}" target="_blank" rel="noopener">{e(u)}</a></li>' for a, b, u in s["sources"]) + "</ol>"
    else:
        raise SystemExit(f"未知版型：{L}")
    note = f'<p class="note">{e(s["note"])}</p>' if s.get("note") else ""
    return f'<section class="slide" id="s{i}">{h}<div class="body">{c}{note}</div>{basis(s["refs"])}</section>'

slides = "\n".join(render(i, s) for i, s in enumerate(data["slides"], 1))

PAGE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AGENTS.md 教學簡報</title>
<style>
:root{--navy:#0d2c5c;--ink:#15151a;--paper:#fff;--stone:#f4f2ed;--rule:#d8d4ca;--muted:#6a6862;--accent:#b23a2e;
--serif:"Noto Serif TC","Songti TC","PMingLiU",serif;--sans:"Noto Sans TC","PingFang TC","Microsoft JhengHei",system-ui,sans-serif}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--stone);color:var(--ink);font-family:var(--sans);line-height:1.7}
.deck{max-width:1100px;margin:0 auto;padding:16px}
.slide{background:var(--paper);border-top:6px solid var(--navy);padding:44px 52px 28px;margin:0 0 20px;min-height:520px;display:flex;flex-direction:column}
.kicker{font-size:.78rem;letter-spacing:.14em;color:var(--accent);margin:0 0 6px;font-weight:600}
h1,h2,h3{font-family:var(--serif);margin:0;line-height:1.35}
h2{font-size:1.9rem;color:var(--navy);margin-bottom:22px}
h3{font-size:1.1rem;margin-bottom:8px;color:var(--navy)}
.body{flex:1;font-size:1.15rem}
ul{margin:0;padding-left:1.2em}li{margin:.4em 0}
.note{margin-top:22px;padding:10px 14px;border-left:3px solid var(--accent);background:var(--stone);font-size:.95rem;color:#3d3b36}
table{border-collapse:collapse;width:100%;font-size:1.05rem}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--rule);vertical-align:top}
th{border-bottom:2px solid var(--ink);font-size:.9rem;color:var(--muted)}
.cols{display:grid;gap:18px}.cols.n3{grid-template-columns:repeat(3,1fr)}.cols.n6{grid-template-columns:repeat(3,1fr)}
.col{border-top:2px solid var(--ink);padding-top:10px;font-size:1rem}
pre{background:var(--ink);color:#f2efe6;padding:16px 20px;font-size:1rem;overflow:auto;margin:0 0 16px}
.src{padding-left:1.4em;font-size:1rem}.src a{color:var(--navy);word-break:break-all;font-size:.85rem}
.basis{margin-top:22px;padding-top:10px;border-top:1px solid var(--rule);font-size:.78rem;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
.basis a{color:var(--navy)}
.title{background:var(--navy);color:#fff;border-top:6px solid var(--accent);justify-content:center;min-height:520px}
.title h1{font-size:2.6rem;margin:6px 0 16px}.title .kicker{color:#e8c98b}.title .sub{font-size:1.2rem;color:#c9d3e6;margin:0}
.nav{position:sticky;bottom:0;background:var(--navy);color:#fff;display:flex;gap:12px;align-items:center;justify-content:center;padding:8px;font-size:.9rem}
.nav button{background:none;border:1px solid #fff;color:#fff;padding:4px 14px;cursor:pointer;font-size:.9rem}
.hint{color:#c9d3e6}
@media(max-width:700px){.slide{padding:28px 20px 18px;min-height:0}h2{font-size:1.45rem}.title h1{font-size:1.8rem}.cols.n3,.cols.n6{grid-template-columns:1fr}.body{font-size:1.05rem}}
@media(min-width:701px){.deck.present .slide{display:none}.deck.present .slide.on{display:flex}}
@media print{.nav{display:none}.slide{break-after:page;margin:0;border-top:0}body{background:#fff}}
</style>
</head>
<body>
<main class="deck" id="deck">
__SLIDES__
</main>
<div class="nav"><button id="prev">← 上一頁</button><span id="pos"></span><button id="next">下一頁 →</button><button id="mode">投影模式</button><span class="hint">鍵盤 ← → 換頁</span></div>
<script>
(function(){
  var deck=document.getElementById('deck'),sl=[].slice.call(deck.querySelectorAll('.slide')),i=0,pos=document.getElementById('pos');
  function show(n){i=Math.max(0,Math.min(sl.length-1,n));sl.forEach(function(s,k){s.classList.toggle('on',k===i)});
    pos.textContent=(i+1)+' / '+sl.length;
    if(!deck.classList.contains('present'))sl[i].scrollIntoView({behavior:'smooth',block:'start'});}
  document.getElementById('prev').onclick=function(){show(i-1)};
  document.getElementById('next').onclick=function(){show(i+1)};
  document.getElementById('mode').onclick=function(){deck.classList.toggle('present');show(i)};
  document.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='PageDown')show(i+1);if(e.key==='ArrowLeft'||e.key==='PageUp')show(i-1);});
  show(0);window.scrollTo(0,0);
})();
</script>
</body>
</html>
"""
(ROOT / "slides" / "index.html").write_text(PAGE.replace("__SLIDES__", slides), encoding="utf-8")
print(f"已產生 slides/index.html（{len(data['slides'])} 頁）")
