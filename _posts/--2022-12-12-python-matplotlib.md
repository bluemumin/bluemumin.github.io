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

-----------------------------------


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


----------------------------------

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

-------------------------------------

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

-------------------------------------

----------------

with seaborn

plt.scatter(x, y, s=scale)

sns.scatterplot("bill_length_mm", "bill_depth_mm", hue="species", data=penguins, alpha=0.3, ax=axes[1])