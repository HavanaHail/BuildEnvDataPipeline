import mne
import os.path as op
from matplotlib import pyplot as plt


data_path = op.join(mne.datasets.sample.data_path(), 'MEG',
                    'sample', 'sample_audvis_raw.fif')
#raw = mne.io.read_raw_fif(data_path, preload=True)
raw = mne.io.read_raw_edf('opensignals_scrappy.edf')
raw.set_eeg_reference('average', projection=True)  # set EEG average reference

# Give the sample rate
print('sample rate:', raw.info['sfreq'], 'Hz')
# Give the size of the data matrix
print('%s channels x %s samples' % (raw.info['nchan'], len(raw.times)))

# Extract data from the first 5 channels, from 1 s to 3 s.
sfreq = raw.info['sfreq']
data, times = raw[:5, int(sfreq * 1):int(sfreq * 3)]
_ = plt.plot(times, data.T)
_ = plt.title('Sample channels')
plt.show()



########################################################################

# # Pull all MEG gradiometer channels:
# # Make sure to use .copy() or it will overwrite the data
# meg_only = raw.copy().pick_types(meg=True)
# eeg_only = raw.copy().pick_types(meg=False, eeg=True)

# # The MEG flag in particular lets you specify a string for more specificity
# grad_only = raw.copy().pick_types(meg='grad')

# # Or you can use custom channel names
# pick_chans = ['MEG 0112', 'MEG 0111', 'MEG 0122', 'MEG 0123']
# specific_chans = raw.copy().pick_channels(pick_chans)
# print(meg_only)
# print(eeg_only)
# print(grad_only)
# print(specific_chans)

