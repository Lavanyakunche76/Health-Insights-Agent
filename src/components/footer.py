import streamlit as st

def show_footer(in_sidebar=False):
    st.markdown(
        """
        <div style='text-align: center; padding: 0.75rem; border-top: 1px solid rgba(100, 181, 246, 0.15); margin-top: 2rem;'>
            <p style='color: #64B5F6; font-size: 0.75rem; margin: 0;'>
                <a href='https://github.com/Lavanyakunche76' target='_blank'
                   style='color: #64B5F6; text-decoration: none; font-weight: 500;'>
                    Created by Lavanya Kunche
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
