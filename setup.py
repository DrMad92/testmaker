from cx_Freeze import setup, Executable

setup(name='testmaker',
      version = 1.0,
      description = 'Makes tests',
      executables = [Executable('main.py')])