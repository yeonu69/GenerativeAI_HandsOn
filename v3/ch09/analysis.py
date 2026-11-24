"""9장 메인 실습: 「별빛극장」 상영 계획 분석 (코랩에서 셀마다 나누어 실행해도 됩니다)
데이터: byeolbit2026.csv (수업용 가상 데이터, 실수 3개가 숨어 있음)
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("byeolbit2026.csv")

# 1단계: 크기와 열 확인 (1,460줄, 12열이어야 함)
print("줄 수:", len(df), "열 수:", df.shape[1])
print(df.dtypes)
print("빈칸 수:\n", df.isna().sum())

# 2단계: 이상한 값 찾기 - 고치거나 지우기 전에 먼저 보기
odd = df[(df["관객수"] > df["좌석수"]) | df["관객수"].isna() | ~df["날씨"].isin(["맑음", "흐림", "비", "눈"])]
print(odd[["날짜", "시간대", "날씨", "관객수", "좌석수"]])

# 정리 규칙(사람이 정하고 기록함): 좌석 초과·빈칸은 빼고, '맑움'은 '맑음'으로 고친다
clean = df.copy()
clean["날씨"] = clean["날씨"].replace({"맑움": "맑음"})
clean = clean[clean["관객수"].notna() & (clean["관객수"] <= clean["좌석수"])]
print("정리 뒤 줄 수:", len(clean), "(뺀 줄:", len(df) - len(clean), ")")

# 3단계: 요일별 한 회 평균 관객 (월~일 순서, 세로축 0부터)
order = ["월", "화", "수", "목", "금", "토", "일"]
week = clean.groupby("요일")["관객수"].mean().reindex(order).round(1)
print(week)
plt.rcParams["font.family"] = "NanumGothic"   # 코랩에서 한글이 깨지면 나눔 글꼴을 설치하세요
week.plot.bar(ylim=(0, None), color="#4A55A2", title="요일별 한 회 평균 관객")
plt.ylabel("명"); plt.tight_layout(); plt.savefig("week.png"); plt.show()

# 4단계: 방학(1·2·7·8월)과 학기 중으로 나눠 다시 보기
clean["방학"] = clean["월"].isin([1, 2, 7, 8])
print(clean.groupby(["방학", "요일"])["관객수"].mean().unstack().reindex(columns=order).round(1))

# 한 줄 손계산 검증: 1월 1일 하루 총 관객
print("1월 1일 총 관객:", clean[clean["날짜"] == "2026-01-01"]["관객수"].sum())

# 짧은 실습: 기온과 관객(5~8월) - 한 덩어리 vs 나눠 보기
day = clean.groupby("날짜").agg(관객=("관객수", "sum"), 기온=("기온", "first"), 월=("월", "first"))
s = day[day["월"].between(5, 8)]
print("5~8월 전체 r =", round(s["관객"].corr(s["기온"]), 2))
for v, g in s.groupby(s["월"].isin([7, 8])):
    print("방학" if v else "학기 중", "r =", round(g["관객"].corr(g["기온"]), 2))
