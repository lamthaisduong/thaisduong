import streamlit as st

# --- Dữ liệu mẫu ---
laptops = [
    {
        "name": "MacBook Air M2 2024",
        "price": 28990000,
        "img": "https://cdn.tgdd.vn/Products/Images/44/322927/macbook-air-m2-2024-13-inch-1-2.jpg",
        "desc": "Chip Apple M2, 8GB, SSD 256GB, màn 13.6 inch, pin 18h, siêu nhẹ chỉ 1.24kg."
    },
    {
        "name": "Dell XPS 13 Plus",
        "price": 36990000,
        "img": "https://cdn.tgdd.vn/Products/Images/44/309776/dell-xps-13-plus-9320-i7-1200x800.jpg",
        "desc": "Intel Core i7 Gen 12, RAM 16GB, SSD 512GB, màn OLED 13.4 inch, thiết kế cao cấp."
    },
    {
        "name": "ASUS ROG Zephyrus G14",
        "price": 32990000,
        "img": "https://cdn.tgdd.vn/Products/Images/44/309779/asus-rog-zephyrus-g14-2023-1.jpg",
        "desc": "AMD Ryzen 7, RTX 4060, RAM 16GB, SSD 1TB, màn 14 inch 165Hz, gaming siêu mỏng nhẹ."
    },
    {
        "name": "HP Pavilion 15",
        "price": 15990000,
        "img": "https://cdn.tgdd.vn/Products/Images/44/309778/hp-pavilion-15-eg2082tu-i5-7c0x3pa-1.jpg",
        "desc": "Intel Core i5 Gen 12, RAM 8GB, SSD 512GB, màn 15.6 inch Full HD, pin lâu."
    }
]

# --- Quản lý user ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": "123456"}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page" not in st.session_state:
    st.session_state.page = "login"
if "cart" not in st.session_state:
    st.session_state.cart = []

def register():
    st.header("Đăng ký tài khoản")
    new_user = st.text_input("Tên đăng nhập mới")
    new_pass = st.text_input("Mật khẩu mới", type="password")
    confirm_pass = st.text_input("Nhập lại mật khẩu", type="password")
    if st.button("Đăng ký"):
        if not new_user or not new_pass:
            st.error("Vui lòng nhập đầy đủ thông tin.")
        elif new_user in st.session_state.users:
            st.error("Tên đăng nhập đã tồn tại.")
        elif new_pass != confirm_pass:
            st.error("Mật khẩu nhập lại không khớp.")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Đăng ký thành công! Bạn có thể đăng nhập.")
            st.session_state.page = "login"
    if st.button("Quay lại đăng nhập"):
        st.session_state.page = "login"

def login():
    st.header("Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Đăng nhập thành công!")
            st.session_state.page = "shop"
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")
    if st.button("Đăng ký tài khoản mới"):
        st.session_state.page = "register"

def logout():
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.cart = []
        st.session_state.page = "login"
        st.success("Đã đăng xuất.")

def show_cart():
    st.subheader("🛒 Giỏ hàng của bạn")
    if not st.session_state.cart:
        st.info("Giỏ hàng đang trống.")
        return
    total = 0
    for item in st.session_state.cart:
        st.image(item["img"], width=120)
        st.write(f"**{item['name']}**")
        st.write(f"Giá: {item['price']:,} VNĐ")
        st.write("---")
        total += item["price"]
    st.write(f"### Tổng cộng: {total:,} VNĐ")
    if st.button("Thanh toán"):
        st.success("Cảm ơn bạn đã mua hàng! Đơn hàng của bạn đang được xử lý.")
        st.session_state.cart = []

def shop():
    st.markdown("<h1 style='text-align:center;color:#1976d2;'>💻 Laptop Shop</h1>", unsafe_allow_html=True)
    st.write(f"Xin chào, **{st.session_state.username}**")
    logout()
    st.markdown("---")
    st.subheader("Danh sách sản phẩm")
    cols = st.columns(2)
    for i, laptop in enumerate(laptops):
        with cols[i % 2]:
            st.image(laptop["img"], use_column_width=True)
            st.markdown(f"**{laptop['name']}**")
            st.write(laptop["desc"])
            st.write(f"### Giá: {laptop['price']:,} VNĐ")
            if st.button("Thêm vào giỏ", key=f"add_{i}"):
                st.session_state.cart.append(laptop)
                st.success(f"Đã thêm {laptop['name']} vào giỏ hàng!")
    st.markdown("---")
    show_cart()

# --- ĐIỀU HƯỚNG ---
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login()
    else:
        register()
else:
    shop()
