# iUsePython

I user python.

## Install Dependency

- `pip install -r requirements.txt`

## 创建、进入和退出独立且隔离的 Python 运行环境（由 virtualenv 模块提供的）

### 安装 virtualenv：

- `pip install virtualenv`

### 创建：

- `virtualenv venv` 安装到系统 Python 环境中的所有第三方包都会复制过来
- `virtualenv --no-site-packages venv` 已经安装到系统 Python 环境中的所有第三方包都不会复制过来

### 进入：

- `/venv/Scripts/activate.bat`

### 退出：

- `deactivate`
