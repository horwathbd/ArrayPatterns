""" Functions dealing with rectangular patch antenna."""
import numpy as np
import pandas as pd
from PlotPatterns import *

if __name__ == "__main__":
    """Create an element pattern and plot in 3-D"""
    
    phiStart=0
    phiStop=361
    thetaStart=0
    thetaStop=91
    elementPattern=np.ones((phiStop,thetaStop))                                                                              # Ideal point source

    SurfacePlot(elementPattern)                                                                                              # 3D plot of element pattern
    EHPlanePlot(elementPattern,phiStart,phiStop,thetaStart,thetaStop)                                                        # 2D plots of element pattern 
    df=pd.DataFrame(data=elementPattern)
    df.to_csv('ideal_test.csv')
