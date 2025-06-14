import streamlit as st

# Sample laptop data
laptops = [
    {
        "name": "Dell XPS 13",
        "price": 1200,
        "desc": "13.3-inch FHD, Intel i7, 16GB RAM, 512GB SSD",
        "image": "https://cdn.pixabay.com/photo/2014/05/02/21/50/home-office-336377_1280.jpg"
    },
    {
        "name": "MacBook Air M2",
        "price": 1400,
        "desc": "13.6-inch Retina, Apple M2, 8GB RAM, 256GB SSD",
        "image": "https://cdn.pixabay.com/photo/2015/01/21/14/14/apple-606761_1280.jpg"
    },
    {
        "name": "HP Spectre x360",
        "price": 1100,
        "desc": "13.5-inch OLED, Intel i5, 8GB RAM, 512GB SSD",
        "image": "https://cdn.pixabay.com/photo/2016/11/29/09/32/adult-1867756_1280.jpg"
    }
]

st.title("💻 Laptop E-Commerce Store")

# Initialize cart in session state
if "cart" not in st.session_state:
    st.session_state.cart = []

# Show laptops
for idx, laptop in enumerate(laptops):
    st.image(laptop["image"], width=250)
    st.subheader(laptop["name"])
    st.write(laptop["desc"])
    st.write(f"**Giá:** ${laptop['price']}")
    if st.button(f"Thêm vào giỏ hàng", key=f"add_{idx}"):
        st.session_state.cart.append(laptop)
        st.success(f"Đã thêm {laptop['name']} vào giỏ hàng!")

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
