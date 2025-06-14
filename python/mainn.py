import streamlit as st

# Sample CV templates data
cv_templates = [
    {
        "name": "Modern CV",
        "price": 5,
        "desc": "Thiết kế hiện đại, phù hợp cho mọi ngành nghề.",
        "image": "https://cdn.pixabay.com/photo/2017/01/31/13/14/template-2023681_1280.png"
    },
    {
        "name": "Professional CV",
        "price": 7,
        "desc": "Phong cách chuyên nghiệp, nổi bật kinh nghiệm làm việc.",
        "image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/resume-1295664_1280.png"
    },
    {
        "name": "Creative CV",
        "price": 6,
        "desc": "Thiết kế sáng tạo, phù hợp ngành nghệ thuật, thiết kế.",
        "image": "https://cdn.pixabay.com/photo/2017/08/10/07/32/cv-2618607_1280.jpg"
    }
]

st.title("📄 E-Commerce CV Template Store")

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Show CV templates
for idx, cv in enumerate(cv_templates):
    st.image(cv["image"], width=250)
    st.subheader(cv["name"])
    st.write(cv["desc"])
    st.write(f"**Giá:** ${cv['price']}")
    if st.button(f"Thêm vào giỏ hàng", key=f"add_{idx}"):
        st.session_state.cart.append(cv)
        st.success(f"Đã thêm {cv['name']} vào giỏ hàng!")

st.markdown("---")
st.header("🛒 Giỏ hàng")

if st.session_state.cart:
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['name']} (${item['price']})")
        total += item['price']
    st.write(f"**Tổng cộng:** ${total}")
else:
    st.write("Giỏ hàng trống.")

st.info("Đây là demo đơn giản. Bạn có thể mở rộng thêm chức năng thanh toán, đăng nhập, quản lý sản phẩm,...")
