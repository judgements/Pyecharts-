from pyecharts.charts import Bar, Timeline
import pandas as pd

df = pd.read_excel("C:\\Users\\LIUXIANG\\Desktop\\华师资料\\20华师\\【灰灰考研】19情况\\一志愿复试考生名单-教育信息技术协同创新中心.xlsx")
# print(df)

# 实例化Bar()对象
bar = Bar()
# 横轴标签
bar.add_xaxis(df["姓名"].tolist())
# 纵轴图例, 数据
bar.add_yaxis(df.columns[4], df["政治理论成绩"].tolist())
bar.add_yaxis(df.columns[5], df["外国语成绩"].tolist())

# 生成效果图
bar.render("temp.html")
