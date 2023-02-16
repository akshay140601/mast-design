# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:18:07 2023

@author: fl9768
"""

import pandas as pd
import streamlit as st
import pickle
import re
from PIL import Image
from sectionproperties.analysis.section import Section
import sectionproperties.pre.library.steel_sections as steel_sections
import sectionproperties.pre.library.primitive_sections as sections

st.set_page_config(page_title="Mast design", layout="wide", page_icon = "sandvik logo.png")

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem; padding-bottom:0rem; padding-left:0.5rem; padding-right:1rem; margin: -1rem -1rem -1rem -1rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

pattern_style = """
    <style> 
        div.header {
        background: #0099ff;
        -webkit-clip-path: polygon(16% 0%, 83% 0%, 88% 100%, 100% 100%, 10% 100%);  
        clip-path: polygon(16% 0%, 83% 0%, 88% 100%, 100% 100%, 10% 100%);  
        font-size: 1.770833vw;  
        color: #fff;  
        text-align: center;
        margin: -1rem -1rem -1rem -1rem;
        }
    </style>
"""
st.markdown(pattern_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,10,1])
with col2:

    st.markdown("<div class = 'header'><h2 style = 'text-align: center; color: #fff; row-gap: 0rem'>MAST DESIGN AUTOMATION</h2></div>", unsafe_allow_html=True)
with col3:
    st.image("logo-sandvik.png")
    
hr_line_style = """
    <style>
        <hr style = "height: 10px; border: none; color: #0099ff; background-color: #0099ff;"/>
    </style>
"""
st.markdown("""<hr style = "height: 6px; border: none; color: #0099ff; background-color: #0099ff; margin: -0.3rem -1.5rem -1rem -1rem"/>""", unsafe_allow_html=True)

st.write("")
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,]')

feed_actuation = st.sidebar.selectbox("Feed Type", ("Cylinder feed", "Motor feed"))

download_style = """
    <style>
        div.stDownloadButton > button:first-child {
            background-color: #ff6d00;
            color: #fff;
            height: 3rem;
            width: 8rem;
            font-size: 20px;
            text-align: center;
            margin: -1rem;
            }
    </style>
"""

with st.sidebar:
    st.markdown("<h3 style='text-align: center'>IMPORTANT</h3>", unsafe_allow_html=True)
    st.write("1. Length values should be entered in inches")
    st.write("2. Force values should be entered in lbf")
    st.write("3. Stress and Young's Modulus values should be entered in psi")
    st.write("4. All inputs are mandatory. Do not use commas. Deflection is always in Loc. 5")
    st.write("5. If you encounter a 'TopologicalError' the entered geometry cannot be constructed. Please enter a valid geometry in that case")
    st.write("6. Click below button to download data of previous masts for reference")
    _,col,_ = st.columns(3)
    with col:
        with open("Previous Mast Data.xlsx", "rb") as file:
            st.markdown(download_style, unsafe_allow_html=True)
            btn = st.download_button("DOWNLOAD", file, file_name = "Existing Mast Data.xlsx")

if feed_actuation == "Cylinder feed":
    

    mast_height_img = Image.open('Mast height.png')
    st.image(mast_height_img, use_column_width=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns([4,4,1,1,1,1])
    
    input_label_size = """
        <style>
            div[class*="stTextInput"] label {
                font-size: 20px;
                }
            div[class*="stSelectbox"] label {
                font-size: 20px;
                }
        </style>
    """
    
    subheading_size = """
        <style>
            div[class*="stWrite"] label {
                font-size: 20px;
                }
            .css-pxxe24 {
            visibility: hidden;
            }
        </style>
    """
    
    with col1:
        st.write(input_label_size, unsafe_allow_html=True)
        mast_width = st.text_input("Mast width (in)")
        if mast_width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        st.write(input_label_size, unsafe_allow_html=True)
        mast_depth = st.text_input("Mast depth (in)")
        if mast_depth.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col3:
        # st.markdown("""
        #             <style>
        # .big-font {
        #     font-size:20px !important;
        # }
        # </style>
        # """, unsafe_allow_html=True)
    
        # st.markdown('<p class="big-font">Mast height(in)</p>', unsafe_allow_html=True)
        # st.write(input_label_size, unsafe_allow_html=True)
        st.write("")
        A = st.text_input("A (in)")
        if A.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        st.write("")
        B = st.text_input("B (in)")
        if B.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col5:
        st.write("")
        C = st.text_input("C (in)")
        if C.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col6:
        st.write("")
        D = st.text_input("D (in)")
        if D.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    st.write("")
        

# _,_,_,_,_,_,_,_,_,_,_,_,_, col, _,_,_,_,_,_,_,_,_,_,_,_,_ = st.columns(27)
# Next = col.button('Next')

# if Next:
#     if feed_actuation == 'Cylinder feed':

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h5 style='text-align: center'>C/S - 1 (Crown to mast rest)</h5>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h5 style='text-align: center'>C/S - 2 (Mast rest to table)</h5>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<h5 style='text-align: center'>C/S - 3 (Pivot region)</h5>", unsafe_allow_html=True)
    
    
    col1, col2, col3 = st.columns([1.2,1.2,1])
    with col1:
        cs1 = Image.open('cross section - 1.png')
        st.image(cs1, use_column_width=True)
        st.markdown("<h5 style='text-align: center'>Long member C/S</h5>", unsafe_allow_html=True)
        
    with col2:
        cs2 = Image.open('cross section - 2.png')
        st.image(cs2, use_column_width=True)
        st.markdown("<h5 style='text-align: center'>Long member with angle plate</h5>", unsafe_allow_html=True)
        
    with col3:
        cs3 = Image.open('cross section - 3.png')
        st.image(cs3, use_column_width=True)
        st.markdown("<h5 style='text-align: center'>Long member with pivot plates</h5>", unsafe_allow_html=True)
        
    col1, col2, col3, col4, col5, col6, col7 = st.columns([0.6,0.6,0.4,0.4,0.4,0.5,0.5])
    df = pd.read_excel("Long member cross sections.xlsx")
    df_2 = pd.read_excel("Angle plate cross sections.xlsx")
    with col1:
        width = st.selectbox('w', df.Width.unique())
        # width = st.text_input("w")
        # if width.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        height = st.selectbox('h', df.loc[df.Width==width]['Height'].unique())
        # thck = st.text_input("t")
        # if thck.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col2:
        thck = st.selectbox('t', df.loc[(df.Width==width) & (df.Height==height)]['Thickness'].unique())
        # height = st.text_input("h")
        # if height.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col3:
        angle_plate_width = st.selectbox('b', df_2.Breadth.unique())
        # if angle_plate_width.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        angle_plate_height = st.selectbox('d', df_2.loc[df_2.Breadth==angle_plate_width]['Depth'].unique())
        # angle_root_radius = st.text_input("rr")
        # if angle_root_radius.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col4:
        angle_plate_thck = st.selectbox('ta', df_2.loc[(df_2.Breadth==angle_plate_width) & (df_2.Depth==angle_plate_height)]['thickness'].unique())
        angle_toe_radius = st.text_input("rt")
        if angle_toe_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
    
    with col5: 
        angle_root_radius = st.text_input("rr")
        if angle_root_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
        
    with col6:
        plate_thck = st.text_input("pt")
        if plate_thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        dist_bottoms = st.text_input("db")
        if dist_bottoms.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col7:
        plate_height = st.text_input("ph")
        if plate_height.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5 = st.columns([1.2,2.1,1,1,1])
    
    with col1:
        bp1 = Image.open('bottom plate - 1.png')
        st.image(bp1, use_column_width=True)   
        
    with col2:
        bp2 = Image.open('bottom plate - 2.png')
        st.image(bp2, use_column_width=True)
        st.markdown("<h5 style='text-align: center'>Front view</h5>", unsafe_allow_html=True)
                
    with col3:
        ff_plate_thck = st.text_input("tp")
        if ff_plate_thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        ff_plate_length = st.text_input("L")
        if ff_plate_length.isalpha():
            st.write("Enter a valid number")
        else:
            pass    
            
    with col4:
        ff_plate_height = st.text_input("H")
        if ff_plate_height.isalpha():
            st.write("Enter a valid number")
        else:
            pass  
        
        washer_1_thck = st.text_input("Washer1 thickness")
        if washer_1_thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col5:
        washer_2_thck = st.text_input("Washer2 thickness")
        if washer_2_thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
    
    st.write("")

    col1, col2, col3, col4, col5, col6, col7 = st.columns([1.3,1,1,1,1,1,1])
    
    with col1:
        mast_weight = st.text_input("Mast Assembly Weight (kg)")
        if mast_weight.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        pulldown = st.text_input("Pulldown")
        if pulldown.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col3:
        pullback = st.text_input("Pullback")
        if pullback.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        torque = st.text_input("Rotary torque")
        if torque.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col5:
        extending = st.text_input("MRC Extending force")
        if extending.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col6:
        retracting = st.text_input("MRC Retracting force")
        if retracting.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col7:
        yield_limit = st.text_input("Material Yield stress")
        if yield_limit.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    st.write("")
        
    _,_,_,_,_,_,_,_,_,_,_,_,_, col, _,_,_,_,_,_,_,_,_,_,_,_,_ = st.columns(27)
    
    predict_style = """
        <style>
            div.stButton > button:first-child {
                background-color: #ff6d00;
                color: #fff;
                height: 3rem;
                width: 6rem;
                font-size: 20px;
                text-align: center;
                margin: -1rem -1rem -1rem -1rem;
                }
        </style>
    """
    
    with col:
        st.markdown(predict_style, unsafe_allow_html=True)
        predict = st.button('PREDICT')
    
    if predict:
        variables = [mast_width, mast_depth, A, B, C, D, dist_bottoms, plate_thck, plate_height, ff_plate_thck,
                     ff_plate_length, ff_plate_height, angle_toe_radius, 
                     angle_root_radius, mast_weight, pulldown, pullback, torque, extending, retracting, yield_limit,
                     washer_1_thck, washer_2_thck]
        
        proceed = 'Yes'
        for i in range(len(variables)):
            if (variables[i].isalpha() == True or len(variables[i]) == 0 or regex.search(variables[i]) != None):
                proceed = 'No'
                _,_,_, col, _,_,_ = st.columns(7)
                with col:
                    st.write("Please check all the inputs")
                    hide_st_style = """
                                <style>
                                #MainMenu {visibility: hidden;}
                                footer {visibility: hidden;}
                                header {visibility: hidden;}
                                </style>
                                """
                    st.markdown(hide_st_style, unsafe_allow_html=True)
                st.stop()
            
            else:
                proceed = 'Yes'
                
        if proceed == 'Yes':
            # variables = [mast_width, mast_depth, A, B, C, D, width, height, thck, r_out, dist_bottoms, plate_thck, plate_height,
            #              angle_plate_width, angle_plate_height, angle_plate_thck, angle_toe_radius, angle_root_radius]
            
            # for i in range(len(variables)):
            #     variables[i] = float(variables[i])
            
            mast_width = float(mast_width)
            mast_depth = float(mast_depth)
            A = float(A)
            B = float(B)
            C = float(C)
            D = float(D)
            width = float(width)
            height = float(height)
            thck = float(thck)
            r_out = 2*thck
            dist_bottoms = float(dist_bottoms)
            plate_thck = float(plate_thck)
            plate_height = float(plate_height)
            angle_plate_width = float(angle_plate_width)
            angle_plate_height = float(angle_plate_height)
            angle_plate_thck = float(angle_plate_thck)
            angle_toe_radius = float(angle_toe_radius)
            angle_root_radius = float(angle_root_radius)
            mast_weight = float(mast_weight)
            pulldown = float(pulldown)
            pullback = float(pullback)
            torque = float(torque)
            extending = float(extending)
            retracting = float(retracting)
            yield_limit = float(yield_limit)
            washer_1_thck = float(washer_1_thck)
            washer_2_thck = float(washer_2_thck)
            ff_plate_thck = float(ff_plate_thck)
            ff_plate_height = float(ff_plate_height)
            ff_plate_length = float(ff_plate_length)

            geometry = steel_sections.rectangular_hollow_section(d = height, b = width, t = thck, r_out = r_out, n_r = 30)
            geometry.create_mesh(mesh_sizes = [0.1])
            section = Section(geometry)
            section.calculate_geometric_properties()
            (zxx_01, zxx_02, _, _) = section.get_z()
            if (zxx_01 < zxx_02):
                section_1_modulus = zxx_01
            else:
                section_1_modulus = zxx_02
            
            geometry_1 = steel_sections.rectangular_hollow_section(d = width, b = height, t = thck, r_out = r_out, n_r = 30)
            plate_left = sections.rectangular_section(d = plate_height, b = plate_thck)
            plate_right = sections.rectangular_section(d = plate_height, b = plate_thck)
            plate_left = plate_left.shift_section(x_offset = -(plate_thck), y_offset = -(dist_bottoms))
            if (plate_thck or plate_height != 0):
                geom = geometry_1 + plate_left
            else:
                geom = geometry_1
            plate_right = plate_left.shift_section(x_offset = height + plate_thck, y_offset = 0)
            if (plate_thck or plate_height != 0):
                sec_geom = geom + plate_right
            else:
                sec_geom = geom
            sec_geom.create_mesh(mesh_sizes = [0.1])
            section_1 = Section(sec_geom)
            section_1.calculate_geometric_properties()
            (zxx_11, zxx_12, _, _) = section_1.get_z()
            if (zxx_11 < zxx_12):
                section_2_modulus = zxx_11
            else:
                section_2_modulus = zxx_12
                
            geometry_2 = steel_sections.rectangular_hollow_section(d = height, b = width, t = thck, r_out = r_out, n_r = 30)
            angle = steel_sections.angle_section(d = angle_plate_width, b = angle_plate_height, t = angle_plate_thck, 
                                              r_r = angle_root_radius, r_t = angle_toe_radius, n_r = 30)
            angle = angle.rotate_section(270, [0,0])
            angle = angle.shift_section(x_offset = -(angle_plate_thck), y_offset = height + angle_plate_thck)
            if (angle_plate_height and angle_plate_width != 0):
                section_geometry = geometry_2 + angle
            else:
                section_geometry = geometry_2
            section_geometry.create_mesh(mesh_sizes = [0.1])
            section_2 = Section(section_geometry)
            section_2.calculate_geometric_properties()
            (zxx_21, zxx_22, _, _) = section_2.get_z()
            if (zxx_21 < zxx_22):
                section_3_modulus = zxx_21
            else:
                section_3_modulus = zxx_22
                
            # st.write(section_1_modulus)
            # st.write(section_3_modulus)
            # st.write(section_2_modulus) 
            
            # Retract Prediction
            retract = open("retracting_xgb.pkl","rb")
            retract_regressor = pickle.load(retract)       
            retract_list = [retracting, section_1_modulus, D]
            X_test = pd.DataFrame([retract_list], columns = ['retracting force', 'section modulus (in^3)', 'Overhang (in)'])
            pass_data = X_test[['retracting force', 'section modulus (in^3)', 'Overhang (in)']]
            retract_prediction = retract_regressor.predict(pass_data)
            retract_prediction_print = retract_prediction.item()
            retract_prediction_print = int(retract_prediction_print)
            retract_variation = 500
            retract_prediction_print_LL = str(retract_prediction_print - retract_variation)
            retract_prediction_print_UL = retract_prediction_print + retract_variation
            yield_limit_check = 0.6*yield_limit
            if retract_prediction_print_UL<yield_limit_check:
                retract_safe = 'Yes'
            else:
                retract_safe = 'No'
            retract_prediction_print_UL = str(retract_prediction_print_UL)
            
            # Just about to lift prediction
            just_lift_regressor = pickle.load(open("just_lift_stack.pkl","rb"))
            mrc_pivot_overhang = C + D
            just_lift_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_prediction = just_lift_regressor.predict(pass_data)
            just_lift_prediction_print = just_lift_prediction.item()
            just_lift_prediction_print = int(just_lift_prediction_print)
            just_lift_variation = 1000
            just_lift_prediction_print_LL = str(just_lift_prediction_print - just_lift_variation)
            just_lift_prediction_print_UL = just_lift_prediction_print + just_lift_variation
            if just_lift_prediction_print_UL<yield_limit_check:
                just_lift_safe = 'Yes'
            else:
                just_lift_safe = 'No'
            just_lift_prediction_print_UL = str(just_lift_prediction_print_UL)
                
            # Just about to lift deflection prediction
            just_lift_deflection_regressor = pickle.load(open("just_lift_stack_deflection.pkl","rb"))
            just_lift_deflection_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_deflection_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_deflection_prediction = just_lift_deflection_regressor.predict(pass_data)
            just_lift_deflection_prediction_print = float('%.3f'%(just_lift_deflection_prediction.item()))
            just_lift_def_variation = 0.5
            just_lift_deflection_prediction_print_LL = float('%.3f'%(just_lift_deflection_prediction_print - just_lift_def_variation))
            if just_lift_deflection_prediction_print_LL < 0:
                just_lift_deflection_prediction_print_LL = 0
            else:
                just_lift_deflection_prediction_print_LL = just_lift_deflection_prediction_print_LL
            just_lift_deflection_prediction_print_UL = float('%.3f'%(just_lift_deflection_prediction_print + just_lift_def_variation))
            if just_lift_deflection_prediction_print_UL < just_lift_def_variation:
                just_lift_deflection_prediction_print_UL = just_lift_def_variation
            else:
                just_lift_deflection_prediction_print_UL = just_lift_deflection_prediction_print_UL
            just_lift_deflection_prediction_print_LL = str(just_lift_deflection_prediction_print_LL)
            just_lift_deflection_prediction_print_UL = str(just_lift_deflection_prediction_print_UL)
        
            # Horizontal tramming prediction
            hor_tram_regressor = pickle.load(open("hor_tram_stack.pkl","rb"))
            hor_tram_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_prediction = hor_tram_regressor.predict(pass_data)
            hor_tram_prediction_print = hor_tram_prediction.item()
            hor_tram_prediction_print = int(hor_tram_prediction_print)
            hor_tram_variation = 800
            hor_tram_prediction_print_LL = str(hor_tram_prediction_print - hor_tram_variation)
            hor_tram_prediction_print_UL = hor_tram_prediction_print + hor_tram_variation
            if hor_tram_prediction_print_UL<yield_limit_check:
                hor_tram_safe = 'Yes'
            else:
                hor_tram_safe = 'No'
            hor_tram_prediction_print_UL = str(hor_tram_prediction_print_UL)
                
            # Horizontal tramming deflection prediction
            hor_tram_def_regressor = pickle.load(open("hor_tram_stack_deflection.pkl","rb"))
            hor_tram_def_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_def_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_def_prediction = hor_tram_def_regressor.predict(pass_data)
            hor_tram_def_prediction_print = float('%.3f'%(hor_tram_def_prediction.item()))
            hor_tram_def_variation = 0.35
            hor_tram_def_prediction_print_LL = float('%.3f'%(hor_tram_def_prediction_print - hor_tram_def_variation))
            if hor_tram_def_prediction_print_LL < 0:
                hor_tram_def_prediction_print_LL = 0
            else:
                hor_tram_def_prediction_print_LL = hor_tram_def_prediction_print_LL
            hor_tram_def_prediction_print_UL = float('%.3f'%(hor_tram_def_prediction_print + hor_tram_def_variation))
            if hor_tram_def_prediction_print_UL < hor_tram_def_variation:
                hor_tram_def_prediction_print_UL = hor_tram_def_variation
            else:
                hor_tram_def_prediction_print_UL = hor_tram_def_prediction_print_UL
            hor_tram_def_prediction_print_LL = str(hor_tram_def_prediction_print_LL)
            hor_tram_def_prediction_print_UL = str(hor_tram_def_prediction_print_UL)
                
            # Extending prediction
            extending_regressor = pickle.load(open("extending_stack.pkl","rb"))
            extending_list = [extending, section_2_modulus, mast_depth, section_3_modulus]
            X_test = pd.DataFrame([extending_list], columns = ['extendingforce', 'Sectionmodulus', 'Mastdepth', 'Sectionmodulus2'])
            pass_data = X_test[['extendingforce', 'Sectionmodulus', 'Mastdepth', 'Sectionmodulus2']]
            extending_prediction = extending_regressor.predict(pass_data)
            extending_prediction_print = extending_prediction.item()
            extending_prediction_print = int(extending_prediction_print)
            extending_variation = 1100
            extending_prediction_print_LL = str(extending_prediction_print - extending_variation)
            extending_prediction_print_UL = extending_prediction_print + extending_variation
            if extending_prediction_print_UL<yield_limit_check:
                extending_safe = 'Yes'
            else:
                extending_safe = 'No'
            extending_prediction_print_UL = str(extending_prediction_print_UL)
            
            # Pulldown - Cylinder prediction
            pulldown_regressor = pickle.load(open("pulldown_cylinder_stack.pkl","rb"))
            pulldown_list = [pulldown*1.2, torque*1.35, ff_plate_thck, ff_plate_height, ff_plate_length, washer_1_thck, washer_2_thck]
            X_test = pd.DataFrame([pulldown_list], columns = ['Pulldownload', 'Rotation', 'FFthickness', 'FFheight', 'Distance', 'Washer1thck',
                                                              'Washer2thck'])
            pass_data = X_test[['Pulldownload', 'Rotation', 'FFthickness', 'FFheight', 'Distance', 'Washer1thck', 'Washer2thck']]
            pulldown_prediction = pulldown_regressor.predict(pass_data)
            pulldown_prediction_print = pulldown_prediction.item()
            pulldown_prediction_print = int(pulldown_prediction_print)
            pulldown_variation = 850
            pulldown_prediction_print_LL = str(pulldown_prediction_print - pulldown_variation)
            pulldown_prediction_print_UL = pulldown_prediction_print + pulldown_variation
            if pulldown_prediction_print_UL<yield_limit_check:
                pulldown_safe = 'Yes'
            else:
                pulldown_safe = 'No'
            pulldown_prediction_print_UL = str(pulldown_prediction_print_UL)
            
            # Pullback prediction
            pullback_regressor = pickle.load(open("pullback_lr.pkl", "rb"))
            pullback_list = [pullback*1.2, torque*1.35, section_1_modulus]
            X_test = pd.DataFrame([pullback_list], columns = ['Pullbackload', 'Rotation', 'Sectionmodulus'])
            pass_data = X_test[['Pullbackload', 'Rotation', 'Sectionmodulus']]
            pullback_prediction = pullback_regressor.predict(pass_data)
            pullback_prediction_print = int(pullback_prediction.item())
            pullback_variation = 750
            pullback_prediction_print_LL = str(pullback_prediction_print - pullback_variation)
            pullback_prediction_print_UL = pullback_prediction_print + pullback_variation
            if pullback_prediction_print_UL<yield_limit_check:
                pullback_safe = 'Yes'
            else:
                pullback_safe = 'No'
            pullback_prediction_print_UL = str(pullback_prediction_print_UL)
            
            #Code for remaining models
            
            data = [['Mast Horizontal & MRC Retracting', str(1), retract_prediction_print_LL + ' - ' + retract_prediction_print_UL, '-', retract_safe], 
                    ['Just about to lift (1.1G Lift Factor)', str(3), just_lift_prediction_print_LL + ' - ' + just_lift_prediction_print_UL, just_lift_deflection_prediction_print_LL + ' - ' + just_lift_deflection_prediction_print_UL, just_lift_safe],
                    ['Horizontal Tramming (1.5G Vertical Load)', str(1), hor_tram_prediction_print_LL + ' - ' + hor_tram_prediction_print_UL, hor_tram_def_prediction_print_LL + ' - ' + hor_tram_def_prediction_print_UL, hor_tram_safe], 
                    ['Mast vertical & MRC Extending', str(2), extending_prediction_print_LL + ' - ' + extending_prediction_print_UL, '-', extending_safe],
                    ['Vertical Drilling (120% Pulldown and 135% Torque)', str(4), pulldown_prediction_print_LL + ' - ' + pulldown_prediction_print_UL, '-', pulldown_safe],
                    ['Vertical Drilling (120% Pullback and 135% Torque)', str(6), pullback_prediction_print_LL + ' - ' + pullback_prediction_print_UL, '-', pullback_safe]]
            df = pd.DataFrame(data, columns = ['Load case', 'Loc. No.', 'Stress', 'Deflection', 'Compliant?'])
            def color_unsafe(val):
                color = 'red' if val == 'No' else 'green'
                return f'background-color: {color}'
            
            df = df.style.applymap(color_unsafe, subset = ['Compliant?'])
            
            st.markdown("<h3 style='text-align: center'>Static compliance</h3>", unsafe_allow_html=True)
            st.write("")
            
            col1, col2 = st.columns(2)
            with col1:
                sf = Image.open('Mast static failure locations.png')
                st.image(sf, use_column_width=True)
                
            with col2:
                st.table(df)
                
            #Code for fatigue models and cumulative damage calculation
            
            m_160 = 5
            m_90 = 3
            A_160 = (160**m_160)*2000000      #FAT 160 calculated for 2E+6 number of cycles
            A_90 = (90**m_90)*2000000
            oc = 64000          #Number of occurences for mast raising cycle
            # asr_160 = int(math.exp((1/m_160) * math.log(A_160/oc)))     #Allowable stress range for the 
            # asr_90 = int(math.exp((1/m_90) * math.log(A_90/oc)))
            
            
            #Location number 1
            
            #Just about to lift - Loc - 1 prediction
            
            just_lift_loc_1_regressor = pickle.load(open("just_lift_loc_1_xgb.pkl", "rb"))
            just_lift_loc_1_list = [mast_weight*1.1, section_2_modulus, mast_depth, mrc_pivot_overhang]
            X_test = pd.DataFrame([just_lift_loc_1_list], columns = ['Mastweight', 'Sectionmodulus', 'Mastdepth', 'Overhang'])
            pass_data = X_test[['Mastweight', 'Sectionmodulus', 'Mastdepth', 'Overhang']]
            just_lift_loc_1_prediction = just_lift_loc_1_regressor.predict(pass_data)
            just_lift_loc_1_prediction_print = int(just_lift_loc_1_prediction.item())
            
            #Extending - Loc - 1 prediction
            
            extending_loc_1_regressor = pickle.load(open("extending_loc_1_stack.pkl", "rb"))
            extending_loc_1_list = [extending, section_2_modulus, mast_depth]
            X_test = pd.DataFrame([extending_loc_1_list], columns = ['Extendingforce', 'Sectionmodulus', 'Mastdepth'])
            pass_data = X_test[['Extendingforce', 'Sectionmodulus', 'Mastdepth']]
            extending_loc_1_prediction = extending_loc_1_regressor.predict(pass_data)
            extending_loc_1_prediction_print = int(extending_loc_1_prediction.item())
            
            wsr_loc_1 = extending_loc_1_prediction_print - just_lift_loc_1_prediction_print
            wsr_loc_1_mpa = int(wsr_loc_1/145)
            n_loc_1 = A_160/(wsr_loc_1_mpa**m_160)
            cd_loc_1 = float(oc/n_loc_1)
            cd_loc_1_print = '%.2f'%cd_loc_1
            cd_loc_1_variation = 0.07
            if cd_loc_1 < 0.07:
                cd_loc_1_LL = str(0)
            else:
                cd_loc_1_LL = cd_loc_1 - 0.07
                cd_loc_1_LL = str('%.2f'%cd_loc_1_LL)
                
            cd_loc_1_UL = cd_loc_1 + 0.07
            
            if cd_loc_1_UL > 1:
                loc_1_safe = "No"
            else:
                loc_1_safe = "Yes"
                
            cd_loc_1_UL = str('%.2f'%cd_loc_1_UL)
            
            #Location number 2
            
            #Retracting - Loc - 2 prediction
            
            
            #Extending - Loc - 2 prediction
            
            
            data_fatigue = [["Mast Raising-Lowering Cycle", str(1) + ' (Material stress)', cd_loc_1_LL + '-' + cd_loc_1_UL, loc_1_safe]]
            df_fatigue = pd.DataFrame(data_fatigue, columns = ['Cycle', 'Loc. No.', 'Cumulative Damage', 'Compliant?'])
            df_fatigue = df_fatigue.style.applymap(color_unsafe, subset = ['Compliant?'])
            
            st.write("")
            st.markdown("<h3 style='text-align: center'>Fatigue compliance</h3>", unsafe_allow_html=True)
            st.write("")
            
            col1, col2 = st.columns(2)
            with col1:
                ff = Image.open('Mast fatigue failure locations.png')
                st.image(ff, use_column_width=True)
                
            with col2:
                st.table(df_fatigue)
                
            

elif feed_actuation == 'Motor feed':
    
    mast_height_img = Image.open('Mast height.png')
    st.image(mast_height_img, use_column_width=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns([4,4,1,1,1,1])
    
    input_label_size = """
        <style>
            div[class*="stTextInput"] label {
                font-size: 20px;
                }
            div[class*="stSelectbox"] label {
                font-size: 20px;
                }
        </style>
    """
    
    subheading_size = """
        <style>
            div[class*="stWrite"] label {
                font-size: 20px;
                }
            .css-pxxe24 {
            visibility: hidden;
            }
        </style>
    """
    
    with col1:
        st.write(input_label_size, unsafe_allow_html=True)
        mast_width = st.text_input("Mast width (in)")
        if mast_width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        st.write(input_label_size, unsafe_allow_html=True)
        mast_depth = st.text_input("Mast depth (in)")
        if mast_depth.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col3:
        # st.markdown("""
        #             <style>
        # .big-font {
        #     font-size:20px !important;
        # }
        # </style>
        # """, unsafe_allow_html=True)
    
        # st.markdown('<p class="big-font">Mast height(in)</p>', unsafe_allow_html=True)
        # st.write(input_label_size, unsafe_allow_html=True)
        st.write("")
        A = st.text_input("A (in)")
        if A.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        st.write("")
        B = st.text_input("B (in)")
        if B.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col5:
        st.write("")
        C = st.text_input("C (in)")
        if C.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col6:
        st.write("")
        D = st.text_input("D (in)")
        if D.isalpha():
            st.write("Enter a valid number")
        else:
            pass

    st.write("")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h5 style='text-align: center'>C/S - 1 (Crown to mast rest)</h5>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h5 style='text-align: center'>C/S - 2 (Mast rest to table)</h5>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<h5 style='text-align: center'>C/S - 3 (Pivot region)</h5>", unsafe_allow_html=True)
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        cs1 = Image.open('cross section - 1.png')
        st.image(cs1, use_column_width=True)
        
    with col2:
        cs2 = Image.open('cross section - 2.png')
        st.image(cs2, use_column_width=True)
        
    with col3:
        cs3 = Image.open('cross section - 3.png')
        st.image(cs3, use_column_width=True)
        
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5,1.5,1,1,1,1.5,1.5])
    df = pd.read_excel("Long member cross sections.xlsx")
    df_2 = pd.read_excel("Angle plate cross sections.xlsx")
    with col1:
        width = st.selectbox('w', df.Width.unique())
        # width = st.text_input("w")
        # if width.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        height = st.selectbox('h', df.loc[df.Width==width]['Height'].unique())
        # thck = st.text_input("t")
        # if thck.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col2:
        thck = st.selectbox('t', df.loc[(df.Width==width) & (df.Height==height)]['Thickness'].unique())
        # height = st.text_input("h")
        # if height.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col3:
        angle_plate_width = st.selectbox('b', df_2.Breadth.unique())
        # if angle_plate_width.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        angle_plate_height = st.selectbox('d', df_2.loc[df_2.Breadth==angle_plate_width]['Depth'].unique())
        # angle_root_radius = st.text_input("rr")
        # if angle_root_radius.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    with col4:
        angle_plate_thck = st.selectbox('ta', df_2.loc[(df_2.Breadth==angle_plate_width) & (df_2.Depth==angle_plate_height)]['thickness'].unique())
        angle_toe_radius = st.text_input("rt")
        if angle_toe_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
    
    with col5: 
        angle_root_radius = st.text_input("rr")
        if angle_root_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
        
    with col6:
        plate_thck = st.text_input("pt")
        if plate_thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        dist_bottoms = st.text_input("db")
        if dist_bottoms.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col7:
        plate_height = st.text_input("ph")
        if plate_height.isalpha():
            st.write("Enter a valid number")
        else:
            pass 
        
    ## Enter code for sections
    st.write("")
    st.write("")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1.3,1,1,1,1,1,1])
    
    with col1:
        mast_weight = st.text_input("Mast Assembly weight (kg)")
        if mast_weight.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        pulldown = st.text_input("Pulldown")
        if pulldown.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col3:
        pullback = st.text_input("Pullback")
        if pullback.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        torque = st.text_input("Rotary torque")
        if torque.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col5:
        extending = st.text_input("MRC Extending force")
        if extending.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col6:
        retracting = st.text_input("MRC Retracting force")
        if retracting.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col7:
        yield_limit = st.text_input("Yield stress")
        if yield_limit.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    
    st.write("")
        
    _,_,_,_,_,_,_,_,_,_,_,_,_, col, _,_,_,_,_,_,_,_,_,_,_,_,_ = st.columns(27)
    
    predict_style = """
        <style>
            div.stButton > button:first-child {
                background-color: #ff6d00;
                color: #fff;
                height: 3rem;
                width: 6rem;
                font-size: 20px;
                text-align: center;
                margin: -1rem -1rem -1rem -1rem;
                }
        </style>
    """
    
    with col:
        st.markdown(predict_style, unsafe_allow_html=True)
        predict = st.button('PREDICT')  
    
    if predict:
        variables = [mast_width, mast_depth, A, B, C, D, dist_bottoms, plate_thck, plate_height,
                     angle_toe_radius, angle_root_radius, mast_weight,
                     pulldown, pullback, torque, extending, retracting, yield_limit]
        
        proceed = 'Yes'
        for i in range(len(variables)):
            if (variables[i].isalpha() == True or len(variables[i]) == 0 or regex.search(variables[i]) != None):
                proceed = 'No'
                _,_,_, col, _,_,_ = st.columns(7)
                with col:
                    st.write("Please check all the inputs")
                    hide_st_style = """
                                <style>
                                #MainMenu {visibility: hidden;}
                                footer {visibility: hidden;}
                                header {visibility: hidden;}
                                </style>
                                """
                    st.markdown(hide_st_style, unsafe_allow_html=True)
                st.stop()
            
            else:
                proceed = 'Yes'
                
        if proceed == 'Yes':
            # variables = [mast_width, mast_depth, A, B, C, D, width, height, thck, r_out, dist_bottoms, plate_thck, plate_height,
            #              angle_plate_width, angle_plate_height, angle_plate_thck, angle_toe_radius, angle_root_radius]
            
            # for i in range(len(variables)):
            #     variables[i] = float(variables[i])
            
            mast_width = float(mast_width)
            mast_depth = float(mast_depth)
            A = float(A)
            B = float(B)
            C = float(C)
            D = float(D)
            width = float(width)
            height = float(height)
            thck = float(thck)
            r_out = 2*thck
            dist_bottoms = float(dist_bottoms)
            plate_thck = float(plate_thck)
            plate_height = float(plate_height)
            angle_plate_width = float(angle_plate_width)
            angle_plate_height = float(angle_plate_height)
            angle_plate_thck = float(angle_plate_thck)
            angle_toe_radius = float(angle_toe_radius)
            angle_root_radius = float(angle_root_radius)
            mast_weight = float(mast_weight)
            pulldown = float(pulldown)
            pullback = float(pullback)
            torque = float(torque)
            extending = float(extending)
            retracting = float(retracting)
            yield_limit = float(yield_limit)

            geometry = steel_sections.rectangular_hollow_section(d = height, b = width, t = thck, r_out = r_out, n_r = 30)
            geometry.create_mesh(mesh_sizes = [0.1])
            section = Section(geometry)
            section.calculate_geometric_properties()
            (zxx_01, zxx_02, _, _) = section.get_z()
            if (zxx_01 < zxx_02):
                section_1_modulus = zxx_01
            else:
                section_1_modulus = zxx_02
            
            geometry_1 = steel_sections.rectangular_hollow_section(d = width, b = height, t = thck, r_out = r_out, n_r = 30)
            plate_left = sections.rectangular_section(d = plate_height, b = plate_thck)
            plate_right = sections.rectangular_section(d = plate_height, b = plate_thck)
            plate_left = plate_left.shift_section(x_offset = -(plate_thck), y_offset = -(dist_bottoms))
            if (plate_thck or plate_height != 0):
                geom = geometry_1 + plate_left
            else:
                geom = geometry_1
            plate_right = plate_left.shift_section(x_offset = height + plate_thck, y_offset = 0)
            if (plate_thck or plate_height != 0):
                sec_geom = geom + plate_right
            else:
                sec_geom = geom
            sec_geom.create_mesh(mesh_sizes = [0.1])
            section_1 = Section(sec_geom)
            section_1.calculate_geometric_properties()
            (zxx_11, zxx_12, _, _) = section_1.get_z()
            if (zxx_11 < zxx_12):
                section_2_modulus = zxx_11
            else:
                section_2_modulus = zxx_12
                
            geometry_2 = steel_sections.rectangular_hollow_section(d = height, b = width, t = thck, r_out = r_out, n_r = 30)
            angle = steel_sections.angle_section(d = angle_plate_width, b = angle_plate_height, t = angle_plate_thck, 
                                              r_r = angle_root_radius, r_t = angle_toe_radius, n_r = 30)
            angle = angle.rotate_section(270, [0,0])
            angle = angle.shift_section(x_offset = -(angle_plate_thck), y_offset = height + angle_plate_thck)
            if (angle_plate_height and angle_plate_width != 0):
                section_geometry = geometry_2 + angle
            else:
                section_geometry = geometry_2
            section_geometry.create_mesh(mesh_sizes = [0.1])
            section_2 = Section(section_geometry)
            section_2.calculate_geometric_properties()
            (zxx_21, zxx_22, _, _) = section_2.get_z()
            if (zxx_21 < zxx_22):
                section_3_modulus = zxx_21
            else:
                section_3_modulus = zxx_22
    
            # Retract Prediction
            retract = open("retracting_xgb.pkl","rb")
            retract_regressor = pickle.load(retract)       
            retract_list = [retracting, section_1_modulus, D]
            X_test = pd.DataFrame([retract_list], columns = ['retracting force', 'section modulus (in^3)', 'Overhang (in)'])
            pass_data = X_test[['retracting force', 'section modulus (in^3)', 'Overhang (in)']]
            retract_prediction = retract_regressor.predict(pass_data)
            retract_prediction_print = retract_prediction.item()
            retract_prediction_print = int(retract_prediction_print)
            retract_variation = 500
            retract_prediction_print_LL = str(retract_prediction_print - retract_variation)
            retract_prediction_print_UL = retract_prediction_print + retract_variation
            yield_limit_check = 0.6*yield_limit
            if retract_prediction_print_UL<yield_limit_check:
                retract_safe = 'Yes'
            else:
                retract_safe = 'No'
            retract_prediction_print_UL = str(retract_prediction_print_UL)
            
            # Just about to lift prediction
            just_lift_regressor = pickle.load(open("just_lift_stack.pkl","rb"))
            mrc_pivot_overhang = C + D
            just_lift_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_prediction = just_lift_regressor.predict(pass_data)
            just_lift_prediction_print = just_lift_prediction.item()
            just_lift_prediction_print = int(just_lift_prediction_print)
            just_lift_variation = 1000
            just_lift_prediction_print_LL = str(just_lift_prediction_print - just_lift_variation)
            just_lift_prediction_print_UL = just_lift_prediction_print + just_lift_variation
            if just_lift_prediction_print_UL<yield_limit_check:
                just_lift_safe = 'Yes'
            else:
                just_lift_safe = 'No'
            just_lift_prediction_print_UL = str(just_lift_prediction_print_UL)
                
            # Just about to lift deflection prediction
            just_lift_deflection_regressor = pickle.load(open("just_lift_stack_deflection.pkl","rb"))
            just_lift_deflection_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_deflection_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_deflection_prediction = just_lift_deflection_regressor.predict(pass_data)
            just_lift_deflection_prediction_print = float('%.3f'%(just_lift_deflection_prediction.item()))
            just_lift_def_variation = 0.5
            just_lift_deflection_prediction_print_LL = float('%.3f'%(just_lift_deflection_prediction_print - just_lift_def_variation))
            if just_lift_deflection_prediction_print_LL < 0:
                just_lift_deflection_prediction_print_LL = 0
            else:
                just_lift_deflection_prediction_print_LL = just_lift_deflection_prediction_print_LL
            just_lift_deflection_prediction_print_UL = float('%.3f'%(just_lift_deflection_prediction_print + just_lift_def_variation))
            if just_lift_deflection_prediction_print_UL < just_lift_def_variation:
                just_lift_deflection_prediction_print_UL = just_lift_def_variation
            else:
                just_lift_deflection_prediction_print_UL = just_lift_deflection_prediction_print_UL
            just_lift_deflection_prediction_print_LL = str(just_lift_deflection_prediction_print_LL)
            just_lift_deflection_prediction_print_UL = str(just_lift_deflection_prediction_print_UL)
        
            # Horizontal tramming prediction
            hor_tram_regressor = pickle.load(open("hor_tram_stack.pkl","rb"))
            hor_tram_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_prediction = hor_tram_regressor.predict(pass_data)
            hor_tram_prediction_print = hor_tram_prediction.item()
            hor_tram_prediction_print = int(hor_tram_prediction_print)
            hor_tram_variation = 800
            hor_tram_prediction_print_LL = str(hor_tram_prediction_print - hor_tram_variation)
            hor_tram_prediction_print_UL = hor_tram_prediction_print + hor_tram_variation
            if hor_tram_prediction_print_UL<yield_limit_check:
                hor_tram_safe = 'Yes'
            else:
                hor_tram_safe = 'No'
            hor_tram_prediction_print_UL = str(hor_tram_prediction_print_UL)
                
            # Horizontal tramming deflection prediction
            hor_tram_def_regressor = pickle.load(open("hor_tram_stack_deflection.pkl","rb"))
            hor_tram_def_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_def_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_def_prediction = hor_tram_def_regressor.predict(pass_data)
            hor_tram_def_prediction_print = float('%.3f'%(hor_tram_def_prediction.item()))
            hor_tram_def_variation = 0.35
            hor_tram_def_prediction_print_LL = float('%.3f'%(hor_tram_def_prediction_print - hor_tram_def_variation))
            if hor_tram_def_prediction_print_LL < 0:
                hor_tram_def_prediction_print_LL = 0
            else:
                hor_tram_def_prediction_print_LL = hor_tram_def_prediction_print_LL
            hor_tram_def_prediction_print_UL = float('%.3f'%(hor_tram_def_prediction_print + hor_tram_def_variation))
            if hor_tram_def_prediction_print_UL < hor_tram_def_variation:
                hor_tram_def_prediction_print_UL = hor_tram_def_variation
            else:
                hor_tram_def_prediction_print_UL = hor_tram_def_prediction_print_UL
            hor_tram_def_prediction_print_LL = str(hor_tram_def_prediction_print_LL)
            hor_tram_def_prediction_print_UL = str(hor_tram_def_prediction_print_UL)
                
            # Extending prediction
            extending_regressor = pickle.load(open("extending_stack.pkl","rb"))
            extending_list = [extending, section_2_modulus, mast_depth, section_3_modulus]
            X_test = pd.DataFrame([extending_list], columns = ['extendingforce', 'Sectionmodulus', 'Mastdepth', 'Sectionmodulus2'])
            pass_data = X_test[['extendingforce', 'Sectionmodulus', 'Mastdepth', 'Sectionmodulus2']]
            extending_prediction = extending_regressor.predict(pass_data)
            extending_prediction_print = extending_prediction.item()
            extending_prediction_print = int(extending_prediction_print)
            extending_variation = 1100
            extending_prediction_print_LL = str(extending_prediction_print - extending_variation)
            extending_prediction_print_UL = extending_prediction_print + extending_variation
            if extending_prediction_print_UL<yield_limit_check:
                extending_safe = 'Yes'
            else:
                extending_safe = 'No'
            extending_prediction_print_UL = str(extending_prediction_print_UL)
                        
            # Pullback prediction
            pullback_regressor = pickle.load(open("pullback_lr.pkl", "rb"))
            pullback_list = [pullback*1.2, torque*1.35, section_1_modulus]
            X_test = pd.DataFrame([pullback_list], columns = ['Pullbackload', 'Rotation', 'Sectionmodulus'])
            pass_data = X_test[['Pullbackload', 'Rotation', 'Sectionmodulus']]
            pullback_prediction = pullback_regressor.predict(pass_data)
            pullback_prediction_print = int(pullback_prediction.item())
            pullback_variation = 750
            pullback_prediction_print_LL = str(pullback_prediction_print - pullback_variation)
            pullback_prediction_print_UL = pullback_prediction_print + pullback_variation
            if pullback_prediction_print_UL<yield_limit_check:
                pullback_safe = 'Yes'
            else:
                pullback_safe = 'No'
            pullback_prediction_print_UL = str(pullback_prediction_print_UL)
            
            #Code for remaining models
            
            data = [['Mast Horizontal & MRC Retracting', str(1), retract_prediction_print_LL + ' - ' + retract_prediction_print_UL, '-', retract_safe], 
                    ['Just about to lift (1.1G Lift Factor)', str(3), just_lift_prediction_print_LL + ' - ' + just_lift_prediction_print_UL, just_lift_deflection_prediction_print_LL + ' - ' + just_lift_deflection_prediction_print_UL, just_lift_safe],
                    ['Horizontal Tramming (1.5G Vertical Load)', str(1), hor_tram_prediction_print_LL + ' - ' + hor_tram_prediction_print_UL, hor_tram_def_prediction_print_LL + ' - ' + hor_tram_def_prediction_print_UL, hor_tram_safe], 
                    ['Mast vertical & MRC Extending', str(2), extending_prediction_print_LL + ' - ' + extending_prediction_print_UL, '-', extending_safe],
                    ['Vertical Drilling (120% Pullback and 135% Torque)', str(6), pullback_prediction_print_LL + ' - ' + pullback_prediction_print_UL, '-', pullback_safe]]
            df = pd.DataFrame(data, columns = ['Load case', 'Loc. No.', 'Stress', 'Deflection', 'Compliant?'])
            def color_unsafe(val):
                color = 'red' if val == 'No' else 'green'
                return f'background-color: {color}'
            
            df = df.style.applymap(color_unsafe, subset = ['Compliant?'])
            
            col1, col2 = st.columns(2)
            with col1:
                sf = Image.open('Mast static failure locations.png')
                st.image(sf, use_column_width=True)
                
            with col2:
                st.table(df)
            
            #Code for fatigue models and cumulative damage calculation
            
            m_160 = 5
            m_90 = 3
            A_160 = (160**m_160)*2000000      #FAT 160 calculated for 2E+6 number of cycles
            A_90 = (90**m_90)*2000000
            oc = 64000          #Number of occurences for mast raising cycle
            # asr_160 = int(math.exp((1/m_160) * math.log(A_160/oc)))     #Allowable stress range for the 
            # asr_90 = int(math.exp((1/m_90) * math.log(A_90/oc)))
            
            
            #Location number 1
            
            #Just about to lift - Loc - 1 prediction
            
            just_lift_loc_1_regressor = pickle.load(open("just_lift_loc_1_xgb.pkl", "rb"))
            just_lift_loc_1_list = [mast_weight*1.1, section_2_modulus, mast_depth, mrc_pivot_overhang]
            X_test = pd.DataFrame([just_lift_loc_1_list], columns = ['Mastweight', 'Sectionmodulus', 'Mastdepth', 'Overhang'])
            pass_data = X_test[['Mastweight', 'Sectionmodulus', 'Mastdepth', 'Overhang']]
            just_lift_loc_1_prediction = just_lift_loc_1_regressor.predict(pass_data)
            just_lift_loc_1_prediction_print = int(just_lift_loc_1_prediction.item())
            
            #Extending - Loc - 1 prediction
            
            extending_loc_1_regressor = pickle.load(open("extending_loc_1_stack.pkl", "rb"))
            extending_loc_1_list = [extending, section_2_modulus, mast_depth]
            X_test = pd.DataFrame([extending_loc_1_list], columns = ['Extendingforce', 'Sectionmodulus', 'Mastdepth'])
            pass_data = X_test[['Extendingforce', 'Sectionmodulus', 'Mastdepth']]
            extending_loc_1_prediction = extending_loc_1_regressor.predict(pass_data)
            extending_loc_1_prediction_print = int(extending_loc_1_prediction.item())
            
            wsr_loc_1 = extending_loc_1_prediction_print - just_lift_loc_1_prediction_print
            wsr_loc_1_mpa = int(wsr_loc_1/145)
            n_loc_1 = A_160/(wsr_loc_1_mpa**m_160)
            cd_loc_1 = float(oc/n_loc_1)
            cd_loc_1_print = '%.2f'%cd_loc_1
            cd_loc_1_variation = 0.07
            if cd_loc_1 < 0.07:
                cd_loc_1_LL = str(0)
            else:
                cd_loc_1_LL = cd_loc_1 - 0.07
                cd_loc_1_LL = str('%.2f'%cd_loc_1_LL)
                
            cd_loc_1_UL = cd_loc_1 + 0.07
            
            if cd_loc_1_UL > 1:
                loc_1_safe = "No"
            else:
                loc_1_safe = "Yes"
                
            cd_loc_1_UL = str('%.2f'%cd_loc_1_UL)
            
            #Location number 2
            
            #Retracting - Loc - 2 prediction
            
            
            #Extending - Loc - 2 prediction
            
            
            data_fatigue = [["Mast Raising-Lowering Cycle", str(1) + ' (Material stress)', cd_loc_1_LL + '-' + cd_loc_1_UL, loc_1_safe]]
            df_fatigue = pd.DataFrame(data_fatigue, columns = ['Cycle', 'Loc. No.', 'Cumulative Damage', 'Compliant?'])
            df_fatigue = df_fatigue.style.applymap(color_unsafe, subset = ['Compliant?'])
            
            st.write("")
            st.markdown("<h3 style='text-align: center'>Fatigue compliance</h3>", unsafe_allow_html=True)
            st.write("")
            
            col1, col2 = st.columns(2)
            with col1:
                ff = Image.open('Mast fatigue failure locations.png')
                st.image(ff, use_column_width=True)
                
            with col2:
                st.table(df_fatigue)
 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
