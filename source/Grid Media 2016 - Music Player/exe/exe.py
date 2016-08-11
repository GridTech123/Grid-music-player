import cx_Freeze

executables = [cx_Freeze.Executable('Grid_Media_2016___Music_Player.py')]

cx_Freeze.setup(name = 'grid music player', version = '1', options = {'build_exe': {'packages':['pygame', 'pickle'], 'include_files':['close.png', 'pause.png', 'play.png', 'upload.png', 'size.csf']}}, executables = executables)
