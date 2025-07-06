# %% [markdown]
# # Giới thiệu khái niệm Đại số Tuyến tính
#
# Chào mừng bạn đến với notebook tìm hiểu về Đại số tuyến tính! Chúng ta sẽ cùng nhau khám phá những khái niệm cốt lõi của môn học này, bắt đầu từ những viên gạch đầu tiên: **vector**.
#
# Để dễ hình dung, chúng ta sẽ sử dụng một ví dụ xuyên suốt: điều khiển một chiếc drone. Mọi di chuyển, vị trí, và lực tác động lên drone đều có thể được mô tả bằng vector.

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## 1. Vector và Scalar
#
# Trong cuộc sống, có những đại lượng ta chỉ cần một con số để mô tả, ví dụ như nhiệt độ (25°C) hay khối lượng (5kg). Những con số đơn lẻ này được gọi là **scalar** (đại lượng vô hướng).
#
# Tuy nhiên, để xác định vị trí của drone, ta cần nhiều hơn một con số. Ví dụ, drone đang ở "cách 3 mét về phía Đông và 4 mét về phía Bắc" so với vị trí của bạn. Cặp số `(3, 4)` này không chỉ cho biết khoảng cách mà còn cả hướng. Đây chính là một **vector** (đại lượng có hướng).
#
# - **Scalar**: Một con số duy nhất.
# - **Vector**: Một danh sách các con số được sắp xếp theo thứ tự, biểu diễn cả độ lớn và hướng.

# %% [markdown]
# ### 1.1. Định nghĩa Scalar và Vector trong Python
#
# Chúng ta sẽ dùng thư viện `NumPy` để làm việc với vector.

# %%
# Scalar
s = 25
print(f"Scalar s: {s}")
print(f"Kiểu dữ liệu của s: {type(s)}")

# Vector (sử dụng NumPy array)
# Vector v biểu diễn vị trí: 3 mét về phía Đông (trục x), 4 mét về phía Bắc (trục y)
v = np.array([3, 4])
print(f"\nVector v: {v}")
print(f"Shape của v: {v.shape}")
print(f"Kiểu dữ liệu của v: {type(v)}")

# %%[markdown]
# ### 1.2. Trực quan hóa Vector
#
# Một vector thường được biểu diễn bằng một mũi tên bắt đầu từ gốc tọa độ `(0,0)` đến điểm có tọa độ là các thành phần của vector.

# %%
# Thiết lập plot
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector v = [3, 4]')

# Tùy chỉnh plot cho dễ nhìn
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.xlabel("Trục X (Phía Đông)")
plt.ylabel("Trục Y (Phía Bắc)")
plt.title("Trực quan hóa Vector vị trí của Drone")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# %% [markdown]
# ## 2. Các Phép toán trên Vector
#
# Giống như các con số, chúng ta có thể thực hiện các phép toán trên vector.

# %% [markdown]
# ### 2.1. Phép Cộng Vector
#
# Giả sử drone bay từ gốc tọa độ đến vị trí `v = [3, 4]`. Sau đó, nó lại di chuyển một đoạn nữa, được biểu diễn bằng vector `w = [5, 1]` (5 mét về Đông, 1 mét về Bắc). Vị trí cuối cùng của drone so với gốc là tổng của hai vector `v` và `w`.
#
# - **Đại số**: Cộng từng thành phần tương ứng.
# - **Hình học**: Quy tắc "đầu-nối-đuôi" hoặc quy tắc hình bình hành.

# %%
w = np.array([5, 1])
v_plus_w = v + w

print(f"Vector v: {v}")
print(f"Vector w: {w}")
print(f"Vector v + w: {v_plus_w}")

# Trực quan hóa phép cộng
plt.figure(figsize=(8, 8))
# Vẽ vector v từ gốc
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector v = [3, 4]')
# Vẽ vector w bắt đầu từ ngọn của v
plt.quiver(v[0], v[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector w = [5, 1]')
# Vẽ vector tổng v + w
plt.quiver(0, 0, v_plus_w[0], v_plus_w[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector v+w = [8, 5]')

plt.xlim(0, 9)
plt.ylim(0, 6)
plt.grid(True)
plt.title("Phép Cộng Vector (Quy tắc Đầu-nối-đuôi)")
plt.xlabel("Trục X")
plt.ylabel("Trục Y")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# %% [markdown]
# ### 2.2. Phép Nhân Vector với Scalar
#
# Phép nhân một vector với một scalar sẽ "co" hoặc "giãn" độ dài của vector đó. Nếu scalar là số âm, nó sẽ đổi chiều của vector.
#
# Ví dụ, `2*v` sẽ là một vector cùng hướng với `v` nhưng dài gấp đôi.

# %%
v_scaled = 2 * v
v_scaled_neg = -0.5 * v

print(f"Vector v: {v}")
print(f"Vector 2*v: {v_scaled}")
print(f"Vector -0.5*v: {v_scaled_neg}")

# Trực quan hóa
plt.figure(figsize=(7, 7))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v = [3, 4]')
plt.quiver(0, 0, v_scaled[0], v_scaled[1], angles='xy', scale_units='xy', scale=1, color='g', label='2v = [6, 8]')
plt.quiver(0, 0, v_scaled_neg[0], v_scaled_neg[1], angles='xy', scale_units='xy', scale=1, color='r', label='-0.5v = [-1.5, -2]')

plt.xlim(-3, 7)
plt.ylim(-3, 9)
plt.grid(True)
plt.title("Phép Nhân Vector với Scalar")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# %% [markdown]
# ### 2.3. Tổ hợp Tuyến tính
#
# Một tổ hợp tuyến tính của các vector là tổng của các vector đó sau khi đã được nhân với các scalar. Ví dụ, `a*v + b*w` là một tổ hợp tuyến tính của `v` và `w`. Đây là một trong những ý tưởng quan trọng nhất của Đại số tuyến tính.

# %% [markdown]
# ## 3. Hình học và Phép đo Vector

# %% [markdown]
# ### 3.1. Độ dài (Độ lớn) của Vector
#
# Độ dài của vector chính là khoảng cách từ gốc tọa độ đến điểm cuối của vector. Chúng ta có thể tính nó bằng định lý Pythagoras.
#
# `||v|| = sqrt(x^2 + y^2)`

# %%
v = np.array([3, 4])
length_v = np.linalg.norm(v)

print(f"Vector v: {v}")
print(f"Độ dài của v (tính bằng Pythagoras): sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5")
print(f"Độ dài của v (tính bằng NumPy): {length_v}")

# %% [markdown]
# ### 3.2. Tích Vô hướng (Dot Product)
#
# Tích vô hướng là một phép toán giữa hai vector và cho ra kết quả là một scalar. Nó giúp chúng ta tính toán góc giữa hai vector và kiểm tra xem chúng có vuông góc với nhau không.
#
# - **Đại số**: `v · w = v1*w1 + v2*w2 + ...`
# - **Hình học**: `v · w = ||v|| * ||w|| * cos(θ)`
#
# Nếu tích vô hướng của hai vector (khác zero) bằng 0, chúng vuông góc với nhau.

# %%
v = np.array([3, 4])
w = np.array([5, 1])
z = np.array([-4, 3]) # Vector z vuông góc với v

dot_vw = np.dot(v, w)
dot_vz = np.dot(v, z)

print(f"v · w = {v[0]}*{w[0]} + {v[1]}*{w[1]} = {dot_vw}")
print(f"v · z = {v[0]}*{z[0]} + {v[1]}*{z[1]} = {dot_vz}")
if dot_vz == 0:
    print("Vì v · z = 0, vector v và z vuông góc với nhau.")

# Tính góc giữa v và w
cos_theta = dot_vw / (np.linalg.norm(v) * np.linalg.norm(w))
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)
print(f"\nGóc giữa v và w: {angle_deg:.2f} độ")

# Trực quan hóa tính vuông góc
plt.figure(figsize=(7, 7))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v = [3, 4]')
plt.quiver(0, 0, z[0], z[1], angles='xy', scale_units='xy', scale=1, color='r', label='z = [-4, 3]')
plt.xlim(-5, 5)
plt.ylim(-1, 5)
plt.grid(True)
plt.title("Hai Vector Vuông góc")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# %% [markdown]
# ### 3.3. Phép chiếu Vector
#
# Phép chiếu vector `w` lên vector `v` là việc tìm "hình chiếu" của `w` trên đường thẳng chứa `v`. Nó cho chúng ta thành phần của `w` theo phương của `v`.
#
# Công thức: `proj_v(w) = ( (w · v) / (v · v) ) * v`

# %%
v = np.array([3, 4])
w = np.array([5, 1])

# Tính phép chiếu của w lên v
proj_v_w = (np.dot(w, v) / np.dot(v, v)) * v

print(f"Vector v: {v}")
print(f"Vector w: {w}")
print(f"Hình chiếu của w lên v: {proj_v_w}")

# Trực quan hóa
plt.figure(figsize=(8, 8))
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v (phương chiếu)')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='r', label='w (vector được chiếu)')
plt.quiver(0, 0, proj_v_w[0], proj_v_w[1], angles='xy', scale_units='xy', scale=1, color='g', label='Hình chiếu của w lên v')

# Vẽ đường gióng
plt.plot([w[0], proj_v_w[0]], [w[1], proj_v_w[1]], 'k--')

plt.xlim(0, 6)
plt.ylim(0, 5)
plt.grid(True)
plt.title("Phép chiếu Vector")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# %% [markdown]
# ## 4. Không gian sinh bởi Vector (Span)
#
# "Span" của một tập hợp các vector là tập hợp tất cả các điểm bạn có thể đến được bằng cách sử dụng các tổ hợp tuyến tính của chúng.
#
# - **Span của một vector `v`**: Là một đường thẳng đi qua gốc tọa độ và chứa vector `v`.
# - **Span của hai vector `v`, `w` (không cùng phương)**: Là toàn bộ mặt phẳng 2D. Bạn có thể "lát gạch" cả mặt phẳng bằng các hình bình hành tạo bởi `v` và `w`.

# %%
v = np.array([3, 4])
w = np.array([5, 1])

plt.figure(figsize=(8, 8))

# Minh họa span(v, w) bằng cách vẽ một lưới hình bình hành
for i in range(-5, 6):
    for j in range(-5, 6):
        # Tính toán các đỉnh của hình bình hành
        origin = i * v + j * w
        p1 = origin + v
        p2 = origin + w
        p3 = origin + v + w
        # Vẽ các cạnh của hình bình hành
        plt.plot([origin[0], p1[0]], [origin[1], p1[1]], color='lightgray')
        plt.plot([origin[0], p2[0]], [origin[1], p2[1]], color='lightgray')

# Vẽ 2 vector cơ sở
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector v')
plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector w')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.title("Span(v, w) tạo thành một lưới hình bình hành phủ kín mặt phẳng")
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()