# classification-of-voice-samples-as-male-or-female<br/>
we will use features given in the data.csv file to classify male and female voice samples<br/>
step 1 <br/>
   20 independent feature variables:<br />
      meanfreq: mean frequency in kHz <br />
      sd: standard deviation of frequency<br />
      median: median frequency in kHz <br />
      Q25: first quantile in kHz <br />
      Q75: third quantile in kHz<br />
      IQR: interquantile range in kHz<br />
      skew: skewness <br/>
      kurt: kurtosis <br/>
      sp.ent: spectral entropy<br/>
      sfm: spectral flatness<br/>
      mode: mode frequency<br/>
      centroid: frequency centroid (see specprop)<br/>
      meanfun: mean fundamental frequency measured across acoustic signal<br/>
      minfun: minimum fundamental frequency measured across acoustic signal<br/>
      maxfun: maximum fundamental frequency measured across acoustic signal<br/>
      meandom: mean of dominant frequency measured across acoustic signal<br/>
      mindom: minimum of dominant frequency measured across acoustic signal<br/>
      maxdom: maximum of dominant frequency measured across acoustic signal<br/>
      dfrange: range of dominant frequency measured across acoustic signal<br/>
      modindx: modulation index<br/>

  since here we have a lot of features here we will first try to select those features that will help in the classification problem<br/> 
  for this plot.py will read these feature values  and plot a histogram using matplotlib corresponding to male and female samples.<br/>
  we will use only those feature values which will give a nearly bimodal histogram<br/>
    
  we will use sd, Q25, IQR, sfm, mode, and meanfun that elp us separate male voices from female voices.<br/>
  for more information kindly refer pictures folder <br/>
   IQR is a good feature for classification<br/>
   Skew is not a good feature for image classification as male and female have overlapped histograms<br/>
   
