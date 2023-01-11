# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 12:18:07 2023

@author: fl9768
"""

import pandas as pd
import numpy as np
import streamlit as st
import pickle
import re
from PIL import Image
#from sectionproperties.pre.geometry import CompoundGeometry
from sectionproperties.analysis.section import Section
import sectionproperties.pre.library.steel_sections as steel_sections
import sectionproperties.pre.library.primitive_sections as sections
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mast design", layout="wide")

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem; padding-bottom:0rem; padding-left:0.5rem; padding-right:0.5rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center'>Mast design Automation</h1>", unsafe_allow_html=True)

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

feed_actuation = st.sidebar.selectbox("Feed Type", ("Cylinder feed", "Motor feed"))

with st.sidebar:
    st.markdown("<h3 style='text-align: center'>IMPORTANT</h3>", unsafe_allow_html=True)
    st.write("1. Length values should be entered in inches")
    st.write("2. Force values should be entered in lbf")
    st.write("3. Stress and Young's Modulus values should be entered in psi")
    st.write("4. All inputs are mandatory")
    st.write("5. If you encounter a 'TopologicalError' the entered geometry cannot be constructed. Please enter a valid geometry in that case")

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
    
    # col1, col2, col3 = st.columns(3)
    # col1_1, col1_2 = col1.columns([1, 1])
    # col2_1, col2_2 = col2.columns([1, 1])
    # col3_1, col3_2 = col3.columns([1, 1])
    
    # with col1_1:
    #     cs1 = Image.open('cross section - 1.png')
    #     st.image(cs1, use_column_width=True)
    
    # col1_2_1, col1_2_2 = col1_2.columns(2)  
      
    # with col1_2_1:
    #     width = st.text_input("w")
    #     if width.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     thck = st.text_input("t")
    #     if thck.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col1_2_2:
    #     height = st.text_input("h")
    #     if height.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     r_out = st.text_input("r")
    #     if r_out.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
        
    # with col2_1:
    #     cs2 = Image.open('cross section - 2.png')
    #     st.image(cs2, use_column_width=True)
    
    # col2_2_1, col2_2_2, col2_2_3 = col2_2.columns(3)  
      
    # with col2_2_1:
    #     angle_plate_width = st.text_input("b")
    #     if angle_plate_width.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     angle_root_radius = st.text_input("rr")
    #     if angle_root_radius.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col2_2_2:
        # angle_plate_height = st.text_input("d")
        # if angle_plate_height.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        # angle_toe_radius = st.text_input("rt")
        # if angle_toe_radius.isalpha():
        #     st.write("Enter a valid number")
        # else:
        #     pass
        
    # with col2_2_3:
    #     angle_plate_thck = st.text_input("ta")
    #     if angle_plate_thck.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col3_1:
    #     cs3 = Image.open('cross section - 3.png')
    #     st.image(cs3, use_column_width=True)
    
    # col3_2_1, col3_2_2 = col3_2.columns(2)  
      
    # with col3_2_1:
    #     plate_thck = st.text_input("pt")
    #     if plate_thck.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     dist_bottoms = st.text_input("db")
    #     if dist_bottoms.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col3_2_2:
    #     plate_height = st.text_input("ph")
    #     if plate_height.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #  from here  
    # col1, col2, col3 = st.columns(3)
    # col1_1, col1_2 = col1.columns([1.2,2])
    
    # with col1_1:
    #     bp1 = Image.open('bottom plate - 1.png')
    #     st.image(bp1, use_column_width=True)
        
    # with col1_2:
    #     bp2 = Image.open('bottom plate - 2.png')
    #     st.image(bp2, use_column_width=True)
    
    # col2_1, col2_2, col2_3 = col2.columns([1,1,2])
    
    # with col2_1:
    #     ff_plate_thck = st.text_input("tp")
    #     if ff_plate_thck.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     ff_plate_length = st.text_input("L")
    #     if ff_plate_length.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col2_2:
    #     ff_plate_height = st.text_input("H")
    #     if ff_plate_height.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     mast_weight = st.text_input("Mast weight (kg)")
    #     if mast_weight.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col2_3:  
    #     feed_actuation = st.selectbox('Feed Actuation', ('Cylinder feed', 'Motor feed'))
    #     torque = st.text_input('Rotary Torque (lbf-in)')
    #     if torque.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # col3_1, col3_2 = col3.columns(2)
    
    # with col3_1:
    #     pulldown = st.text_input('Pulldown load (lbf)')
    #     if pulldown.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     extending = st.text_input('Extending force (lbf)')
    #     if extending.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # with col3_2:
    #     pullback = st.text_input('Pullback load (lbf)')
    #     if pullback.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    #     retracting = st.text_input('Retracting force (lbf)')
    #     if retracting.isalpha():
    #         st.write("Enter a valid number")
    #     else:
    #         pass
    
    # button_style = """
    #         <style>
    #         .stButton > button {
    #             width: 100px;
    #             height: 50px;
    #         }
    #         </style>
    #         """
    # st.markdown(button_style, unsafe_allow_html=True)
    
    ## IF NESTED COLUMNS NOT ALLOWED IN HEROKU
    
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
    with col1:
        width = st.text_input("w")
        if width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        thck = st.text_input("t")
        if thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        height = st.text_input("h")
        if height.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        r_out = st.text_input("r")
        if r_out.isalpha():
            st.write("Enter a valid number")
        else:
            pass 
        
    with col3:
        angle_plate_width = st.text_input("b")
        if angle_plate_width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        angle_root_radius = st.text_input("rr")
        if angle_root_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        angle_plate_height = st.text_input("d")
        if angle_plate_height.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        angle_toe_radius = st.text_input("rt")
        if angle_toe_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
    
    with col5: 
        angle_plate_thck = st.text_input("ta")
        if angle_plate_thck.isalpha():
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
        
    

    col1, col2, col3, col4 = st.columns([1,1.2,1,1])
    
    with col1:
        bp1 = Image.open('bottom plate - 1.png')
        st.image(bp1, use_column_width=True)   
        
    with col2:
        bp2 = Image.open('bottom plate - 2.png')
        st.image(bp2, use_column_width=True)
                
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
        
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    with col1:
        mast_weight = st.text_input("Mast weight (kg)")
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
        
    with col8:
        youngs_modulus = st.text_input("Young's Modulus")
        if youngs_modulus.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    _,_,_,_,_,_,_,_,_,_,_,_,_, col, _,_,_,_,_,_,_,_,_,_,_,_,_ = st.columns(27)
    predict = col.button('Predict')
    
    if predict:
        variables = [mast_width, mast_depth, A, B, C, D, width, height, thck, r_out, dist_bottoms, plate_thck, plate_height, ff_plate_thck,
                     ff_plate_length, ff_plate_height, angle_plate_width, angle_plate_height, angle_plate_thck, angle_toe_radius, 
                     angle_root_radius, mast_weight, pulldown, pullback, torque, extending, retracting, yield_limit, youngs_modulus]
        
        proceed = 'Yes'
        for i in range(len(variables)):
            if (variables[i].isalpha() == True or len(variables[i]) == 0 or regex.search(variables[i]) != None):
                proceed = 'No'
                _,_,_, col, _,_,_ = st.columns(7)
                with col:
                    st.write("Please check all the inputs")
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
            r_out = float(r_out)
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
            youngs_modulus = float(youngs_modulus)

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
            yield_limit_check = 0.6*yield_limit
            if retract_prediction_print<yield_limit_check:
                retract_safe = 'Yes'
            else:
                retract_safe = 'No'
            
            # Just about to lift prediction
            just_lift_regressor = pickle.load(open("just_lift_stack.pkl","rb"))
            mrc_pivot_overhang = C + D
            just_lift_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_prediction = just_lift_regressor.predict(pass_data)
            just_lift_prediction_print = just_lift_prediction.item()
            just_lift_prediction_print = int(just_lift_prediction_print)
            if just_lift_prediction_print<yield_limit_check:
                just_lift_safe = 'Yes'
            else:
                just_lift_safe = 'No'
                
            # Horizontal tramming prediction
            hor_tram_regressor = pickle.load(open("hor_tram_stack.pkl","rb"))
            hor_tram_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_prediction = hor_tram_regressor.predict(pass_data)
            hor_tram_prediction_print = hor_tram_prediction.item()
            hor_tram_prediction_print = int(hor_tram_prediction_print)
            if hor_tram_prediction_print<yield_limit_check:
                hor_tram_safe = 'Yes'
            else:
                hor_tram_safe = 'No'
                
            # Extending prediction
            #Code for remaining models
            
            data = [[1, 'Mast Horizontal & MRC Retracting', retract_prediction_print, retract_safe], [3, 'Just about to lift (1.1G Lift Factor)', just_lift_prediction_print, just_lift_safe],
                    [1, 'Horizontal Tramming (1.5G Vertical Load)', hor_tram_prediction_print, hor_tram_safe]]
            df = pd.DataFrame(data, columns = ['Loc. No.', 'Load case', 'Stress', 'Compliant?'])
            
            col1, col2 = st.columns(2)
            with col1:
                sf = Image.open('Mast static failure locations.png')
                st.image(sf, use_column_width=True)
                
            with col2:
                st.table(df)
                
            

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
    with col1:
        width = st.text_input("w")
        if width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        thck = st.text_input("t")
        if thck.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col2:
        height = st.text_input("h")
        if height.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        r_out = st.text_input("r")
        if r_out.isalpha():
            st.write("Enter a valid number")
        else:
            pass 
        
    with col3:
        angle_plate_width = st.text_input("b")
        if angle_plate_width.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        angle_root_radius = st.text_input("rr")
        if angle_root_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    with col4:
        angle_plate_height = st.text_input("d")
        if angle_plate_height.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        angle_toe_radius = st.text_input("rt")
        if angle_toe_radius.isalpha():
            st.write("Enter a valid number")
        else:
            pass
    
    with col5: 
        angle_plate_thck = st.text_input("ta")
        if angle_plate_thck.isalpha():
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
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    with col1:
        mast_weight = st.text_input("Mast weight (kg)")
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
        
    with col8:
        youngs_modulus = st.text_input("Young's Modulus")
        if youngs_modulus.isalpha():
            st.write("Enter a valid number")
        else:
            pass
        
    _,_,_,_,_,_,_,_,_,_,_,_,_, col, _,_,_,_,_,_,_,_,_,_,_,_,_ = st.columns(27)
    predict = col.button('Predict')  
    
    if predict:
        variables = [mast_width, mast_depth, A, B, C, D, width, height, thck, r_out, dist_bottoms, plate_thck, plate_height,
                     angle_plate_width, angle_plate_height, angle_plate_thck, angle_toe_radius, angle_root_radius, mast_weight,
                     pulldown, pullback, torque, extending, retracting, yield_limit, youngs_modulus]
        
        proceed = 'Yes'
        for i in range(len(variables)):
            if (variables[i].isalpha() == True or len(variables[i]) == 0 or regex.search(variables[i]) != None):
                proceed = 'No'
                _,_,_, col, _,_,_ = st.columns(7)
                with col:
                    st.write("Please check all the inputs")
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
            r_out = float(r_out)
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
            youngs_modulus = float(youngs_modulus)

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
            yield_limit_check = 0.6*yield_limit
            if retract_prediction_print<yield_limit_check:
                retract_safe = 'Yes'
            else:
                retract_safe = 'No'
            
            # Just about to lift prediction
            just_lift_regressor = pickle.load(open("just_lift_stack.pkl","rb"))
            mrc_pivot_overhang = C + D
            just_lift_list = [mast_weight*1.1, section_3_modulus, mrc_pivot_overhang, mast_depth]
            X_test = pd.DataFrame([just_lift_list], columns = ['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang', 'Mastdepth']]
            just_lift_prediction = just_lift_regressor.predict(pass_data)
            just_lift_prediction_print = just_lift_prediction.item()
            just_lift_prediction_print = int(just_lift_prediction_print)
            if just_lift_prediction_print<yield_limit_check:
                just_lift_safe = 'Yes'
            else:
                just_lift_safe = 'No'
                
            # Horizontal tramming prediction
            hor_tram_regressor = pickle.load(open("hor_tram_stack.pkl","rb"))
            hor_tram_list = [mast_weight*1.5, section_1_modulus, D]
            X_test = pd.DataFrame([hor_tram_list], columns = ['Weight', 'Sectionmodulus', 'Overhang'])
            pass_data = X_test[['Weight', 'Sectionmodulus', 'Overhang']]
            hor_tram_prediction = hor_tram_regressor.predict(pass_data)
            hor_tram_prediction_print = hor_tram_prediction.item()
            hor_tram_prediction_print = int(hor_tram_prediction_print)
            if hor_tram_prediction_print<yield_limit_check:
                hor_tram_safe = 'Yes'
            else:
                hor_tram_safe = 'No'
                
            # Extending prediction
            #Code for remaining models
            
            data = [[1, 'Mast Horizontal & MRC Retracting', retract_prediction_print, retract_safe], [3, 'Just about to lift (1.1G Lift Factor)', just_lift_prediction_print, just_lift_safe],
                    [1, 'Horizontal Tramming (1.5G Vertical Load)', hor_tram_prediction_print, hor_tram_safe]]
            df = pd.DataFrame(data, columns = ['Loc. No.', 'Load case', 'Stress', 'Compliant?'])
            
            col1, col2 = st.columns(2)
            with col1:
                sf = Image.open('Mast static failure locations.png')
                st.image(sf, use_column_width=True)
                
            with col2:
                st.table(df)
 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
