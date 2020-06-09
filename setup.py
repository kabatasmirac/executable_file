
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:14:46 2019

@author: mirac.kabatas
"""

import cx_Freeze
import sys
import os
import os.path


    
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
#her bilgisayara uyum sağlasın ve pathini kullansın diye python install dir

os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

#ilgili işletim sistemi parçalarının ilgili yerlere kopyalanması
executables=[cx_Freeze.Executable('pythonfile.py',base = "Win32GUI")]
#programın adı ve konsolun kapanmasını istediğimiz için base win32gui

cx_Freeze.setup(
    name='C:\\Users\\mirac.kabatas\\Desktop\\python file',#exe dosyasının nereye oluşturulacağı
    version='1.5',
    executables=executables,
    options ={"build_exe":{"packages":["tkinter","re","scipy","scipy.signal","skimage","PIL","openpyxl","pydicom","cv2","pandas","pathlib","PIL.Image"],#kod içerisinde kullanılan modüller
                           "include_files":[
                               os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),
                               os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll')
                               ]}}
    
    )
