import requests
import streamlit as st
from PIL import Image
st.set_page_config(page_title="Ishit Choudhary", page_icon="👨‍🎓", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
profile_image = Image.open(r'images\ishit_picture.jpg')
ccc1_image = Image.open(r'images\Fundamentals of Accelerated Computing with CUDA Python.jpg')
ccc2_image = Image.open(r'images\Fundamentals of Accelerated Computing with CUDA C++.jpg')
ccc3_image = Image.open(r'images\Accelerating Cuda C++ Application with Concurrent Streams.jpg')
ccc4_image = Image.open(r'images\Getting Started on AI with Jetson Nano.jpg')
ccc5_image = Image.open(r'images\STEM Connect Virtual Experience Program.jpg')
ccc6_image = Image.open(r'images\Artificial Intelligence.jpg')
ccc7_image = Image.open(r'images\Shakura Science Exchange Program.jpg')

ddd1_image = Image.open(r'images\Canadian Senior Mathematics Contest.jpg')
ddd2_image = Image.open(r'images\IEO International Rank Holder.jpg')
ddd3_image = Image.open(r'images\Bord Topper Computer Applications.jpg')
ddd4_image = Image.open(r'images\Bord Topper Mathmatics.jpg')

eee1_image = Image.open(r'images\F1inschools Time of Sports National Finals Research and Development Award.jpg')
eee2_image = Image.open(r'images\F1inschools Time of Sports National Finals Enterprise Portfolio Award.jpg')
eee3_image = Image.open(r'images\F1inschools Time of Sports Regional Finals Sponsorship and marketing Award.jpg')
eee4_image = Image.open(r'images\F1inschools Time of Sports Regional Finals Best Trainee Award.jpg')
eee5_image = Image.open(r'images\Techkriti Open School Championship (IIT Kanpur).jpg')
# eee6_image = Image.open(r'.\images\')
# eee7_image = Image.open(r'.\images\')
# eee8_image = Image.open(r'.\images\')

thapar_image = Image.open(r'images2\Thapar-University.jpg')
shri_ram_image = Image.open(r'images2\shri-ram-school.png')
shikshantar_image = Image.open(r'images2\shikshantar school.jpg')



with st.container():
    col1, col2,colextra,col3,col4 = st.columns([1,7,1,3,1])
    with colextra:
        st.empty()
    with col1:
        st.empty()
    with col2:
        st.title('Ishit Choudhary')
        st.subheader('Computer Engineer')
        st.write('''I am a passionate and dedicated 4th year computer engineering 
        student at Thapar University, specializing in ML, AI, DL, and CV. 
        With hands-on project experience, I have honed my technical skills and witnessed 
        the transformative power of these fields. I thrive in collaborative environments, 
        bring a creative mindset to problem-solving, and aim to make a meaningful impact 
        by pushing the boundaries of technology. Explore my portfolio to see 
        the projects I\'ve undertaken and connect with me for exciting collaborations 
        in this ever-evolving domain.''')
    with col3:
        st.image(profile_image)
    with col4:
        st.empty()

st.write("---")
divcol1, divcol2, divcol3 = st.columns([1,5,1])
with divcol1:
    st.empty()
with divcol2:
    tpersonal, teducation, tprojects, tcertificate, tgit = st.tabs(['Personal','Education','Projects','Certificates','Get in touch'])
with divcol3:
    st.empty()

with tpersonal:
    with st.container():
        st.write("---")

with teducation:
    with st.container():
        st.write("---")
        st.subheader('Thapar Institute of Engineering and Technology, Patiala')
        #st.title()
        col1, col2 = st.columns([3,7])
        with col2:
            st.subheader('B.E. Computer Engineering (2020-2024)')
            st.write('CGPA (Out of 10): 9.28 ')
            st.write('CGPA (Out of 4) : 3.71')
        with col1:
            st.image(thapar_image)
    with st.container():
        st.write("---")
        st.subheader('The Shri Ram School, Aravali')
        #st.title()
        col1, col2 = st.columns([3,7])
        with col2:
            st.subheader('Senior Secondary (2018-2020)')
            st.write('ISC Boards (PCM-CS): 94.6%')
            st.write('Maths Board Topper (100%)')
            st.write('Computer Science Board Topper (100%)')
            #st.write('CGPA (Out of 4) : 3.71')
        with col1:
            st.image(shri_ram_image)
    with st.container():
        st.write("---")
        st.subheader('The Shri Ram School, Aravali')
        #st.title()
        col1, col2 = st.columns([3,7])
        with col2:
            st.subheader('Secondary School (2016-2018)')
            st.write('ICSE Boards: 96.7%')
            st.write('Maths Board Topper (100%)')
            st.write('Computer Science Board Topper (100%)')
            #st.write('CGPA (Out of 4) : 3.71')
        with col1:
            st.image(shri_ram_image)
    with st.container():
        st.write("---")
        st.subheader('Shikshantar School')
        #st.title()
        col1, col2 = st.columns([3,7])
        with col2:
            st.subheader('Secondary School (2006-2018)')
            # st.write('ISC Boards: 94.6%')
            # st.write('Maths Board Topper (100%)')
            # st.write('Computer Science Board Topper (100%)')
            #st.write('CGPA (Out of 4) : 3.71')
        with col1:
            st.image(shikshantar_image)

with tprojects:
    with st.container():
        st.write("---")

with tcertificate:
    with st.container():
        with st.expander('Course Certificates',False):
            ccc1, ccc2, ccc3, ccc4 = st.columns(4)
            with ccc1:
                st.image(ccc4_image)
                st.write('Getting Started on AI with Jetson Nano')
                st.write('March 28, 2023')
            with ccc2:
                st.image(ccc3_image)
                st.write('Accelerating Cuda C++ Application with Concurrent Streams')
                st.write('December 3, 2022')
            with ccc3:
                st.image(ccc2_image)
                st.write('Fundamentals of Accelerated Computing with CUDA C/C++')
                st.write('September 30, 2022')
            with ccc4:
                st.image(ccc1_image)
                st.write('Fundamentals of Accelerated Computing with CUDA Python')
                st.write('September 30, 2022')
            ccc5, ccc6, ccc7, ccc8 = st.columns(4)
            with ccc5:
                st.image(ccc5_image)
                st.write('STEM Connect Virtual Experience Program')
                st.write('January 30, 2022')
            with ccc6:
                st.image(ccc6_image)
                st.write('Artificial Intelligence')
                st.write('January 23, 2022')
            with ccc7:
                st.image(ccc7_image)
                st.write('Shakura Science Exchange Program')
                st.write('Japan Science and Technology Agency')
                st.write('April 2019')
            with ccc8:
                st.empty()

    with st.container():
        with st.expander('Academic Examination Certificates',False):
            ddd1, ddd2, ddd3, ddd4 = st.columns(4)
            with ddd1:
                st.image(ddd1_image)
                st.write('Canadian Senior Mathematics Contest')
                st.write('University of Waterloo')
                st.write('DISTINCTION')
                st.write('2019')
            with ddd2:
                st.image(ddd2_image)
                st.write('SOF International English Olympiad')
                st.write('International Rank Holder')
                st.write('2019')
            with ddd3:
                st.image(ddd3_image)
                st.write('ICSE Bord Topper Computer Applications')
                st.write('100% Marks')
                st.write('2018-2019')
            with ddd4:
                st.image(ddd4_image)
                st.write('ICSE Bord Topper Mathematics')
                st.write('100% Marks')
                st.write('2018-2019')

    with st.container():
        with st.expander('Competition Certificates',False):
            eee1, eee2, eee3, eee4 = st.columns(4)
            with eee1:
                st.image(eee1_image)
                st.write('F1inschools, Time of Sports, National Finals')
                st.write('Research and Development Award')
                st.write('2018-2019')
            with eee2:
                st.image(eee2_image)
                st.write('F1inschools, Time of Sports, National Finals')
                st.write('Enterprise Portfolio Award')
                st.write('2018-2019')
            with eee3:
                st.image(eee3_image)
                st.write('F1inschools, Time of Sports, Regional Finals')
                st.write('Sponsorship and Marketing Award')
                st.write('2018-2019')
            with eee4:
                st.image(eee4_image)
                st.write('F1inschools, Time of Sports, Regional Finals')
                st.write('Best Trainee Award')
                st.write('2018-2019')
            eee5, eee6, eee7, eee8 = st.columns(4)
            with eee5:
                st.image(eee5_image)
                st.write('Techkriti Open School Championship (IIT Kanpur)')
                st.write('Outstanding Performance Award')
                st.write('December 2018')
            with eee6:
                st.empty()
            with eee7:
                st.empty()
            with eee8:
                st.empty()

    with st.container():
        with st.expander('Extra-Curricular Activity Certificates',False):
            st.empty()

with tgit:
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/ishit.chy@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <input type="text" name="phone number" placeholder="Your phone number" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()