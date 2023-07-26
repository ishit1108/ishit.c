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
profile_image = Image.open('images/ishit_picture.jpg')
ccc1_image = Image.open('images/Fundamentals of Accelerated Computing with CUDA Python.jpg')
ccc2_image = Image.open('images/Fundamentals of Accelerated Computing with CUDA C++.jpg')
ccc3_image = Image.open('images/Accelerating Cuda C++ Application with Concurrent Streams.jpg')
ccc4_image = Image.open('images/Getting Started on AI with Jetson Nano.jpg')
ccc5_image = Image.open('images/STEM Connect Virtual Experience Program.jpg')
ccc6_image = Image.open('images/Artificial Intelligence.jpg')
ccc7_image = Image.open('images/Shakura Science Exchange Program.jpg')

ddd1_image = Image.open('images/Canadian Senior Mathematics Contest.jpg')
ddd2_image = Image.open('images/IEO International Rank Holder.jpg')
ddd3_image = Image.open('images/Bord Topper Computer Applications.jpg')
ddd4_image = Image.open('images/Bord Topper Mathmatics.jpg')

eee1_image = Image.open('images/F1inschools Time of Sports National Finals Research and Development Award.jpg')
eee2_image = Image.open('images/F1inschools Time of Sports National Finals Enterprise Portfolio Award.jpg')
eee3_image = Image.open('images/F1inschools Time of Sports Regional Finals Sponsorship and marketing Award.jpg')
eee4_image = Image.open('images/F1inschools Time of Sports Regional Finals Best Trainee Award.jpg')
eee5_image = Image.open('images/Techkriti Open School Championship (IIT Kanpur).jpg')

confidential = Image.open('images2/Classified2.png')
# eee6_image = Image.open(r'.\images\')
# eee7_image = Image.open(r'.\images\')
# eee8_image = Image.open(r'.\images\')

thapar_image = Image.open('images2/Thapar-University.jpg')
shri_ram_image = Image.open('images2/shri-ram-school.png')
shikshantar_image = Image.open('images2/shikshantar school.jpg')



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
        student, specializing in ML, AI, DL, and CV. 
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
        pp1, pp2, pp3 = st.columns([1, 20, 1])
        with pp1:
            st.empty()
        with pp3:
            st.empty()
        with pp2:
            st.write("---")
            st.write("Name: CC41")
            st.write("Age: 20")
            st.write("---")
            st.write("Add: ")
            #st.image(confidential)
            st.write("Tower 19, Flat 1001")
            st.write("\t Orchid Petals, Sohna Road")
            st.write("\t Sector 49, Gurgaon")
            st.write("\t pin code - 122018")
            st.write("\t Haryana, India")
            st.write("---")
            st.write("\t ph: +91 88265-64722")
            st.write(" mail: ishit.chy@gmail.com")



with teducation:
    with st.container():
        st.write("---")
        #st.image(confidential)
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
    projtabcv, projtabml, projtabrobo, projtabsw, projtabfs = st.tabs(['Computer Vision','AI/ML','Robotics','Software Development','Full-Stack/Applications'])
    with projtabcv:
        # Drone Based Surveillance System
        with st.container():
            with st.expander('Drone Based Surveillance System',False):
                st.write('[Github Link](https://github.com/ishit1108/Drone-Based-Surveillance-System)')
                dbss1, dbss2, dbss3 = st.columns([1,5,1])
                with dbss1:
                    st.empty()
                with dbss3:
                    st.empty()
                with dbss2:
                    st.write('''An autonomous camera drone is used to keep surveillance. 
                    This particular project is made for college campuses to keep a track on prohibited activities. 
                     All the prohibited activities are detected via various Computer Vision and Deep Learning Models.
                      ''')
                    st.write('')
                    st.write('Models Include:')
                    st.write('1. Smoking Detector (Cigarette, Vape, Weed, etc)')
                    st.write('2. Illegal Trespassing (Climbing over boundary fences)')
                    st.write('3. Illegal possession of weapons (Knife, Gun)')
                    st.write('4. Fire Detector (Forest fire, Building Fire)')
                    st.write('')
                    st.write('''We build an entire end-to-end application. 
                    For server nad database we used MongoDB.''')
                    st.write('''We experimented with various Image Enhancement Techniques such as Applying various filters, Edge Enhancement GAN (EEGAN), Super Resolution GAN (SRGAN) and finally we concluded with a mix of the various methods that we explored to get outstanding results on our models.''')
        # Nvidia JETBOT: Character Tracer
        with st.container():
            with st.expander('Nvidia Jetbot: Character Tracer',False):
                st.write('[Github Link](https://github.com/ishit1108/Nvidia_Jetbot-Character_Tracer)')
                dbss1, dbss2, dbss3 = st.columns([1,5,1])
                with dbss1:
                    st.empty()
                with dbss3:
                    st.empty()
                with dbss2:
                    st.write('''Build on Nvidia's JETBOT Platform, this robot can be maneuvered in the shape of any letter, digit or special character. Its special maneuverability originates from the extensive optical flow model training and tuning performed. Also features a follow
                    me mode that locks onto any object specified by the user and changes its position to maintain the relative distance from the target. It performs optical flow calculations by first identifying unique landmarks from each frame of the video input from the camera. Then 
                    it performs a keypoint matching to recognise the movement of the key-points. On detecting a change in the relative positioning of the keypoints, it moves accordingly to adjust for the targets movement. It can calculate vector that it needs to travel to negate the movement of the target through the process of camera and motor calibration. 
                      ''')

        # JETSON NANO: Smart Garbage Segregator
        with st.container():
            with st.expander('Jetson Nano: Smart Garbage Segregator',False):
                st.write('[Github Link](https://github.com/ishit1108/Garbage_Segregator-Jetson_Nano)')
                # dbss1, dbss2, dbss3 = st.columns([1,5,1])
                # with dbss1:
                #     st.empty()
                # with dbss3:
                #     st.empty()
                # with dbss2:
                #     st.write('''An autonomous camera drone is used to keep surveillance.
                #     This particular project is made for college campuses to keep a track on prohibited activities.
                #      All the prohibited activities are detected via various Computer Vision and Deep Learning Models.
                #       ''')
                #     st.write('')
                #     st.write('Models Include:')
                #     st.write('1. Smoking Detector (Cigarette, Vape, Weed, etc)')
                #     st.write('2. Illegal Trespassing (Climbing over boundary fences)')
                #     st.write('3. Illegal possession of weapons (Knife, Gun)')
                #     st.write('4. Fire Detector (Forest fire, Building Fire)')
                #     st.write('')
                #     st.write('''We build an entire end-to-end application.
                #     For server nad database we used MongoDB.''')
                #     st.write('''Special Image alignment and enhancement was performed
                #     before passing the drone footage to  the respective models''')
        # Smart AI Image Filtering and Augmentation Platform
        with st.container():
            with st.expander('Smart AI Image Filtering and Augmentation Platform',False):
                st.write('Work in Progress')
                # dbss1, dbss2, dbss3 = st.columns([1,5,1])
                # with dbss1:
                #     st.empty()
                # with dbss3:
                #     st.empty()
                # with dbss2:
                #     st.write('''An autonomous camera drone is used to keep surveillance.
                #     This particular project is made for college campuses to keep a track on prohibited activities.
                #      All the prohibited activities are detected via various Computer Vision and Deep Learning Models.
                #       ''')
                #     st.write('')
                #     st.write('Models Include:')
                #     st.write('1. Smoking Detector (Cigarette, Vape, Weed, etc)')
                #     st.write('2. Illegal Trespassing (Climbing over boundary fences)')
                #     st.write('3. Illegal possession of weapons (Knife, Gun)')
                #     st.write('4. Fire Detector (Forest fire, Building Fire)')
                #     st.write('')
                #     st.write('''We build an entire end-to-end application.
                #     For server and database we used MongoDB.''')
                #     st.write('''ESRGAN implementation for enhancing images''')
        # Face Recognition Attendance System
        with st.container():  #FRAS
            with st.expander('Face Recognition Attendance System',False):
                st.write('Work in Progress')
                # dbss1, dbss2, dbss3 = st.columns([1,5,1])
                # with dbss1:
                #     st.empty()
                # with dbss3:
                #     st.empty()
                # with dbss2:
                #     st.write('''An autonomous camera drone is used to keep surveillance.
                #     This particular project is made for college campuses to keep a track on prohibited activities.
                #      All the prohibited activities are detected via various Computer Vision and Deep Learning Models.
                #       ''')
                #     st.write('')
                #     st.write('Models Include:')
                #     st.write('1. Smoking Detector (Cigarette, Vape, Weed, etc)')
                #     st.write('2. Illegal Trespassing (Climbing over boundary fences)')
                #     st.write('3. Illegal possession of weapons (Knife, Gun)')
                #     st.write('4. Fire Detector (Forest fire, Building Fire)')
                #     st.write('')
                #     st.write('''We build an entire end-to-end application.
                #     For server nad database we used MongoDB.''')
                #     st.write('''Special Image alignment and enhancement was performed
                #     before passing the drone footage to  the respective models''')
        with st.container():
            with st.expander('Jetson Nano: ASL-Sign Language Detector', False):
                st.write('[Github Link](https://github.com/ishit1108/ASL_Sign_Language_Detector-Jetson_Nano)')

    with projtabml:
        # Drone Based Surveillance System - Hotspot Detection
        with st.container():
            with st.expander('Hire or Fire - Employability Score Predictor', False):
                st.write('[Github Link](https://github.com/ishit1108/Hire-or-Fire)')
        # Min-Max based Tic-Tac Toe
        with st.container():
            with st.expander('Min-Max based Tic-Tac Toe', False):
                st.write('[Github Link](https://github.com/ishit1108/Tic_Tac_Toe_Game-Min_Max_algorithm)')
    with projtabrobo:
        with st.container():
            with st.expander('Optical Flow - Face Following Camera', False):
                st.write('[Github Link](https://github.com/ishit1108/Optical_Flow_Face_Following_Camera)')
        with st.container():
            with st.expander('Nvidia Jetbot: Character Tracer',False):
                st.write('[Github Link](https://github.com/ishit1108/Nvidia_Jetbot-Character_Tracer)')
                dbss1, dbss2, dbss3 = st.columns([1,5,1])
                with dbss1:
                    st.empty()
                with dbss3:
                    st.empty()
                with dbss2:
                    st.write('''Build on Nvidia's JETBOT Platform, this robot can be maneuvered in the shape of any letter, digit or special character. Its special maneuverability originates from the extensive optical flow model training and tuning performed. Also features a follow
                    me mode that locks onto any object specified by the user and changes its position to maintain the relative distance from the target. It performs optical flow calculations by first identifying unique landmarks from each frame of the video input from the camera. Then 
                    it performs a keypoint matching to recognise the movement of the key-points. On detecting a change in the relative positioning of the keypoints, it moves accordingly to adjust for the targets movement. It can calculate vector that it needs to travel to negate the movement of the target through the process of camera and motor calibration. 
                      ''')

    with projtabsw:
        with st.container():
            with st.expander('Movie Ticket Booking System - Java', False):
                st.write('[Github Link](https://github.com/ishit1108/Java_Movie_Ticket_Booking_System)')
        # Min-Max based Tic-Tac Toe
        with st.container():
            with st.expander('OpenGL/C++ based game - Airplane Run', False):
                st.write('[Github Link](https://github.com/ishit1108/OenGL_CPP_Game-Airplane_Run)')
    with projtabfs:
        with st.container():
            with st.expander('QR Code/Barcode Scanning and Indexing app (Android)', False):
                st.write('[Github Link](https://github.com/ishit1108/QR_Barcode_Scanning_Android_App)')
        with st.container():
            with st.expander('Jobs for All - Website for inclusive hiring', False):
                st.write('[Github Link](https://github.com/ishit1108/Jobs_For_All)')
        with st.container():
            with st.expander('Book Exchange Android Application', False):
                st.write('[Github Link](https://github.com/ishit1108/BookExchange_Android_Application)')
        with st.container():
            with st.expander('Aroma Mocha - Website for a cafe', False):
                st.write('[Github Link](https://github.com/ishit1108/Aroma_Mocha-HTML_CSS_Website)')


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

    # with st.container():
    #     with st.expander('Extra-Curricular Activity Certificates',False):
    #         st.empty()

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