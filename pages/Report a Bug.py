from initialization import *
import time as t
import os
st.set_page_config(page_title="Chris Irag", page_icon="♿")

st.header("Report a Bug")

with st.form("my_form"):
    text = st.text_input("Bug Description")

    submitted = st.form_submit_button("Submit")

    if submitted and text != '':
        time = t.localtime()
        formatted_time = f"{time[0]}-{time[1]}-{time[2]} {time[3]}-{time[4]}-{time[5]}.txt"
        dir_path = "./pages/bugs/"
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, formatted_time)


        with open(file_path, 'w') as file:
            file.write(text)

        st.success("Submitted")

        with st.empty():
            for i in range(5):
                st.write(f"Refreshing in {5-i} seconds.")
                t.sleep(1)
            st.rerun()
    elif submitted:
        st.error("Please provide a bug description.")
    

