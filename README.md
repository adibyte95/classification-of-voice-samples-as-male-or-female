# classification-of-voice-samples-as-male-or-female
we will use features given in the data.csv file to classify male and female voice samples
step 1:
   20 independent feature variables:
      meanfreq: mean frequency (in kHz)
      sd: standard deviation of frequency
      median: median frequency (in kHz)
      Q25: first quantile (in kHz)
      Q75: third quantile (in kHz)
      IQR: interquantile range (in kHz)
      skew: skewness 
      kurt: kurtosis 
      sp.ent: spectral entropy
      sfm: spectral flatness
      mode: mode frequency
      centroid: frequency centroid (see specprop)
      meanfun: mean fundamental frequency measured across acoustic signal
      minfun: minimum fundamental frequency measured across acoustic signal
      maxfun: maximum fundamental frequency measured across acoustic signal
      meandom: mean of dominant frequency measured across acoustic signal
      mindom: minimum of dominant frequency measured across acoustic signal
      maxdom: maximum of dominant frequency measured across acoustic signal
      dfrange: range of dominant frequency measured across acoustic signal
      modindx: modulation index

  since here we have a lot of features here we will first try to select those features that will help in the classification problem 
  for this plot.py will read these feature values  and plot a histogram using matplotlib corresponding to male and female samples.
  we will use only those feature values which will give a nearly bimodal histogram
    
  we will use sd, Q25, IQR, sfm, mode, and meanfun that elp us separate male voices from female voices.
  for more information kindly refer pictures folder 
   IQR is a good feature for classification
    ![IQR](pictures/IQR.png?raw= True "IQR")
   Skew is not a good feature for image classification as male and female have overlapped histograms
    ![skew](pictures/skew.png?raw= True "skew")
