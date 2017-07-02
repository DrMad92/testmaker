from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["database_operation", "file_operation", "quiz", "settings"],
                     "include_files": ["lang_files"]}

setup(name="testmaker",
      version="1.0",
      description="Test making application",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py",targetName="testmaker.exe")])
