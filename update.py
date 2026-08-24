import pandas as pd
import json

df = pd.read_excel(
    "data/预测性维修.xlsx",
    engine="openpyxl"
)

devices = []

for _, row in df.iterrows():

    health = 100

    health -= row["主轴跳动"] * 1000
    health -= row["主轴磨损"] * 500

    if health >= 85:
        risk = "低"
    elif health >= 70:
        risk = "中"
    else:
        risk = "高"

    devices.append({
        "name": row["设备名称"],
        "health": round(health,1),
        "risk": risk
    })

result = {
    "total": len(devices),
    "devices": devices
}

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=4
    )
