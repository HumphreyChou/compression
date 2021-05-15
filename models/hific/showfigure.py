import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import glob

inp_filename = glob.glob('/content/drive/My Drive/Colab Notebooks/CLIC2021/usr_out/*inp.png')[0]
otp_filename = glob.glob('/content/drive/My Drive/Colab Notebooks/CLIC2021/usr_out/*otp.png')[0]
inp = mpimg.imread(inp_filename)
otp = mpimg.imread(otp_filename)

plt.figure()
plt.title('Original Figure (Left) vs. Decompressed Figure (Right)')
plt.subplot(1,2,1)
plt.imshow(inp)
plt.subplot(1,2,2)
plt.imshow(otp)
plt.show()