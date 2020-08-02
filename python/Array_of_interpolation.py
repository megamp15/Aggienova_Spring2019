# Array_of_Interpolation by Mahir Pirmohammed

# Inputs
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)
from matplotlib.colors import LogNorm

# opening the file
with fits.open('SN2011dh_uu_tempsum.img.gz') as imguuu:
    imguuu.info()
    dataUUU = fits.getdata('SN2011dh_uu_tempsum.img.gz')

# prints the image data from the fits file in the console
# print(image_data[500:600,500:650])


# This is an array of interpolation methods that replaces the intepolation= argument when plotting the image.
methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

# This creates the array of plotted images to see the different interpolation methods side by side.
fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9.3, 6),
                        subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(left=0.03, right=0.97, hspace=0.3, wspace=0.05)

# plots the image with a different interpolation in each of the different squares
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(dataUUU, cmap='Blues', vmin=5, vmax=300, interpolation=interp_method, norm=LogNorm())
    ax.set_title(str(interp_method))
    ax.set_xlim(450, 950)  # sets the x lim for the smoothing area
    ax.set_ylim(550, 1050) # sets the y lim for the smoothing area

# makes the layout concise and shows the plots
plt.tight_layout()
plt.show()

# I used this website to develop this code : https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html
