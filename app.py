import pandas as pd
import streamlit as st

# --- 1. DỮ LIỆU VÀ TÍNH TOÁN ---
data = {
    'Ho_va_ten': [
        'Nguyễn Văn A',
        'Trần Thị B',
        'Lê Văn C',
        'Phạm Thị D',
        'Hoàng Văn E',
        'Vũ Thị F',
        'Đỗ Văn G',
        'Bùi Thị H',
        'Ngô Văn I',
        'Dương Thị K',
    ],
    'Chuyen_can': [9.0, 8.0, 7.5, 6.0, 4.5, 8.5, 9.5, 5.0, 6.5, 10.0],
    'Giua_ky': [8.0, 7.0, 6.5, 5.0, 4.0, 8.0, 9.0, 4.5, 6.0, 9.5],
    'Cuoi_ky': [8.5, 7.5, 7.0, 5.5, 4.0, 8.0, 9.0, 5.0, 6.5, 9.0],
}

df = pd.DataFrame(data)
df['Tong_ket'] = (
    0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']
).round(2)


def xep_loai(dtk):
  if dtk >= 8.5:
    return 'Giỏi'
  elif dtk >= 7.0:
    return 'Khá'
  elif dtk >= 5.0:
    return 'Trung bình'
  else:
    return 'Yếu'


df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# --- 2. GIAO DIỆN WEB APP ---
st.title('QUẢN LÝ ĐIỂM SINH VIÊN')
st.subheader('Bảng điểm chi tiết')
st.dataframe(df, use_container_width=True)

st.subheader('Thống kê kết quả học tập')
diem_tb_lop = df['Tong_ket'].mean()
max_sv = df.loc[df['Tong_ket'].idxmax()]
min_sv = df.loc[df['Tong_ket'].idmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

col1, col2 = st.columns(2)
with col1:
  st.metric(label='Điểm trung bình lớp', value=f'{diem_tb_lop:.2f}')
  st.metric(label='Số sinh viên đạt (>= 5.0)', value=so_sv_dat)
with col2:
  st.metric(
      label='Sinh viên điểm cao nhất',
      value=f'{max_sv["Ho_va_ten"]} ({max_sv["Tong_ket"]})',
  )
  st.metric(
      label='Sinh viên điểm thấp nhất',
      value=f'{min_sv["Ho_va_ten"]} ({min_sv["Tong_ket"]})',
  )

st.subheader('Tra cứu thông tin sinh viên')
selected_student = st.selectbox(
    'Chọn họ và tên sinh viên:', df['Ho_va_ten'].tolist()
)
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

st.markdown(f"""
* **Họ và tên:** {student_info['Ho_va_ten']}
* **Điểm chuyên cần:** {student_info['Chuyen_can']}
* **Điểm giữa kỳ:** {student_info['Giua_ky']}
* **Điểm cuối kỳ:** {student_info['Cuoi_ky']}
* **Điểm tổng kết:** **{student_info['Tong_ket']}**
* **Xếp loại:** **{student_info['Xep_loai']}**
""")

st.subheader('Biểu đồ điểm tổng kết lớp')
# Sử dụng biểu đồ tích hợp sẵn của Streamlit, chạy cực nhanh và không cần matplotlib
chart_data = df.set_index('Ho_va_ten')[['Tong_ket']]
st.bar_chart(chart_data)
ax.set_ylabel('Điểm tổng kết')
plt.xticks(rotation=45, ha='right')
ax.set_ylim(0, 10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
