import numpy as np
import mne
import os


sample_data_folder = mne.datasets.sample.data_path()
raw = mne.io.read_raw_edf('EMILY\emily0007804b1875_2022-12-15_16-24-08.edf')
raw = raw.pick_types(meg=False, eeg=True, eog=False,)

print(raw)
print(raw.info)
raw.plot_psd(fmax=20)
#raw.plot()




"""


# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these are omitted here
ica.plot_properties(raw, picks=ica.exclude)



orig_raw = raw.copy()
raw.load_data()
ica.apply(raw)

# show some frontal channels to clearly illustrate the artifact removal
chs = [ 'EEG 001', 'EEG 002']
chan_idxs = [raw.ch_names.index(ch) for ch in chs]
orig_raw.plot(order=chan_idxs, start=12, duration=4)
#raw.plot(order=chan_idxs, start=12, duration=4)

"""
