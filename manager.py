import subprocess
import os
import shutil
import tempfile


temp_directory = tempfile.mkdtemp()
player1_directory = os.path.join(temp_directory, 'player1')
player2_directory = os.path.join(temp_directory, 'player2')
os.mkdir(player1_directory)
os.mkdir(player2_directory)
print('Player directories created')

os.mkfifo(os.path.join(player1_directory, 'in'), mode=0o777)
os.mkfifo(os.path.join(player1_directory, 'out'), mode=0o777)
os.mkfifo(os.path.join(player2_directory, 'in'), mode=0o777)
os.mkfifo(os.path.join(player2_directory, 'out'), mode=0o777)
print('Fifos created')

try:
    print('Starting driver process')
    print(f'{temp_directory}')
    driver_process = subprocess.Popen([
        'docker',
        'run',
        '--rm',
        '-v',
        f'{temp_directory}/:/fifos',
        'codecharacter-driver'
    ])

    print('Starting player1 process')
    player1_process = subprocess.Popen([
        'docker',
        'run',
        '--rm',
        '-v',
        f'{os.getcwd()}/player-code/python/optimal.py:/player.py',
        '-v',
        f'{temp_directory}/player1/in:/in',
        'codecharacter-python-runner',
        '/player.py'
    ], stdin=os.open(os.path.join(player1_directory, 'in'), os.O_RDONLY),
        stdout=os.open(os.path.join(player1_directory, 'out'), os.O_RDWR))

    print('Starting player2 process')
    player2_process = subprocess.Popen([
        'docker',
        'run',
        '--rm',
        '-v',
        f'{os.getcwd()}/ai-code/ai.py:/player.py',
        '-v',
        f'{temp_directory}/player2/in:/in',
        'codecharacter-python-runner',
        '/player.py'
    ], stdin=os.open(os.path.join(player2_directory, 'in'), os.O_RDONLY),
        stdout=os.open(os.path.join(player2_directory, 'out'), os.O_RDWR))

    driver_process.wait()

except Exception as e:
    print(e)
    pass

finally:
    player1_process.kill()
    player2_process.kill()
    driver_process.kill()
    shutil.rmtree(temp_directory)
