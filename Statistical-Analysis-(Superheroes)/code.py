# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)

data.head()

data["Gender"]=data["Gender"].replace("-","Agender")

gender_count=data["Gender"].value_counts()
gender_count

gender_count.plot.bar()



# --------------
#Code starts here
alignment=data["Alignment"].value_counts()
alignment

alignment.plot.pie()
plt.xlabel("Character Alignment")


# --------------
#Code starts here
sc_df=data[["Strength","Combat"]]
sc_df

sc_covariance=sc_df["Strength"].cov(sc_df["Combat"])
sc_covariance

sc_strength=sc_df["Strength"].std()
sc_strength

sc_combat=sc_df["Combat"].std()
sc_combat

sc_pearson=sc_covariance/(sc_strength*sc_combat)
sc_pearson

ic_df=data[["Intelligence","Combat"]]
ic_df

ic_covariance=ic_df["Intelligence"].cov(ic_df["Combat"])
ic_covariance
ic_intelligence=ic_df["Intelligence"].std()
ic_combat=ic_df["Combat"].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
ic_pearson


# --------------
#Code starts here

total_high=data["Total"].quantile(0.99)
total_high

super_best=data[data["Total"]>total_high]
super_best

super_best_names=list(super_best["Name"])
super_best_names


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(15,15))
data["Intelligence"].plot.box(ax=ax_1)
ax_1.set_title("Intelligence")
data["Speed"].plot.box(ax=ax_2)
ax_2.set_title("Speed")
data["Power"].plot.box(ax=ax_3)
ax_3.set_title("Power")
plt.show()


