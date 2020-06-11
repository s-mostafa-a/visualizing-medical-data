import nibabel as nib
import matplotlib.pyplot as plt
img1 = nib.load('./coronacase.nii.gz')
data = img1.get_fdata()
affine = img1.affine
img1.orthoview()
plt.show()
