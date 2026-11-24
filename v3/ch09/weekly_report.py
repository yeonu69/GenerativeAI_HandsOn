"""9.6절 반복 작업 자동화: 월별 파일을 합쳐 보고서 한 장 만들기
안전한 자동화의 네 원칙: 원본은 읽기만 / 작은 표본으로 먼저 / 무엇을 했는지 기록 / 사람이 마지막에 확인
"""
import glob, os
import pandas as pd

# 0) 연습용 월별 파일 만들기 (처음 한 번만)
if not glob.glob("data/2026-*.csv"):
    os.makedirs("data", exist_ok=True)
    full = pd.read_csv("byeolbit2026.csv")
    for m, part in full.groupby("월"):
        part.to_csv("data/2026-%02d.csv" % m, index=False)

SAMPLE = False                     # True로 바꾸면 파일 두 개만으로 먼저 시험
files = sorted(glob.glob("data/2026-*.csv"))[: 2 if SAMPLE else None]

# 1) 읽고 합치기 (원본 파일은 고치지 않는다)
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
before = len(df)

# 2) 정리 규칙 적용
df["날씨"] = df["날씨"].replace({"맑움": "맑음"})
df = df[df["관객수"].notna() & (df["관객수"] <= df["좌석수"])]
removed = before - len(df)

# 3) 계산과 차트
order = ["월", "화", "수", "목", "금", "토", "일"]
week = df.groupby("요일")["관객수"].mean().reindex(order).round(1)
os.makedirs("report", exist_ok=True)
bars = "".join('<div style="display:flex;align-items:center;gap:8px"><span style="width:24px">%s</span><div style="background:#4A55A2;height:22px;width:%dpx"></div><span>%.1f명</span></div>' % (d, v * 6, v) for d, v in week.items())

# 4) 보고서 + 기록
html = """<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>별빛극장 주간 리포트</title></head>
<body style="font-family:sans-serif;max-width:720px;margin:20px auto">
<h1>별빛극장 요일별 한 회 평균 관객</h1>%s
<p style="color:#666">읽은 파일 %d개 · 합친 줄 %d줄 · 정리 규칙으로 뺀 줄 %d줄 · 수업용 가상 데이터</p></body></html>""" % (bars, len(files), before, removed)
open("report/report.html", "w", encoding="utf-8").write(html)
print("완료: report/report.html  (읽은 파일 %d, 뺀 줄 %d)" % (len(files), removed))
