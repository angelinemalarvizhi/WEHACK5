import os
import math
import random
from datetime import datetime

import streamlit as st

# ============================================================
# AEGIS EDGE — QUALCOMM-STYLE ENVIRONMENTAL INTELLIGENCE UI
# Single-file Streamlit dashboard
#
# Run from:
#   C:\Users\amosj\Downloads\AegisEdge
#
#   $env:GOOGLE_MAPS_API_KEY="YOUR_KEY"
#   py -m streamlit run dashboard\app.py
#
# Google 3D Maps requires the appropriate Google Maps Platform
# APIs/billing to be enabled for the supplied key.
# ============================================================

st.set_page_config(
    page_title="AEGIS EDGE | Environmental Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Theme / global CSS
# -----------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #03070b;
    --panel: #071017;
    --panel2: #0a151d;
    --line: #17303a;
    --cyan: #19e6ff;
    --cyan2: #6af4ff;
    --green: #3ef0a5;
    --amber: #ffb74d;
    --red: #ff4d68;
    --purple: #b67cff;
    --text: #e9f8fb;
    --muted: #718992;
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 50% -10%, rgba(16,86,105,.18), transparent 35%),
        #03070b !important;
    color: var(--text);
    font-family: Inter, sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(3,7,11,.88) !important;
}

[data-testid="stToolbar"] { display:none; }

.block-container {
    padding: 0.65rem 1rem 1rem 1rem !important;
    max-width: 1900px !important;
}

.brand {
    display:flex;
    align-items:center;
    gap:12px;
    padding:4px 0 10px 0;
}

.logo {
    width:42px;
    height:42px;
    border:1px solid rgba(25,230,255,.55);
    border-radius:11px;
    display:grid;
    place-items:center;
    color:#19e6ff;
    font-size:22px;
    box-shadow:0 0 28px rgba(25,230,255,.12), inset 0 0 20px rgba(25,230,255,.06);
}

.brand-name {
    font-family:"Space Grotesk", sans-serif;
    font-size:20px;
    font-weight:800;
    letter-spacing:2.5px;
}

.brand-sub {
    color:#5e7780;
    font-size:8px;
    letter-spacing:2px;
    margin-top:2px;
}

.top-status {
    border:1px solid rgba(62,240,165,.25);
    background:rgba(62,240,165,.045);
    border-radius:999px;
    padding:7px 12px;
    color:#6ff2bb;
    font-size:9px;
    letter-spacing:1.5px;
    font-weight:700;
    text-align:center;
}

.section-label {
    color:#4d8b9b;
    font-size:8px;
    font-weight:800;
    letter-spacing:2px;
    text-transform:uppercase;
    margin:4px 0 7px 0;
}

.panel {
    background:
        linear-gradient(145deg, rgba(10,21,29,.98), rgba(5,12,17,.98));
    border:1px solid rgba(30,57,67,.85);
    border-radius:13px;
    padding:14px;
    box-shadow:0 12px 40px rgba(0,0,0,.25);
}

.metric {
    background:linear-gradient(145deg, rgba(10,22,29,.96), rgba(5,12,17,.98));
    border:1px solid rgba(30,57,67,.75);
    border-radius:12px;
    padding:13px 14px;
    min-height:90px;
}

.metric-label {
    color:#66818b;
    font-size:7px;
    font-weight:800;
    letter-spacing:1.7px;
}

.metric-value {
    font-family:"Space Grotesk", sans-serif;
    font-size:27px;
    line-height:1;
    font-weight:700;
    margin-top:9px;
}

.metric-note {
    color:#506973;
    font-size:7px;
    margin-top:7px;
}

.node {
    padding:11px 10px;
    border:1px solid #15303a;
    border-radius:10px;
    background:#071117;
    margin-bottom:8px;
}

.node-title {
    font-size:9px;
    font-weight:800;
    letter-spacing:.7px;
}

.node-sub {
    color:#5f7882;
    font-size:7px;
    margin-top:4px;
}

.badge {
    display:inline-block;
    padding:3px 7px;
    border-radius:999px;
    font-size:6px;
    font-weight:800;
    letter-spacing:1px;
}

.badge-red { color:#ff7183; background:rgba(255,77,104,.10); border:1px solid rgba(255,77,104,.25); }
.badge-amber { color:#ffc46e; background:rgba(255,183,77,.09); border:1px solid rgba(255,183,77,.23); }
.badge-green { color:#63f2b5; background:rgba(62,240,165,.08); border:1px solid rgba(62,240,165,.22); }

.alert {
    border-left:3px solid var(--red);
    background:linear-gradient(90deg, rgba(255,77,104,.08), rgba(255,77,104,.015));
    border-top:1px solid rgba(255,77,104,.18);
    border-right:1px solid rgba(255,77,104,.12);
    border-bottom:1px solid rgba(255,77,104,.12);
    border-radius:9px;
    padding:10px;
    margin:7px 0;
}

.alert-title {
    color:#ff7285;
    font-size:8px;
    font-weight:800;
    letter-spacing:1px;
}

.alert-body {
    color:#7f969e;
    font-size:7px;
    line-height:1.45;
    margin-top:4px;
}

.hardware {
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:9px 0;
    border-bottom:1px solid #12262f;
}

.hardware:last-child { border-bottom:0; }

.hardware-name {
    font-size:8px;
    font-weight:800;
}

.hardware-sub {
    color:#536d77;
    font-size:6px;
    margin-top:2px;
}

.small-status {
    color:#55efaa;
    font-size:6px;
    font-weight:800;
    letter-spacing:1px;
}

div[data-testid="stButton"] > button {
    background:#08151c !important;
    color:#9cb8c0 !important;
    border:1px solid #18343e !important;
    border-radius:8px !important;
    font-size:8px !important;
    font-weight:700 !important;
    min-height:34px !important;
}

div[data-testid="stButton"] > button:hover {
    border-color:#1ce5ff !important;
    color:#d9fbff !important;
    box-shadow:0 0 18px rgba(25,230,255,.10);
}

[data-testid="stSelectbox"] label,
[data-testid="stSlider"] label {
    color:#63808a !important;
    font-size:8px !important;
}

div[data-baseweb="select"] > div {
    background:#071117 !important;
    border-color:#18343e !important;
    color:#cce2e7 !important;
    font-size:8px !important;
}

hr {
    border-color:#142a33 !important;
}

.footer {
    color:#304c56;
    text-align:center;
    font-size:7px;
    letter-spacing:1.4px;
    padding:8px 0;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Data model
# -----------------------------
NODES = {
    "RIVER_01": {
        "name": "Chennai River Basin",
        "place": "Chennai, Tamil Nadu",
        "lat": 13.0827,
        "lng": 80.2707,
        "risk": 97.8,
        "hazard": "FLOOD",
        "color": "#ff4d68",
        "confidence": 95,
        "status": "CRITICAL",
        "details": "Rapid water-level rise, intense rainfall and high flow conditions.",
    },
    "FOREST_01": {
        "name": "Nilgiris Forest",
        "place": "Ooty / Nilgiris, Tamil Nadu",
        "lat": 11.4102,
        "lng": 76.6950,
        "risk": 93.5,
        "hazard": "WILDFIRE",
        "color": "#ff9a4d",
        "confidence": 95,
        "status": "CRITICAL",
        "details": "Thermal anomaly with smoke/gas indicators and elevated fire risk.",
    },
    "URBAN_01": {
        "name": "Chennai Urban Air",
        "place": "Central Chennai, Tamil Nadu",
        "lat": 13.0674,
        "lng": 80.2376,
        "risk": 100.0,
        "hazard": "AIR QUALITY",
        "color": "#b67cff",
        "confidence": 85,
        "status": "CRITICAL",
        "details": "High particulate concentration and elevated gas readings.",
    },
}

# -----------------------------
# Session state
# -----------------------------
if "selected_node" not in st.session_state:
    st.session_state.selected_node = "RIVER_01"

if "refresh_count" not in st.session_state:
    st.session_state.refresh_count = 0

if "map_mode" not in st.session_state:
    st.session_state.map_mode = "HYBRID"

# -----------------------------
# Header
# -----------------------------
h1, h2, h3 = st.columns([5, 2, 1.5])

with h1:
    st.markdown(
        """
        <div class="brand">
            <div class="logo">◈</div>
            <div>
                <div class="brand-name">AEGIS EDGE</div>
                <div class="brand-sub">AI ENVIRONMENTAL INTELLIGENCE SYSTEM</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with h2:
    st.markdown(
        '<div class="top-status">● EDGE SYSTEM LIVE</div>',
        unsafe_allow_html=True,
    )

with h3:
    st.markdown(
        f'<div style="text-align:right;color:#59727b;font-size:8px;padding-top:12px">'
        f'{datetime.now().strftime("%H:%M:%S")} IST<br>'
        f'<span style="font-size:6px">CYCLE {st.session_state.refresh_count:02d}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

# -----------------------------
# Toolbar
# -----------------------------
c1, c2, c3, c4, c5 = st.columns([1.5, 1.5, 1.5, 1.5, 3])

with c1:
    hazard_filter = st.selectbox(
        "HAZARD",
        ["ALL", "FLOOD", "WILDFIRE", "AIR QUALITY"],
        label_visibility="visible",
    )

with c2:
    region_filter = st.selectbox(
        "REGION",
        ["ALL", "CHENNAI", "NILGIRIS"],
        label_visibility="visible",
    )

with c3:
    map_mode = st.selectbox(
        "3D MAP MODE",
        ["HYBRID", "SATELLITE", "ROADMAP"],
        index=["HYBRID", "SATELLITE", "ROADMAP"].index(st.session_state.map_mode),
        label_visibility="visible",
    )
    st.session_state.map_mode = map_mode

with c4:
    if st.button("↻  REFRESH", use_container_width=True):
        st.session_state.refresh_count += 1
        st.rerun()

with c5:
    st.markdown(
        """
        <div style="text-align:right;padding-top:23px;color:#46626c;font-size:7px;letter-spacing:1.4px">
        TACTICAL ENVIRONMENTAL COMMAND SURFACE&nbsp;&nbsp;•&nbsp;&nbsp;LOCAL EDGE INFERENCE
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Top metrics
# -----------------------------
visible_nodes = list(NODES.values())

if hazard_filter != "ALL":
    visible_nodes = [n for n in visible_nodes if n["hazard"] == hazard_filter]

if region_filter != "ALL":
    visible_nodes = [
        n for n in visible_nodes
        if region_filter in n["place"].upper()
    ]

avg_risk = sum(n["risk"] for n in visible_nodes) / len(visible_nodes) if visible_nodes else 0
critical = sum(1 for n in visible_nodes if n["risk"] >= 90)

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.markdown(
        f'<div class="metric"><div class="metric-label">SYSTEM RISK INDEX</div>'
        f'<div class="metric-value" style="color:#ffb74d">{avg_risk:.1f}%</div>'
        f'<div class="metric-note">Multi-hazard fused score</div></div>',
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        f'<div class="metric"><div class="metric-label">ACTIVE THREATS</div>'
        f'<div class="metric-value" style="color:#ff4d68">{critical:02d}</div>'
        f'<div class="metric-note">Priority response queue</div></div>',
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        '<div class="metric"><div class="metric-label">SENSOR FABRIC</div>'
        '<div class="metric-value" style="color:#3ef0a5">03/03</div>'
        '<div class="metric-note">Telemetry synchronized</div></div>',
        unsafe_allow_html=True,
    )

with m4:
    st.markdown(
        '<div class="metric"><div class="metric-label">EDGE INFERENCE</div>'
        '<div class="metric-value" style="color:#19e6ff">LIVE</div>'
        '<div class="metric-note">Local decision layer</div></div>',
        unsafe_allow_html=True,
    )

with m5:
    st.markdown(
        '<div class="metric"><div class="metric-label">LATENCY TARGET</div>'
        '<div class="metric-value" style="color:#3ef0a5">LOW</div>'
        '<div class="metric-note">Event-driven response</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# -----------------------------
# Main three-column dashboard
# -----------------------------
left, center, right = st.columns([1.55, 5.6, 1.75], gap="small")

# -----------------------------
# LEFT: nodes + hardware
# -----------------------------
with left:
    st.markdown('<div class="section-label">Field Intelligence</div>', unsafe_allow_html=True)

    for node_id, node in NODES.items():
        selected = st.session_state.selected_node == node_id
        border = "rgba(25,230,255,.55)" if selected else "#15303a"
        glow = "box-shadow:0 0 20px rgba(25,230,255,.08);" if selected else ""

        st.markdown(
            f"""
            <div class="node" style="border-color:{border};{glow}">
                <div style="display:flex;justify-content:space-between;align-items:center">
                    <div class="node-title">{node_id}</div>
                    <span class="badge badge-red">{node["status"]}</span>
                </div>
                <div style="font-size:9px;font-weight:700;margin-top:6px">{node["name"]}</div>
                <div class="node-sub">{node["place"]}</div>
                <div style="display:flex;justify-content:space-between;margin-top:8px">
                    <span style="font-size:6px;color:#58727c">RISK</span>
                    <strong style="font-size:9px;color:{node["color"]}">{node["risk"]:.1f}%</strong>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            f"VIEW {node_id}",
            key=f"node_{node_id}",
            use_container_width=True,
        ):
            st.session_state.selected_node = node_id
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Edge Hardware Fabric</div>', unsafe_allow_html=True)

    hardware = [
        ("PYNQ-Z2", "Zynq-7000 edge gateway", "ACTIVE"),
        ("BASYS 3", "Artix-7 FPGA prototype", "READY"),
        ("RISK ENGINE", "Local multi-hazard inference", "RUNNING"),
        ("LOCAL BUFFER", "Offline telemetry queue", "READY"),
    ]

    for name, sub, status in hardware:
        st.markdown(
            f"""
            <div class="hardware">
                <div>
                    <div class="hardware-name">{name}</div>
                    <div class="hardware-sub">{sub}</div>
                </div>
                <div class="small-status">● {status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------
# CENTER: Google 3D map
# -----------------------------
with center:
    selected = NODES[st.session_state.selected_node]

    st.markdown(
        f"""
        <div style="position:relative;margin-bottom:7px">
            <div class="section-label">Drone / Photorealistic Intelligence View</div>
            <div style="font-family:'Space Grotesk';font-size:18px;font-weight:700">
                LIVE ENVIRONMENTAL THREAT SURFACE
            </div>
            <div style="color:#5c7781;font-size:7px;letter-spacing:1px;margin-top:3px">
                {selected["name"].upper()} • {selected["place"].upper()} •
                3D TERRAIN • SENSOR FUSION • EDGE DECISION
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    api_key = "AIzaSyA5gZfSAs74Ny2ziK3qRSVZgKFZEjL2duE"

    # Google 3D Maps HTML. Kept deliberately compact to avoid the
    # unterminated-triple-quote problem in the old dashboard.
    nodes_js = []
    for node_id, n in NODES.items():
        nodes_js.append(
            "{"
            f"id:'{node_id}',"
            f"name:'{n['name']}',"
            f"lat:{n['lat']},lng:{n['lng']},"
            f"risk:{n['risk']},hazard:'{n['hazard']}',"
            f"color:'{n['color']}'"
            "}"
        )

    nodes_literal = "[" + ",".join(nodes_js) + "]"

    map_html = """
<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#02060a;font-family:Arial,sans-serif}
#map{width:100%;height:100%;position:relative;overflow:hidden}
#map3d{width:100%;height:100%;display:block}
.hud{position:absolute;left:14px;top:14px;z-index:10;color:#dffbff;background:rgba(3,9,13,.82);border:1px solid rgba(31,74,84,.9);border-radius:9px;padding:9px 11px;backdrop-filter:blur(10px)}
.hud .k{font-size:7px;letter-spacing:1.6px;color:#69b5c4;font-weight:700}.hud .v{font-size:13px;font-weight:800;margin-top:3px}.hud .s{font-size:6px;letter-spacing:1px;color:#6e8992;margin-top:3px}
.controls{position:absolute;right:14px;top:14px;z-index:10;display:flex;flex-direction:column;gap:6px}.controls button{border:1px solid rgba(39,76,87,.95);background:rgba(3,10,14,.88);color:#b9d6dc;border-radius:7px;padding:8px 10px;cursor:pointer;font-size:11px}.controls button:hover{border-color:#1be5ff;color:#e7fcff}
.legend{position:absolute;left:14px;bottom:14px;z-index:10;background:rgba(3,9,13,.82);border:1px solid #1c3943;color:#89a4ac;border-radius:8px;padding:8px 10px;font-size:7px}.l{display:inline-flex;align-items:center;margin-right:10px}.dot{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:4px}
.status{position:absolute;right:14px;bottom:14px;z-index:10;color:#63f2b5;font-size:7px;letter-spacing:1px;background:rgba(3,15,11,.84);border:1px solid rgba(62,240,165,.28);border-radius:7px;padding:7px 9px}
#error{display:none;position:absolute;inset:0;z-index:30;place-items:center;background:radial-gradient(circle at center,rgba(15,36,46,.96),rgba(2,6,10,.99));color:#dffbff;text-align:center}.errbox{max-width:520px;padding:24px;border:1px solid #29444e;border-radius:14px;background:rgba(5,14,19,.96)}.errtitle{color:#ff6b7e;font-weight:800;letter-spacing:1px;font-size:14px}.errtext{color:#8ca7af;font-size:11px;line-height:1.6;margin-top:9px}
</style></head>
<body><div id="map">
<div id="error"><div class="errbox"><div class="errtitle">3D MAP CONNECTION FAILED</div><div class="errtext" id="errtext">Google Maps could not initialize.</div></div></div>
<div class="hud"><div class="k">AEGIS EDGE • TACTICAL 3D</div><div class="v">LIVE THREAT SURFACE</div><div class="s">CHENNAI / NILGIRIS • PHOTOREALISTIC 3D TERRAIN</div></div>
<div class="controls"><button id="home">⌂ HOME</button><button id="orbit">◉ ORBIT</button><button id="tilt">↕ TILT</button><button id="zoomIn">＋ ZOOM</button><button id="zoomOut">－ ZOOM</button></div>
<div class="legend"><span class="l"><span class="dot" style="background:#ff4d68"></span>FLOOD</span><span class="l"><span class="dot" style="background:#ff9a4d"></span>WILDFIRE</span><span class="l"><span class="dot" style="background:#b67cff"></span>AIR</span></div>
<div class="status">● EDGE SENSOR FABRIC ONLINE</div></div>
<script async src="https://maps.googleapis.com/maps/api/js?key=__KEY__&v=beta&libraries=maps3d&loading=async"></script>
<script>
const nodes=__NODES__; let map3d=null,orbiting=false,timer=null;
function showError(msg){document.getElementById("error").style.display="grid";document.getElementById("errtext").textContent=msg;}
async function init(){
 try{
  const {Map3DElement,Marker3DElement}=await google.maps.importLibrary("maps3d");
  map3d=new Map3DElement({center:{lat:13.0827,lng:80.2707,altitude:0},range:36000,tilt:62,heading:335,mode:"__MODE__",gestureHandling:"GREEDY"});
  map3d.id="map3d"; document.getElementById("map").prepend(map3d);
  for(const n of nodes){
   const marker=new Marker3DElement({position:{lat:n.lat,lng:n.lng,altitude:60},label:n.id+" • "+n.name+" • "+n.risk.toFixed(1)+"%",altitudeMode:"RELATIVE_TO_GROUND",extruded:true,sizePreserved:true,zIndex:Math.round(n.risk)});
   map3d.append(marker);
  }
  document.getElementById("home").onclick=()=>{map3d.center={lat:13.0827,lng:80.2707,altitude:0};map3d.range=36000;map3d.tilt=62;map3d.heading=335;};
  document.getElementById("tilt").onclick=()=>{map3d.tilt=map3d.tilt>=74?45:map3d.tilt+8;};
  document.getElementById("zoomIn").onclick=()=>{map3d.range=Math.max(4000,map3d.range*.72);};
  document.getElementById("zoomOut").onclick=()=>{map3d.range=Math.min(120000,map3d.range*1.35);};
  document.getElementById("orbit").onclick=()=>{orbiting=!orbiting;if(orbiting){timer=setInterval(()=>{map3d.heading=(map3d.heading+.45)%360;},50);}else if(timer){clearInterval(timer);timer=null;}};
 }catch(e){console.error(e);showError("Google 3D Maps returned an error: "+(e&&e.message?e.message:String(e)));}
}
let tries=0;const wait=setInterval(()=>{tries++;if(window.google&&google.maps&&google.maps.importLibrary){clearInterval(wait);init();}else if(tries>120){clearInterval(wait);showError("Google Maps did not load. Check the API key, Maps JavaScript API, billing, network connection, and browser console.");}},150);
</script></body></html>
"""


    if not api_key:
        st.error(
            "GOOGLE_MAPS_API_KEY is not set. In PowerShell run: "
            '$env:GOOGLE_MAPS_API_KEY="YOUR_KEY"'
        )
    else:
        safe_key = api_key.replace("&", "&amp;").replace('"', "&quot;")
        map_html = (
            map_html
            .replace("__KEY__", safe_key)
            .replace("__MODE__", map_mode)
            .replace("__NODES__", nodes_literal)
        )

        # Streamlit 1.56+ supports st.iframe directly and can render
        # an HTML string in an iframe. This avoids the deprecated
        # st.components.v1.html call.
        st.iframe(map_html, height=650)

# -----------------------------
# RIGHT: alerts + telemetry
# -----------------------------
with right:
    st.markdown('<div class="section-label">AI Priority Alerts</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="color:#5b747d;font-size:7px;margin-bottom:8px">EDGE-GENERATED RESPONSE QUEUE</div>',
        unsafe_allow_html=True,
    )

    alerts = [
        (
            "CRITICAL",
            "FLOOD RESPONSE REQUIRED",
            "RIVER_01 reports critical flood conditions in the Chennai River Basin.",
            "97.8%",
            "95%",
        ),
        (
            "CRITICAL",
            "WILDFIRE DETECTED",
            "FOREST_01 shows thermal, smoke and gas indicators consistent with elevated fire risk.",
            "93.5%",
            "95%",
        ),
        (
            "CRITICAL",
            "AIR QUALITY ALERT",
            "URBAN_01 reports severe particulate concentration and elevated gas levels.",
            "100%",
            "85%",
        ),
    ]

    for sev, title, body, risk, conf in alerts:
        st.markdown(
            f"""
            <div class="alert">
                <div class="alert-title">● {sev}</div>
                <div style="font-size:8px;font-weight:800;margin-top:5px">{title}</div>
                <div class="alert-body">{body}</div>
                <div style="color:#4f6972;font-size:6px;margin-top:7px">
                    RISK <b>{risk}</b> &nbsp;•&nbsp; CONFIDENCE <b>{conf}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-label" style="margin-top:15px">Live Telemetry</div>', unsafe_allow_html=True)

    telemetry = {
        "Water Level": ("4.82 m", "CRIT"),
        "Rainfall": ("82 mm/h", "CRIT"),
        "Flow Rate": ("184 m³/s", "CRIT"),
        "Soil Moisture": ("91%", "CRIT"),
        "Temperature": ("48.0 °C", "CRIT"),
        "Humidity": ("20%", "CRIT"),
        "PM2.5": ("210 µg/m³", "CRIT"),
        "PM10": ("280 µg/m³", "CRIT"),
    }

    rows = ""
    for k, (v, s) in telemetry.items():
        rows += (
            f"<div style='display:flex;justify-content:space-between;"
            f"padding:6px 0;border-bottom:1px solid #10242c;font-size:7px'>"
            f"<span style='color:#7d949c'>{k}</span>"
            f"<span style='color:#d4e5e9'>{v}</span>"
            f"<span style='color:#ff6377;font-size:6px;font-weight:800'>{s}</span>"
            f"</div>"
        )

    st.markdown(rows, unsafe_allow_html=True)

    st.markdown('<div class="section-label" style="margin-top:15px">Edge Decision</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="panel">
            <div style="font-size:7px;color:#54717b;letter-spacing:1px">DECISION MODE</div>
            <div style="color:#19e6ff;font-size:10px;font-weight:800;margin-top:5px">
                LOCAL / REAL-TIME
            </div>
            <div style="color:#5c747c;font-size:7px;line-height:1.5;margin-top:5px">
                High-value environmental events are prioritized at the edge before cloud transmission.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Bottom analytics
# -----------------------------
st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

a1, a2, a3 = st.columns([1.25, 1.25, 1.5])

with a1:
    st.markdown('<div class="panel"><div class="section-label">Threat Distribution</div>', unsafe_allow_html=True)
    for label, value, color in [
        ("FLOOD", 97.8, "#ff4d68"),
        ("WILDFIRE", 93.5, "#ff9a4d"),
        ("AIR QUALITY", 100.0, "#b67cff"),
    ]:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;color:#8098a0;font-size:7px;margin-top:9px">
                <span>{label}</span><b style="color:{color}">{value:.1f}%</b>
            </div>
            <div style="height:4px;background:#12252d;border-radius:5px;margin-top:4px">
                <div style="width:{min(value,100)}%;height:100%;background:{color};border-radius:5px;
                box-shadow:0 0 10px {color}"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

with a2:
    st.markdown('<div class="panel"><div class="section-label">AI Model Performance</div>', unsafe_allow_html=True)
    for label, value in [
        ("FLOOD MODEL", 95.2),
        ("WILDFIRE MODEL", 92.1),
        ("ANOMALY ENGINE", 94.8),
    ]:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;color:#8098a0;font-size:7px;margin-top:9px">
                <span>{label}</span><b style="color:#19e6ff">{value:.1f}%</b>
            </div>
            <div style="height:4px;background:#12252d;border-radius:5px;margin-top:4px">
                <div style="width:{value}%;height:100%;background:#19e6ff;border-radius:5px"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

with a3:
    st.markdown(
        """
        <div class="panel">
            <div class="section-label">Architecture Status</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <div style="border:1px solid #15313b;border-radius:8px;padding:9px">
                    <div style="font-size:6px;color:#59757e">SENSOR SIMULATION</div>
                    <div style="font-size:10px;color:#3ef0a5;font-weight:800;margin-top:5px">ONLINE</div>
                </div>
                <div style="border:1px solid #15313b;border-radius:8px;padding:9px">
                    <div style="font-size:6px;color:#59757e">EDGE RISK ENGINE</div>
                    <div style="font-size:10px;color:#3ef0a5;font-weight:800;margin-top:5px">ONLINE</div>
                </div>
                <div style="border:1px solid #15313b;border-radius:8px;padding:9px">
                    <div style="font-size:6px;color:#59757e">PYNQ-Z2</div>
                    <div style="font-size:10px;color:#19e6ff;font-weight:800;margin-top:5px">ACTIVE</div>
                </div>
                <div style="border:1px solid #15313b;border-radius:8px;padding:9px">
                    <div style="font-size:6px;color:#59757e">ARTIX-7</div>
                    <div style="font-size:10px;color:#19e6ff;font-weight:800;margin-top:5px">READY</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer">AEGIS EDGE • AI ENVIRONMENTAL INTELLIGENCE • PYNQ-Z2 • BASYS 3 ARTIX-7 • EDGE-FIRST ARCHITECTURE</div>',
    unsafe_allow_html=True,
)
 