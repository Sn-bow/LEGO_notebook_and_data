import pandas as pd
import matplotlib.pyplot as plt

colors_df = pd.read_csv('data/colors.csv')

# 고유한 색상의 총 갯수
color_count = colors_df["name"].nunique()

#  레고에서 불투명한 색상 대비 투명한 색상이 어느 정도 있는지
opaque_count = colors_df.groupby(by="is_trans").count()
# .value_counts() 메소드는 데이터프레임의 column(열) 의 갯수가 몆개인지 반환
opaque_count_value_counts = colors_df["is_trans"].value_counts()



# 레고 sets data frame
sets_df = pd.read_csv("data/sets.csv")
print(sets_df)


# 최초의 레고 세트가 출시된 연도와 이 세트의 이름은
for_the_first_time_set = sets_df.sort_values("year")
print(for_the_first_time_set)

# 레고는 운영 첫해에 얼마나 많은 제품을 팔았나
sell_lego = sets_df["year"].value_counts()[1949]
print(sell_lego)
# 조건에 따라 데이터를 필터링
sell_lego = sets_df[sets_df["year"] == 1949]
print(sell_lego)

# 부품 수가 가장 많은 상위 5개 레고 세트
many_num_parts_five_data = sets_df.sort_values(by="num_parts", ascending=False).head()
print(many_num_parts_five_data)



# 데이터 시각화

# 연도별에 따른 세트수
sets_by_year = sets_df.groupby('year').count()
print(sets_by_year["set_num"].head())
print(sets_by_year["set_num"].tail())

# 시각화
plt.plot(sets_by_year.index[:-2] ,sets_by_year["set_num"][:-2] )

# 연도별 테마수
## 연도별 테마수 평균값
sets_by_theme_mean = sets_df[["year", "theme_id", "num_parts"]].groupby("year").mean()
print(sets_by_theme_mean["theme_id"].head())
## 연도별 테마 총 수 (고유값)
sets_by_theme_agg = sets_df.groupby("year").agg({"theme_id" : pd.Series.nunique})
sets_by_theme_agg.rename(columns={"theme_id": "nr_themes"}, inplace=True) # column 명 변경
print(sets_by_theme_agg)

# 연도별로 출시된 테마 수를 선으로 표시 
# 데이터세트에 전체 달이 들어간 연도만 포함(1949~2019)
plt.plot(sets_by_theme_agg.index[:-2], sets_by_theme_agg["nr_themes"][:-2])