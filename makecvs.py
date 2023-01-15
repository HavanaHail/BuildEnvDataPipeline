import numpy as np
import mne

edf = mne.io.read_raw_edf('opensignals_scrappy.edf')
header = ','.join(edf.ch_names)
#print(raw.info)
