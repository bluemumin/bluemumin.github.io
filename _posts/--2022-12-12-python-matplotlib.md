---
layout: post
title:  "python 그래프 축 설정 법"
subtitle:   "python 그래프 축 설정 법"
categories: Python
tags: Graph
comments: true
---

## python 그래프 축 설정 법에 대해서 아는대로 포스팅 합니다.


import matplotlib.pyplot as plt
import matplotlib as mpl
%matplotlib inline


#기본 설정

plt.rcParams['figure.figsize'] = (5,5) #그래프 사이즈 설정
plt.rcParams['figure.dpi'] = 72 #인치당 도트수(그림 구성 픽셀 수) #기본 100
plt.rcParams['lines.linewidth'] = 4 #선 굵기
plt.rcParams['lines.color'] = 'blue' #선 색깔
plt.rcParams['axes.grid'] = True #격자무늬 설정

plt.rcParams['savefig.dpi'] = 200 #저장시 도트 수
plt.rcParams['savefig.transparent'] = True #투명 배경 #기본 false

plt.rcParams['font.family'] = 'Dejavu Sans' #폰트 설정
plt.rcParams['font.size'] = 14 #폰트 크기



from matplotlib import rc

rc('figure', figsize = (5,5))
rc('lines', linewidth = 4)
rc('axes', grid = True)

rc('lines', linewidth = 2, color = 'r')
rc('savefig', dpi = 200, transparent = True)
rc('font', family = 'Denaju Sans', size = 14)

plt.savefig("my_square_function.png", transparent=True)

plt.rcParams


#폰트 설정

font = {'family' : 'Denaju Sans',
        'size' : 14,
        'weight' : 'bold'
       }

rc('font', **font)


from matplotlib import font_manager as fm

# font setting
font_setting0 = fm.FontProperties()
font_setting0.set_family('Dejavu Sans') # 'serif' 'sans-serif', 'cursive', 'fantasy', 'monospace' #폰트 스타일

font_setting0.set_size(20) #크기
font_setting0.set_style('normal') # 'normal', 'oblique', 'italic' #기울임 설정 등
font_setting0.set_weight('bold') #강조표시



fig, ax = plt.subplots(figsize=(5,3))

data = [10, 24, 30, 50, 40]
ax.plot(data)
ax.set_title("title", fontproperties=font_setting0)

plt.show()


# font setting
fontdict = {
    'family': 'serif', #스타일
    'size': 15, #크기
    'backgroundcolor': 'yellow', #뒤에 배경
    'color': 'blue', #글자색
    'weight': 'normal', #강조표시
    'verticalalignment': 'baseline', #베이스라인, 좌표가 텍스트 위, 아래, 센터
    'horizontalalignment': 'left' #좌표가 텍스트 왼쪽, 오른쪽, center
}

fig, ax = plt.subplots(figsize=(5,3))

data = [10, 24, 30, 50, 40]
ax.plot(data)
ax.set_title("title", fontdict=fontdict)

plt.suptitle("suptitle", fontdict=fontdict)
plt.subplots_adjust(top=0.7)
plt.show()


#색깔 설정
# cycler 수정
from cycler import cycler
plt.rc('axes', prop_cycle=(cycler(color=['r', 'g', 'b', 'y']) +
                           cycler(linestyle=['-', '--', ':', '-.'])))

#색깔 범위 barchart

fig, ax = plt.subplots(figsize=(4,4))

im = ax.scatter(dfb['DIS'], dfb['MEDV'], s=5, c=dfb['AGE'], cmap='jet', alpha=0.5)
ax.set_xlabel(labelb['DIS'])
ax.set_ylabel(labelb['MEDV'])

cbar = plt.colorbar(im, ax=ax[i], ticks=[15, 50, 60], format='%1.2e', drawedges=i)
cbar.set_label(labelb['AGE'])
plt.tight_layout(rect=(0, 0, 0.75, 1)) #위치 지정 기본은 0, 0, 1, 1 #left, bottom, right, top


# Add average annotate
arrowprops = {
    'arrowstyle': '->'
}
ax.annotate("average", (group_mean, 2.5), xytext=(125000, 2.5),
          color='green', fontfamily='serif', fontstyle='italic', fontsize=15,
          arrowprops=arrowprops)

plt.annotate("Beautiful point", xy=(px, py), xytext=(px-1.3,py+0.5),
                           color="green", weight="heavy", fontsize=14,
                           arrowprops={"facecolor": "lightgreen"})

#subplot

plt.subplot(131) #1행 3열 1,2,3
plt.bar(names, values)

plt.subplot(132)
plt.scatter(names, values)

plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')

# subplot(2,2,1)은 subplot(221)로 축약할 수 있습니다.
plt.subplot(2, 2, 1)  # 2 행 2 열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단
plt.plot(x, x)
plt.subplot(2, 2, 2)  # 2 행 2 열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
plt.plot(x, x**2)
plt.subplot(2, 2, 3)  # 2 행 2 열 크기의 격자 중 세 번째 부분 그래프 = 좌측 하단
plt.plot(x, x**3)
plt.subplot(2, 2, 4)  # 2 행 2 열 크기의 격자 중 네 번째 부분 그래프 = 우측 하단
plt.plot(x, x**4)
plt.show()

fig, ax = plt.subplots(2, 2) # 순서대로 row의 갯수, col의 갯수입니다. nrows=2, cols=2로 지정할 수도 있습니다.

# plot위치는 ax[row, col] 또는 ax[row][col]로 지정합니다.
ax[0, 0].plot(x, x)      # 2 행 2 열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단
ax[0, 1].plot(x, x**2)   # 2 행 2 열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
ax[1, 0].plot(x, x**3)   # 2 행 2 열 크기의 격자 중 세 번째 부분 그래프 = 좌측 하단
ax[1, 1].plot(x, x**4)   # 2 행 2 열 크기의 격자 중 네 번째 부분 그래프 = 우측 하단


grid = plt.GridSpec(2, 2)  # 2행 2열 크기의 격?자를 준비합니다.

ax1 = plt.subplot(grid[0, 0])  # 2행 2열 크기의 격자 중 첫 번째 부분 그래프 = 좌측 상단
ax2 = plt.subplot(grid[0, 1])  # 2행 2열 크기의 격자 중 두 번째 부분 그래프 = 우측 상단
ax3 = plt.subplot(grid[1, 0:]) # 2행 *1*열의 두 번째 부분 그래프 = 하단
                               # 범위를 [1, 0:]으로 설정하여 2행 전체를 지정함.


plt.figure(1)


# text

plt.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='blue', horizontalalignment="center")
plt.text(px - 0.08, py, "Beautiful point", ha="right", weight="heavy")
plt.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=50, color='gray')


ax.text(0, 1.5, "Square function\n$y = x^2$", fontsize=20, color='blue', horizontalalignment="center")
ax.text(px - 0.08, py, "Beautiful point", ha="right", weight="heavy")
ax.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=50, color='gray')

#범례

plt.legend(loc="best")
ax.legend(loc="best")

fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(6, 4))
fig.legend(loc="upper left", bbox_to_anchor=(0.8, 0.95))  # legend의 loc와 bbox_to_anchor를 다시 조정합니다.       
fig.tight_layout(rect=[0, 0, 0.8, 1])  # axes가 표현될 공간을 지정합니다. 


fig, ax = plt.subplots(constrained_layout=True)
plt.rcParams['figure.constrained_layout.use'] = True

#안되는 버전
fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(7, 4),
                        constrained_layout=True)  # 여기에 적용합니다.
fig.set_facecolor("lightgray")
axs = axes.ravel()

for i, ax in enumerate(axs, 1):
    R, G, B = np.random.random(), np.random.random(), np.random.random()
    color = [R, G, B]
    ax.set_aspect("equal")
    ax.plot(X, Y, "o-", c=color, label=f"plot {i}")

ax_center = fig.add_axes([0.23, 0.1, 0.5, 0.8])
ax_center.imshow(im_wm, alpha=0.3)
ax_center.axis("off")
    
fig.legend(loc="upper left", bbox_to_anchor=(1, 0.95))       

fig.savefig("45_tightlayout_9.png")

#되는 버전
fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(7, 4),
                        constrained_layout=True)
fig.set_facecolor("lightgray")
axs = axes.ravel()

handles = []  # 도형을 여기에 모읍니다. 
labels = []   # 레이블을 여기에 모읍니다.
for i, ax in enumerate(axs, 1):
    R, G, B = np.random.random(), np.random.random(), np.random.random()
    color = [R, G, B]
    ax.set_aspect("equal")
    handle = ax.plot(X, Y, "o-", c=color, label=f"plot {i}")
    handles.append(handle[0])  # 도형을 handles에 넣습니다.
    labels.append(f"plot {i}") # label을 labels에 넣습니다.

ax_center = fig.add_axes([0.23, 0.1, 0.5, 0.8])
ax_center.imshow(im_wm, alpha=0.3)
ax_center.axis("off")
    
# 범례를 여기에 답니다.
axs[2].legend(handles, labels, loc="upper left", bbox_to_anchor=(1, 1.05))

fig.savefig("45_tightlayout_10.png")



#축 설정

plt.xlabel('some') #x축 이름
plt.ylabel('numbers') #y축 이름

plt.axis([-10, 110, -10, 140]) #x축 범위 / y축 범위
plt.grid(True)

ax[0].grid(axis="both")

# ax[1] : x축에서만
ax[1].grid(axis="x")

# ax[2] : y축에서만
ax[2].grid(axis="y")

# ax[0] : major, minor 둘 다
ax[0].grid(axis="y", which="both")

# ax[1] : major만
ax[1].grid(axis="y", which="major")

# ax[2] : major만 + 여러 옵션
ax[2].grid(axis="y", which="major", color="r", ls=":", lw=0.5, alpha=0.5)


fig, ax = plt.subplots(figsize=(7,4))
sns.barplot(group_data, group_names)

ax.set_xlabel('Total Revenue')
ax.set_ylabel('Company', labelpad=20) #거리 지정 인자 이름
ax.set_title('Company Revenue',pad=12)

ax.set_xlim(75000, 150000) #축 범위 설정
ax.set_ylim(-10, 140)

ax.set_xticklabels(xlabels.astype('int'), rotation=45, 
                   horizontalalignment='right') #x축 라벨별 설정

ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines["left"].set_bounds(1, 3)

ax.spines["left"].set_position(("outward", 10))

axs[0].spines["left"].set_color("w")
axs[0].spines["bottom"].set_linewidth(2)
axs[0].spines["bottom"].set_color("w")


# ticks

ax.xaxis.set_ticks(np.arange(-2, 2, 1))

plt.minorticks_on()
ax.tick_params(axis='x', which='minor', bottom='off')

ax.xaxis.set_ticks([-2, 0, 1, 2])
ax.yaxis.set_ticks(np.arange(-5, 5, 1))
ax.yaxis.set_ticklabels(["min", -4, -3, -2, -1, 0, 1, 2, 3, "max"])

#y축 tick 설정
ax.yaxis.set_major_locator(MultipleLocator(1))    # major tick을 1 단위로 설정
ax.yaxis.set_major_formatter('{x:0.2f}')          # major tick format 지정 (오류가 나면 matplotlib upgrade)
ax.yaxis.set_minor_locator(MultipleLocator(0.5))  # minor tick을 0.5 단위로 지정

# y축 눈금 제거 (길이를 0으로 만들어서 안보이게)
ax.tick_params(axis="y", length=0)

----------------

with seaborn

plt.scatter(x, y, s=scale)

sns.scatterplot("bill_length_mm", "bill_depth_mm", hue="species", data=penguins, alpha=0.3, ax=axes[1])