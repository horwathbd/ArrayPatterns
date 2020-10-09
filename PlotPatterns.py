import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def SurfacePlot(fieldPattern):
    """Plots 3D surface plot over given theta/phi range in fieldPattern by calculating cartesian coordinate equivalent of spherical form."""

    print("Processing SurfacePlot...")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phiSize = fieldPattern.shape[0]                                                                             # Finds the phi & theta range
    thetaSize = fieldPattern.shape[1]

    X = np.ones((phiSize, thetaSize))                                                                           # Prepare arrays to hold the cartesian coordinate data.
    Y = np.ones((phiSize, thetaSize))
    Z = np.ones((phiSize, thetaSize))

    for phi in range(phiSize):                                                                                  # Iterate over all phi/theta range
        for theta in range(thetaSize):
            eF = fieldPattern[phi][theta]

            # Calculate and store Cartesian coordinates
            ph=radians(phi)
            th=radians(theta)
            X[phi, theta] = eF * cos(ph) * sin(th)
            Y[phi, theta] = eF * sin(ph) * sin(th)
            Z[phi, theta] = eF * cos(th)

    surf=ax.plot_surface(X, Y, Z, cmap=cm.rainbow)                                                              # Plot surface
    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.ylabel('Y')
    plt.xlabel('X')                                                                                             # Plot formatting
    plt.title("3-D Radiation Pattern (no freq)")
    plt.show()

def EHPlanePlot(fields,phiStart,phiStop,thetaStart,thetaStop,isLog=True):
    """
    Plot 2D plots showing E-field for E-plane (phi = 0°) and the H-plane (phi = 90°).
    """

    Xtheta = np.linspace(thetaStart, thetaStop, thetaStop)                                                                             # Theta range array used for plotting

    if isLog:                                                                                                   # Can plot the log scale or normal
        plt.plot(Xtheta, 20 * np.log10(abs(fields[90, :])), label="H-plane (Phi=90°)")                          # Log = 20 * log10(E-field)
        plt.plot(Xtheta, 20 * np.log10(abs(fields[0, :])), label="E-plane (Phi=0°)")
        plt.ylabel('E-Field (dB)')
    else:
        plt.plot(Xtheta, fields[90, :], label="H-plane (Phi=90°)")
        plt.plot(Xtheta, fields[0, :], label="E-plane (Phi=0°)")
        plt.ylabel('E-Field')

    plt.xlabel('Theta (degs)')                                                                                  # Plot formatting
    plt.title("2-D Radiation Pattern (no freq)")
    plt.ylim((-40,5))
    plt.xlim((0, 90))

    start, end = plt.xlim()
    plt.xticks(np.arange(start, end, 5))
    plt.grid(b=True, which='major')
    plt.legend()
    plt.show()                                                                                                  # Show plot
