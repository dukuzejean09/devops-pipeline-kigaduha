# 📋 Task Management App

A modern, full-stack task management application with a complete DevOps pipeline. Built with React (frontend) and Flask (backend), featuring CI/CD automation, infrastructure as code, and production-ready deployment configurations.

## ✨ Features

- ✅ Create, read, update, and delete tasks
- 📊 Real-time task statistics dashboard
- 🎯 Task prioritization (High, Medium, Low)
- 🔄 Task status tracking (Pending, In Progress, Completed)
- 🎨 Modern, responsive UI with gradient design
- 🔍 Filter tasks by status
- 📱 Mobile-friendly interface
- 🐳 Fully containerized with Docker
- 🚀 Complete CI/CD pipeline with GitHub Actions
- ☁️ Infrastructure as Code with Terraform
- ⚙️ Automated deployment with Ansible

## 🏗️ Architecture

```
┌─────────────────┐      ┌─────────────────┐
│   React UI      │─────▶│   Flask API     │
│   (Frontend)    │      │   (Backend)     │
│   Port: 80      │      │   Port: 5000    │
└─────────────────┘      └─────────────────┘
        │                         │
        └─────────┬───────────────┘
                  ▼
           Docker Network
```
