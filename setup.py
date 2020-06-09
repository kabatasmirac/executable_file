
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:14:46 2019

@author: mirac.kabatas
"""

import cx_Freeze
import sys
import os
import os.path

build_exe_options = {"packages": ["os"],"includes":["tkinter"]}
#os modülü sadece packages içinde yer almalı includes içinde yer alırsa çalışmıyor
base = None
if sys.platform == "win32":
    base = "Win32GUI"
#win32gui konsolun açılmamasını sağlıyor
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
#her bilgisayara uyum sağlasın ve pathini kullansın diye python install dir
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')
#ilgili işletim sistemi parçalarının ilgili yerlere kopyalanması
executables=[cx_Freeze.Executable('pythonfile.py',base = "Win32GUI")]
#programın adı ve konsolun kapanmasını istediğimiz için base win32gui
cx_Freeze.setup(
    name='C:\\Users\\mirac.kabatas\\Desktop\\python file',#nereye oluşturulacağı
    version='1.5',
    executables=executables,
    options ={"build_exe":{"packages":["tkinter","re","scipy","scipy.signal","skimage","PIL","openpyxl","pydicom","cv2","pandas","pathlib","PIL.Image"],#içeride kullanılan modüller
                           "include_files":[
                               os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),
                               os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll')
                               ]}}
    
    )
