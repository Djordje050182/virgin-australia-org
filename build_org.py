import pathlib
sp = pathlib.Path(__file__).parent
fraunces = (sp / "Fraunces-600.b64").read_text().strip()
grotesk = (sp / "SpaceGrotesk-400.b64").read_text().strip()

html = """<title>Virgin Australia — Leadership Organogram</title>
<style>
@font-face{font-family:'Fraunces';font-style:normal;font-weight:600 700;src:url(data:font/woff2;base64,__FRAUNCES__) format('woff2');}
@font-face{font-family:'Space Grotesk';font-style:normal;font-weight:400 700;src:url(data:font/woff2;base64,__GROTESK__) format('woff2');}

:root{
  --paper:#FBFAF8; --card:#FFFFFF; --ink:#221B2E; --muted:#6F6879;
  --line:#E6E1EA; --red:#E10A0A; --violet:#2D054E; --violet-soft:#F1EBF7;
  --red-soft:#FDECEC; --shadow:0 1px 2px rgba(34,27,46,.05),0 4px 14px rgba(34,27,46,.06);
}
@media (prefers-color-scheme: dark){:root{
  --paper:#1C1526; --card:#261E33; --ink:#F2EEF6; --muted:#A99FB6;
  --line:#3A3049; --red:#FF4D4D; --violet:#C9A8EC; --violet-soft:#332349;
  --red-soft:#3D1B22; --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
}}
:root[data-theme="dark"]{
  --paper:#1C1526; --card:#261E33; --ink:#F2EEF6; --muted:#A99FB6;
  --line:#3A3049; --red:#FF4D4D; --violet:#C9A8EC; --violet-soft:#332349;
  --red-soft:#3D1B22; --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.25);
}
:root[data-theme="light"]{
  --paper:#FBFAF8; --card:#FFFFFF; --ink:#221B2E; --muted:#6F6879;
  --line:#E6E1EA; --red:#E10A0A; --violet:#2D054E; --violet-soft:#F1EBF7;
  --red-soft:#FDECEC; --shadow:0 1px 2px rgba(34,27,46,.05),0 4px 14px rgba(34,27,46,.06);
}

*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;
  margin:0;padding:48px 24px 64px;line-height:1.45;}
.wrap{max-width:1060px;margin:0 auto;}

.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--red);font-weight:700;margin:0 0 10px;}
h1{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:clamp(28px,4.5vw,42px);
  margin:0 0 6px;letter-spacing:-.01em;text-wrap:balance;}
.sub{color:var(--muted);font-size:15px;margin:0 0 8px;max-width:64ch;}
.asat{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 40px;}

.tier-label{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
  font-weight:700;text-align:center;margin:0 0 12px;}

/* Board */
.board{border:1px solid var(--line);border-radius:14px;background:var(--card);box-shadow:var(--shadow);
  padding:20px 24px;margin:0 auto 0;}
.chair{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);
  padding-bottom:14px;margin-bottom:14px;}
.chair .name{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:20px;}
.chair .role{color:var(--violet);font-weight:700;font-size:12px;letter-spacing:.1em;text-transform:uppercase;}
.neds{display:grid;grid-template-columns:repeat(4,1fr);gap:10px 20px;}
.ned{font-size:13px;}
.ned b{display:block;font-weight:700;font-size:13.5px;}
.ned span{color:var(--muted);font-size:12px;}

/* connectors */
.drop{width:2px;height:34px;background:var(--line);margin:0 auto;}
.drop.red{background:var(--red);}

/* CEO */
.ceo{max-width:460px;margin:0 auto;background:var(--card);border:1px solid var(--line);
  border-top:4px solid var(--red);border-radius:14px;box-shadow:var(--shadow);padding:20px 24px;text-align:center;}
.ceo .name{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:24px;}
.ceo .role{color:var(--red);font-weight:700;font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin:4px 0 8px;}
.ceo .note{color:var(--muted);font-size:13px;}

/* ELT branches */
.branches{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:0 22px;padding-top:34px;}
.branches::before{content:"";position:absolute;top:0;left:16.667%;width:66.666%;height:2px;background:var(--line);}
.cluster{position:relative;display:flex;flex-direction:column;gap:12px;}
.cluster::before{content:"";position:absolute;top:-34px;left:50%;width:2px;height:34px;background:var(--line);transform:translateX(-50%);}
.cluster-h{text-align:center;font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:700;
  color:var(--violet);background:var(--violet-soft);border-radius:999px;padding:7px 10px;margin:0 auto 4px;width:100%;}

.exec{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);padding:16px 18px;}
.exec .name{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:17.5px;line-height:1.2;}
.exec .role{color:var(--red);font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin:5px 0 7px;line-height:1.5;}
.exec .note{color:var(--muted);font-size:12.5px;line-height:1.5;}
.chip{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  color:var(--violet);background:var(--violet-soft);border-radius:999px;padding:3px 9px;margin-top:9px;}

/* below-ELT technology tier */
.drop.dashed{background:none;border-left:2px dashed var(--line);}
.techtier{max-width:720px;margin:0 auto;border:1px dashed var(--line);border-radius:14px;padding:18px 20px;}
.techtier .tt-head{text-align:center;margin-bottom:14px;}
.techtier .tt-label{font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--muted);}
.techtier .tt-note{font-size:12.5px;color:var(--muted);margin-top:4px;}
.cio{max-width:340px;margin:0 auto 0;background:var(--card);border:1px solid var(--line);border-radius:12px;
  box-shadow:var(--shadow);padding:14px 18px;text-align:center;}
.cio .name{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:17px;}
.cio .role{color:var(--violet);font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-top:3px;}
.techrow{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:26px;position:relative;}
.techrow::before{content:"";position:absolute;top:-26px;left:16.667%;width:66.666%;height:2px;background:var(--line);}
.techrow .exec{position:relative;}
.techrow .exec::before{content:"";position:absolute;top:-26px;left:50%;width:2px;height:26px;background:var(--line);transform:translateX(-50%);}
.exec.ai{border:1.5px solid var(--red);}
.chip.red{color:var(--red);background:var(--red-soft);}

/* Bain thread */
.thread{margin-top:52px;border:1px solid var(--line);border-radius:14px;background:var(--card);box-shadow:var(--shadow);padding:22px 24px;}
.thread h2{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:21px;margin:0 0 4px;}
.thread .tsub{color:var(--muted);font-size:13.5px;margin:0 0 18px;max-width:70ch;}
.chain{display:flex;align-items:stretch;gap:0;flex-wrap:wrap;}
.chain-node{flex:1 1 180px;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:14px 16px;min-width:180px;}
.chain-node b{display:block;font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:15.5px;margin-bottom:3px;}
.chain-node span{font-size:12.5px;color:var(--muted);line-height:1.5;display:block;}
.chain-link{display:flex;align-items:center;justify-content:center;padding:0 10px;color:var(--red);font-weight:700;font-size:18px;}
@media (max-width:760px){.chain{flex-direction:column;}.chain-link{transform:rotate(90deg);padding:6px 0;}}

/* pitch notes */
.notes{margin-top:52px;border-top:1px solid var(--line);padding-top:28px;}
.notes h2{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:21px;margin:0 0 14px;}
.notes ul{margin:0;padding-left:20px;color:var(--ink);font-size:14px;display:flex;flex-direction:column;gap:9px;}
.notes li::marker{color:var(--red);}
.notes .muted{color:var(--muted);}
.src{margin-top:26px;font-size:12px;color:var(--muted);line-height:1.7;}
.src a{color:var(--muted);}

.scroller{overflow-x:auto;}
.chart{min-width:720px;}

@media (max-width:760px){
  body{padding:32px 16px 48px;}
  .neds{grid-template-columns:repeat(2,1fr);}
}
</style>

<div class="wrap">
  <p class="eyebrow">Virgin Australia Holdings &middot; ASX:VGN</p>
  <h1>Leadership organogram</h1>
  <p class="sub">Account briefing: board and Executive Leadership Team as published by Virgin Australia, with the technology tier and investor connections assembled from public sources. Bain Capital and Qatar Airways remain cornerstone shareholders following the June 2025 ASX re-listing.</p>
  <p class="asat">As at 5 July 2026</p>

  <div class="scroller"><div class="chart">

    <p class="tier-label">Board of Directors</p>
    <div class="board">
      <div class="chair">
        <span class="name">Peter Warne</span>
        <span class="role">Independent Non-Executive Chairman</span>
      </div>
      <div class="neds">
        <div class="ned"><b>Pippa Downes</b><span>Independent NED</span></div>
        <div class="ned"><b>Melinda Conrad</b><span>Independent NED</span></div>
        <div class="ned"><b>Warwick Negus</b><span>Independent NED</span></div>
        <div class="ned"><b>Dimitri Courtelis</b><span>Non-Executive Director</span></div>
        <div class="ned"><b>Ryan Cotton</b><span>NED &middot; Bain Capital</span></div>
        <div class="ned"><b>Mike Murphy</b><span>NED &middot; Bain Capital</span></div>
        <div class="ned"><b>Charles Lawson</b><span>NED &middot; Bain Capital</span></div>
        <div class="ned"><b>Dave Emerson</b><span>Managing Director</span></div>
      </div>
    </div>

    <div class="drop red"></div>

    <div class="ceo">
      <div class="name">Dave Emerson</div>
      <div class="role">Chief Executive Officer &amp; Managing Director</div>
      <div class="note">CEO since March 2025; previously Virgin Australia CCO and led Bain &amp; Company&rsquo;s global airline practice.</div>
    </div>

    <div class="branches">
      <div class="cluster">
        <div class="cluster-h">Commercial &amp; Customer</div>
        <div class="exec">
          <div class="name">Paul Jones</div>
          <div class="role">Chief Commercial Officer</div>
          <div class="note">Network, revenue and sales; background across aviation, FMCG and technology.</div>
        </div>
        <div class="exec">
          <div class="name">Andrew Cleary</div>
          <div class="role">Chief Customer Officer &amp; CEO, Velocity</div>
          <div class="note">Owns customer experience and the Velocity Frequent Flyer business.</div>
          <span class="chip">Velocity</span>
        </div>
        <div class="exec">
          <div class="name">Libby Minogue</div>
          <div class="role">Chief Marketing Officer</div>
          <div class="note">25+ years across media, content, digital and technology.</div>
        </div>
      </div>

      <div class="cluster">
        <div class="cluster-h">Operations &amp; Risk</div>
        <div class="exec">
          <div class="name">Chris Snook</div>
          <div class="role">Chief Operations Officer</div>
          <div class="note">COO since Feb 2025; 39 years in aviation incl. senior roles at Qantas and Jetstar.</div>
        </div>
        <div class="exec">
          <div class="name">Stuart Aggs</div>
          <div class="role">Chief Risk Officer</div>
          <div class="note">CRO since March 2025; 20+ years inside Virgin Australia operations.</div>
        </div>
      </div>

      <div class="cluster">
        <div class="cluster-h">Corporate &amp; Enablement</div>
        <div class="exec">
          <div class="name">Race Strauss</div>
          <div class="role">Chief Financial Officer</div>
          <div class="note">CFO since March 2023; prior airline and consumer-sector finance leadership.</div>
        </div>
        <div class="exec">
          <div class="name">Lisa Burquest</div>
          <div class="role">Chief People Officer</div>
          <div class="note">CPO since Feb 2021; 30 years in people and culture at ASX-listed companies.</div>
        </div>
        <div class="exec">
          <div class="name">Susan Schneider</div>
          <div class="role">Chief Legal Officer &amp; Company Secretary</div>
          <div class="note">20+ years of legal and risk experience in Australia and overseas.</div>
        </div>
      </div>
    </div>

    <div class="drop dashed"></div>
    <div class="techtier">
      <div class="tt-head">
        <div class="tt-label">Technology function &middot; below ELT</div>
        <div class="tt-note">Virgin deliberately moved technology inside the <b>customer division</b> during the transformation &mdash; it sits close to customer strategy, product and the contact centres. Post-2025 reshuffle reporting line unconfirmed publicly.</div>
      </div>
      <div class="cio">
        <div class="name">David Hogarth</div>
        <div class="role">Chief Information Officer</div>
      </div>
      <div class="techrow">
        <div class="exec">
          <div class="name">Emma Taylor</div>
          <div class="role">Head of Technology</div>
          <div class="note">Architecture, integration, digital development, agile CoE, RPA.</div>
        </div>
        <div class="exec">
          <div class="name">Mark Allen</div>
          <div class="role">Head of Data Platform</div>
          <div class="note">Data platforms; Databricks-based analytics estate.</div>
        </div>
        <div class="exec ai">
          <div class="name">Head of AI</div>
          <div class="role">New role &middot; hired 2026</div>
          <div class="note">Advertised on Virgin careers, now filled; team also hiring conversational AI designers and an AI transformation lead.</div>
          <span class="chip red">Your pitch audience</span>
        </div>
      </div>
    </div>

  </div></div>

  <div class="thread">
    <h2>The investor thread</h2>
    <p class="tsub">Virgin Australia and Decagon share a common thread through Bain Capital &mdash; the strongest warm-introduction path into this chart. All facts below are public record.</p>
    <div class="chain">
      <div class="chain-node">
        <b>Bain Capital</b>
        <span>Cornerstone Virgin shareholder since 2020; retained a major stake through the June 2025 ASX re-listing. Three partners on the Virgin board: Cotton, Murphy, Lawson.</span>
      </div>
      <div class="chain-link">&rarr;</div>
      <div class="chain-node">
        <b>Bain Capital Ventures</b>
        <span>Bain Capital&rsquo;s venture arm. Led Decagon&rsquo;s $65M Series B (Oct 2024) and invested again in the Series C ($1.5B, Jun 2025) and Series D ($250M at $4.5B, Jan 2026).</span>
      </div>
      <div class="chain-link">&rarr;</div>
      <div class="chain-node">
        <b>Decagon</b>
        <span>Enterprise AI concierge platform; 100+ enterprise customers incl. Avis Budget Group and Deutsche Telekom, with a dedicated travel &amp; hospitality practice.</span>
      </div>
    </div>
    <p class="tsub" style="margin:16px 0 0;">Second thread: CEO <b>Dave Emerson</b> led Bain &amp; Company&rsquo;s global airline practice before joining Virgin &mdash; the Bain alumni network reaches the very top of this chart.</p>
  </div>

  <div class="notes">
    <h2>Notes for the Decagon pitch</h2>
    <ul>
      <li><b>Work the warm path first.</b> Ask BCV for a board-level introduction (Cotton, Murphy or Lawson) before any formal process exists &mdash; portfolio cross-introduction is standard practice, and it puts Decagon in the room ahead of an RFP.</li>
      <li><b>Your economic buyer is Andrew Cleary</b> (Chief Customer Officer &amp; CEO Velocity). He owns customer experience, Velocity and the contact centres &mdash; and technology, including the new Head of AI, sits inside his division. One decision chain, not two. Note the acronym trap: Paul Jones is also &ldquo;CCO&rdquo; (Commercial).</li>
      <li><b>The competition is build, not buy.</b> Virgin is hiring its own AI team (Head of AI, AI transformation lead, conversational AI designers) and announced an OpenAI collaboration in Nov 2025. Counter with time-to-value, enterprise CX proof in travel, and outcome-based pricing against the cost and risk of an in-house build.</li>
      <li><b>Voice objection is pre-answered.</b> Decagon Voice is powered by ElevenLabs&rsquo; voice models &mdash; Virgin gets best-in-class voice quality inside an enterprise concierge platform, without assembling the stack themselves.</li>
      <li><b>Frame for a Bain-heavy audience:</b> Emerson is an ex-Bain airline strategist and a former CCO himself &mdash; lead with containment rates, cost-to-serve and unit economics, not technology novelty.</li>
      <li class="muted">ELT roles verified against the official Virgin Australia leadership page, July 2026. The technology tier is assembled from iTnews reporting and Virgin job listings; the CIO&rsquo;s exact ELT reporting line post the March 2025 reshuffle is not publicly disclosed.</li>
    </ul>
    <p class="src">Sources: virginaustralia.com/about-us/leadership-team &middot; Virgin Australia newsroom (CEO appointment Mar 2025; OpenAI collaboration Nov 2025) &middot; iTnews (IT leadership; contact-centre conversational AI) &middot; CIO.com (Hogarth profile) &middot; Virgin Australia careers (Head of AI listing 509157, since removed) &middot; decagon.ai (Series B/C/D announcements; travel &amp; hospitality) &middot; elevenlabs.io/blog/decagon (voice partnership)</p>
  </div>
</div>
"""

html = html.replace("__FRAUNCES__", fraunces).replace("__GROTESK__", grotesk)
out = sp / "va-organogram.html"
out.write_text(html)
print(out, len(html))

# standalone build for GitHub Pages
head, body = html.split('<div class="wrap">', 1)
standalone = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
  '<meta name="robots" content="noindex">\n'
  + head + '\n</head>\n<body>\n<div class="wrap">' + body + '\n</body>\n</html>\n')
gh_out = sp / "index.html"
gh_out.write_text(standalone)
print(gh_out, len(standalone))
