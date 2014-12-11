import sys

from pykern.emulator import Emulator
from pykern.kernel import Kernel


if len(sys.argv) < 2:
    print 'Command required'
    sys.exit(1)

command = sys.argv[1]

emulator = Emulator()

if command == 'install':
    fs_file_name = None
    if len(sys.argv) >= 3:
        fs_file_name = sys.argv[2]
    emulator.install(fs_file_name)
elif command == 'run':
    fs_file_name = None
    if len(sys.argv) >= 3:
        fs_file_name = sys.argv[2]
    Kernel(fs_file_name).boot()
else:
    print 'Command "%s" not found' % command
    sys.exit(1)