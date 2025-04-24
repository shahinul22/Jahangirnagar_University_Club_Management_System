# Jahangirnagar University Club Management System

A web-based platform to manage clubs at Jahangirnagar University. Built with Django backend and Tailwind CSS + daisyUI frontend. The system supports two types of users: **Organizers** and **Regular Users**. Each can register, login, and access a role-specific dashboard.

---

## 🔧 Tech Stack

- **Backend:** Django 5.x
- **Frontend:** Tailwind CSS + daisyUI
- **Authentication:** Django built-in auth (username, password)
- **Styling:** Tailwind CSS via CDN, daisyUI for components

---

## ⚙️ Features

- Separate registration pages for **Organizers** and **Regular Users**
- Custom login system with redirect to dashboard
- Dashboard view protected via login
- Logout via POST method (CSRF protected)
- Responsive navigation bar with hamburger drawer on small screens

---

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/jahangirnagar_club.git
cd jahangirnagar_club
