# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2025/1/31
Last Modified: 2025/1/31
Description: 
"""
from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)