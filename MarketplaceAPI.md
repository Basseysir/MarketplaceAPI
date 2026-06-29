# 🛒 Marketplace API

A **Multi-Vendor Marketplace REST API** built with **Django REST Framework (DRF)** that enables buyers and sellers to interact on a single platform. Buyers can browse products, manage carts, and place orders, while sellers can manage products, receive customer orders, and monitor sales through a dashboard.

---

# 📌 Features

## 🔐 Authentication

- User Registration
- JWT Login
- Refresh Access Token
- Role-Based Authentication (Buyer & Seller)

---

## 👥 User Roles

### Buyer

- Register/Login
- Browse Products
- Search Products
- Filter Products
- Add Products to Cart
- Update Cart
- Remove Cart Items
- Checkout
- View Order History
- Receive Order Confirmation Email

### Seller

- Create Seller Profile
- Upload Products
- Update Products
- Delete Products
- View Seller Dashboard
- View Seller Orders
- Update Order Status
- Receive New Order Email Notifications

---

# 🚀 Technologies Used

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Pillow
- Gmail SMTP
- Postman

---

# 📂 Project Structure

```
MarketplaceAPI/
│
├── Marketplace/
├── users/
├── sellers/
├── products/
├── carts/
├── orders/
├── media/
├── manage.py
└── requirements.txt
```

---

# 🔐 Authentication

This project uses **JWT Authentication**.

After login, include the access token in every authenticated request.

```
Authorization: Bearer <access_token>
```

---

# 📡 API Endpoints

## Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register/` | POST | Register a new user |
| `/auth/login/` | POST | Login |
| `/auth/refresh/` | POST | Refresh Access Token |

---

## Seller Profile

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/seller/profile/` | POST | Create Seller Profile |
| `/api/seller/profile/` | GET | View Seller Profile |
| `/api/dashboard/` | GET | Seller Dashboard |

---

## Categories

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/categories/` | GET | List Categories |
| `/api/categories/` | POST | Create Category |

---

## Products

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/products/` | GET | List Products |
| `/api/products/` | POST | Create Product |
| `/api/products/{id}/` | GET | Product Details |
| `/api/products/{id}/` | PUT | Update Product |
| `/api/products/{id}/` | PATCH | Partial Update |
| `/api/products/{id}/` | DELETE | Delete Product |

---

## Cart

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cart/` | GET | View Cart |
| `/api/cart/add/` | POST | Add Product |
| `/api/cart/update/{id}/` | PATCH | Update Quantity |
| `/api/cart/remove/{id}/` | DELETE | Remove Item |
| `/api/cart/clear/` | DELETE | Clear Cart |

---

## Orders

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/orders/checkout/` | POST | Checkout |
| `/api/orders/my-orders/` | GET | Buyer Orders |
| `/api/orders/seller-orders/` | GET | Seller Orders |
| `/api/orders/update/{id}/` | PATCH | Update Seller Order |

---

# 🔍 Product Search & Filters

### Search

```
GET /api/products/?search=laptop
```

### Filter by Category

```
GET /api/products/?category=1
```

### Filter by Price

```
GET /api/products/?min_price=100
GET /api/products/?max_price=1000
```

---

# 🛍 Checkout Workflow

```
Buyer

    │

    ▼

View Products

    │

    ▼

Add to Cart

    │

    ▼

Checkout

    │

    ▼

Validate Stock

    │

    ▼

Create Order

    │

    ▼

Group Products by Seller

    │

    ▼

Create Seller Orders

    │

    ▼

Create Order Items

    │

    ▼

Reduce Product Stock

    │

    ▼

Send Seller Emails

    │

    ▼

Send Buyer Email

    │

    ▼

Clear Cart
```

---

# 📧 Email Notifications

### Buyer

After successful checkout, the buyer receives:

- Order Confirmation
- Order ID
- Total Amount

---

### Seller

Each seller receives:

- New Order Notification
- Order ID
- Seller Subtotal
- Processing Reminder

---

# 🗃 Database Relationships

```
User
│
├── Buyer
│
└── SellerProfile
        │
        ├── Products
        │       │
        │       └── Category
        │
        └── SellerOrders
                │
                └── OrderItems

Buyer
│
└── Cart
      │
      └── CartItems

Buyer
│
└── Order
        │
        ├── SellerOrder
        │        │
        │        └── OrderItems
```

---

# 📊 Seller Dashboard

Displays:

- Shop Name
- Total Products
- Total Orders
- Pending Orders
- Shipped Orders
- Delivered Orders
- Total Revenue

---

# ✅ Completed Features

- JWT Authentication
- Buyer & Seller Roles
- Seller Profiles
- Product Categories
- Product CRUD
- Product Search
- Product Filtering
- Product Images
- Shopping Cart
- Multi-Vendor Checkout
- Order Management
- Seller Dashboard
- Inventory Management
- Buyer Email Notifications
- Seller Email Notifications
- Role-Based Permissions

---

# 🧪 Testing

The API was tested using **Postman**.


# 👨‍💻 Author

**Ekanem Ekanem**

Backend Developer | Django REST Framework Developer

---

## ⭐ If you found this project helpful, consider giving it a star!