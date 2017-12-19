# classification-of-voice-samples-as-male-or-female<br/>
we will use features given in the data.csv file to classify male and female voice samples<br/>
## step 1 <br/>
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
   ## meanfun is a good feature for classification <br/>
   ![meanfun](https://user-images.githubusercontent.com/12728710/34156702-5f8956a4-e4e4-11e7-97fe-2d5fc9137624.png)<br/>
   ## skew is not a good feature because histograms for male and female are overlapping
   ![skew](https://user-images.githubusercontent.com/12728710/34156732-83ae104c-e4e4-11e7-89d9-fa943b1bdfd7.png)

   
