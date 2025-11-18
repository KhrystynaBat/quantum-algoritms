# import qutip.testing
# qutip.testing.run()
#

import qutip

dm = qutip.rand_dm(4)
fig, ax = qutip.hinton(dm)
fig.show()

qutip.settings.colorblind_safe = True
fig, ax = qutip.hinton(dm, color_style="threshold")
fig.show()
qutip.settings.colorblind_safe = False

fig, ax = qutip.hinton(dm, color_style="phase")
fig.show()