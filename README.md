
# Project Setup Guide

## Prerequisites

This project requires the following essentials to set up locally:

### 1. Git
Git is a version control system that helps manage code changes.

- **Installation**:
    - **Windows**: Download from [git-scm.com](https://git-scm.com/download/win)

### 2. Python
Python is the programming language used in this project.
- **Installation**:
    - **Windows**: Download from [python.org](https://www.python.org/downloads/windows/)

### 3. Virtual Environment

A Python virtual environment isolates project dependencies from your system Python installation.

### 4. UV Package Manager

UV is a fast, reliable Python package manager and resolver.

- **Installation**: Follow [UV documentation](https://docs.astral.sh/uv/)

## Installation Steps by OS

### Windows
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```
2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. **Install Dependencies with UV**:
    ```bash
    uv install
    ```
4. **Run the Project**:
    ```bash
    uv run
    ```