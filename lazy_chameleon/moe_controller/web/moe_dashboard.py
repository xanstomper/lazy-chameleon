"""MoE WebView Dashboard."""
from __future__ import annotations
from typing import Any, Dict, List, Optional
import json
import time
import http.server
import threading
import logging

logger = logging.getLogger(__name__)


class MoEDashboard:
    def __init__(self, host: str = "0.0.0.0", port: int = 9191):
        self.host = host
        self.port = port
        self._server = None
        self._thread = None
        self._crawler = None
        self._controller = None
        self._param_gen = None
        self._running = False
        self._start_time = time.time()

    def attach_crawler(self, crawler):
        self._crawler = crawler

    def attach_controller(self, controller):
        self._controller = controller

    def attach_param_gen(self, param_gen):
        self._param_gen = param_gen

    def start(self):
        dash = self
        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/api/stats":
                    self.send_json(dash._get_stats())
                elif self.path == "/api/experts":
                    self.send_json(dash._get_experts())
                elif self.path == "/api/crawler":
                    self.send_json(dash._get_crawler_stats())
                elif self.path == "/":
                    self.send_html(dash._get_index_html())
                else:
                    self.send_response(404)
                    self.end_headers()
            def send_json(self, data):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(data, default=str).encode())
            def send_html(self, html):
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())
            def log_message(self, fmt, *args):
                pass
        self._server = http.server.HTTPServer((self.host, self.port), H)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()
        self._running = True
        logger.info(f"MoE Dashboard at http://{self.host}:{self.port}")

    def stop(self):
        if self._server:
            self._server.shutdown()
        self._running = False

    def is_running(self):
        return self._running

    def _get_stats(self) -> Dict:
        stats = {"status": "running", "uptime_s": round(time.time() - self._start_time, 1)}
        if self._controller:
            try:
                r = self._controller.get_full_report()
                stats["moe"] = r.get("expert_split", {})
            except Exception as e:
                stats["moe_error"] = str(e)
        if self._crawler:
            try:
                stats["crawler"] = self._crawler.get_stats()
            except Exception as e:
                stats["crawler_error"] = str(e)
        return stats

    def _get_experts(self) -> List:
        experts = []
        if self._controller:
            try:
                splitter = self._controller.splitter
                for eid, a in splitter._assignments.items():
                    experts.append({"id": eid, "role": a.role.value, "budget": a.compute_budget, "spec": a.specialization})
            except:
                pass
        return experts

    def _get_crawler_stats(self) -> Dict:
        if self._crawler:
            try:
                return self._crawler.get_stats()
            except:
                pass
        return {"status": "not_attached"}

    def _get_index_html(self) -> str:
        return """<!DOCTYPE html>
<html><head>
<title>Lazy Chameleon MoE</title>
<style>
body{font-family:monospace;background:#0a0a0a;color:#0f8;margin:20px}
h1{color:#0f8;border-bottom:1px solid #0f8}
h2{color:#0c6}
.card{background:#111;border:1px solid #0f8;border-radius:8px;padding:15px;margin:10px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
.stat{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #222}
.label{color:#888}
.value{color:#0f8;font-weight:bold}
.badge{background:#0f8;color:#000;padding:2px 8px;border-radius:4px}
pre{background:#000;padding:10px;border-radius:4px;overflow:auto;max-height:200px}
</style></head>
<body>
<h1>🦎 Lazy Chameleon MoE</h1>
<div class=grid>
  <div class=card><h2>Stats</h2><div id=stats>Loading...</div></div>
  <div class=card><h2>Experts</h2><div id=experts>Loading...</div></div>
  <div class=card><h2>Crawler</h2><div id=crawler>Loading...</div></div>
</div>
<div class=card><h2>Details</h2><pre id=detail>Select expert</pre></div>
<script>
setInterval(async()=>{
  let r=await(await fetch("/api/stats")).json();
  document.getElementById("stats").innerHTML=Object.entries(r).map(([k,v])=>`<div class=stat><span class=label>${k}</span><span class=value>${typeof v=="object"?JSON.stringify(v).slice(0,80):v}</span></div>`).join("");
},2000);
setInterval(async()=>{
  let r=await(await fetch("/api/experts")).json();
  document.getElementById("experts").innerHTML=r.slice(0,30).map(e=>`<div class=stat><span class=label>#${e.id}</span><span class=badge>${e.role}</span><span class=value>${e.spec}</span></div>`).join("");
},3000);
setInterval(async()=>{
  let r=await(await fetch("/api/crawler")).json();
  document.getElementById("crawler").innerHTML=Object.entries(r).map(([k,v])=>`<div class=stat><span class=label>${k}</span><span class=value>${v}</span></div>`).join("");
},4000);
</script>
</body></html>"""
