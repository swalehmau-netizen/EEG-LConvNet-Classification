def preprocessing (filepath):
    data=mne.io.read_raw_edf(filepath, preload=True) #reading eeg files from directory
    info = mne.create_info(ch_names=25, sfreq=128, ch_types='eeg', verbose=None)
    data.set_eeg_reference("average")   #setting eeg-reference to avrage of all channels
    data.resample(sfreq=128)
    data.filter(l_freq=1, h_freq=45) #filtering low and high pass filters
    data.crop(tmin = 1, tmax=200) #data cropping, min/max durations in sec
    #picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False)
    #data.pick(picks);   #Discarding non-eeg signals
    epochs=mne.make_fixed_length_epochs(data, duration=5, overlap=1)
    array=epochs.get_data() #converts object to array
    pca = UnsupervisedSpatialFilter(PCA(25), average=False)
    eeg_pca_data = pca.fit_transform(array) #dimensionality reduction
    return eeg_pca_data
