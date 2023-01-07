import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!"

# st.write("DataFrame")

# df = pd.DataFrame(
#     np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
#     columns=['lat','lon'],
# )

# #st.table(df.style.highlight_max(axis=0))
# st.map(df)

#st.write("Display Image")

#st.write("interactive widgets")

# if st.checkbox("Show Image"):
#     img = Image.open("2023_Tsuki.png")
#     st.image(img, caption="Tsuki 2023", use_column_width=True)

# option = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は、", option, "です。"

# first = st.slider("第1主成分" , -5, 5, 0)
# "第1主成分：", first
# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1,11))
# )

# "あなたの好きな数字は、", option, "です。"



left_column,center_column, right_column = st.columns(3)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("Pushed!!")
    center_column.write("yeah!")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ内容を書く")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ内容を書く")
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

