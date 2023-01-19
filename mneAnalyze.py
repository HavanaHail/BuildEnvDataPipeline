import numpy as np
import mne
import os
import mne.time_frequency


sample_data_folder = mne.datasets.sample.data_path()
#raw = mne.io.read_raw_edf('EMILY\emily0007804b1875_2022-12-15_16-24-08.edf', preload = 'true')
#raw = raw.pick_types(meg=False, eeg=True, eog=False,)
#h5 has events
raw = mne.time_frequency.read_tfrs('EMILY\emily0007804b1875_2022-12-15_16-24-08.h5')
raw = raw.pick_types(meg=False, eeg=True, eog=False,)
print(type(raw))
data_array = raw[:][0]
#data = np.array([raw])

#print(raw)
#print(raw.info)

#prints frequency vs. amplitude 
raw.plot_psd(fmax=20)



#rawTimeData = mne.io.RawArray(data = timeData, info = raw.info)
#timeData.plot_psd()
#timeData.plot()




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
